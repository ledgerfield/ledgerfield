"""Kingdom of Saudi Arabia corporate tax + Zakat calculator.

Saudi Arabia operates a dual regime administered by ZATCA (Zakat, Tax and
Customs Authority):

    * **Corporate Income Tax (CIT)** at 20% applies to the profit share
      attributable to *non-GCC (foreign)* owners.
    * **Zakat** at 2.5% applies to the Zakat base attributable to *Saudi /
      GCC* owners. Zakat is a religiously-grounded levy on wealth, not a
      profit tax, but for a first-order estimate it is applied here to the
      owner-share of taxable profit as a proxy for the Zakat base.

A wholly Saudi/GCC-owned company therefore pays Zakat only; a wholly
foreign-owned company pays CIT only; mixed ownership pays a blend.

Special CIT rates (85%/20% band for oil & hydrocarbons, 30% for natural gas
investment) are out of scope for this SME estimator — see params.json.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultSA:
    winst: float
    jaar: int
    foreign_ownership_share: float
    cit_rate: float
    zakat_rate: float
    cit_totaal: float
    zakat_totaal: float
    heffing_totaal: float
    effectief_tarief: float


def bereken_cit_saudi(
    winst: float,
    jaar: int,
    foreign_ownership_share: float = 1.0,
) -> CITResultSA:
    """Bereken Saoedische CIT + Zakat.

    Args:
        winst: Belastbare winst / Zakat-basis in SAR.
        jaar: Belastingjaar (bijv. 2025).
        foreign_ownership_share: Aandeel niet-GCC (buitenlandse) eigenaren,
            tussen 0.0 (volledig Saoedisch/GCC) en 1.0 (volledig buitenlands).

    Returns:
        CITResultSA met gescheiden CIT- en Zakat-bedragen.
    """
    if not 0.0 <= foreign_ownership_share <= 1.0:
        raise ValueError("foreign_ownership_share must be between 0.0 and 1.0")

    CIT_RATE = 0.20
    ZAKAT_RATE = 0.025
    gcc_share = 1.0 - foreign_ownership_share

    if winst <= 0:
        return CITResultSA(
            winst=winst, jaar=jaar, foreign_ownership_share=foreign_ownership_share,
            cit_rate=CIT_RATE, zakat_rate=ZAKAT_RATE,
            cit_totaal=0.0, zakat_totaal=0.0, heffing_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * foreign_ownership_share * CIT_RATE
    zakat_totaal = winst * gcc_share * ZAKAT_RATE
    heffing_totaal = cit_totaal + zakat_totaal
    effectief_tarief = heffing_totaal / winst

    return CITResultSA(
        winst=winst,
        jaar=jaar,
        foreign_ownership_share=foreign_ownership_share,
        cit_rate=CIT_RATE,
        zakat_rate=ZAKAT_RATE,
        cit_totaal=cit_totaal,
        zakat_totaal=zakat_totaal,
        heffing_totaal=heffing_totaal,
        effectief_tarief=effectief_tarief,
    )
