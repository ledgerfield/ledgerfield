"""Tunisia corporate income tax calculator (2025, Finance Law 2025).

Finance Law 2025 (Loi de Finances 2025) **raised the standard CIT rate from
15% to 20%**, applicable to FY2024 profits declared in 2025 onwards. Banks,
financial institutions and insurance companies were raised from 35% to
**40%**; telecom and hydrocarbon operators pay **35%**; a reduced **10%**
regime applies to agriculture, regional development and support activities.

A conjunctural contribution (contribution conjoncturelle) has applied to
certain large companies in recent finance laws — see params.json.
VAT: 19% standard, with 13% and 7% reduced rates.
Administered by the Ministère des Finances (impots.finances.gov.tn).
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.20,
    "banks_insurance": 0.40,
    "telecom_hydrocarbons": 0.35,
    "reduced": 0.10,
}


@dataclass
class CITResultTN:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_tunesie(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultTN:
    """Bereken Tunesische vennootschapsbelasting (Loi de Finances 2025).

    Args:
        winst: Belastbare winst in TND.
        jaar: Belastingjaar (bijv. 2025).
        sector: Sectorregime — "standard" (20%, verhoogd van 15% door de
            Loi de Finances 2025), "banks_insurance" (40%, verhoogd van 35%),
            "telecom_hydrocarbons" (35%) of "reduced" (10%: landbouw,
            regionale ontwikkeling, ondersteunende activiteiten).

    Returns:
        CITResultTN dataclass.

    Raises:
        ValueError: Bij een onbekende sector.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"Unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    cit_rate = SECTOR_RATES[sector]

    if winst <= 0:
        return CITResultTN(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultTN(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
