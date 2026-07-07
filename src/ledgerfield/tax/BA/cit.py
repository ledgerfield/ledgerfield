"""Bosnia and Herzegovina corporate income tax calculator.

Bosnia and Herzegovina has a two-entity fiscal system. Corporate income tax is
levied at the entity level, but both entities apply the same flat rate of
**10%**:

* Federation of Bosnia and Herzegovina (FBiH) — 10%.
* Republika Srpska (RS) — 10%.

(The Brčko District broadly follows entity rules.) Indirect taxation — value
added tax at **17%** — is unified and administered state-wide by the Indirect
Taxation Authority (UINO/ITA). Because the profit-tax rate is identical across
entities, this estimator applies a single flat 10% regardless of entity.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultBA:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_bosnie(winst: float, jaar: int) -> CITResultBA:
    """Bereken Bosnische vennootschapsbelasting (vlak 10%, beide entiteiten).

    Args:
        winst: Belastbare winst in BAM.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultBA dataclass. Niet-positieve winst levert 0 belasting op.
        Zowel FBiH als Republika Srpska hanteren 10%, dus entiteit is niet
        van invloed op het tarief.
    """
    CIT_RATE = 0.10

    if winst <= 0:
        return CITResultBA(
            winst=winst,
            jaar=jaar,
            cit_rate=CIT_RATE,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultBA(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
