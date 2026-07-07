"""Federal Democratic Republic of Ethiopia corporate income tax calculator.

Ethiopia levies a flat **30%** business income tax on bodies (corporations)
under the Federal Income Tax Proclamation No. 979/2016, administered by the
Ministry of Revenues (MoR).

VAT is 15% under VAT Proclamation No. 1341/2024 (which modernised the 2002
VAT regime). Businesses below the VAT registration threshold pay Turnover
Tax (TOT) of 2% on goods / 10% on services instead — out of scope for this
profit-based SME estimator (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultET:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_ethiopie(
    winst: float,
    jaar: int,
) -> CITResultET:
    """Bereken Ethiopische vennootschapsbelasting (30% flat op winst).

    Args:
        winst: Belastbare winst in ETB.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultET dataclass.
    """
    CIT_RATE = 0.30

    if winst <= 0:
        return CITResultET(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultET(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
