"""Russian Federation tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.RU.ru_gaap import RU_GAAP
from ledgerfield.tax.RU.cit import bereken_cit_rusland

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/RU/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ru_schema_min_60_accounts():
    assert len(RU_GAAP) >= 60


# 2 — standard CIT rate = 25% (raised from 2025)
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — standard company: 25% on profit (post-2025 increase)
def test_standard_company_25pct():
    result = bereken_cit_rusland(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 4 — IT company: 5% on profit
def test_it_company_5pct():
    result = bereken_cit_rusland(1_000_000.0, 2025, it_company=True)
    assert result.cit_totaal == pytest.approx(50_000.0)
    assert result.cit_rate == pytest.approx(0.05)


# 5 — VAT standard rate = 20%
def test_vat_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)
    assert _params()["vat"]["implemented"] is True


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_rusland(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_rusland(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_rusland(-75_000.0, 2025, it_company=True).cit_totaal == pytest.approx(0.0)


# 7 — 2025 rate-increase note present (20% -> 25%)
def test_2025_rate_increase_documented():
    cit = _params()["cit"]
    assert cit["rate_increase_2025"] is True
    assert cit["previous_rate"] == pytest.approx(0.20)
    assert "25%" in cit["basis"]


# 8 — sanctions note present in metadata (Issue #39)
def test_sanctions_note_present():
    assert "sanction" in _params()["metadata"]["sanctions_note"].lower()


# 9 — needs_verification flag + sources URL present (Issue #39)
def test_needs_verification_and_sources():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert p["sources"][0]["url"] == "https://www.nalog.gov.ru/"


# 10 — IT reduced rate documented in params
def test_it_rate_in_params():
    assert _params()["cit"]["special_rates"]["it_companies"] == pytest.approx(0.05)
