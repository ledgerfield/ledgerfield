"""WBSO Speur & Ontwikkeling — Loonkostenvoordeel calculator NL 2022-2025."""
import json
import os
from dataclasses import dataclass

__all__ = ["WBSOResult", "bereken_wbso"]

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


@dataclass
class WBSOResult:
    jaar: int
    loonkosten_so: float          # loonkosten S&O medewerkers
    tarief_schijf_1: float        # 36% in 2025
    tarief_schijf_2: float        # 16% in 2025
    schijf_1_grens: float         # 380k in 2025
    voordeel_schijf_1: float
    voordeel_schijf_2: float
    totaal_voordeel: float        # totale WBSO-aftrek op loonheffing


def bereken_wbso(loonkosten_so: float, jaar: int = 2025) -> WBSOResult:
    p = json.load(open(PARAMS_PATH))["years"][str(jaar)]
    if "WBSO" not in p:
        # 2022 heeft geen WBSO-block; geen regeling (of buiten scope)
        return WBSOResult(jaar, loonkosten_so, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    w = p["WBSO"]
    t1 = w["tarief_schijf_1"]
    t2 = w["tarief_schijf_2"]
    grens = w["schijf_1_grens"]
    v1 = min(loonkosten_so, grens) * t1
    v2 = max(0.0, loonkosten_so - grens) * t2
    return WBSOResult(jaar, loonkosten_so, t1, t2, grens, v1, v2, v1 + v2)
