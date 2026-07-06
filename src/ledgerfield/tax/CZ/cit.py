"""Czech Republic (Czechia) corporate income tax calculator.

Czechia levies a flat **21%** corporate income tax (daň z příjmů právnických
osob), raised from 19% by the 2024 consolidation package (konsolidační
balíček), administered by the Financial Administration (Finanční správa).

A temporary windfall tax (daň z neočekávaných zisků) applies a 60% surcharge
on excess profits of large banks and energy companies for 2023-2025 — out of
scope for this SME estimator (see params.json). VAT applies at 21% standard
with a single reduced rate of 12% since the 2024 reform.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultCZ:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_tsjechie(
    winst: float,
    jaar: int,
) -> CITResultCZ:
    """Bereken Tsjechische vennootschapsbelasting (21% vlak tarief).

    Args:
        winst: Belastbare winst in CZK.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultCZ dataclass.
    """
    CIT_RATE = 0.21

    if winst <= 0:
        return CITResultCZ(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultCZ(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
