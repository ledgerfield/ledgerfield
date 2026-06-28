"""Canada tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CA.ca_gaap import CA_GAAP
from ledgerfield.tax.CA.cit import bereken_cit_canada

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ca_schema_min_60_accounts():
    assert len(CA_GAAP) >= 60


# 2 — CCPC small-business tranche: first CAD 500k at 9% = CAD 45,000
def test_ccpc_first_500k_cit_equals_45000():
    result = bereken_cit_canada(500_000.0, 2025, is_ccpc=True)
    assert result.cit_small_business == pytest.approx(45_000.0)


# 3 — general rate applies at 15% above the small-business limit
def test_general_rate_above_500k_is_15pct():
    result = bereken_cit_canada(600_000.0, 2025, is_ccpc=True)
    # the 100k over the limit is taxed at 15%
    assert result.cit_general == pytest.approx(100_000.0 * 0.15)


# 4 — CCPC total CIT is lower than non-CCPC for the same profit
def test_ccpc_cit_lower_than_non_ccpc():
    ccpc = bereken_cit_canada(500_000.0, 2025, is_ccpc=True)
    non_ccpc = bereken_cit_canada(500_000.0, 2025, is_ccpc=False)
    assert ccpc.cit_totaal < non_ccpc.cit_totaal


# 5 — federal personal income tax: bracket 1 rate = 15%
def test_federal_income_bracket_1_rate_15pct():
    bracket = _params()["income_tax_brackets_2025"][0]
    assert bracket["rate"] == pytest.approx(0.15)


# 6 — GST federal rate = 5%
def test_gst_federal_rate_5pct():
    assert _params()["gst_hst"]["federal_gst"] == pytest.approx(0.05)


# 7 — CPP employer rate = 5.95%
def test_cpp_employer_rate_595pct():
    assert _params()["cpp"]["employer_rate"] == pytest.approx(0.0595)


# 8 — CPP employee rate = 5.95%
def test_cpp_employee_rate_595pct():
    assert _params()["cpp"]["employee_rate"] == pytest.approx(0.0595)


# 9 — zero profit returns zero CIT
def test_bereken_cit_canada_zero_winst():
    result = bereken_cit_canada(0.0, 2025)
    assert result.cit_totaal == pytest.approx(0.0)


# 10 — effective rate for CCPC at exactly 500k equals 9%
def test_effectief_tarief_ccpc_at_500k_equals_9pct():
    result = bereken_cit_canada(500_000.0, 2025, is_ccpc=True)
    assert result.effectief_tarief == pytest.approx(0.09)
