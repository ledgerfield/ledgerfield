"""Republic of Fiji corporate income tax calculator.

Fiji levies corporate income tax administered by the Fiji Revenue and Customs
Service (FRCS). For the 2025 target period the headline rates are:

* **20%** — resident companies.
* **25%** — non-resident / foreign companies (e.g. branches of foreign
  companies).

A Value Added Tax (VAT) of **15%** applies to most goods and services. VAT is
out of scope for this simplified CIT estimator (see params.json).

NOTE: Rates are AI-estimated and require verification against official FRCS
guidance before any filing or production use.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultFJ:
    winst: float
    jaar: int
    non_resident: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_fiji(
    winst: float,
    jaar: int,
    non_resident: bool = False,
) -> CITResultFJ:
    """Bereken Fijische vennootschapsbelasting.

    Args:
        winst: Belastbare winst in FJD.
        jaar: Belastingjaar (bijv. 2025).
        non_resident: True voor niet-ingezeten / buitenlandse vennootschappen
            (25%); False voor ingezeten vennootschappen (20%).

    Returns:
        CITResultFJ dataclass.
    """
    cit_rate = 0.25 if non_resident else 0.20

    if winst <= 0:
        return CITResultFJ(
            winst=winst,
            jaar=jaar,
            non_resident=non_resident,
            cit_rate=cit_rate,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultFJ(
        winst=winst,
        jaar=jaar,
        non_resident=non_resident,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
