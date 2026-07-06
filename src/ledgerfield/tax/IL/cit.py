"""State of Israel corporate income tax calculator.

Israel levies a flat **23%** corporate income tax (Income Tax Ordinance),
administered by the Israel Tax Authority. Preferred Enterprise / Special
Preferred Enterprise regimes under the Encouragement of Capital Investments
Law offer reduced rates (16%, or 7.5% in development area A) — captured in
params.json as special_rates; out of scope for this SME estimator's flat
calculation.

The 3% surtax (mas yesef) applies to *individuals* above the annual threshold
(~NIS 721,560 in 2025) — it is personal income tax, not corporate, and is
recorded under personal_income_tax in params.json.

VAT was raised from 17% to **18% effective 1 January 2025** (approved
October 2024).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultIL:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_israel(winst: float, jaar: int) -> CITResultIL:
    """Bereken Israëlische vennootschapsbelasting (23% flat).

    Args:
        winst: Belastbare winst in ILS (NIS).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultIL dataclass.
    """
    CIT_RATE = 0.23

    if winst <= 0:
        return CITResultIL(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultIL(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
