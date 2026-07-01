"""Argentina tax property tests — 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.AR.schema import AR_GAAP

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AR/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ar_schema_min_60_accounts():
    assert len(AR_GAAP) >= 60


# 2 — CIT flat rate = 35%
def test_cit_rate_35pct():
    assert _params()["cit"]["rate"] == pytest.approx(0.35)


# 3 — IVA standard rate = 21%
def test_iva_standard_rate_21pct():
    assert _params()["iva"]["standard_rate"] == pytest.approx(0.21)


# 4 — IVA reduced rate = 10.5%
def test_iva_reduced_rate_10_5pct():
    assert _params()["iva"]["reduced_rate"] == pytest.approx(0.105)


# 5 — top income tax bracket = 35%
def test_income_tax_top_bracket_35pct():
    brackets = _params()["income_tax_2025"]["brackets"]
    top_rate = max(b["rate"] for b in brackets)
    assert top_rate == pytest.approx(0.35)
