"""Brazil tax property tests — 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.BR.schema import BR_NBC_TG

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/BR/params.json",
)
RULESET_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../rulesets/BR_2025.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


def _ruleset():
    with open(RULESET_PATH) as f:
        return json.load(f)


# 1 — schema has sufficient accounts (NBC TG CPC chart)
def test_br_schema_min_80_accounts():
    assert len(BR_NBC_TG) >= 80


# 2 — IRPJ base rate is 15%
def test_irpj_base_rate_15pct():
    assert _params()["cit"]["irpj_base_rate"] == pytest.approx(0.15)


# 3 — CSLL rate is 9%
def test_csll_rate_9pct():
    assert _params()["cit"]["csll_rate"] == pytest.approx(0.09)


# 4 — Effective combined CIT rate (IRPJ + surtax + CSLL) is 34%
def test_effective_combined_rate_34pct():
    assert _params()["cit"]["effective_combined_rate"] == pytest.approx(0.34)


# 5 — Personal income tax top rate is 27.5%
def test_income_tax_top_rate_275pct():
    assert _params()["income_tax_top_rate"] == pytest.approx(0.275)
