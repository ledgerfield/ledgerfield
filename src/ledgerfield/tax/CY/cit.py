"""Republic of Cyprus corporate income tax calculator.

Cyprus levies a flat **12.5%** corporate income tax (Income Tax Law
118(I)/2002, as amended), administered by the Tax Department (Ministry of
Finance). Notable regimes (informational, out of scope for this SME
estimator):

- **IP box**: 80% exemption on qualifying IP profits (nexus approach),
  yielding an effective rate as low as 2.5%.
- **Tonnage tax**: qualifying shipping companies are taxed on tonnage
  instead of profit (Merchant Shipping Law).
- **Planned reform**: a 15% CIT rate has been announced as part of the
  Cyprus tax reform, but is not yet law within the target period (2025).

A Special Defence Contribution (SDC) applies to passive income of
Cyprus-resident and domiciled persons (dividends 17%, interest 17%, rents)
— see params.json.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultCY:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_cyprus(winst: float, jaar: int) -> CITResultCY:
    """Bereken Cypriotische vennootschapsbelasting (12,5% vlak tarief).

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultCY dataclass.
    """
    CIT_RATE = 0.125

    if winst <= 0:
        return CITResultCY(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultCY(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
