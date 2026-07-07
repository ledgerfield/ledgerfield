"""Republic of Mauritius corporate income tax calculator.

Mauritius levies a flat **15%** corporate income tax (Income Tax Act 1995),
administered by the Mauritius Revenue Authority (MRA). Under the partial
exemption regime — the successor to the Global Business Company (GBC) deemed
foreign tax credit — **80%** of qualifying foreign-source income (foreign
dividends, interest, ship and aircraft leasing, CIS/closed-end fund
management, etc.) is exempt, leaving 15% tax on the remaining 20% slice:
an **effective 3%** rate.

Other headline features (see params.json): export of goods taxed at 3%,
a 2% Corporate Climate Responsibility (CCR) levy on companies with turnover
above Rs 50m (introduced 2024-25), and VAT at 15%.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultMU:
    winst: float
    jaar: int
    gbc_partial_exemption: bool
    cit_rate: float
    exempt_deel: float
    belastbaar_deel: float
    cit_totaal: float
    effectieve_druk: float


def bereken_cit_mauritius(
    winst: float,
    jaar: int,
    gbc_partial_exemption: bool = False,
) -> CITResultMU:
    """Bereken Mauritiaanse vennootschapsbelasting (15% flat; GBC effectief 3%).

    Args:
        winst: Belastbare winst in MUR.
        jaar: Belastingjaar (bijv. 2025).
        gbc_partial_exemption: True voor het Global Business / partial
            exemption regime — 80% van kwalificerend buitenlands inkomen
            is vrijgesteld, zodat 15% over de resterende 20% een
            effectieve druk van 3% oplevert.

    Returns:
        CITResultMU dataclass.
    """
    CIT_RATE = 0.15
    PARTIAL_EXEMPTION = 0.80

    if winst <= 0:
        return CITResultMU(
            winst=winst, jaar=jaar, gbc_partial_exemption=gbc_partial_exemption,
            cit_rate=CIT_RATE, exempt_deel=0.0, belastbaar_deel=0.0,
            cit_totaal=0.0, effectieve_druk=0.0,
        )

    if gbc_partial_exemption:
        exempt_deel = winst * PARTIAL_EXEMPTION
    else:
        exempt_deel = 0.0

    belastbaar_deel = winst - exempt_deel
    cit_totaal = belastbaar_deel * CIT_RATE
    effectieve_druk = cit_totaal / winst

    return CITResultMU(
        winst=winst,
        jaar=jaar,
        gbc_partial_exemption=gbc_partial_exemption,
        cit_rate=CIT_RATE,
        exempt_deel=exempt_deel,
        belastbaar_deel=belastbaar_deel,
        cit_totaal=cit_totaal,
        effectieve_druk=effectieve_druk,
    )
