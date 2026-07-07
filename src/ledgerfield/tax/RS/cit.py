"""Republic of Serbia corporate income tax calculator.

Serbia levies a flat **15%** corporate income tax (porez na dobit pravnih lica),
administered by the Tax Administration (Poreska uprava). The standard VAT (PDV)
rate is **20%**.

NOTE: Rates in this module are AI-estimated for the 2025 target period and have
not been verified against primary sources. See params.json metadata
(source_status = "ai_estimated_needs_verification"). Verify with the Poreska
uprava (https://www.purs.gov.rs/) and a local advisor before any real use.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultRS:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_servie(winst: float, jaar: int) -> CITResultRS:
    """Bereken Servische vennootschapsbelasting (15% flat).

    Args:
        winst: Belastbare winst in RSD.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultRS dataclass.
    """
    CIT_RATE = 0.15

    if winst <= 0:
        return CITResultRS(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultRS(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
