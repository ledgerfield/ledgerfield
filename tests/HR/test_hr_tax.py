"""Croatia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.HR.hr_gaap import HR_GAAP
from ledgerfield.tax.HR.cit import bereken_cit_kroatie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/HR/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_hr_schema_min_60_accounts():
    assert len(HR_GAAP) >= 60


# 2 — CIT rates: 18% standard, 10% small
def test_cit_rates_params():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.18)
    assert _params()["cit"]["small_taxpayer_rate"] == pytest.approx(0.10)


# 3 — standard: 1,000,000 profit → 180,000 CIT
def test_cit_standard_1m_profit():
    result = bereken_cit_kroatie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(180_000.0)
    assert result.cit_rate == pytest.approx(0.18)


# 4 — small taxpayer (revenue <= EUR 1m): 1,000,000 profit → 100,000 CIT
def test_cit_small_1m_profit():
    result = bereken_cit_kroatie(1_000_000.0, 2025, small=True)
    assert result.cit_totaal == pytest.approx(100_000.0)
    assert result.cit_rate == pytest.approx(0.10)


# 5 — small-taxpayer revenue threshold = EUR 1,000,000
def test_small_taxpayer_threshold():
    assert _params()["cit"]["small_taxpayer_revenue_threshold_eur"] == 1_000_000


# 6 — effectief tarief matches the applied rate
def test_effectief_tarief():
    assert bereken_cit_kroatie(500_000.0, 2025).effectief_tarief == pytest.approx(0.18)
    assert bereken_cit_kroatie(500_000.0, 2025, small=True).effectief_tarief == pytest.approx(0.10)


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_kroatie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_kroatie(-100_000.0, 2025, small=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_kroatie(-100_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 8 — VAT (PDV) standard rate 25%
def test_vat_standard_25pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.25)


# 9 — reduced VAT rates 13% and 5%
def test_vat_reduced_rates():
    reduced = _params()["vat"]["reduced_rates"]
    assert reduced["reduced_13"] == pytest.approx(0.13)
    assert reduced["reduced_5"] == pytest.approx(0.05)


# 10 — EU OSS eligible
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 11 — Pillar Two note present
def test_pillar_two_note():
    assert "Pillar Two" in _params()["cit"]["pillar_two_note"]


# 12 — PIT municipal-rate system note and official source Porezna uprava
def test_pit_municipal_and_source():
    assert _params()["personal_income_tax"]["system"] == "municipal_rates"
    sources = _params()["metadata"]["official_sources"]
    assert any("porezna-uprava.hr" in s["url"] for s in sources)
    assert _params()["metadata"]["effective_date_range"]["start"].startswith("2025")
