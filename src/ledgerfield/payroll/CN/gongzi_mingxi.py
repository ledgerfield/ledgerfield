"""工资明细 — China payslip generator (2025, employee side).

Computes the monthly Chinese payslip: gross salary (工资) minus the
"five insurances and one fund" (五险一金, wuxianyijin) employee
contributions and Individual Income Tax (个人所得税, IIT) withholding,
yielding net take-home pay (实发工资).

Rates modelled here are Shanghai/typical 2025 employee rates. Actual
percentages and the contribution base cap vary by city (城市差异); this
estimator uses gross salary as the contribution base and applies the
monthly-equivalent progressive IIT brackets (see note below).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum

__all__ = [
    "Employee", "PayslipLineType", "PayslipLine", "Payslip",
    "generate_payslip",
]

# ---------------------------------------------------------------------------
# Statutory constants (2025, employee side, Shanghai/typical)
# ---------------------------------------------------------------------------

# 五险一金 (wuxianyijin) — employee contribution rates
PENSION_RATE = 0.08        # 养老保险 pension insurance
MEDICAL_RATE = 0.02        # 医疗保险 medical insurance
UNEMPLOYMENT_RATE = 0.005  # 失业保险 unemployment insurance
HOUSING_FUND_RATE = 0.07   # 住房公积金 housing provident fund
# Total employee social + housing ≈ 17.5% of the contribution base.

# Note on the contribution base (缴费基数): legally capped at 300% of the
# local average wage and floored at 60%. This estimator uses gross salary
# directly as the base (cap simplification).

# 个人所得税 (IIT) — basic monthly deduction (起征点)
IIT_BASIC_DEDUCTION = 5000.0  # ¥5,000 / month standard basic deduction

# Employer-side note (雇主缴纳, not withheld from employee): pension ~16%,
# medical ~9-10%, unemployment ~0.5%, work injury ~0.2-0.5%, maternity,
# plus matching housing fund ~7% — informational only.
EMPLOYER_PENSION_RATE_NOTE = 0.16

# ---------------------------------------------------------------------------
# IIT brackets — monthly-equivalent method.
#
# China withholds comprehensive income (综合所得) using an annual cumulative
# method. For a single-month estimator we apply the monthly-equivalent
# progressive table (the pre-2019 monthly bracket table, which equals the
# annual table divided by 12) with quick deductions (速算扣除数). This is
# exact for a stable monthly salary and is the documented choice here.
#
# Each tuple: (upper_bound_of_monthly_taxable, rate, quick_deduction)
# ---------------------------------------------------------------------------
_IIT_MONTHLY_BRACKETS: list[tuple[float, float, float]] = [
    (3000.0, 0.03, 0.0),
    (12000.0, 0.10, 210.0),
    (25000.0, 0.20, 1410.0),
    (35000.0, 0.25, 2660.0),
    (55000.0, 0.30, 4410.0),
    (80000.0, 0.35, 7160.0),
    (float("inf"), 0.45, 15160.0),
]


def _compute_iit(monthly_taxable: float) -> tuple[float, float, float]:
    """Return (iit, rate, quick_deduction) for a monthly taxable amount.

    月度应纳税所得额 → 个人所得税. Returns zero tax for non-positive
    taxable income.
    """
    if monthly_taxable <= 0.0:
        return 0.0, 0.0, 0.0
    for upper, rate, quick in _IIT_MONTHLY_BRACKETS:
        if monthly_taxable <= upper:
            return max(0.0, monthly_taxable * rate - quick), rate, quick
    # Unreachable: last bracket upper is inf.
    return 0.0, 0.0, 0.0


# ---------------------------------------------------------------------------
# Enums and dataclasses
# ---------------------------------------------------------------------------

class PayslipLineType(Enum):
    GROSS_SALARY = "工资 Gross salary"
    PENSION = "养老保险 Pension insurance"
    MEDICAL = "医疗保险 Medical insurance"
    UNEMPLOYMENT = "失业保险 Unemployment insurance"
    HOUSING_FUND = "住房公积金 Housing provident fund"
    IIT_WITHHOLDING = "个人所得税 IIT withholding"
    NET_SALARY = "实发工资 Net salary"
    EMPLOYER_CONTRIBUTION = "雇主缴纳 Employer contribution (note)"


@dataclass
class Employee:
    id: str
    name: str
    gross_salary: float = 0.0                    # 工资, monthly gross (¥)
    special_additional_deductions: float = 0.0   # 专项附加扣除 (monthly ¥)
    id_number: str = ""                          # 身份证号 — never logged


@dataclass
class PayslipLine:
    line_type: PayslipLineType
    label: str                       # human-readable, includes Chinese term
    amount: float                    # positive = income, negative = deduction


@dataclass
class Payslip:
    employee_id: str
    period: str                      # YYYY-MM
    employer_id: str = ""
    lines: list[PayslipLine] = field(default_factory=list)
    year: int = 2025

    # -- component accessors --------------------------------------------
    def _amount_for(self, line_type: PayslipLineType) -> float:
        return sum(l.amount for l in self.lines if l.line_type == line_type)

    @property
    def gross_salary(self) -> float:
        return self._amount_for(PayslipLineType.GROSS_SALARY)

    @property
    def pension(self) -> float:
        return -self._amount_for(PayslipLineType.PENSION)

    @property
    def medical(self) -> float:
        return -self._amount_for(PayslipLineType.MEDICAL)

    @property
    def unemployment(self) -> float:
        return -self._amount_for(PayslipLineType.UNEMPLOYMENT)

    @property
    def housing_fund(self) -> float:
        return -self._amount_for(PayslipLineType.HOUSING_FUND)

    @property
    def iit_withholding(self) -> float:
        return -self._amount_for(PayslipLineType.IIT_WITHHOLDING)

    @property
    def social_insurance_and_housing(self) -> float:
        """五险一金 total employee contribution."""
        return (self.pension + self.medical
                + self.unemployment + self.housing_fund)

    @property
    def net_salary(self) -> float:
        """实发工资 = gross - social/housing - IIT (employer note excluded)."""
        return sum(
            l.amount for l in self.lines
            if l.line_type != PayslipLineType.EMPLOYER_CONTRIBUTION
        )

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "period": self.period,
            "employer_id": self.employer_id,
            "year": self.year,
            "gross_salary": round(self.gross_salary, 2),
            "pension": round(self.pension, 2),
            "medical": round(self.medical, 2),
            "unemployment": round(self.unemployment, 2),
            "housing_fund": round(self.housing_fund, 2),
            "social_insurance_and_housing": round(
                self.social_insurance_and_housing, 2),
            "iit_withholding": round(self.iit_withholding, 2),
            "net_salary": round(self.net_salary, 2),
            "lines": [
                {
                    "line_type": l.line_type.value,
                    "label": l.label,
                    "amount": round(l.amount, 2),
                }
                for l in self.lines
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def generate_payslip(
    employee: Employee,
    period: str,
    employer_id: str = "",
    year: int = 2025,
) -> Payslip:
    """Generate a monthly Chinese payslip (工资明细).

    Computation order (employee side):
      1. Gross salary (工资) = employee.gross_salary.
      2. 五险一金 employee contributions on the gross base:
         - Pension 养老 8%, Medical 医疗 2%, Unemployment 失业 0.5%,
           Housing fund 住房公积金 7%.
      3. Monthly taxable = gross - social_insurance_and_housing
         - ¥5,000 basic deduction - special_additional_deductions.
      4. IIT (个人所得税) via monthly-equivalent progressive brackets.
      5. Net (实发工资) = gross - social/housing - IIT.

    Employer contributions (~16% pension + medical/unemployment/injury +
    matching housing fund) are added as an informational line only and do
    not affect net pay.
    """
    gross = employee.gross_salary

    # --- 五险一金 (base = gross; cap simplification) ---
    base = gross
    pension = base * PENSION_RATE
    medical = base * MEDICAL_RATE
    unemployment = base * UNEMPLOYMENT_RATE
    housing_fund = base * HOUSING_FUND_RATE
    social_total = pension + medical + unemployment + housing_fund

    # --- IIT taxable income ---
    monthly_taxable = (
        gross - social_total - IIT_BASIC_DEDUCTION
        - employee.special_additional_deductions
    )
    iit, rate, _quick = _compute_iit(monthly_taxable)

    # --- Employer contribution note (informational) ---
    employer_note = base * EMPLOYER_PENSION_RATE_NOTE + housing_fund

    lines: list[PayslipLine] = [
        PayslipLine(
            PayslipLineType.GROSS_SALARY,
            "工资 Gross salary",
            gross,
        ),
        PayslipLine(
            PayslipLineType.PENSION,
            f"养老保险 Pension ({PENSION_RATE * 100:.0f}%)",
            -pension,
        ),
        PayslipLine(
            PayslipLineType.MEDICAL,
            f"医疗保险 Medical ({MEDICAL_RATE * 100:.0f}%)",
            -medical,
        ),
        PayslipLine(
            PayslipLineType.UNEMPLOYMENT,
            f"失业保险 Unemployment ({UNEMPLOYMENT_RATE * 100:.1f}%)",
            -unemployment,
        ),
        PayslipLine(
            PayslipLineType.HOUSING_FUND,
            f"住房公积金 Housing fund ({HOUSING_FUND_RATE * 100:.0f}%)",
            -housing_fund,
        ),
        PayslipLine(
            PayslipLineType.IIT_WITHHOLDING,
            f"个人所得税 IIT withholding ({rate * 100:.0f}% bracket)",
            -iit,
        ),
        PayslipLine(
            PayslipLineType.EMPLOYER_CONTRIBUTION,
            f"雇主缴纳 Employer contribution (~{EMPLOYER_PENSION_RATE_NOTE * 100:.0f}% "
            f"pension + housing match, note only)",
            employer_note,
        ),
    ]

    return Payslip(
        employee_id=employee.id,
        period=period,
        employer_id=employer_id,
        lines=lines,
        year=year,
    )
