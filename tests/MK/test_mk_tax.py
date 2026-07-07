"""Republic of North Macedonia tax property tests — 8 tests.

NOTE: MK rates are AI-estimated (issue #39) and must be source-verified.
"""
import json
import os

import pytest

from ledgerfield.schemas.MK.mk_gaap import MK_GAAP
from ledgerfield.tax.MK.cit import bereken_cit_noord_macedonie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MK/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_mk_schema_min_60_accounts():
    assert len(MK_GAAP) >= 60


# 2 — CIT rate = 10%
def test_cit_rate_10pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.10)


# 3 — 1,000,000 profit → 100,000 CIT
def test_cit_on_one_million():
    result = bereken_cit_noord_macedonie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(100_000.0)


# 4 — effective rate equals 10% on positive profit
def test_effectief_tarief():
    result = bereken_cit_noord_macedonie(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.10)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_noord_macedonie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_noord_macedonie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_noord_macedonie(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 6 — VAT = 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)


# 7 — needs_verification flag true and sources URL present (issue #39)
def test_needs_verification_and_sources():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://www.ujp.gov.mk/" in p["sources"]


# 8 — VAT implemented flag true
def test_vat_implemented():
    assert _params()["vat"]["implemented"] is True
