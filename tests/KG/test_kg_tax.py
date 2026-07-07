"""Kyrgyz Republic tax property tests."""
import json
import os

import pytest

from ledgerfield.schemas.KG.kg_gaap import KG_GAAP
from ledgerfield.tax.KG.cit import bereken_cit_kirgizie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/KG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_kg_schema_min_60_accounts():
    assert len(KG_GAAP) >= 60


# 2 — CIT rate = 10%
def test_cit_rate_10pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.10)


# 3 — flat 10% on 1,000,000 → 100,000
def test_cit_flat_10pct():
    result = bereken_cit_kirgizie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(100_000.0)
    assert result.effectief_tarief == pytest.approx(0.10)


# 4 — VAT standard rate = 12%
def test_vat_12pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.12)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_kirgizie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_kirgizie(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — sales tax note present
def test_sales_tax_note():
    assert "sales_tax" in _params()


# 7 — needs verification + source URL (issue #39)
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://www.sti.gov.kg/" in p["sources"]
