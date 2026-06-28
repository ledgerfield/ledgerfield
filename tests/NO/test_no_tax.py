"""Norway (NO) tax property tests -- 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.NO.schema import NO_GAAP

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 -- schema coverage
def test_no_schema_min_60_accounts():
    assert len(NO_GAAP) >= 60


# 2 -- CIT standard rate = 22%
def test_cit_standard_rate_22pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.22)


# 3 -- VAT standard rate = 25%
def test_vat_standard_rate_25pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.25)


# 4 -- VAT food reduced rate = 15%
def test_vat_food_rate_15pct():
    assert _params()["vat"]["reduced_rate_food"] == pytest.approx(0.15)


# 5 -- Employer NI zone 1 = 14.1%
def test_employer_ni_zone1_141pct():
    assert _params()["employer_ni"]["zones"]["zone1_standard"] == pytest.approx(0.141)
