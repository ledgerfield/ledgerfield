"""Republic of Kazakhstan corporate income tax calculator.

Kazakhstan levies a flat **20%** corporate income tax (CIT), in Kazakh/Russian
"КПН" (corporate income tax), administered by the State Revenue Committee of the
Ministry of Finance. Value Added Tax (VAT / НДС) applies at a standard **12%**.

Subsurface users (mining, oil & gas) are subject to additional special taxes
(excess-profit tax, mineral extraction tax) beyond standard CIT — out of scope
for this SME estimator (see params.json).

A new Tax Code has been adopted that raises certain rates from 2026 (notably a
higher standard CIT/VAT trajectory for some sectors); this estimator models the
2025 standard flat 20% CIT only.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultKZ:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_kazachstan(winst: float, jaar: int) -> CITResultKZ:
    """Bereken Kazachse vennootschapsbelasting (КПН, 20% flat).

    Args:
        winst: Belastbare winst in KZT.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultKZ dataclass. Bij niet-positieve winst is de belasting 0.
    """
    CIT_RATE = 0.20

    if winst <= 0:
        return CITResultKZ(
            winst=winst,
            jaar=jaar,
            cit_rate=CIT_RATE,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultKZ(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
