"""Myanmar corporate income tax calculator.

Myanmar levies a **22%** corporate income tax under the Union Tax Law (2022
onwards, reduced from 25%), administered by the Internal Revenue Department
(IRD). Companies listed on the Yangon Stock Exchange (YSX) enjoy a reduced
**17%** rate. Oil and gas exploration/production is taxed at 25% per
production-sharing terms — out of scope for this SME estimator.

Myanmar has no VAT; instead a **Commercial Tax** (generally 5%, 0–8% band)
applies to goods and services, with an excise-like Specific Goods Tax (SGT)
on tobacco, liquor and vehicles. The fiscal year runs October–September
(FY2024-25).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultMM:
    winst: float
    jaar: int
    ysx_listed: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_myanmar(
    winst: float,
    jaar: int,
    ysx_listed: bool = False,
) -> CITResultMM:
    """Bereken Myanmarese vennootschapsbelasting (22% standaard, 17% YSX-genoteerd).

    Args:
        winst: Belastbare winst in MMK.
        jaar: Belastingjaar (bijv. 2025; fiscaal jaar loopt oktober–september).
        ysx_listed: True als de vennootschap genoteerd is aan de Yangon Stock
            Exchange (verlaagd tarief van 17%).

    Returns:
        CITResultMM dataclass.
    """
    STANDARD_RATE = 0.22
    YSX_LISTED_RATE = 0.17

    cit_rate = YSX_LISTED_RATE if ysx_listed else STANDARD_RATE

    if winst <= 0:
        return CITResultMM(
            winst=winst, jaar=jaar, ysx_listed=ysx_listed,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultMM(
        winst=winst,
        jaar=jaar,
        ysx_listed=ysx_listed,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
