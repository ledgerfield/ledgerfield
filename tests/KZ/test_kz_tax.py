"""Republic of Kazakhstan tax property tests."""
import json
import os

import pytest

from ledgerfield.schemas.KZ.kz_gaap import KZ_GAAP
from ledgerfield.tax.KZ.cit import bereken_cit_kazachstan

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/KZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_kz_schema_min_60_accounts():
    assert len(KZ_GAAP) >= 60


# 2 — CIT rate = 20%
def test_cit_rate_20pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.20)


# 3 — flat 20% on 1,000,000 → 200,000
def test_cit_flat_20pct():
    result = bereken_cit_kazachstan(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_kazachstan(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_kazachstan(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — VAT = 12%
def test_vat_12pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.12)


# 6 — effective rate equals 20% on positive profit
def test_effectief_tarief():
    result = bereken_cit_kazachstan(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.20)


# 7 — issue #39: needs verification + official source URL present
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert p["metadata"]["needs_verification"] is True
    urls = [s["url"] for s in p["sources"]]
    assert "https://kgd.gov.kz/" in urls
