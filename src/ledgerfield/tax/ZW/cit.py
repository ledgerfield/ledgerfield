"""Zimbabwe corporate income tax calculator (2025).

Zimbabwe levies a **25%** corporate income tax plus a **3% AIDS levy computed
on the tax itself** (not on profit), giving an effective rate of **25.75%**.
Administered by the Zimbabwe Revenue Authority (ZIMRA).

VAT is 15%. A 2% Intermediated Money Transfer Tax (IMTT) applies to most
electronic money transfers. Zimbabwe operates a dual-currency regime
(ZWG — Zimbabwe Gold — alongside USD); see params.json.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultZW:
    winst: float
    jaar: int
    cit_rate: float
    aids_levy_rate: float
    cit_bedrag: float
    aids_levy_bedrag: float
    totaal_bedrag: float
    effectief_tarief: float


def bereken_cit_zimbabwe(winst: float, jaar: int) -> CITResultZW:
    """Bereken Zimbabwaanse vennootschapsbelasting (25% CIT + 3% AIDS-levy op de belasting).

    De AIDS-levy van 3% wordt geheven over het CIT-bedrag zelf (niet over de
    winst), zodat het effectieve tarief 25% × 1.03 = 25.75% bedraagt.

    Args:
        winst: Belastbare winst (ZWG of USD, afhankelijk van functionele valuta).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultZW dataclass.
    """
    CIT_RATE = 0.25
    AIDS_LEVY_RATE = 0.03  # 3% of the tax, not of profit

    if winst <= 0:
        return CITResultZW(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE,
            aids_levy_rate=AIDS_LEVY_RATE, cit_bedrag=0.0,
            aids_levy_bedrag=0.0, totaal_bedrag=0.0, effectief_tarief=0.0,
        )

    cit_bedrag = winst * CIT_RATE
    aids_levy_bedrag = cit_bedrag * AIDS_LEVY_RATE
    totaal_bedrag = cit_bedrag + aids_levy_bedrag
    effectief_tarief = totaal_bedrag / winst  # 0.2575

    return CITResultZW(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        aids_levy_rate=AIDS_LEVY_RATE,
        cit_bedrag=cit_bedrag,
        aids_levy_bedrag=aids_levy_bedrag,
        totaal_bedrag=totaal_bedrag,
        effectief_tarief=effectief_tarief,
    )
