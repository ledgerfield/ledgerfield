"""Republic of Tajikistan tax property tests."""
import json
import os

import pytest

from ledgerfield.schemas.TJ.tj_gaap import TJ_GAAP
from ledgerfield.tax.TJ.cit import bereken_cit_tadzjikistan

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TJ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_tj_schema_min_60_accounts():
    assert len(TJ_GAAP) >= 60


# 2 — CIT standard rate = 18%
def test_cit_standard_rate_18pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.18)


# 3 — standard 18% on 1,000,000 → 180,000
def test_cit_standard_18pct():
    result = bereken_cit_tadzjikistan(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(180_000.0)
    assert result.producent is False


# 4 — producer 13% on 1,000,000 → 130,000
def test_cit_producer_13pct():
    result = bereken_cit_tadzjikistan(1_000_000.0, 2025, producent=True)
    assert result.cit_totaal == pytest.approx(130_000.0)
    assert result.cit_rate == pytest.approx(0.13)


# 5 — VAT standard rate ~14%
def test_vat_14pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.14)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_tadzjikistan(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_tadzjikistan(-75_000.0, 2025, producent=True).cit_totaal == pytest.approx(0.0)


# 7 — needs verification + source URL (issue #39)
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://andoz.tj/" in p["sources"]
