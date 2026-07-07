"""Republic of Serbia tax property tests — 8 tests."""
import json
import os

import pytest

from ledgerfield.schemas.RS.rs_gaap import RS_GAAP
from ledgerfield.tax.RS.cit import bereken_cit_servie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/RS/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_rs_schema_min_60_accounts():
    assert len(RS_GAAP) >= 60


# 2 — CIT rate = 15%
def test_cit_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — flat 15% on 1,000,000 → 150,000
def test_cit_flat_15pct():
    result = bereken_cit_servie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(150_000.0)
    assert result.effectief_tarief == pytest.approx(0.15)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_servie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_servie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — VAT standard rate = 20%
def test_vat_rate_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)


# 6 — needs_verification flag set true
def test_needs_verification_true():
    assert _params()["metadata"]["needs_verification"] is True
    assert _params()["metadata"]["source_status"] == "ai_estimated_needs_verification"


# 7 — official source URL present
def test_sources_url_present():
    assert "https://www.purs.gov.rs/" in _params()["sources"]


# 8 — arbitrary profit scales linearly at 15%
def test_cit_linear_scaling():
    assert bereken_cit_servie(200_000.0, 2025).cit_totaal == pytest.approx(30_000.0)
