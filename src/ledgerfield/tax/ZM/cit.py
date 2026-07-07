"""Republic of Zambia corporate income tax calculator.

Zambia levies a standard **30%** corporate income tax (Income Tax Act,
Cap. 323), administered by the Zambia Revenue Authority (ZRA). A reduced rate
of **10%** applies to income from farming and agro-processing.

Other sector regimes are out of scope for this SME estimator (see
params.json): hotels/tourism enjoy 15% on income from accommodation and food
services, mining companies fall under a variable-profit tax regime with
mineral royalties, and businesses with annual turnover up to K5,000,000 may
instead be subject to 5% turnover tax. VAT is 16%.
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES_ZM: dict[str, float] = {
    "standard": 0.30,
    "farming_agro": 0.10,
}


@dataclass
class CITResultZM:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_zambia(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultZM:
    """Bereken Zambiaanse vennootschapsbelasting (Income Tax Act, Cap. 323).

    Args:
        winst: Belastbare winst in ZMW (Zambiaanse kwacha).
        jaar: Belastingjaar (bijv. 2025).
        sector: Een van "standard" (30%) of "farming_agro" (10%, landbouw en
            agro-verwerking).

    Returns:
        CITResultZM dataclass.
    """
    if sector not in CIT_RATES_ZM:
        raise ValueError(
            f"unknown sector {sector!r}; expected one of {sorted(CIT_RATES_ZM)}"
        )

    cit_rate = CIT_RATES_ZM[sector]

    if winst <= 0:
        return CITResultZM(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultZM(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
