"""Bulgaria corporate income tax calculator.

Bulgaria levies a flat **10%** corporate income tax (Corporate Income Tax
Act — Закон за корпоративното подоходно облагане), administered by the
National Revenue Agency (NRA / НАП). Personal income tax is likewise a flat
10%.

Despite the 10% headline rate, Bulgaria implemented the EU Pillar Two rules
(Directive (EU) 2022/2523) as of 2024, including a Qualified Domestic Minimum
Top-up Tax (QDMTT) for in-scope groups (consolidated revenue ≥ EUR 750m) —
out of scope for this SME estimator (see params.json).

Bulgaria adopts the euro on 1 January 2026; the target year 2025 still uses
the Bulgarian lev (BGN, pegged at 1.95583 BGN/EUR).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultBG:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_bulgarije(winst: float, jaar: int) -> CITResultBG:
    """Bereken Bulgaarse vennootschapsbelasting (10% flat).

    Args:
        winst: Belastbare winst in BGN.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultBG dataclass.
    """
    CIT_RATE = 0.10

    if winst <= 0:
        return CITResultBG(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultBG(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
