"""Ireland Corporate Income Tax calculator."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CITResultIE:
    winst: float
    jaar: int
    trading: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_ireland(
    winst: float,
    jaar: int,
    trading: bool = True,
) -> CITResultIE:
    """Bereken Ierse vennootschapsbelasting (Corporation Tax).

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).
        trading: True voor trading income (12.5%); False voor non-trading/passive (25%).

    Returns:
        CITResultIE dataclass.
    """
    TRADING_RATE = 0.125
    NON_TRADING_RATE = 0.25

    cit_rate = TRADING_RATE if trading else NON_TRADING_RATE

    if winst <= 0:
        return CITResultIE(
            winst=winst, jaar=jaar, trading=trading,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultIE(
        winst=winst,
        jaar=jaar,
        trading=trading,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
