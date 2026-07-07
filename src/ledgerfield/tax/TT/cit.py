"""Trinidad and Tobago corporate income tax calculator.

Trinidad and Tobago levies corporation tax under the Corporation Tax Act,
administered by the Inland Revenue Division (IRD):

* **30%** standard rate for most companies,
* **35%** for commercial banks and petrochemical companies,
* **50%** for petroleum production companies (Petroleum Profits Tax regime).

In addition, a **business levy of 0.6%** of gross revenue and a **green fund
levy of 0.3%** of gross revenue apply (the business levy is creditable
against corporation tax; the green fund levy is not) — both are noted in
params.json but out of scope for this profit-based SME estimator. VAT
applies at 12.5%.
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES: dict[str, float] = {
    "standard": 0.30,
    "banks_petrochemical": 0.35,
    "petroleum": 0.50,
}


@dataclass
class CITResultTT:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_trinidad(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultTT:
    """Bereken Trinidadiaanse vennootschapsbelasting (30% / 35% / 50%).

    Args:
        winst: Belastbare winst in TTD.
        jaar: Belastingjaar (bijv. 2025).
        sector: "standard" (30%), "banks_petrochemical" (35%) of
            "petroleum" (50%, Petroleum Profits Tax-regime).

    Returns:
        CITResultTT dataclass.

    Raises:
        ValueError: bij een onbekende sector.
    """
    if sector not in CIT_RATES:
        raise ValueError(
            f"Unknown sector {sector!r}; expected one of {sorted(CIT_RATES)}"
        )

    cit_rate = CIT_RATES[sector]

    if winst <= 0:
        return CITResultTT(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultTT(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
