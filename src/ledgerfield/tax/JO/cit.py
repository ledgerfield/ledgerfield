"""Hashemite Kingdom of Jordan corporate income tax calculator.

Jordan levies a sector-based corporate income tax under the Income Tax Law
No. 38 of 2018 (as amended), administered by the Income and Sales Tax
Department (ISTD):

* Standard / industrial / other companies: **20%**
* Banks: **35%**
* Financial institutions, insurance and leasing companies: **24%**
* Telecommunications, electricity generation/distribution, mining and main
  fuel importers: **24%** (activity-specific rates fall in a 24%-35% band)

On top of CIT, Article 11 of Law 38/2018 imposes a **National Contribution
Tax** ("tadamun") on taxable income, at sector-based rates ranging 1%-7%:
1% for other/standard companies, 3% for banks, 4% for financial
institutions/insurance/leasing, and up to 7% for basic mining.

Simplification: this SME estimator collapses telecom, electricity, mining
and main fuel importers into one ``telecom_energy_mining`` bucket at 24% CIT
with a 7% national contribution (the mining rate, the conservative upper
bound of the band); actual per-activity national-contribution rates within
this bucket range 2%-7% under the law. See params.json for the sourced
schedule and limitations.
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.20,
    "banking": 0.35,
    "financial": 0.24,
    "telecom_energy_mining": 0.24,
}

NATIONAL_CONTRIBUTION: dict[str, float] = {
    "standard": 0.01,
    "banking": 0.03,
    "financial": 0.04,
    "telecom_energy_mining": 0.07,
}


@dataclass
class CITResultJO:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    national_contribution_rate: float
    cit: float
    national_contribution: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_jordanie(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultJO:
    """Bereken Jordaanse vennootschapsbelasting (sectortarief + national contribution).

    Args:
        winst: Belastbare winst in JOD.
        jaar: Belastingjaar (bijv. 2025).
        sector: Een van "standard" (20% + 1% NC), "banking" (35% + 3% NC),
            "financial" (24% + 4% NC) of "telecom_energy_mining"
            (24% + 7% NC, vereenvoudigd; zie module docstring).

    Returns:
        CITResultJO dataclass met cit, national_contribution en cit_totaal.

    Raises:
        ValueError: Bij een onbekende sector.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"Unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    cit_rate = SECTOR_RATES[sector]
    nc_rate = NATIONAL_CONTRIBUTION[sector]

    if winst <= 0:
        return CITResultJO(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, national_contribution_rate=nc_rate,
            cit=0.0, national_contribution=0.0,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit = winst * cit_rate
    national_contribution = winst * nc_rate
    cit_totaal = cit + national_contribution
    effectief_tarief = cit_totaal / winst

    return CITResultJO(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        national_contribution_rate=nc_rate,
        cit=cit,
        national_contribution=national_contribution,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
