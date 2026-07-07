"""Turkmenistan tax property tests."""
import json
import os

import pytest

from ledgerfield.schemas.TM.tm_gaap import TM_GAAP
from ledgerfield.tax.TM.cit import bereken_cit_turkmenistan

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_tm_schema_min_60_accounts():
    assert len(TM_GAAP) >= 60


# 2 — private/domestic CIT rate = 8%
def test_cit_private_rate_8pct():
    assert _params()["cit"]["private_domestic_rate"] == pytest.approx(0.08)


# 3 — private/domestic 8% on 1,000,000 → 80,000
def test_cit_private_8pct():
    result = bereken_cit_turkmenistan(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(80_000.0)
    assert result.staats_of_buitenlands is False


# 4 — state/foreign 20% on 1,000,000 → 200,000
def test_cit_state_or_foreign_20pct():
    result = bereken_cit_turkmenistan(1_000_000.0, 2025, staats_of_buitenlands=True)
    assert result.cit_totaal == pytest.approx(200_000.0)
    assert result.cit_rate == pytest.approx(0.20)


# 5 — VAT standard rate = 15%
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_turkmenistan(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_turkmenistan(-90_000.0, 2025, staats_of_buitenlands=True).cit_totaal == pytest.approx(0.0)


# 7 — needs verification + source URL (issue #39)
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://www.minfin.gov.tm/" in p["sources"]
