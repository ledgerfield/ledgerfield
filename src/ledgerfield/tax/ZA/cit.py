"""South Africa Corporate Income Tax calculator."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CITResultZA:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_south_africa(
    winst: float,
    jaar: int,
) -> CITResultZA:
    """Bereken Zuid-Afrikaanse vennootschapsbelasting.

    Args:
        winst: Belastbare winst in ZAR.
        jaar: Belastingjaar (bijv. 2025 = jaar eindigend 31 maart 2025).

    Returns:
        CITResultZA dataclass.

    Notes:
        CIT rate reduced from 28% to 27% effective 1 April 2022
        (years of assessment ending on or after 31 March 2023).
        Small Business Corporations (SBC) have tiered rates but
        this calculator uses the standard company rate.
    """
    CIT_RATE = 0.27

    if winst <= 0:
        return CITResultZA(
            winst=winst,
            jaar=jaar,
            cit_rate=CIT_RATE,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultZA(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
