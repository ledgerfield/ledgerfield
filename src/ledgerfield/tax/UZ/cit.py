"""Republic of Uzbekistan corporate income tax calculator.

Uzbekistan levies a standard **15%** corporate income tax (CIT), administered by
the State Tax Committee. Certain sectors — banks, mobile (cellular) operators,
and cement producers — are taxed at a higher **20%** rate. Value Added Tax
(VAT / QQS) applies at a standard **12%**.

This SME estimator models the standard 15% rate, with an optional flag for the
higher 20% sectors (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultUZ:
    winst: float
    jaar: int
    hoger_tarief_sector: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_oezbekistan(
    winst: float,
    jaar: int,
    hoger_tarief_sector: bool = False,
) -> CITResultUZ:
    """Bereken Oezbeekse vennootschapsbelasting (15% standaard, 20% sectoren).

    Args:
        winst: Belastbare winst in UZS.
        jaar: Belastingjaar (bijv. 2025).
        hoger_tarief_sector: True voor banken, mobiele operators en
            cementproducenten (20%); anders standaard 15%.

    Returns:
        CITResultUZ dataclass. Bij niet-positieve winst is de belasting 0.
    """
    cit_rate = 0.20 if hoger_tarief_sector else 0.15

    if winst <= 0:
        return CITResultUZ(
            winst=winst,
            jaar=jaar,
            hoger_tarief_sector=hoger_tarief_sector,
            cit_rate=cit_rate,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultUZ(
        winst=winst,
        jaar=jaar,
        hoger_tarief_sector=hoger_tarief_sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
