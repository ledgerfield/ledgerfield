"""Republic of Lithuania tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.LT.lt_gaap import LT_GAAP
from ledgerfield.tax.LT.cit import bereken_cit_litouwen

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/LT/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_lt_schema_min_60_accounts():
    assert len(LT_GAAP) >= 60


# 2 — standard CIT rate = 16% (raised from 15% on 1 Jan 2025)
def test_cit_standard_rate_16pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.16)


# 3 — standard company: 1,000,000 → 160,000
def test_standard_company_16pct():
    result = bereken_cit_litouwen(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(160_000.0)
    assert result.effectief_tarief == pytest.approx(0.16)


# 4 — small company (≤10 employees, income ≤ EUR 300k): 6%
def test_small_company_6pct():
    result = bereken_cit_litouwen(1_000_000.0, 2025, small=True)
    assert result.cit_totaal == pytest.approx(60_000.0)
    assert result.cit_rate == pytest.approx(0.06)


# 5 — small company in first tax year: 0%
def test_small_company_first_year_0pct():
    result = bereken_cit_litouwen(1_000_000.0, 2025, small=True, first_year=True)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.cit_rate == pytest.approx(0.0)


# 6 — small-company thresholds in params
def test_small_company_thresholds():
    criteria = _params()["cit"]["small_company_criteria"]
    assert criteria["max_employees"] == 10
    assert criteria["max_income_eur"] == 300_000


# 7 — VAT (PVM) standard 21%
def test_vat_standard_21pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.21)


# 8 — reduced VAT rates 9% and 5%
def test_vat_reduced_rates():
    reduced = _params()["vat"]["reduced_rates"]
    assert 0.09 in reduced
    assert 0.05 in reduced


# 9 — OSS eligible (EU member state)
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 10 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_litouwen(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_litouwen(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_litouwen(-25_000.0, 2025, small=True).cit_totaal == pytest.approx(0.0)


# 11 — official source is VMI
def test_official_source_vmi():
    sources = _params()["metadata"]["official_sources"]
    assert any("vmi.lt" in s["url"] for s in sources)
