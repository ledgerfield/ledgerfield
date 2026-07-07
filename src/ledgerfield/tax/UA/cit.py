"""Ukraine corporate income tax calculator.

Ukraine levies a **flat 18%** corporate income tax (CIT) on taxable profit,
administered by the State Tax Service of Ukraine (Державна податкова служба).
Banks are taxed at a raised **25%** rate (increased from 18% with effect from
the 2024 tax year, retained for 2025).

Value Added Tax (VAT / ПДВ) applies at the standard rate of 20%.

Micro and small businesses may instead elect the **simplified single-tax**
system (Groups 1–4, sproshchena systema), which replaces CIT with a turnover-
or unit-based single tax — out of scope for this SME CIT estimator (see
params.json). Wartime budget levies (e.g. temporary 50% bank rate for 2023,
increased military levy) have applied in recent years; verify current status.

RATES ARE AI-ESTIMATED AND REQUIRE VERIFICATION against the State Tax Service
(https://tax.gov.ua/) before any filing or production use.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultUA:
    winst: float
    jaar: int
    bank: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_oekraine(
    winst: float,
    jaar: int,
    bank: bool = False,
) -> CITResultUA:
    """Bereken Oekraïense vennootschapsbelasting (18% standaard, 25% banken).

    Args:
        winst: Belastbare winst in UAH.
        jaar: Belastingjaar (bijv. 2025).
        bank: True voor banken (25%-tarief vanaf 2024); anders standaard 18%.

    Returns:
        CITResultUA dataclass.
    """
    CIT_RATE = 0.25 if bank else 0.18

    if winst <= 0:
        return CITResultUA(
            winst=winst, jaar=jaar, bank=bank,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultUA(
        winst=winst,
        jaar=jaar,
        bank=bank,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
