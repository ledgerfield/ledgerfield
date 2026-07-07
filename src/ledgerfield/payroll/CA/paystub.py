"""Paystub generator — Canada 2025 (federal + provincial, Ontario default).

Employee-side annual paystub with CPP, CPP2, EI and income tax deductions.
All amounts are annual unless noted. Province is a parameter; Ontario is the
default. Other provinces/territories have different rates and basic personal
amounts — see ``_PROVINCIAL_PARAMS`` and extend as needed.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum

__all__ = [
    "Employee", "LineType", "PaystubLine", "Paystub", "generate_paystub",
]

# ---------------------------------------------------------------------------
# Statutory parameters 2025 (federal, employee side)
# ---------------------------------------------------------------------------

# Canada Pension Plan (CPP)
_CPP_RATE = 0.0595            # 5.95% employee
_CPP_BASIC_EXEMPTION = 3500.0
_CPP_YMPE = 71300.0          # Year's Maximum Pensionable Earnings 2025

# CPP2 (second additional CPP)
_CPP2_RATE = 0.04            # 4.00%
_CPP2_LOWER = 71300.0        # starts at YMPE
_CPP2_UPPER = 81200.0        # Year's Additional Maximum Pensionable Earnings 2025

# Employment Insurance (EI) — outside Quebec
_EI_RATE = 0.0164            # 1.64% employee 2025
_EI_MAX_INSURABLE = 65700.0  # maximum insurable earnings 2025

# Federal income tax 2025: (upper_bound, rate)
_FEDERAL_BRACKETS: list[tuple[float, float]] = [
    (57375.0, 0.15),
    (114750.0, 0.205),
    (177882.0, 0.26),
    (253414.0, 0.29),
    (float("inf"), 0.33),
]
_FEDERAL_BPA = 16129.0       # federal basic personal amount 2025 (approx)

# Provincial income tax 2025: brackets + basic personal amount.
# Ontario is the default. Extend this table for other provinces/territories.
_PROVINCIAL_PARAMS: dict[str, dict] = {
    "ON": {
        "name": "Ontario",
        "brackets": [
            (52886.0, 0.0505),
            (105775.0, 0.0915),
            (150000.0, 0.1116),
            (220000.0, 0.1216),
            (float("inf"), 0.1316),
        ],
        "bpa": 12747.0,
    },
}


# ---------------------------------------------------------------------------
# Enums and dataclasses
# ---------------------------------------------------------------------------

class LineType(Enum):
    GROSS_PAY = "Gross pay"
    CPP = "CPP contribution"
    CPP2 = "CPP2 contribution"
    EI = "EI premium"
    FEDERAL_TAX = "Federal income tax"
    PROVINCIAL_TAX = "Provincial income tax"
    NET_PAY = "Net pay"


@dataclass
class Employee:
    id: str
    name: str
    sin: str = ""                 # Social Insurance Number — encrypted in vault, never logged
    gross_annual: float = 0.0
    province: str = "ON"          # Ontario default; injectable


@dataclass
class PaystubLine:
    kind: LineType
    description: str
    amount: float                 # positive = income, negative = deduction


@dataclass
class Paystub:
    employee_id: str
    period: str                   # e.g. "2025" (annual) or "YYYY-MM"
    year: int = 2025
    province: str = "ON"
    employer_id: str = ""
    lines: list[PaystubLine] = field(default_factory=list)

    def gross(self) -> float:
        return sum(l.amount for l in self.lines if l.kind == LineType.GROSS_PAY)

    def total_deductions(self) -> float:
        return -sum(l.amount for l in self.lines if l.amount < 0)

    def net(self) -> float:
        return sum(l.amount for l in self.lines)

    def _amount_for(self, kind: LineType) -> float:
        return sum(l.amount for l in self.lines if l.kind == kind)

    @property
    def cpp(self) -> float:
        return -self._amount_for(LineType.CPP)

    @property
    def cpp2(self) -> float:
        return -self._amount_for(LineType.CPP2)

    @property
    def ei(self) -> float:
        return -self._amount_for(LineType.EI)

    @property
    def federal_tax(self) -> float:
        return -self._amount_for(LineType.FEDERAL_TAX)

    @property
    def provincial_tax(self) -> float:
        return -self._amount_for(LineType.PROVINCIAL_TAX)

    @property
    def net_annual(self) -> float:
        return self.net()

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "period": self.period,
            "year": self.year,
            "province": self.province,
            "employer_id": self.employer_id,
            "gross_annual": round(self.gross(), 2),
            "cpp": round(self.cpp, 2),
            "cpp2": round(self.cpp2, 2),
            "ei": round(self.ei, 2),
            "federal_tax": round(self.federal_tax, 2),
            "provincial_tax": round(self.provincial_tax, 2),
            "total_deductions": round(self.total_deductions(), 2),
            "net_annual": round(self.net(), 2),
            "lines": [
                {
                    "kind": l.kind.value,
                    "description": l.description,
                    "amount": round(l.amount, 2),
                }
                for l in self.lines
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)


# ---------------------------------------------------------------------------
# Deduction calculations
# ---------------------------------------------------------------------------

def _calc_cpp(gross: float) -> float:
    """Base CPP: 5.95% of (min(gross, YMPE) - basic exemption), floored at 0."""
    pensionable = min(gross, _CPP_YMPE) - _CPP_BASIC_EXEMPTION
    return max(0.0, pensionable) * _CPP_RATE


def _calc_cpp2(gross: float) -> float:
    """CPP2: 4.00% of earnings between YMPE and YAMPE."""
    upper = min(gross, _CPP2_UPPER)
    band = upper - _CPP2_LOWER
    return max(0.0, band) * _CPP2_RATE


def _calc_ei(gross: float) -> float:
    """EI premium: 1.64% of insurable earnings up to the annual maximum."""
    return min(gross, _EI_MAX_INSURABLE) * _EI_RATE


def _bracket_tax(taxable: float, brackets: list[tuple[float, float]]) -> float:
    """Progressive tax over (upper_bound, rate) brackets."""
    tax = 0.0
    lower = 0.0
    for upper, rate in brackets:
        if taxable <= lower:
            break
        band = min(taxable, upper) - lower
        if band > 0:
            tax += band * rate
        lower = upper
    return tax


def _calc_federal_tax(gross: float) -> float:
    """Federal income tax: progressive brackets less credit on basic personal amount."""
    tax = _bracket_tax(gross, _FEDERAL_BRACKETS)
    lowest_rate = _FEDERAL_BRACKETS[0][1]
    credit = min(gross, _FEDERAL_BPA) * lowest_rate
    return max(0.0, tax - credit)


def _calc_provincial_tax(gross: float, province: str) -> float:
    """Provincial income tax: progressive brackets less BPA credit."""
    params = _PROVINCIAL_PARAMS.get(province)
    if params is None:
        raise ValueError(
            f"Unsupported province {province!r}; supported: "
            f"{sorted(_PROVINCIAL_PARAMS)}"
        )
    brackets = params["brackets"]
    tax = _bracket_tax(gross, brackets)
    lowest_rate = brackets[0][1]
    credit = min(gross, params["bpa"]) * lowest_rate
    return max(0.0, tax - credit)


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def generate_paystub(
    employee: Employee,
    period: str = "2025",
    year: int = 2025,
    province: str | None = None,
    employer_id: str = "",
) -> Paystub:
    """Generate an annual Canadian paystub with all employee-side deductions.

    Deductions computed (2025):
    - CPP  : 5.95% of (min(gross, YMPE $71,300) - $3,500 basic exemption)
    - CPP2 : 4.00% of earnings between $71,300 and $81,200
    - EI   : 1.64% of insurable earnings up to $65,700
    - Federal tax : 2025 brackets less basic-personal-amount credit
    - Provincial tax : province brackets less BPA credit (Ontario default)

    ``province`` overrides the employee's province when provided.
    """
    prov = province or employee.province or "ON"
    gross = employee.gross_annual

    cpp = _calc_cpp(gross)
    cpp2 = _calc_cpp2(gross)
    ei = _calc_ei(gross)
    federal_tax = _calc_federal_tax(gross)
    provincial_tax = _calc_provincial_tax(gross, prov)

    prov_name = _PROVINCIAL_PARAMS[prov]["name"]

    lines: list[PaystubLine] = [
        PaystubLine(LineType.GROSS_PAY, "Gross annual pay", gross),
        PaystubLine(LineType.CPP, f"CPP ({_CPP_RATE * 100:.2f}%)", -cpp),
        PaystubLine(LineType.CPP2, f"CPP2 ({_CPP2_RATE * 100:.2f}%)", -cpp2),
        PaystubLine(LineType.EI, f"EI premium ({_EI_RATE * 100:.2f}%)", -ei),
        PaystubLine(LineType.FEDERAL_TAX, "Federal income tax", -federal_tax),
        PaystubLine(
            LineType.PROVINCIAL_TAX,
            f"Provincial income tax ({prov_name})",
            -provincial_tax,
        ),
    ]

    return Paystub(
        employee_id=employee.id,
        period=period,
        year=year,
        province=prov,
        employer_id=employer_id,
        lines=lines,
    )
