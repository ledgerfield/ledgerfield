"""Republic of Ghana corporate income tax calculator.

Ghana levies a **25%** standard corporate income tax (Income Tax Act, 2015,
Act 896, as amended), administered by the Ghana Revenue Authority (GRA).
Sector-specific rates apply: mining and upstream petroleum operations are
taxed at **35%**, while hotels are taxed at **22%**.

On top of CIT, the **Growth & Sustainability Levy (GSL)** applies at **5% of
profit before tax** for most sectors (2023-2025; banks and mining fall into
higher bands — simplified to the 5% standard band in this SME estimator).

VAT (see params.json) is a standard 15% plus non-deductible levies: NHIL 2.5%,
GETFund 2.5% and COVID-19 levy 1%, giving an effective rate of roughly 21.9%.
The 2025 reform announced abolition of the COVID-19 levy.
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.25,
    "mining_petroleum": 0.35,
    "hotels": 0.22,
}

GSL_RATE = 0.05


@dataclass
class CITResultGH:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_bedrag: float
    gsl_rate: float
    gsl_bedrag: float
    totaal_bedrag: float
    effectief_tarief: float


def bereken_cit_ghana(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultGH:
    """Bereken Ghanese vennootschapsbelasting plus Growth & Sustainability Levy.

    Args:
        winst: Belastbare winst (winst vóór belasting) in GHS.
        jaar: Belastingjaar (bijv. 2025).
        sector: Sector — "standard" (25%), "mining_petroleum" (35%) of
            "hotels" (22%).

    Returns:
        CITResultGH dataclass met cit_bedrag, gsl_bedrag (5% van winst) en
        totaal_bedrag.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    cit_rate = SECTOR_RATES[sector]

    if winst <= 0:
        return CITResultGH(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_bedrag=0.0,
            gsl_rate=GSL_RATE, gsl_bedrag=0.0,
            totaal_bedrag=0.0, effectief_tarief=0.0,
        )

    cit_bedrag = winst * cit_rate
    gsl_bedrag = winst * GSL_RATE
    totaal_bedrag = cit_bedrag + gsl_bedrag
    effectief_tarief = totaal_bedrag / winst

    return CITResultGH(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_bedrag=cit_bedrag,
        gsl_rate=GSL_RATE,
        gsl_bedrag=gsl_bedrag,
        totaal_bedrag=totaal_bedrag,
        effectief_tarief=effectief_tarief,
    )
