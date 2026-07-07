"""Russian Federation corporate income tax (profits tax) calculator.

Russia levies a corporate profits tax (nalog na pribyl) administered by the
Federal Tax Service (Federalnaya nalogovaya sluzhba, FTS).

**RATE INCREASE 2025:** The standard rate was RAISED from 20% to **25%** with
effect from 1 January 2025 (Federal Law No. 176-FZ of 12 July 2024). The 25%
comprises a federal portion (8% for 2025-2030) and a regional portion (17%).

Accredited **IT companies** are taxed at a reduced **5%** rate for the period
2025-2030 (previously 0% for 2022-2024). Value Added Tax (NDS) applies at the
standard rate of 20%.

WARNING — INTERNATIONAL SANCTIONS: Extensive international sanctions imposed on
the Russian Federation since 2022 may materially affect the applicability,
enforceability, and practical use of these figures for non-resident parties.

RATES ARE AI-ESTIMATED AND REQUIRE VERIFICATION against the Federal Tax Service
(https://www.nalog.gov.ru/) before any filing or production use.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultRU:
    winst: float
    jaar: int
    it_company: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_rusland(
    winst: float,
    jaar: int,
    it_company: bool = False,
) -> CITResultRU:
    """Bereken Russische winstbelasting (25% standaard vanaf 2025, 5% IT).

    Vanaf 1 januari 2025 is het standaardtarief verhoogd van 20% naar 25%
    (Federale Wet nr. 176-FZ). Geaccrediteerde IT-bedrijven: 5% (2025-2030).

    Args:
        winst: Belastbare winst in RUB.
        jaar: Belastingjaar (bijv. 2025).
        it_company: True voor geaccrediteerde IT-bedrijven (5%); anders 25%.

    Returns:
        CITResultRU dataclass.
    """
    CIT_RATE = 0.05 if it_company else 0.25

    if winst <= 0:
        return CITResultRU(
            winst=winst, jaar=jaar, it_company=it_company,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultRU(
        winst=winst,
        jaar=jaar,
        it_company=it_company,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
