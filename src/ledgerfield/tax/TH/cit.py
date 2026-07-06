"""Thailand corporate income tax calculator.

Thailand levies a flat **20%** corporate income tax on net profit under the
Revenue Code, administered by The Revenue Department.

Qualifying SMEs (paid-up capital <= THB 5 million AND revenue from the sale of
goods and services <= THB 30 million in the accounting period) are taxed under
progressive brackets on net profit:

* first THB 300,000 — exempt (0%)
* THB 300,001 – 3,000,000 — 15%
* above THB 3,000,000 — 20%

VAT is 7% (the statutory rate is 10%, temporarily reduced by repeated royal
decree extensions — the current extension runs through September 2025).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultTH:
    winst: float
    jaar: int
    sme: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


SME_BRACKET_EXEMPT_TOP = 300_000.0
SME_BRACKET_MID_TOP = 3_000_000.0
SME_MID_RATE = 0.15
STANDARD_RATE = 0.20


def bereken_cit_thailand(
    winst: float,
    jaar: int,
    sme: bool = False,
) -> CITResultTH:
    """Bereken Thaise vennootschapsbelasting (Revenue Code).

    Args:
        winst: Belastbare nettowinst in THB.
        jaar: Belastingjaar (bijv. 2025).
        sme: True voor kwalificerende SME (gestort kapitaal <= THB 5 mln EN
            omzet <= THB 30 mln) — progressieve schijven; anders vlak 20%.

    Returns:
        CITResultTH dataclass.
    """
    if winst <= 0:
        return CITResultTH(
            winst=winst, jaar=jaar, sme=sme,
            cit_rate=STANDARD_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    if sme:
        cit_totaal = 0.0
        if winst > SME_BRACKET_EXEMPT_TOP:
            mid_base = min(winst, SME_BRACKET_MID_TOP) - SME_BRACKET_EXEMPT_TOP
            cit_totaal += mid_base * SME_MID_RATE
        if winst > SME_BRACKET_MID_TOP:
            cit_totaal += (winst - SME_BRACKET_MID_TOP) * STANDARD_RATE
    else:
        cit_totaal = winst * STANDARD_RATE

    effectief_tarief = cit_totaal / winst

    return CITResultTH(
        winst=winst,
        jaar=jaar,
        sme=sme,
        cit_rate=STANDARD_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
