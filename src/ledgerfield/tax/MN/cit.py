"""Mongolia corporate income tax calculator.

Mongolia levies a **two-band progressive** corporate income tax (CIT),
administered by the General Department of Taxation (GDT / MTA):

    * 10% on annual taxable income up to MNT 6,000,000,000;
    * 25% on the portion of taxable income exceeding MNT 6,000,000,000.

Amounts are denominated in Mongolian tögrög (MNT). Value Added Tax is levied
separately at 10% (see params.json).

WARNING: The rates and thresholds encoded here are AI-estimated and require
verification against official General Department of Taxation guidance
(https://mta.mn/) before any filing or production use.
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
class CITResultMN:
    winst: float
    jaar: int
    band1_tax: float
    band2_tax: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_mongolie(winst: float, jaar: int) -> CITResultMN:
    """Bereken Mongoolse vennootschapsbelasting (2-schijf progressief).

    Args:
        winst: Belastbare winst in MNT (Mongoolse tögrög).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultMN dataclass met de opsplitsing per schijf.

    Rekenregel:
        * 10% over het deel van de winst t/m MNT 6.000.000.000;
        * 25% over het deel van de winst boven MNT 6.000.000.000.
    """
    params = _load_params()
    cit = params["cit"]
    drempel = float(cit["progressive_threshold_mnt"])
    laag_tarief = float(cit["lower_rate"])
    hoog_tarief = float(cit["upper_rate"])

    if winst <= 0:
        return CITResultMN(
            winst=winst, jaar=jaar, band1_tax=0.0, band2_tax=0.0,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    band1_tax = min(winst, drempel) * laag_tarief
    band2_tax = max(0.0, winst - drempel) * hoog_tarief
    cit_totaal = band1_tax + band2_tax
    effectief_tarief = cit_totaal / winst

    return CITResultMN(
        winst=winst,
        jaar=jaar,
        band1_tax=band1_tax,
        band2_tax=band2_tax,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
