"""Republic of Fiji tax property tests — 9 tests."""
import json
import os

import pytest

from ledgerfield.schemas.FJ.fj_gaap import FJ_GAAP
from ledgerfield.tax.FJ.cit import bereken_cit_fiji

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/FJ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_fj_schema_min_60_accounts():
    assert len(FJ_GAAP) >= 60


# 2 — resident CIT: 20% on 1,000,000 → 200,000
def test_resident_cit_20pct():
    result = bereken_cit_fiji(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.20)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 3 — non-resident CIT: 25% on 1,000,000 → 250,000
def test_non_resident_cit_25pct():
    result = bereken_cit_fiji(1_000_000.0, 2025, non_resident=True)
    assert result.cit_rate == pytest.approx(0.25)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_fiji(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_fiji(-50_000.0, 2025, non_resident=True).cit_totaal == pytest.approx(0.0)


# 5 — VAT is 15%
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)


# 6 — issue #39: needs_verification flag + source URL present
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://www.frcs.org.fj/" in p["sources"]


# 7 — effective rate equals statutory rate on positive profit
def test_effectief_tarief():
    assert bereken_cit_fiji(500_000.0, 2025).effectief_tarief == pytest.approx(0.20)
    assert bereken_cit_fiji(500_000.0, 2025, non_resident=True).effectief_tarief == pytest.approx(0.25)


# 8 — params CIT rates match calculator
def test_params_cit_rates():
    p = _params()
    assert p["cit"]["standard_rate"] == pytest.approx(0.20)
    assert p["cit"]["non_resident_rate"] == pytest.approx(0.25)


# 9 — all account codes are unique
def test_account_codes_unique():
    codes = [a.code for a in FJ_GAAP]
    assert len(codes) == len(set(codes))
