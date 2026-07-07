"""Kyrgyz Republic corporate income tax calculator.

Kyrgyzstan levies a flat **10%** corporate income tax (profit tax) under the
Tax Code, administered by the State Tax Service (STS). A turnover-based **sales
tax** also applies to gross revenue (typically 1%–3% depending on activity and
payment method) and standard **VAT** is 12% — both are handled outside this SME
profit-tax estimator (see params.json).

AI-estimated figures: verify against official State Tax Service guidance before
filing or production use.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

_PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


def _cit_rate() -> float:
    with open(_PARAMS_PATH) as f:
        return float(json.load(f)["cit"]["standard_rate"])


@dataclass
class CITResultKG:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_kirgizie(winst: float, jaar: int) -> CITResultKG:
    """Bereken Kirgizische vennootschapsbelasting (10% flat).

    Args:
        winst: Belastbare winst in KGS.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultKG dataclass.
    """
    cit_rate = _cit_rate()

    if winst <= 0:
        return CITResultKG(
            winst=winst, jaar=jaar, cit_rate=cit_rate,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultKG(
        winst=winst,
        jaar=jaar,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
