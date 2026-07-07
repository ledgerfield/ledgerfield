"""Republic of Kenya tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.KE.ke_gaap import KE_GAAP
from ledgerfield.tax.KE.cit import bereken_cit_kenia

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/KE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ke_schema_min_60_accounts():
    assert len(KE_GAAP) >= 60


# 2 — resident CIT rate = 30%
def test_cit_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — resident company: 30% of 1,000,000 = 300,000
def test_resident_company_30pct():
    result = bereken_cit_kenia(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)


# 4 — non-resident branch: 37.5% of 1,000,000 = 375,000
def test_non_resident_branch_37_5pct():
    result = bereken_cit_kenia(1_000_000.0, 2025, non_resident_branch=True)
    assert result.cit_totaal == pytest.approx(375_000.0)
    assert result.cit_rate == pytest.approx(0.375)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_kenia(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_kenia(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — VAT standard rate = 16%
def test_vat_16pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.16)
    assert _params()["vat"]["implemented"] is True


# 7 — SEP tax 3% (replaced DST per Finance Act 2024)
def test_sep_tax_3pct_note():
    sep = _params()["significant_economic_presence_tax"]
    assert sep["rate"] == pytest.approx(0.03)
    assert "Digital Service Tax" in sep["note"]


# 8 — minimum top-up tax (Pillar Two QDMTT) documented
def test_minimum_top_up_tax_note():
    assert "QDMTT" in _params()["minimum_top_up_tax"]["note"]


# 9 — turnover tax 1.5% for small businesses
def test_turnover_tax_1_5pct():
    assert _params()["turnover_tax"]["rate"] == pytest.approx(0.015)


# 10 — official source is KRA
def test_official_source_kra():
    sources = _params()["metadata"]["official_sources"]
    assert any("kra.go.ke" in s["url"] for s in sources)


# 11 — effective rate equals nominal rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_kenia(2_500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.30)
    branch = bereken_cit_kenia(2_500_000.0, 2025, non_resident_branch=True)
    assert branch.effectief_tarief == pytest.approx(0.375)


# 12 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
