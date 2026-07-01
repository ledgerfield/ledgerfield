"""New Zealand Corporate Income Tax calculator."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CITResultNZ:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_nz(
    winst: float,
    jaar: int,
) -> CITResultNZ:
    """Bereken Nieuw-Zeelandse vennootschapsbelasting.

    Args:
        winst: Belastbare winst in NZD.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultNZ dataclass.
    """
    CIT_RATE = 0.28  # flat rate

    if winst <= 0:
        return CITResultNZ(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultNZ(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
