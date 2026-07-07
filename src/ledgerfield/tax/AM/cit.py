"""Republic of Armenia corporate (profit) tax calculator.

Armenia levies a flat **18%** profit tax (Corporate Income / Profit Tax),
administered by the State Revenue Committee (SRC / Petekamutner). The tax
applies to the taxable profit of resident entities.

Alternative simplified regimes exist for smaller taxpayers — a turnover tax
and a micro-business regime — which replace profit tax below certain revenue
thresholds (see params.json). This SME estimator models the standard 18%
profit tax only.

Armenia applies a standard **20%** VAT.

WARNING: Rates in this pack are AI-estimated and MUST be verified against the
State Revenue Committee before any production filing (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultAM:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_armenie(winst: float, jaar: int) -> CITResultAM:
    """Bereken Armeense winstbelasting (18% flat).

    Args:
        winst: Belastbare winst in AMD.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultAM dataclass. Niet-positieve winst levert nul belasting.
    """
    CIT_RATE = 0.18

    if winst <= 0:
        return CITResultAM(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultAM(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
