"""Ukraine tax property tests — 9 tests."""
import json
import os

import pytest

from ledgerfield.schemas.UA.ua_gaap import UA_GAAP
from ledgerfield.tax.UA.cit import bereken_cit_oekraine

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/UA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ua_schema_min_60_accounts():
    assert len(UA_GAAP) >= 60


# 2 — standard CIT rate = 18%
def test_cit_rate_18pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.18)


# 3 — standard company: 18% on profit
def test_standard_company_18pct():
    result = bereken_cit_oekraine(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(180_000.0)


# 4 — bank: 25% on profit
def test_bank_25pct():
    result = bereken_cit_oekraine(1_000_000.0, 2025, bank=True)
    assert result.cit_totaal == pytest.approx(250_000.0)
    assert result.cit_rate == pytest.approx(0.25)


# 5 — VAT standard rate = 20%
def test_vat_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)
    assert _params()["vat"]["implemented"] is True


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_oekraine(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oekraine(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oekraine(-50_000.0, 2025, bank=True).cit_totaal == pytest.approx(0.0)


# 7 — simplified single-tax system documented
def test_simplified_single_tax_note():
    assert _params()["simplified_single_tax"]["applies"] is True
    assert "single" in _params()["simplified_single_tax"]["note"].lower()


# 8 — wartime levies documented
def test_wartime_levies_note():
    assert _params()["wartime_levies"]["applies"] is True
    assert "levy" in _params()["wartime_levies"]["note"].lower()


# 9 — needs_verification flag + sources URL present (Issue #39)
def test_needs_verification_and_sources():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert p["sources"][0]["url"] == "https://tax.gov.ua/"
