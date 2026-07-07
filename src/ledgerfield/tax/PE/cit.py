"""Peru corporate income tax (Impuesto a la Renta) calculator.

Peru levies a flat **29.5%** corporate income tax under the general regime
(Régimen General, Ley del Impuesto a la Renta — LIR), administered by SUNAT.

Small and medium enterprises may qualify for the **MYPE Tributario** regime
(Régimen MYPE Tributario, Decreto Legislativo N.° 1269): net income up to
15 UIT is taxed at **10%**, and the excess at **29.5%**. For 2025 the UIT
(Unidad Impositiva Tributaria) is S/ 5,350, so the 15-UIT bracket threshold
is S/ 80,250.

VAT (IGV) is 18% — composed of 16% IGV proper plus 2% IPM (Impuesto de
Promoción Municipal). Dividend withholding tax is 5% (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultPE:
    winst: float
    jaar: int
    mype: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


# 2025 general-regime rate (LIR) and MYPE Tributario bracket parameters.
CIT_RATE_GENERAL = 0.295
MYPE_LOWER_RATE = 0.10
UIT_2025 = 5_350.0
MYPE_BRACKET_UIT = 15
MYPE_THRESHOLD = UIT_2025 * MYPE_BRACKET_UIT  # S/ 80,250


def bereken_cit_peru(
    winst: float,
    jaar: int,
    mype: bool = False,
) -> CITResultPE:
    """Bereken Peruaanse vennootschapsbelasting (Impuesto a la Renta).

    Args:
        winst: Belastbare (netto) winst in PEN (S/).
        jaar: Belastingjaar (bijv. 2025).
        mype: True voor het Régimen MYPE Tributario — 10% over de eerste
            15 UIT (S/ 80,250 in 2025) en 29.5% over het meerdere.
            False (default) voor het algemene regime: vlak 29.5%.

    Returns:
        CITResultPE dataclass.
    """
    if winst <= 0:
        return CITResultPE(
            winst=winst, jaar=jaar, mype=mype,
            cit_rate=CIT_RATE_GENERAL, cit_totaal=0.0, effectief_tarief=0.0,
        )

    if mype:
        lower = min(winst, MYPE_THRESHOLD)
        upper = max(winst - MYPE_THRESHOLD, 0.0)
        cit_totaal = lower * MYPE_LOWER_RATE + upper * CIT_RATE_GENERAL
    else:
        cit_totaal = winst * CIT_RATE_GENERAL

    effectief_tarief = cit_totaal / winst

    return CITResultPE(
        winst=winst,
        jaar=jaar,
        mype=mype,
        cit_rate=CIT_RATE_GENERAL,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
