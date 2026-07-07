"""Republic of Albania corporate income tax calculator.

Albania levies a flat **15%** corporate income tax (Tatimi mbi Fitimin),
administered by the General Directorate of Taxes (Drejtoria e Pergjithshme e
Tatimeve). Historically, small businesses with annual turnover at or below
ALL 14 million benefited from a 0% CIT rate; this SME estimator applies the
standard 15% flat rate (see params.json for the small-business note).

Standard VAT is **20%**.

WARNING: rates in this pack are AI-estimated and must be source-verified
against the official tax authority before any production filing.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultAL:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_albanie(winst: float, jaar: int) -> CITResultAL:
    """Bereken Albanese vennootschapsbelasting (15% flat).

    Args:
        winst: Belastbare winst in ALL (Albanese lek).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultAL dataclass.
    """
    CIT_RATE = 0.15

    if winst <= 0:
        return CITResultAL(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultAL(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
