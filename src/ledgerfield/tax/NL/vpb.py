"""Vennootschapsbelasting (VPB) calculator — NL 2022-2025."""
import json
import os
from dataclasses import dataclass

__all__ = ["VPBResult", "bereken_vpb"]

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


@dataclass
class VPBResult:
    jaar: int
    belastbare_winst: float
    tarief_schijf_1: float
    tarief_schijf_2: float
    schijf_1_grens: float
    vpb_schijf_1: float
    vpb_schijf_2: float
    vpb_totaal: float
    effectief_tarief: float


def bereken_vpb(belastbare_winst: float, jaar: int = 2025) -> VPBResult:
    params = json.load(open(PARAMS_PATH))["years"][str(jaar)]["VPB"]
    grens = params["schijf_1_grens"]
    t1, t2 = params["tarief_schijf_1"], params["tarief_schijf_2"]
    s1 = min(belastbare_winst, grens) * t1
    s2 = max(0, belastbare_winst - grens) * t2
    totaal = s1 + s2
    effectief = totaal / belastbare_winst if belastbare_winst > 0 else 0.0
    return VPBResult(jaar, belastbare_winst, t1, t2, grens, s1, s2, totaal, effectief)
