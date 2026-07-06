"""Islamic Republic of Pakistan corporate income tax calculator.

Pakistan taxes companies under the **Income Tax Ordinance 2001**, administered
by the Federal Board of Revenue (FBR). For tax year 2025 (TY2025):

* Standard company rate: **29%**.
* Small company rate: **20%** (paid-up capital plus reserves <= PKR 50m,
  employees <= 250, annual turnover <= PKR 250m).
* Banking companies: **39%** (and subject to a higher super tax).

A progressive **super tax** (section 4C) of 0-10% applies on high incomes
(top 10% for income above PKR 500m) — noted in params.json but not modelled
here to keep the SME estimator clean. Pakistan operates a withholding-tax
(WHT) heavy regime; sales tax on goods (GST) is 18% standard at federal
level, with provincial sales taxes on services of roughly 13-16%.
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES: dict[str, float] = {
    "standard": 0.29,
    "small": 0.20,
    "banking": 0.39,
}


@dataclass
class CITResultPK:
    winst: float
    jaar: int
    company_type: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_pakistan(
    winst: float,
    jaar: int,
    company_type: str = "standard",
) -> CITResultPK:
    """Bereken Pakistaanse vennootschapsbelasting (Income Tax Ordinance 2001).

    Args:
        winst: Belastbare winst in PKR.
        jaar: Belastingjaar (bijv. 2025, TY2025).
        company_type: "standard" (29%), "small" (20%; paid-up capital +
            reserves <= PKR 50m, employees <= 250, turnover <= PKR 250m)
            of "banking" (39%).

    Returns:
        CITResultPK dataclass.

    Note:
        De progressieve super tax (s.4C, 0-10%, top 10% boven PKR 500m
        inkomen) is niet gemodelleerd; zie params.json.
    """
    if company_type not in CIT_RATES:
        raise ValueError(
            f"unknown company_type {company_type!r}; "
            f"expected one of {sorted(CIT_RATES)}"
        )

    cit_rate = CIT_RATES[company_type]

    if winst <= 0:
        return CITResultPK(
            winst=winst, jaar=jaar, company_type=company_type,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultPK(
        winst=winst,
        jaar=jaar,
        company_type=company_type,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
