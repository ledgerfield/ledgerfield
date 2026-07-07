"""Nepal corporate income tax calculator.

Nepal levies corporate income tax at sector-dependent rates, administered by
the Inland Revenue Department (IRD):

    * 25% — standard / general companies;
    * 30% — banks, financial institutions, insurance, telecom and petroleum;
    * 20% — special industries (e.g. certain manufacturing).

Amounts are denominated in Nepalese rupees (NPR). Value Added Tax is levied
separately at 13% (see params.json).

WARNING: The rates encoded here are AI-estimated and require verification
against official Inland Revenue Department guidance (https://ird.gov.np/)
before any filing or production use.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

_PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


def _load_params() -> dict:
    with open(_PARAMS_PATH) as f:
        return json.load(f)


@dataclass
class CITResultNP:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_nepal(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultNP:
    """Bereken Nepalese vennootschapsbelasting (sector-afhankelijk tarief).

    Args:
        winst: Belastbare winst in NPR (Nepalese rupee).
        jaar: Belastingjaar (bijv. 2025).
        sector: Sleutel voor het sectortarief:
            * "standard"           -> 25% (algemeen);
            * "financial_telecom"  -> 30% (banken/financieel/verzekering/
              telecom/petroleum);
            * "special_industry"   -> 20% (bijzondere industrieën).

    Returns:
        CITResultNP dataclass.

    Raises:
        ValueError: bij een onbekende sector.
    """
    params = _load_params()
    sector_rates = params["cit"]["sector_rates"]

    if sector not in sector_rates:
        raise ValueError(
            f"unknown sector '{sector}'; expected one of {sorted(sector_rates)}"
        )

    cit_rate = float(sector_rates[sector])

    if winst <= 0:
        return CITResultNP(
            winst=winst, jaar=jaar, sector=sector, cit_rate=cit_rate,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultNP(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
