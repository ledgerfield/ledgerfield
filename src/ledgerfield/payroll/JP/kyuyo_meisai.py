"""給与明細 (kyuyo meisai) generator — Japan 2025.

Monthly payslip estimator for the employee side of Japanese payroll.
Mirrors the NL ``loonstrook`` module but uses romaji/English identifiers
with Japanese terms in the labels and docstrings.

Simplifications (documented, deterministic):
- Social insurance (社会保険) is computed directly on the gross monthly
  salary as the "standard monthly remuneration" (標準報酬月額) base. The
  real system snaps gross onto a grade table (等級表); we skip the grade
  table and use gross as the base for the estimator.
- Income tax withholding (源泉所得税) uses an annualized progressive
  computation rather than the monthly withholding tax tables (源泉徴収税額表):
  taxable = (gross - social_insurance) * 12
            - employment income deduction (給与所得控除)
            - basic deduction (基礎控除) ¥480,000
  then the 2025 national brackets + 2.1% reconstruction surtax (復興特別所得税),
  divided by 12.
- Resident tax (住民税, ~10%) is levied the following year on prior-year
  income and is therefore NOT withheld here — it is only reported as a note.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum

__all__ = [
    "Employee",
    "PayslipLineType",
    "PayslipLine",
    "Payslip",
    "generate_payslip",
]

# ---------------------------------------------------------------------------
# 2025 statutory parameters (employee side)
# ---------------------------------------------------------------------------

# Social insurance 社会保険 — employee-side rates (employer matches).
HEALTH_INSURANCE_RATE_EMPLOYEE = 0.0499        # 健康保険 ~9.98% split
PENSION_RATE_EMPLOYEE = 0.0915                 # 厚生年金 18.3% split
EMPLOYMENT_INSURANCE_RATE_EMPLOYEE = 0.006     # 雇用保険 2025 (general business)

# Income tax 源泉所得税
BASIC_DEDUCTION = 480_000                       # 基礎控除
RECONSTRUCTION_SURTAX_RATE = 0.021              # 復興特別所得税 2.1%

# Employment income deduction 給与所得控除 (simplified):
# 30% of annual gross, floored at ¥550,000 and capped at ¥1,950,000.
EMPLOYMENT_INCOME_DEDUCTION_RATE = 0.30
EMPLOYMENT_INCOME_DEDUCTION_FLOOR = 550_000
EMPLOYMENT_INCOME_DEDUCTION_CAP = 1_950_000

# Resident tax 住民税 (note only — not withheld here).
RESIDENT_TAX_RATE = 0.10

# 2025 national income tax brackets 所得税 (annual taxable income, JPY):
# (upper_bound, marginal_rate, quick-deduction).  Last bracket unbounded.
_INCOME_TAX_BRACKETS: list[tuple[float, float, float]] = [
    (1_950_000, 0.05, 0),
    (3_300_000, 0.10, 97_500),
    (6_950_000, 0.20, 427_500),
    (9_000_000, 0.23, 636_000),
    (18_000_000, 0.33, 1_536_000),
    (40_000_000, 0.40, 2_796_000),
    (float("inf"), 0.45, 4_796_000),
]


# ---------------------------------------------------------------------------
# Enums and dataclasses
# ---------------------------------------------------------------------------

class PayslipLineType(Enum):
    """給与明細の項目種別 — payslip line types."""
    GROSS_SALARY = "総支給 (gross salary)"
    HEALTH_INSURANCE = "健康保険料 (health insurance)"
    PENSION = "厚生年金保険料 (pension)"
    EMPLOYMENT_INSURANCE = "雇用保険料 (employment insurance)"
    INCOME_TAX_WITHHOLDING = "源泉所得税 (income tax withholding)"
    NET_SALARY = "差引支給額 (net salary)"
    EMPLOYER_COST = "会社負担 (employer cost)"


@dataclass
class Employee:
    """従業員 — employee master record."""
    id: str
    name: str
    my_number_note: str = "encrypted-in-vault"   # マイナンバー — never stored plaintext
    gross_salary: float = 0.0                     # 月額総支給 (monthly gross)
    dependents: int = 0                           # 扶養親族の数


@dataclass
class PayslipLine:
    """給与明細の一行 — one payslip line.

    ``amount`` is positive for earnings, negative for deductions.
    Employer-cost lines are informational (not part of net).
    """
    line_type: PayslipLineType
    label: str
    amount: float


@dataclass
class Payslip:
    """給与明細 — monthly payslip."""
    employee_id: str
    period: str                                   # YYYY-MM
    employer_id: str = ""
    lines: list[PayslipLine] = field(default_factory=list)
    year: int = 2025
    resident_tax_note: str = ""

    def gross(self) -> float:
        """総支給額 — gross earnings."""
        return sum(
            line.amount for line in self.lines
            if line.line_type == PayslipLineType.GROSS_SALARY
        )

    def deductions(self) -> float:
        """控除合計 — total employee deductions (positive number)."""
        return -sum(
            line.amount for line in self.lines
            if line.line_type in {
                PayslipLineType.HEALTH_INSURANCE,
                PayslipLineType.PENSION,
                PayslipLineType.EMPLOYMENT_INSURANCE,
                PayslipLineType.INCOME_TAX_WITHHOLDING,
            }
        )

    def net(self) -> float:
        """差引支給額 — net pay (gross minus employee deductions)."""
        return sum(
            line.amount for line in self.lines
            if line.line_type != PayslipLineType.EMPLOYER_COST
        )

    def employer_cost(self) -> float:
        """会社負担合計 — total employer-side cost (informational)."""
        return sum(
            line.amount for line in self.lines
            if line.line_type == PayslipLineType.EMPLOYER_COST
        )

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "period": self.period,
            "employer_id": self.employer_id,
            "year": self.year,
            "gross": round(self.gross(), 2),
            "deductions": round(self.deductions(), 2),
            "net": round(self.net(), 2),
            "employer_cost": round(self.employer_cost(), 2),
            "resident_tax_note": self.resident_tax_note,
            "lines": [
                {
                    "line_type": line.line_type.value,
                    "label": line.label,
                    "amount": round(line.amount, 2),
                }
                for line in self.lines
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)


# ---------------------------------------------------------------------------
# Tax helpers
# ---------------------------------------------------------------------------

def _employment_income_deduction(annual_gross: float) -> float:
    """給与所得控除 — simplified employment income deduction.

    30% of annual gross, floored at ¥550,000, capped at ¥1,950,000.
    """
    if annual_gross <= 0:
        return 0.0
    raw = annual_gross * EMPLOYMENT_INCOME_DEDUCTION_RATE
    return min(max(raw, EMPLOYMENT_INCOME_DEDUCTION_FLOOR), EMPLOYMENT_INCOME_DEDUCTION_CAP)


def _national_income_tax(annual_taxable: float) -> float:
    """所得税 — national income tax via bracket + quick-deduction table."""
    if annual_taxable <= 0:
        return 0.0
    for upper, rate, quick_deduction in _INCOME_TAX_BRACKETS:
        if annual_taxable <= upper:
            return max(0.0, annual_taxable * rate - quick_deduction)
    return 0.0  # unreachable (last bracket is inf)


def _annual_income_tax_withholding(annual_gross: float, annual_social_insurance: float) -> float:
    """源泉所得税 — annual withholding incl. 復興特別所得税 (2.1% surtax)."""
    if annual_gross <= 0:
        return 0.0
    employment_deduction = _employment_income_deduction(annual_gross)
    taxable = annual_gross - annual_social_insurance - employment_deduction - BASIC_DEDUCTION
    taxable = max(0.0, taxable)
    base_tax = _national_income_tax(taxable)
    return base_tax * (1.0 + RECONSTRUCTION_SURTAX_RATE)


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def generate_payslip(
    employee: Employee,
    period: str,
    year: int = 2025,
    employer_id: str = "",
) -> Payslip:
    """給与明細を生成する — generate a monthly Japanese payslip.

    Flow: gross → social insurance (健保/厚生年金/雇用保険) → income tax
    withholding (源泉所得税) → net (差引支給額). Employer matching cost is
    added as an informational 会社負担 line. Resident tax (住民税) is noted
    but not withheld.
    """
    gross = float(employee.gross_salary)

    # --- Social insurance 社会保険 (employee side) ---
    health = gross * HEALTH_INSURANCE_RATE_EMPLOYEE
    pension = gross * PENSION_RATE_EMPLOYEE
    employment_ins = gross * EMPLOYMENT_INSURANCE_RATE_EMPLOYEE
    social_insurance = health + pension + employment_ins

    # --- Income tax withholding 源泉所得税 (annualized then /12) ---
    annual_gross = gross * 12.0
    annual_social = social_insurance * 12.0
    income_tax = _annual_income_tax_withholding(annual_gross, annual_social) / 12.0

    # --- Employer matching cost 会社負担 (informational) ---
    # Employer matches health (~4.99%) + pension (9.15%) and pays a higher
    # employment-insurance share (~0.95% in 2025).
    employer_cost = (
        gross * HEALTH_INSURANCE_RATE_EMPLOYEE
        + gross * PENSION_RATE_EMPLOYEE
        + gross * 0.0095
    )

    lines: list[PayslipLine] = [
        PayslipLine(PayslipLineType.GROSS_SALARY, "総支給額 (gross salary)", gross),
        PayslipLine(
            PayslipLineType.HEALTH_INSURANCE,
            f"健康保険料 ({HEALTH_INSURANCE_RATE_EMPLOYEE * 100:.2f}%)",
            -health,
        ),
        PayslipLine(
            PayslipLineType.PENSION,
            f"厚生年金保険料 ({PENSION_RATE_EMPLOYEE * 100:.2f}%)",
            -pension,
        ),
        PayslipLine(
            PayslipLineType.EMPLOYMENT_INSURANCE,
            f"雇用保険料 ({EMPLOYMENT_INSURANCE_RATE_EMPLOYEE * 100:.2f}%)",
            -employment_ins,
        ),
        PayslipLine(
            PayslipLineType.INCOME_TAX_WITHHOLDING,
            "源泉所得税 (incl. 2.1% 復興特別所得税)",
            -income_tax,
        ),
        PayslipLine(
            PayslipLineType.EMPLOYER_COST,
            "会社負担 (社会保険 employer match, informational)",
            employer_cost,
        ),
    ]

    resident_tax_note = (
        f"住民税 ~{RESIDENT_TAX_RATE * 100:.0f}% levied next year on this year's "
        f"income; not withheld in this estimate."
    )

    return Payslip(
        employee_id=employee.id,
        period=period,
        employer_id=employer_id,
        lines=lines,
        year=year,
        resident_tax_note=resident_tax_note,
    )
