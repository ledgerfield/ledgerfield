"""Canada Corporate Income Tax calculator."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CITResultCA:
    winst: float
    jaar: int
    is_ccpc: bool
    small_business_income: float
    general_income: float
    cit_small_business: float
    cit_general: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_canada(winst: float, jaar: int, is_ccpc: bool = True) -> CITResultCA:
    """Bereken Canadese vennootschapsbelasting.

    Args:
        winst: Belastbare winst in CAD.
        jaar: Belastingjaar (momenteel 2025 ondersteund).
        is_ccpc: True als Canadian-Controlled Private Corporation (small business deduction).

    Returns:
        CITResultCA dataclass met uitsplitsing.
    """
    SMALL_BUSINESS_RATE = 0.09
    GENERAL_RATE = 0.15
    SMALL_BUSINESS_LIMIT = 500_000.0

    if winst <= 0:
        return CITResultCA(
            winst=winst, jaar=jaar, is_ccpc=is_ccpc,
            small_business_income=0.0, general_income=0.0,
            cit_small_business=0.0, cit_general=0.0,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    if is_ccpc:
        small_business_income = min(winst, SMALL_BUSINESS_LIMIT)
        general_income = max(0.0, winst - SMALL_BUSINESS_LIMIT)
        cit_small_business = small_business_income * SMALL_BUSINESS_RATE
        cit_general = general_income * GENERAL_RATE
    else:
        small_business_income = 0.0
        general_income = winst
        cit_small_business = 0.0
        cit_general = general_income * GENERAL_RATE

    cit_totaal = cit_small_business + cit_general
    effectief_tarief = cit_totaal / winst if winst else 0.0

    return CITResultCA(
        winst=winst,
        jaar=jaar,
        is_ccpc=is_ccpc,
        small_business_income=small_business_income,
        general_income=general_income,
        cit_small_business=cit_small_business,
        cit_general=cit_general,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
