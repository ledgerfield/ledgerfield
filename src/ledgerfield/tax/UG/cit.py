"""Republic of Uganda corporate income tax calculator.

Uganda levies a flat **30%** corporate income tax (Income Tax Act, Cap 340),
administered by the Uganda Revenue Authority (URA). The 30% rate applies to
resident companies and to branches of non-resident companies alike (branches
are additionally subject to a repatriated-income tax — out of scope for this
SME estimator, see params.json).

Uganda's VAT standard rate is 18%. Small businesses below the VAT threshold
may fall under a presumptive turnover-based regime, and a 5% Digital Services
Tax applies to non-residents deriving income from digital services provided
to Ugandan consumers.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultUG:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_oeganda(
    winst: float,
    jaar: int,
) -> CITResultUG:
    """Bereken Oegandese vennootschapsbelasting (30% flat).

    Args:
        winst: Belastbare winst in UGX.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultUG dataclass.
    """
    CIT_RATE = 0.30

    if winst <= 0:
        return CITResultUG(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultUG(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
