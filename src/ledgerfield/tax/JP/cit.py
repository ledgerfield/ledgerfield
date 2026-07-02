"""法人税 (Corporation Income Tax) calculator — Japan 2024-2025.

SME = 資本金1億円以下 (capital ≤ ¥100M).
  - On first ¥8M of taxable income: 19%
  - On income above ¥8M: 23.2%
Large companies:
  - Flat 23.2% on all taxable income.
Local tax estimate (地方法人税 + 法人住民税 + 法人事業税) ~10.7% on top.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

__all__ = ["CITResult", "bereken_cit_japan"]

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


@dataclass
class CITResult:
    jaar: int
    taxable_income: float          # 課税所得
    is_sme: bool                   # SME判定 (資本金1億円以下)
    cit_tier1: float               # 法人税 第1段階
    cit_tier2: float               # 法人税 第2段階
    cit_national: float            # 国税合計
    local_tax_estimate: float      # 地方税概算
    cit_total: float               # 合計税負担
    effective_rate: float          # 実効税率


def bereken_cit_japan(
    taxable_income: float,
    jaar: int = 2025,
    capital: float = 10_000_000,   # 資本金 (default ¥10M = SME)
) -> CITResult:
    """Calculate Japan corporate income tax.

    Args:
        taxable_income: 課税所得 (JPY); non-positive income returns a zero-tax result
        jaar: fiscal year (2024 or 2025)
        capital: paid-in capital in JPY; ≤ ¥100M → SME rates apply

    Returns:
        CITResult with national + local tax breakdown.
    """
    params = json.load(open(PARAMS_PATH))["years"][str(jaar)]["CIT"]
    sme_cap = params["sme_capital_threshold"]
    sme_thresh = params["sme_threshold"]
    sme_rate = params["sme_rate"]
    std_rate = params["standard_rate"]
    local_pct = params["local_tax_estimate_pct"]

    is_sme = capital <= sme_cap

    if taxable_income <= 0:
        return CITResult(
            jaar=jaar,
            taxable_income=taxable_income,
            is_sme=is_sme,
            cit_tier1=0.0,
            cit_tier2=0.0,
            cit_national=0.0,
            local_tax_estimate=0.0,
            cit_total=0.0,
            effective_rate=0.0,
        )

    if is_sme:
        t1 = min(taxable_income, sme_thresh) * sme_rate
        t2 = max(0.0, taxable_income - sme_thresh) * std_rate
    else:
        t1 = 0.0
        t2 = taxable_income * std_rate

    national = t1 + t2
    local_est = national * local_pct
    total = national + local_est
    effective = total / taxable_income if taxable_income > 0 else 0.0

    return CITResult(
        jaar=jaar,
        taxable_income=taxable_income,
        is_sme=is_sme,
        cit_tier1=t1,
        cit_tier2=t2,
        cit_national=national,
        local_tax_estimate=local_est,
        cit_total=total,
        effective_rate=effective,
    )
