"""Socialist Republic of Vietnam corporate income tax calculator.

Vietnam levies a standard **20%** corporate income tax (Law on Corporate
Income Tax), administered by the General Department of Taxation (GDT).
Incentivized projects — notably hi-tech enterprises and projects in
incentivized sectors/zones — qualify for a preferential **10%** rate for
**15 years** (15% and 17% preferential tiers also exist for other
categories).

Oil & gas and other extractive operations are taxed at agreement-based
rates of 32–50% — out of scope for this SME estimator (see params.json).
The revised CIT Law (effective Oct 2025, applying from FY2026) enacts
small-enterprise rates of 15%/17% by revenue — note-only here.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultVN:
    winst: float
    jaar: int
    hi_tech: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_vietnam(
    winst: float,
    jaar: int,
    hi_tech: bool = False,
) -> CITResultVN:
    """Bereken Vietnamese vennootschapsbelasting (20% standaard, 10% hi-tech).

    Args:
        winst: Belastbare winst in VND.
        jaar: Belastingjaar (bijv. 2025).
        hi_tech: True indien het een hi-tech / geïncentiveerd project betreft
            dat kwalificeert voor het preferentiële 10%-tarief (15 jaar).

    Returns:
        CITResultVN dataclass.
    """
    STANDARD_RATE = 0.20
    HI_TECH_RATE = 0.10

    cit_rate = HI_TECH_RATE if hi_tech else STANDARD_RATE

    if winst <= 0:
        return CITResultVN(
            winst=winst, jaar=jaar, hi_tech=hi_tech,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultVN(
        winst=winst,
        jaar=jaar,
        hi_tech=hi_tech,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
