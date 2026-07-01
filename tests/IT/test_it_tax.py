"""Italy (IT) tax property tests — 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.IT.schema import OIC_IT, get_account, accounts_by_category

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/IT/params.json",
)

RULESET_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../rulesets/IT_2025.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


def _ruleset():
    with open(RULESET_PATH) as f:
        return json.load(f)


# 1 — schema has at least 60 accounts
def test_oic_it_schema_min_60_accounts():
    assert len(OIC_IT) >= 60


# 2 — IRES rate is 24%
def test_ires_rate_24pct():
    p = _params()
    assert p["ires"]["rate"] == pytest.approx(0.24)


# 3 — VAT standard rate is 22%
def test_iva_standard_rate_22pct():
    p = _params()
    assert p["iva"]["standard_rate"] == pytest.approx(0.22)


# 4 — IRPEF top rate is 43%
def test_irpef_top_rate_43pct():
    p = _params()
    assert p["irpef"]["top_rate"] == pytest.approx(0.43)


# 5 — ruleset jurisdiction is IT and currency is EUR
def test_ruleset_jurisdiction_and_currency():
    r = _ruleset()
    assert r["jurisdiction"] == "IT"
    assert r["currency"] == "EUR"
