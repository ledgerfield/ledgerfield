"""People's Republic of Bangladesh corporate income tax calculator.

Bangladesh levies corporate income tax under the Income Tax Act 2023,
administered by the National Board of Revenue (NBR). Rates for FY2024-25:

* Non-listed company: **27.5%** (conditionally 25% when *all* receipts and
  expenses are routed through the banking channel — see params.json note).
* Listed company: **22.5%** (25% if less than 10% of shares floated via IPO).
* Banks / insurance / NBFIs: **37.5%** (listed) / **40%** (non-listed).
* Mobile phone operators and tobacco manufacturers: **45%**.

A minimum tax of 0.6% on gross receipts may apply regardless of profit —
out of scope for this SME estimator (see params.json). VAT is 15% standard
(VAT & SD Act 2012), with reduced 5% / 7.5% / 10% bands for specific supplies.
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES_BD: dict[str, float] = {
    "non_listed": 0.275,
    "listed": 0.225,
    "bank_listed": 0.375,
    "bank_non_listed": 0.40,
    "mobile_tobacco": 0.45,
}


@dataclass
class CITResultBD:
    winst: float
    jaar: int
    company_type: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_bangladesh(
    winst: float,
    jaar: int,
    company_type: str = "non_listed",
) -> CITResultBD:
    """Bereken Bengaalse vennootschapsbelasting (Income Tax Act 2023, FY2024-25).

    Args:
        winst: Belastbare winst in BDT.
        jaar: Belastingjaar (bijv. 2025, d.w.z. FY2024-25).
        company_type: Een van "non_listed" (27.5%), "listed" (22.5%),
            "bank_listed" (37.5%), "bank_non_listed" (40%),
            "mobile_tobacco" (45%).

    Returns:
        CITResultBD dataclass.
    """
    if company_type not in CIT_RATES_BD:
        raise ValueError(
            f"unknown company_type {company_type!r}; "
            f"expected one of {sorted(CIT_RATES_BD)}"
        )

    cit_rate = CIT_RATES_BD[company_type]

    if winst <= 0:
        return CITResultBD(
            winst=winst, jaar=jaar, company_type=company_type,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultBD(
        winst=winst,
        jaar=jaar,
        company_type=company_type,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
