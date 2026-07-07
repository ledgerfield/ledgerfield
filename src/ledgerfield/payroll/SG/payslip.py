"""Payslip generator — Singapore 2025 (monthly, CPF).

Singapore payroll characteristics modelled here:

- CPF (Central Provident Fund) contributions are made by both employee and
  employer on Ordinary Wages (OW) up to the OW ceiling. From January 2025 the
  monthly OW ceiling is S$7,400. Rates depend on the employee's age band; the
  default (age 55 and below) is 20% employee / 17% employer.
- There is NO monthly income-tax withholding in Singapore. Personal income tax
  is assessed annually by IRAS; the employer files form IR8A. Therefore net pay
  is simply gross - employee CPF.
- SDL (Skills Development Levy) is an employer-only levy of 0.25% of gross
  (minimum S$2, maximum S$11.25 per employee per month). It does not affect net
  pay; it is shown as information only.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum

__all__ = [
    "AgeBand", "Employee", "PayslipLineType", "PayslipLine", "Payslip",
    "generate_payslip",
]

# ---------------------------------------------------------------------------
# Constants (2025)
# ---------------------------------------------------------------------------

# Ordinary Wages ceiling: CPF is only levied on wages up to this amount.
OW_CEILING_MONTHLY = 7400.0        # S$/month, effective Jan 2025

# Skills Development Levy (employer only)
SDL_RATE = 0.0025                  # 0.25%
SDL_MIN = 2.0                      # S$
SDL_MAX = 11.25                    # S$

INCOME_TAX_NOTE = (
    "No monthly income tax is withheld in Singapore. Personal income tax is "
    "assessed annually by IRAS; the employer files form IR8A."
)


class AgeBand(Enum):
    """CPF contribution age bands with (employee_rate, employer_rate).

    Rates are the 2025 statutory CPF percentages on Ordinary Wages. Older bands
    have progressively lower rates than the default (age 55 and below).
    """
    UP_TO_55 = (0.20, 0.17)
    ABOVE_55_TO_60 = (0.17, 0.155)
    ABOVE_60_TO_65 = (0.115, 0.12)
    ABOVE_65_TO_70 = (0.075, 0.09)
    ABOVE_70 = (0.05, 0.075)

    @property
    def employee_rate(self) -> float:
        return self.value[0]

    @property
    def employer_rate(self) -> float:
        return self.value[1]


# ---------------------------------------------------------------------------
# Enums and dataclasses
# ---------------------------------------------------------------------------

class PayslipLineType(Enum):
    GROSS_SALARY = "Gross salary"
    CPF_EMPLOYEE = "CPF contribution (employee)"
    CPF_EMPLOYER = "CPF contribution (employer)"
    SDL_EMPLOYER = "Skills Development Levy (employer)"
    NET_SALARY = "Net salary"


@dataclass
class Employee:
    id: str
    name: str
    gross_salary: float = 0.0                 # monthly gross (Ordinary Wages)
    age_band: AgeBand = AgeBand.UP_TO_55
    is_cpf_eligible: bool = True              # citizens / PRs contribute CPF


@dataclass
class PayslipLine:
    line_type: PayslipLineType
    description: str
    amount: float                             # positive = pay/cost, negative = deduction


@dataclass
class Payslip:
    employee_id: str
    period: str                               # YYYY-MM
    employee_name: str = ""
    lines: list[PayslipLine] = field(default_factory=list)
    income_tax_note: str = INCOME_TAX_NOTE
    year: int = 2025

    def gross_salary(self) -> float:
        return sum(
            ln.amount for ln in self.lines
            if ln.line_type is PayslipLineType.GROSS_SALARY
        )

    def cpf_employee(self) -> float:
        """Employee CPF as a positive amount."""
        return -sum(
            ln.amount for ln in self.lines
            if ln.line_type is PayslipLineType.CPF_EMPLOYEE
        )

    def cpf_employer(self) -> float:
        return sum(
            ln.amount for ln in self.lines
            if ln.line_type is PayslipLineType.CPF_EMPLOYER
        )

    def sdl_employer(self) -> float:
        return sum(
            ln.amount for ln in self.lines
            if ln.line_type is PayslipLineType.SDL_EMPLOYER
        )

    def net_salary(self) -> float:
        """Net pay to the employee: gross minus employee CPF.

        Employer-side lines (employer CPF, SDL) are informational and do not
        reduce net pay.
        """
        return self.gross_salary() - self.cpf_employee()

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "employee_name": self.employee_name,
            "period": self.period,
            "year": self.year,
            "gross_salary": round(self.gross_salary(), 2),
            "cpf_employee": round(self.cpf_employee(), 2),
            "cpf_employer": round(self.cpf_employer(), 2),
            "sdl_employer": round(self.sdl_employer(), 2),
            "net_salary": round(self.net_salary(), 2),
            "income_tax_note": self.income_tax_note,
            "lines": [
                {
                    "line_type": ln.line_type.value,
                    "description": ln.description,
                    "amount": round(ln.amount, 2),
                }
                for ln in self.lines
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)


# ---------------------------------------------------------------------------
# Calculation helpers
# ---------------------------------------------------------------------------

def _cpf_wage_base(gross: float) -> float:
    """Ordinary Wages subject to CPF: capped at the monthly OW ceiling."""
    return min(max(gross, 0.0), OW_CEILING_MONTHLY)


def _sdl(gross: float) -> float:
    """Skills Development Levy (employer): 0.25%, min S$2, max S$11.25.

    Zero gross yields zero levy (no wage, no levy).
    """
    if gross <= 0.0:
        return 0.0
    return min(max(gross * SDL_RATE, SDL_MIN), SDL_MAX)


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def generate_payslip(employee: Employee, period: str, year: int = 2025) -> Payslip:
    """Generate a monthly Singapore payslip.

    - CPF employee/employer = age-band rate x min(gross, OW ceiling S$7,400)
    - Net pay = gross - employee CPF (no monthly income-tax withholding)
    - Employer CPF and SDL are shown as information only
    """
    gross = employee.gross_salary

    if employee.is_cpf_eligible:
        wage_base = _cpf_wage_base(gross)
        cpf_ee = wage_base * employee.age_band.employee_rate
        cpf_er = wage_base * employee.age_band.employer_rate
    else:
        cpf_ee = 0.0
        cpf_er = 0.0

    sdl = _sdl(gross)

    lines: list[PayslipLine] = []

    lines.append(PayslipLine(
        PayslipLineType.GROSS_SALARY,
        "Gross monthly salary",
        gross,
    ))

    # Employee CPF is a deduction from gross (negative).
    lines.append(PayslipLine(
        PayslipLineType.CPF_EMPLOYEE,
        f"CPF employee ({employee.age_band.employee_rate * 100:.1f}% on OW, "
        f"capped at S${OW_CEILING_MONTHLY:,.0f})",
        -cpf_ee,
    ))

    # Employer CPF (informational — employer cost, not deducted from net).
    lines.append(PayslipLine(
        PayslipLineType.CPF_EMPLOYER,
        f"CPF employer ({employee.age_band.employer_rate * 100:.1f}% on OW, info)",
        cpf_er,
    ))

    # SDL (informational — employer levy).
    lines.append(PayslipLine(
        PayslipLineType.SDL_EMPLOYER,
        f"Skills Development Levy ({SDL_RATE * 100:.2f}%, min S${SDL_MIN:.0f}, "
        f"max S${SDL_MAX:.2f}, info)",
        sdl,
    ))

    net = gross - cpf_ee
    lines.append(PayslipLine(
        PayslipLineType.NET_SALARY,
        "Net salary (gross - employee CPF; no income tax withheld)",
        net,
    ))

    return Payslip(
        employee_id=employee.id,
        employee_name=employee.name,
        period=period,
        lines=lines,
        income_tax_note=INCOME_TAX_NOTE,
        year=year,
    )
