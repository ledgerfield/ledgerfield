"""Portugal (PT) tax property tests — 5 tests.

Covers:
1. PT_SNC schema has sufficient accounts
2. IRC standard rate = 21%
3. SME IRC reduced rate = 17% on first €25k
4. IVA standard rate = 23%
5. IRS top bracket = 48%
"""
import json
import os

import pytest

from ledgerfield.schemas.PT.schema import PT_SNC

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PT/params.json",
)

RULESET_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../rulesets/PT_2025.json",
)


def _params() -> dict:
    with open(PARAMS_PATH) as f:
        return json.load(f)


def _ruleset() -> dict:
    with open(RULESET_PATH) as f:
        return json.load(f)


# 1 — SNC schema coverage: at least 100 accounts
def test_pt_snc_min_100_accounts():
    assert len(PT_SNC) >= 100, f"Expected >=100 SNC accounts, got {len(PT_SNC)}"


# 2 — IRC standard rate is 21%
def test_irc_standard_rate_21pct():
    params = _params()
    assert params["irc"]["standard_rate"] == pytest.approx(0.21), (
        "IRC standard rate should be 21%"
    )


# 3 — SME IRC reduced rate is 17% on first €25k
def test_irc_sme_reduced_rate_17pct():
    params = _params()
    assert params["irc"]["sme_reduced_rate"] == pytest.approx(0.17), (
        "IRC SME reduced rate should be 17%"
    )
    assert params["irc"]["sme_first_tranche_eur"] == 25000, (
        "IRC SME first tranche should be €25.000"
    )


# 4 — IVA (VAT) standard rate is 23%
def test_iva_standard_rate_23pct():
    params = _params()
    assert params["iva"]["standard_rate"] == pytest.approx(0.23), (
        "IVA standard rate should be 23%"
    )


# 5 — IRS top bracket is 48%
def test_irs_top_bracket_48pct():
    params = _params()
    brackets = params["irs_brackets_2025"]
    top_rate = max(b["rate"] for b in brackets)
    assert top_rate == pytest.approx(0.48), (
        f"IRS top bracket should be 48%, got {top_rate}"
    )
