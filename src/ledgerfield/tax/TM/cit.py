"""Turkmenistan corporate income tax calculator.

Turkmenistan levies corporate (profit) income tax under the Tax Code. The rate
depends on the type of entity: **8%** for private/domestic legal entities, and
**20%** for state enterprises and foreign legal entities. Standard **VAT** (15%)
is handled outside this SME profit-tax estimator (see params.json).

Administered by the Main State Tax Service under the Ministry of Finance and
Economy of Turkmenistan.

AI-estimated figures: verify against official guidance before filing or
production use.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

_PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


def _rates() -> tuple[float, float]:
    with open(_PARAMS_PATH) as f:
        cit = json.load(f)["cit"]
    return float(cit["private_domestic_rate"]), float(cit["state_or_foreign_rate"])


@dataclass
class CITResultTM:
    winst: float
    jaar: int
    staats_of_buitenlands: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_turkmenistan(
    winst: float,
    jaar: int,
    staats_of_buitenlands: bool = False,
) -> CITResultTM:
    """Bereken Turkmeense vennootschapsbelasting (8% privaat, 20% staat/buitenlands).

    Args:
        winst: Belastbare winst in TMT.
        jaar: Belastingjaar (bijv. 2025).
        staats_of_buitenlands: True voor staatsondernemingen en buitenlandse
            rechtspersonen (20% tarief), anders het privaat/binnenlandse
            tarief van 8%.

    Returns:
        CITResultTM dataclass.
    """
    private_rate, state_foreign_rate = _rates()
    cit_rate = state_foreign_rate if staats_of_buitenlands else private_rate

    if winst <= 0:
        return CITResultTM(
            winst=winst, jaar=jaar, staats_of_buitenlands=staats_of_buitenlands,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultTM(
        winst=winst,
        jaar=jaar,
        staats_of_buitenlands=staats_of_buitenlands,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
