"""Payslip generator — Australia FY2024-25 / FY2025-26 (annual estimator).

Models PAYG withholding (resident, Stage 3 brackets), the 2% Medicare levy and
the Superannuation Guarantee. Superannuation is an EMPLOYER contribution paid on
top of gross salary (it is NOT deducted from the employee's take-home pay).

All amounts are annual and in AUD.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum

__all__ = [
    "Employee", "PayslipLineType", "PayslipLine", "Payslip", "generate_payslip",
]

# ---------------------------------------------------------------------------
# Tax parameters (FY2024-25 Stage 3 resident brackets, annual)
# ---------------------------------------------------------------------------

# Resident PAYG withholding brackets after the Stage 3 tax cuts (from 1 Jul 2024).
# Each tuple: (lower_bound_exclusive, marginal_rate). Income above the tax-free
# threshold ($18,200) is taxed progressively.
_PAYG_BRACKETS: list[tuple[float, float]] = [
    (18200.0, 0.16),    # $18,201 – $45,000 @ 16%
    (45000.0, 0.30),    # $45,001 – $135,000 @ 30%
    (135000.0, 0.37),   # $135,001 – $190,000 @ 37%
    (190000.0, 0.45),   # $190,001+ @ 45%
]

_TAX_FREE_THRESHOLD = 18200.0
_MEDICARE_LEVY_RATE = 0.02          # 2% flat (low-income thresholds simplified away)
_DEFAULT_SUPER_RATE = 0.12          # Super Guarantee from 1 July 2025 (was 11.5%)


def _income_tax_payg(taxable: float) -> float:
    """Progressive resident PAYG withholding on annual taxable income.

    The tax-free threshold ($18,200) is applied: income at or below it is 0 tax.
    """
    if taxable <= _TAX_FREE_THRESHOLD:
        return 0.0
    tax = 0.0
    # Upper bounds paired with each bracket's lower bound.
    bounds = [45000.0, 135000.0, 190000.0, float("inf")]
    for (lower, rate), upper in zip(_PAYG_BRACKETS, bounds):
        if taxable > lower:
            span = min(taxable, upper) - lower
            tax += span * rate
        else:
            break
    return tax


def _medicare_levy(taxable: float) -> float:
    """Flat 2% Medicare levy.

    Simplification: the low-income reduction/threshold (below which the levy
    phases in from 0%) is not modelled — a flat 2% is applied to all taxable
    income. Sub-threshold cases below the tax-free amount still yield 0 tax
    only for PAYG; the levy here follows the flat-rate convention.
    """
    if taxable <= 0.0:
        return 0.0
    return taxable * _MEDICARE_LEVY_RATE


# ---------------------------------------------------------------------------
# Enums and dataclasses
# ---------------------------------------------------------------------------

class PayslipLineType(Enum):
    GROSS_SALARY = "Gross salary"
    INCOME_TAX_PAYG = "PAYG withholding"
    MEDICARE_LEVY = "Medicare levy"
    SUPERANNUATION = "Superannuation guarantee (employer)"
    NET_PAY = "Net pay"
    EMPLOYER_COST = "Total employer cost"


@dataclass
class Employee:
    id: str
    name: str
    tfn: str = ""                    # Tax File Number — encrypted in vault, never logged
    gross_annual: float = 0.0
    super_rate: float = _DEFAULT_SUPER_RATE
    residency: str = "resident"      # resident tax scales assumed
    claims_tax_free_threshold: bool = True


@dataclass
class PayslipLine:
    line_type: PayslipLineType
    description: str
    amount: float                    # positive = income/employer cost, negative = deduction


@dataclass
class Payslip:
    employee_id: str
    period: str                      # e.g. "FY2024-25"
    employer_id: str = ""
    lines: list[PayslipLine] = field(default_factory=list)
    year: int = 2025

    def gross(self) -> float:
        return sum(l.amount for l in self.lines
                   if l.line_type is PayslipLineType.GROSS_SALARY)

    def income_tax_payg(self) -> float:
        return -sum(l.amount for l in self.lines
                    if l.line_type is PayslipLineType.INCOME_TAX_PAYG)

    def medicare_levy(self) -> float:
        return -sum(l.amount for l in self.lines
                    if l.line_type is PayslipLineType.MEDICARE_LEVY)

    def superannuation(self) -> float:
        """Employer Super Guarantee contribution (on top of gross, not deducted)."""
        return sum(l.amount for l in self.lines
                   if l.line_type is PayslipLineType.SUPERANNUATION)

    def net_annual(self) -> float:
        """Take-home pay: gross minus employee deductions (super excluded)."""
        return self.gross() - self.income_tax_payg() - self.medicare_levy()

    def employer_cost(self) -> float:
        """Total cost to employer: gross salary plus superannuation."""
        return self.gross() + self.superannuation()

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "period": self.period,
            "employer_id": self.employer_id,
            "year": self.year,
            "gross_annual": round(self.gross(), 2),
            "income_tax_payg": round(self.income_tax_payg(), 2),
            "medicare_levy": round(self.medicare_levy(), 2),
            "superannuation": round(self.superannuation(), 2),
            "net_annual": round(self.net_annual(), 2),
            "employer_cost": round(self.employer_cost(), 2),
            "lines": [
                {
                    "line_type": l.line_type.value,
                    "description": l.description,
                    "amount": round(l.amount, 2),
                }
                for l in self.lines
            ],
        }

    def to_json(self, indent: int | None = None) -> str:
        return json.dumps(self.to_dict(), indent=indent, sort_keys=True)


# ---------------------------------------------------------------------------
# Main generator
# ---------------------------------------------------------------------------

def generate_payslip(
    employee: Employee,
    period: str = "FY2024-25",
    year: int = 2025,
    super_rate: float | None = None,
) -> Payslip:
    """Generate an annual Australian payslip estimate.

    Computation order: gross -> deductions (PAYG, Medicare) -> net; super is an
    employer contribution computed on top of gross.

    - PAYG withholding: resident Stage 3 brackets, tax-free threshold applied.
    - Medicare levy: flat 2% of taxable income (low-income thresholds simplified).
    - Superannuation: super_rate x gross (default 12%), employer-paid, NOT deducted.
    """
    gross = employee.gross_annual
    rate = super_rate if super_rate is not None else employee.super_rate

    # Tax-free threshold only when the employee claims it.
    taxable = gross
    if employee.claims_tax_free_threshold:
        payg = _income_tax_payg(taxable)
    else:
        # No tax-free threshold: whole income taxed from the first dollar at the
        # lowest marginal rate upward (simplified — applies 16% from $0).
        payg = _no_threshold_payg(taxable)

    medicare = _medicare_levy(taxable)
    super_contribution = gross * rate

    lines: list[PayslipLine] = [
        PayslipLine(
            PayslipLineType.GROSS_SALARY,
            "Gross annual salary",
            gross,
        ),
        PayslipLine(
            PayslipLineType.INCOME_TAX_PAYG,
            "PAYG withholding (resident, tax-free threshold "
            + ("claimed" if employee.claims_tax_free_threshold else "not claimed") + ")",
            -payg,
        ),
        PayslipLine(
            PayslipLineType.MEDICARE_LEVY,
            "Medicare levy (2%)",
            -medicare,
        ),
        PayslipLine(
            PayslipLineType.SUPERANNUATION,
            f"Superannuation guarantee ({rate * 100:.1f}%, employer-paid)",
            super_contribution,
        ),
    ]

    return Payslip(
        employee_id=employee.id,
        period=period,
        year=year,
        lines=lines,
    )


def _no_threshold_payg(taxable: float) -> float:
    """PAYG when the tax-free threshold is not claimed (16% from the first dollar)."""
    if taxable <= 0.0:
        return 0.0
    tax = 0.0
    bounds = [45000.0, 135000.0, 190000.0, float("inf")]
    lowers = [0.0, 45000.0, 135000.0, 190000.0]
    rates = [0.16, 0.30, 0.37, 0.45]
    for lower, upper, rate in zip(lowers, bounds, rates):
        if taxable > lower:
            tax += (min(taxable, upper) - lower) * rate
        else:
            break
    return tax
