"""Republic of North Macedonia corporate income tax calculator.

North Macedonia levies a flat **10%** corporate income tax (Danok na dobivka),
administered by the Public Revenue Office (Uprava za javni prihodi, UJP).

Standard VAT is **18%**.

WARNING: rates in this pack are AI-estimated and must be source-verified
against the official tax authority before any production filing.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultMK:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_noord_macedonie(winst: float, jaar: int) -> CITResultMK:
    """Bereken Noord-Macedonische vennootschapsbelasting (10% flat).

    Args:
        winst: Belastbare winst in MKD (Macedonische denar).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultMK dataclass.
    """
    CIT_RATE = 0.10

    if winst <= 0:
        return CITResultMK(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultMK(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
