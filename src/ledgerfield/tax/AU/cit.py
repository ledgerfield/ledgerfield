"""Australia Corporate Income Tax calculator."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CITResultAU:
    winst: float
    jaar: int
    base_rate_entity: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_australia(
    winst: float,
    jaar: int,
    base_rate_entity: bool = False,
) -> CITResultAU:
    """Bereken Australische vennootschapsbelasting.

    Args:
        winst: Belastbare winst in AUD.
        jaar: Belastingjaar (bijv. 2025 = FY2024-25).
        base_rate_entity: True als aggregated turnover < AUD 50M
                          (en passief inkomen <= 80% van assessable income).

    Returns:
        CITResultAU dataclass.
    """
    BASE_RATE = 0.25
    GENERAL_RATE = 0.30

    cit_rate = BASE_RATE if base_rate_entity else GENERAL_RATE

    if winst <= 0:
        return CITResultAU(
            winst=winst, jaar=jaar, base_rate_entity=base_rate_entity,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultAU(
        winst=winst,
        jaar=jaar,
        base_rate_entity=base_rate_entity,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
