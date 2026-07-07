"""Republic of Armenia tax property tests."""
import json
import os

import pytest

from ledgerfield.schemas.AM.am_gaap import AM_GAAP
from ledgerfield.tax.AM.cit import bereken_cit_armenie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_am_schema_min_60_accounts():
    assert len(AM_GAAP) >= 60


# 2 — CIT rate = 18%
def test_cit_rate_18pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.18)


# 3 — 1,000,000 profit → 180,000 tax
def test_cit_1m_profit():
    result = bereken_cit_armenie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(180_000.0)


# 4 — non-positive profit yields zero tax
def test_non_positive_profit_zero_tax():
    assert bereken_cit_armenie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_armenie(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — effective rate equals statutory rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_armenie(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.18)


# 6 — VAT standard rate = 20%
def test_vat_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)


# 7 — issue #39: needs_verification true and sources URL present
def test_needs_verification_and_source_url():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    urls = [s["url"] for s in p["sources"]]
    assert "https://www.petekamutner.am/" in urls
