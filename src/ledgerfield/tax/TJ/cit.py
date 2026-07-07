"""Republic of Tajikistan corporate income tax calculator.

Tajikistan levies corporate (profit) income tax under the Tax Code,
administered by the Tax Committee under the Government of the Republic of
Tajikistan. The **standard rate is 18%**, with a reduced **13%** rate for
producers of goods. Standard **VAT** (~14%, being reduced over time) is handled
outside this SME profit-tax estimator (see params.json).

AI-estimated figures: verify against official Tax Committee guidance before
filing or production use.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

_PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


def _rates() -> tuple[float, float]:
    with open(_PARAMS_PATH) as f:
        cit = json.load(f)["cit"]
    return float(cit["standard_rate"]), float(cit["producer_rate"])


@dataclass
class CITResultTJ:
    winst: float
    jaar: int
    producent: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_tadzjikistan(
    winst: float,
    jaar: int,
    producent: bool = False,
) -> CITResultTJ:
    """Bereken Tadzjiekse vennootschapsbelasting (18% standaard, 13% producenten).

    Args:
        winst: Belastbare winst in TJS.
        jaar: Belastingjaar (bijv. 2025).
        producent: True voor producenten van goederen (13% tarief),
            anders het standaardtarief van 18%.

    Returns:
        CITResultTJ dataclass.
    """
    standard_rate, producer_rate = _rates()
    cit_rate = producer_rate if producent else standard_rate

    if winst <= 0:
        return CITResultTJ(
            winst=winst, jaar=jaar, producent=producent, cit_rate=cit_rate,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultTJ(
        winst=winst,
        jaar=jaar,
        producent=producent,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
