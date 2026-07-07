"""Republic of Azerbaijan tax property tests — 8 tests.

AI-estimated pack (issue #39): rules are unverified estimates pending
confirmation against the State Tax Service (https://www.taxes.gov.az/).
"""
import json
import os

import pytest

from ledgerfield.schemas.AZ.az_gaap import AZ_GAAP
from ledgerfield.tax.AZ.cit import bereken_cit_azerbeidzjan

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_az_schema_min_60_accounts():
    assert len(AZ_GAAP) >= 60


# 2 — CIT flat 20% on 1,000,000 → 200,000
def test_cit_flat_20pct():
    result = bereken_cit_azerbeidzjan(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.20)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 3 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_azerbeidzjan(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_azerbeidzjan(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 4 — VAT standard rate 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)


# 5 — needs verification flag + official source URL present
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert p["metadata"]["needs_verification"] is True
    assert "https://www.taxes.gov.az/" in p["sources"]


# 6 — effective rate equals statutory rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_azerbeidzjan(750_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.20)


# 7 — simplified turnover regime is noted in params
def test_simplified_regime_noted():
    assert _params()["simplified_tax"]["implemented"] is True


# 8 — every account has a valid category and normal balance
def test_account_integrity():
    valid_cat = {"Asset", "Liability", "Equity", "Revenue", "Expense"}
    valid_bal = {"Debit", "Credit"}
    for acc in AZ_GAAP:
        assert acc.category in valid_cat
        assert acc.normal_balance in valid_bal
