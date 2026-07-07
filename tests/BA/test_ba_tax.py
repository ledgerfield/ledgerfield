"""Bosnia and Herzegovina tax property tests — 8 tests.

AI-estimated pack (issue #39): rules are unverified estimates pending
confirmation against the Indirect Taxation Authority (https://www.uino.gov.ba/)
and the relevant entity tax administrations.
"""
import json
import os

import pytest

from ledgerfield.schemas.BA.ba_gaap import BA_GAAP
from ledgerfield.tax.BA.cit import bereken_cit_bosnie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/BA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ba_schema_min_60_accounts():
    assert len(BA_GAAP) >= 60


# 2 — CIT flat 10% on 1,000,000 → 100,000
def test_cit_flat_10pct():
    result = bereken_cit_bosnie(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.10)
    assert result.cit_totaal == pytest.approx(100_000.0)


# 3 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_bosnie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bosnie(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 4 — VAT standard rate 17%
def test_vat_17pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.17)


# 5 — needs verification flag + official source URL present
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert p["metadata"]["needs_verification"] is True
    assert "https://www.uino.gov.ba/" in p["sources"]


# 6 — effective rate equals statutory rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_bosnie(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.10)


# 7 — two-entity system: FBiH and RS both at 10%
def test_two_entity_system():
    ents = _params()["cit"]["entities"]
    assert ents["FBiH"]["rate"] == pytest.approx(0.10)
    assert ents["RS"]["rate"] == pytest.approx(0.10)


# 8 — every account has a valid category and normal balance
def test_account_integrity():
    valid_cat = {"Asset", "Liability", "Equity", "Revenue", "Expense"}
    valid_bal = {"Debit", "Credit"}
    for acc in BA_GAAP:
        assert acc.category in valid_cat
        assert acc.normal_balance in valid_bal
