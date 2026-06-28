"""Inkomstenbelasting calculator — NL 2022-2025 Box 1, 2, 3."""
import json
import os
from dataclasses import dataclass

__all__ = [
    "IBBox1Result", "IBBox2Result", "IBBox3Result",
    "bereken_ib_box1", "bereken_ib_box2", "bereken_ib_box3",
]

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


@dataclass
class IBBox1Result:
    jaar: int
    belastbaar_inkomen: float
    ib_voor_heffingskortingen: float
    algemene_heffingskorting: float
    arbeidskorting: float
    ib_na_kortingen: float
    effectief_tarief: float


@dataclass
class IBBox2Result:
    jaar: int
    dividend: float
    tarief_schijf_1: float
    tarief_schijf_2: float
    schijf_1_grens: float
    ib_box2: float


@dataclass
class IBBox3Result:
    jaar: int
    vermogen: float
    heffingsvrij: float
    grondslag: float
    forfaitair_rendement: float
    ib_box3: float


def bereken_ib_box1(
    belastbaar_inkomen: float,
    jaar: int = 2025,
    aftrekposten: float = 0.0,
) -> IBBox1Result:
    p = json.load(open(PARAMS_PATH))["years"][str(jaar)]["IB"]
    inkomen = max(0.0, belastbaar_inkomen - aftrekposten)
    grens = p["schijf_1_grens"]
    t1 = p["tarief_schijf_1"]
    t2 = p["tarief_schijf_2"]
    ib_s1 = min(inkomen, grens) * t1
    ib_s2 = max(0.0, inkomen - grens) * t2
    ib_voor = ib_s1 + ib_s2

    # Heffingskortingen (vereenvoudigd: max-waarden; afbouw niet gemodelleerd)
    ahk = p["max_algemene_heffingskorting"]
    ak = p["max_arbeidskorting"]

    ib_na = max(0.0, ib_voor - ahk - ak)
    effectief = ib_na / belastbaar_inkomen if belastbaar_inkomen > 0 else 0.0
    return IBBox1Result(jaar, belastbaar_inkomen, ib_voor, ahk, ak, ib_na, effectief)


def bereken_ib_box2(dividend: float, jaar: int = 2025) -> IBBox2Result:
    p = json.load(open(PARAMS_PATH))["years"][str(jaar)]["Box2"]
    if "tarief" in p:
        # 2022: enkel tarief
        t1 = p["tarief"]
        t2 = p["tarief"]
        grens = float("inf")
        ib = dividend * t1
    else:
        t1 = p["tarief_schijf_1"]
        t2 = p["tarief_schijf_2"]
        grens = p["schijf_1_grens"]
        ib = min(dividend, grens) * t1 + max(0.0, dividend - grens) * t2
    return IBBox2Result(jaar, dividend, t1, t2, grens, ib)


def bereken_ib_box3(vermogen: float, jaar: int = 2025) -> IBBox3Result:
    p = json.load(open(PARAMS_PATH))["years"][str(jaar)]
    if "Box3" not in p:
        # 2022/2023 hebben geen Box3 block in params; gebruik 0
        return IBBox3Result(jaar, vermogen, 0.0, vermogen, 0.0, 0.0)
    b3 = p["Box3"]
    heffingsvrij = b3["heffingsvrij_per_persoon"]
    grondslag = max(0.0, vermogen - heffingsvrij)
    forfait = b3["forfait_overige_beleggingen"]
    tarief = b3["tarief"]
    ib = grondslag * forfait * tarief
    return IBBox3Result(jaar, vermogen, heffingsvrij, grondslag, forfait, ib)
