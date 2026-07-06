"""Sultanate of Oman corporate income tax calculator.

Oman levies a flat **15%** corporate income tax (Royal Decree No. 28/2009 as
amended), administered by the Oman Tax Authority. Qualifying small enterprises
(registered capital <= OMR 50,000, <= 15 employees, gross income <= OMR
100,000, and sector conditions) benefit from a concessionary **3%** SME rate.

Petroleum income is taxed at a special 55% rate — out of scope for this SME
estimator (see params.json). Oman introduced 5% VAT in April 2021 (Royal
Decree No. 121/2020).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultOM:
    winst: float
    jaar: int
    sme: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_oman(
    winst: float,
    jaar: int,
    sme: bool = False,
) -> CITResultOM:
    """Bereken Omaanse vennootschapsbelasting (15% standaard, 3% SME-regime).

    Args:
        winst: Belastbare winst in OMR.
        jaar: Belastingjaar (bijv. 2025).
        sme: True indien de onderneming kwalificeert voor het 3% SME-regime
            (geregistreerd kapitaal <= OMR 50.000, <= 15 werknemers, bruto
            inkomen <= OMR 100.000, sectorvoorwaarden).

    Returns:
        CITResultOM dataclass.
    """
    STANDARD_RATE = 0.15
    SME_RATE = 0.03

    cit_rate = SME_RATE if sme else STANDARD_RATE

    if winst <= 0:
        return CITResultOM(
            winst=winst, jaar=jaar, sme=sme,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultOM(
        winst=winst,
        jaar=jaar,
        sme=sme,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
