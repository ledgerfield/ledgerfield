"""Republic of Lithuania corporate income tax (pelno mokestis) calculator.

Lithuania levies a **16%** standard corporate income tax as of 1 January 2025
(raised from 15% by the 2025 tax reform), administered by the State Tax
Inspectorate (VMI, Valstybinė mokesčių inspekcija).

Small companies — no more than 10 employees AND annual income not exceeding
EUR 300,000 — qualify for a reduced **6%** rate (raised from 5% on
1 January 2025), and for a **0%** rate in their first tax year.

VAT (PVM, pridėtinės vertės mokestis) is 21% standard with 9% and 5% reduced
rates. Lithuania has implemented the EU Pillar Two minimum tax framework for
large groups (see params.json) — out of scope for this SME estimator.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultLT:
    winst: float
    jaar: int
    small: bool
    first_year: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_litouwen(
    winst: float,
    jaar: int,
    small: bool = False,
    first_year: bool = False,
) -> CITResultLT:
    """Bereken Litouwse vennootschapsbelasting (pelno mokestis, 2025-regels).

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).
        small: True als kleine onderneming (≤10 werknemers EN inkomen
            ≤ EUR 300.000) — verlaagd tarief van 6%.
        first_year: True als eerste belastingjaar; in combinatie met
            ``small`` geldt een 0%-tarief.

    Returns:
        CITResultLT dataclass.
    """
    if small and first_year:
        cit_rate = 0.0
    elif small:
        cit_rate = 0.06
    else:
        cit_rate = 0.16

    if winst <= 0:
        return CITResultLT(
            winst=winst, jaar=jaar, small=small, first_year=first_year,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultLT(
        winst=winst,
        jaar=jaar,
        small=small,
        first_year=first_year,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
