"""Republic of Albania tax property tests — 8 tests.

NOTE: AL rates are AI-estimated (issue #39) and must be source-verified.
"""
import json
import os

import pytest

from ledgerfield.schemas.AL.al_gaap import AL_GAAP
from ledgerfield.tax.AL.cit import bereken_cit_albanie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AL/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_al_schema_min_60_accounts():
    assert len(AL_GAAP) >= 60


# 2 — CIT rate = 15%
def test_cit_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — 1,000,000 profit → 150,000 CIT
def test_cit_on_one_million():
    result = bereken_cit_albanie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(150_000.0)


# 4 — effective rate equals 15% on positive profit
def test_effectief_tarief():
    result = bereken_cit_albanie(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.15)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_albanie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_albanie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_albanie(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 6 — VAT = 20%
def test_vat_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)


# 7 — needs_verification flag true and sources URL present (issue #39)
def test_needs_verification_and_sources():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://www.tatime.gov.al/" in p["sources"]


# 8 — small-business 0% note present
def test_small_business_note_present():
    assert _params()["cit"]["small_business_rate"] == pytest.approx(0.0)
    assert "note" in _params()["cit"]
