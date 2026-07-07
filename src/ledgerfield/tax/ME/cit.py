"""Montenegro corporate income tax calculator.

Montenegro applies a **progressive** corporate income tax (porez na dobit
pravnih lica), administered by the Revenue and Customs Administration (Uprava
prihoda i carina). Tax is computed per-bracket on taxable profit (in EUR):

    * 9%  on profit up to and including €100,000
    * 12% on the portion between €100,000 and €1,500,000
    * 15% on the portion above €1,500,000

The standard VAT (PDV) rate is **21%**.

Worked examples (per-bracket):
    €50,000    -> 9% * 50,000                                    = 4,500
    €1,000,000 -> 9% * 100,000 + 12% * 900,000                   = 117,000
    €2,000,000 -> 9% * 100,000 + 12% * 1,400,000 + 15% * 500,000 = 252,000

NOTE: Rates and thresholds are AI-estimated for the 2025 target period and have
not been verified against primary sources. See params.json metadata
(source_status = "ai_estimated_needs_verification"). Verify with the Uprava
prihoda i carina (https://www.poreskauprava.gov.me/) before any real use.
"""
from __future__ import annotations

from dataclasses import dataclass

# Bracket upper bounds (EUR) and marginal rates.
BAND_1_CAP = 100_000.0
BAND_2_CAP = 1_500_000.0
RATE_1 = 0.09
RATE_2 = 0.12
RATE_3 = 0.15


@dataclass
class CITResultME:
    winst: float
    jaar: int
    cit_band1: float
    cit_band2: float
    cit_band3: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_montenegro(winst: float, jaar: int) -> CITResultME:
    """Bereken Montenegrijnse vennootschapsbelasting (3-schijven progressief).

    De belasting wordt per schijf berekend:
        * 9%  over de winst t/m €100.000
        * 12% over het deel tussen €100.000 en €1.500.000
        * 15% over het deel boven €1.500.000

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultME dataclass met de belasting per schijf en het totaal.
    """
    if winst <= 0:
        return CITResultME(
            winst=winst, jaar=jaar,
            cit_band1=0.0, cit_band2=0.0, cit_band3=0.0,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    # Band 1: 9% on the portion up to €100,000.
    band1_base = min(winst, BAND_1_CAP)
    cit_band1 = band1_base * RATE_1

    # Band 2: 12% on the portion between €100,000 and €1,500,000.
    band2_base = max(0.0, min(winst, BAND_2_CAP) - BAND_1_CAP)
    cit_band2 = band2_base * RATE_2

    # Band 3: 15% on the portion above €1,500,000.
    band3_base = max(0.0, winst - BAND_2_CAP)
    cit_band3 = band3_base * RATE_3

    cit_totaal = cit_band1 + cit_band2 + cit_band3
    effectief_tarief = cit_totaal / winst

    return CITResultME(
        winst=winst,
        jaar=jaar,
        cit_band1=cit_band1,
        cit_band2=cit_band2,
        cit_band3=cit_band3,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
