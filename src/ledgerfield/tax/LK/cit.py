"""Sri Lanka corporate income tax calculator.

Sri Lanka levies corporate income tax under the Inland Revenue Act No. 24 of
2017 (as amended 2022-2025), administered by the Inland Revenue Department
(IRD). The standard CIT rate is **30%**.

Sector rates for the 2025 target period:

* ``standard`` — 30% general corporate rate.
* ``export_services`` — 15% on qualifying export of services (introduced by
  the 2025 budget; such income was previously exempt / zero-rated).
* ``betting_liquor_tobacco`` — 45% on betting and gaming, liquor and tobacco
  businesses.

VAT is 18% (from 1 January 2024, up from 15%); the announced SVAT abolition
has been postponed. A Social Security Contribution Levy (SSCL) of 2.5% applies
on turnover (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.30,
    "export_services": 0.15,
    "betting_liquor_tobacco": 0.45,
}


@dataclass
class CITResultLK:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_srilanka(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultLK:
    """Bereken Sri Lankaanse vennootschapsbelasting (30% standaard).

    Args:
        winst: Belastbare winst in LKR.
        jaar: Belastingjaar (bijv. 2025).
        sector: Een van "standard" (30%), "export_services" (15%) of
            "betting_liquor_tobacco" (45%).

    Returns:
        CITResultLK dataclass.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    cit_rate = SECTOR_RATES[sector]

    if winst <= 0:
        return CITResultLK(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultLK(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
