"""企业所得税 (Corporate Income Tax) — China 2024/2025."""
import json, os
from dataclasses import dataclass
from enum import Enum

__all__ = ["CNEntityType", "ChinaCITResult", "bereken_cit_china"]

class CNEntityType(Enum):
    STANDARD = "standard"       # 标准 25%
    HNTE = "hnte"               # 高新技术企业 15%
    SME = "sme"                 # 小型微利企业 ≤300万 20%/5%
    MICRO = "micro"             # 微利 ≤100万 5%

@dataclass
class ChinaCITResult:
    jaar: int
    belastbare_winst_cny: float
    entity_type: CNEntityType
    applied_rate: float
    cit_totaal: float
    effective_rate: float
    notes: str

def bereken_cit_china(belastbare_winst_cny: float, jaar: int = 2025,
                       entity_type: CNEntityType = CNEntityType.STANDARD) -> ChinaCITResult:
    params = json.load(open(os.path.join(os.path.dirname(__file__), "params.json")))
    cit = params["years"][str(jaar)]["CIT"]

    if entity_type == CNEntityType.MICRO and belastbare_winst_cny <= cit["micro_threshold_cny"]:
        rate = cit["micro_rate"]
        notes = f"微利企业(≤¥{cit['micro_threshold_cny']:,}): {rate*100}%"
    elif entity_type == CNEntityType.SME and belastbare_winst_cny <= cit["sme_threshold_cny"]:
        rate = cit["sme_rate"]
        notes = f"小微企业(≤¥{cit['sme_threshold_cny']:,}): {rate*100}%"
    elif entity_type == CNEntityType.HNTE:
        rate = cit["hnte_rate"]
        notes = f"高新技术企业: {rate*100}%"
    else:
        rate = cit["standard_rate"]
        notes = f"标准税率: {rate*100}%"

    total = belastbare_winst_cny * rate
    eff = total / belastbare_winst_cny if belastbare_winst_cny > 0 else 0
    return ChinaCITResult(jaar, belastbare_winst_cny, entity_type, rate, total, eff, notes)
