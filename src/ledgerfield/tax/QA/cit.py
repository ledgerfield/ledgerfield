"""State of Qatar corporate income tax calculator.

Qatar levies a flat **10%** corporate income tax (Law No. 24 of 2018),
administered by the General Tax Authority (GTA). The tax applies to the profit
share attributable to *foreign (non-GCC)* ownership; wholly Qatari / GCC-owned
entities are, as a rule, exempt from CIT.

Petroleum and petrochemical operations are taxed at higher agreement-based
rates (typically 35%) — out of scope for this SME estimator (see params.json).
Qatar has not implemented VAT as of the target period.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultQA:
    winst: float
    jaar: int
    foreign_ownership_share: float
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_qatar(
    winst: float,
    jaar: int,
    foreign_ownership_share: float = 1.0,
) -> CITResultQA:
    """Bereken Qatarese vennootschapsbelasting (10% flat op buitenlands aandeel).

    Args:
        winst: Belastbare winst in QAR.
        jaar: Belastingjaar (bijv. 2025).
        foreign_ownership_share: Aandeel niet-GCC (buitenlandse) eigenaren,
            tussen 0.0 (volledig Qatarees/GCC, vrijgesteld) en 1.0.

    Returns:
        CITResultQA dataclass.
    """
    if not 0.0 <= foreign_ownership_share <= 1.0:
        raise ValueError("foreign_ownership_share must be between 0.0 and 1.0")

    CIT_RATE = 0.10

    if winst <= 0:
        return CITResultQA(
            winst=winst, jaar=jaar, foreign_ownership_share=foreign_ownership_share,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * foreign_ownership_share * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultQA(
        winst=winst,
        jaar=jaar,
        foreign_ownership_share=foreign_ownership_share,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
