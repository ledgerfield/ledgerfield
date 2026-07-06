"""Croatia corporate income tax calculator.

Croatia levies corporate income tax (porez na dobit) at a standard rate of
**18%**, with a reduced **10%** rate for taxpayers whose annual revenue does
not exceed **EUR 1,000,000** (Profit Tax Act / Zakon o porezu na dobit),
administered by the Tax Administration (Porezna uprava).

Croatia implemented the EU Pillar Two rules (Directive (EU) 2022/2523) for
in-scope groups (consolidated revenue >= EUR 750m) — out of scope for this
SME estimator (see params.json). Personal income tax uses a municipal-rate
system: since 2024 municipalities set the lower/higher PIT rates within
statutory bands (the former surtax was abolished).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultHR:
    winst: float
    jaar: int
    small: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_kroatie(winst: float, jaar: int, small: bool = False) -> CITResultHR:
    """Bereken Kroatische vennootschapsbelasting (18% standaard / 10% klein).

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).
        small: True als de jaaromzet van de belastingplichtige niet hoger is
            dan EUR 1.000.000 — dan geldt het verlaagde 10%-tarief in plaats
            van het standaardtarief van 18%. NB: de drempel geldt voor de
            *omzet* (revenue), niet voor de winst; de aanroeper moet dit zelf
            beoordelen.

    Returns:
        CITResultHR dataclass.
    """
    CIT_RATE_STANDARD = 0.18
    CIT_RATE_SMALL = 0.10

    cit_rate = CIT_RATE_SMALL if small else CIT_RATE_STANDARD

    if winst <= 0:
        return CITResultHR(
            winst=winst, jaar=jaar, small=small,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultHR(
        winst=winst,
        jaar=jaar,
        small=small,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
