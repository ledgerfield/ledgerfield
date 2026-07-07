"""Montenegro tax property tests — 9 tests (progressive CIT)."""
import json
import os

import pytest

from ledgerfield.schemas.ME.me_gaap import ME_GAAP
from ledgerfield.tax.ME.cit import bereken_cit_montenegro

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/ME/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_me_schema_min_60_accounts():
    assert len(ME_GAAP) >= 60


# 2 — band 1 only: €50,000 → 9% → 4,500
def test_cit_band1_only():
    result = bereken_cit_montenegro(50_000.0, 2025)
    assert result.cit_totaal == pytest.approx(4_500.0)
    assert result.cit_band1 == pytest.approx(4_500.0)
    assert result.cit_band2 == pytest.approx(0.0)
    assert result.cit_band3 == pytest.approx(0.0)


# 3 — band 1 + band 2: €1,000,000 → 9%*100k + 12%*900k = 117,000
def test_cit_band1_and_band2():
    result = bereken_cit_montenegro(1_000_000.0, 2025)
    assert result.cit_band1 == pytest.approx(9_000.0)
    assert result.cit_band2 == pytest.approx(108_000.0)
    assert result.cit_totaal == pytest.approx(117_000.0)


# 4 — all three bands: €2,000,000 → 9,000 + 168,000 + 75,000 = 252,000
def test_cit_all_three_bands():
    result = bereken_cit_montenegro(2_000_000.0, 2025)
    assert result.cit_band1 == pytest.approx(9_000.0)
    assert result.cit_band2 == pytest.approx(168_000.0)
    assert result.cit_band3 == pytest.approx(75_000.0)
    assert result.cit_totaal == pytest.approx(252_000.0)


# 5 — exact threshold €100,000 → 9% → 9,000, no band 2 spill
def test_cit_at_first_threshold():
    result = bereken_cit_montenegro(100_000.0, 2025)
    assert result.cit_totaal == pytest.approx(9_000.0)
    assert result.cit_band2 == pytest.approx(0.0)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_montenegro(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_montenegro(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 7 — VAT standard rate = 21%
def test_vat_rate_21pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.21)


# 8 — needs_verification flag set true
def test_needs_verification_true():
    assert _params()["metadata"]["needs_verification"] is True
    assert _params()["metadata"]["source_status"] == "ai_estimated_needs_verification"


# 9 — official source URL present
def test_sources_url_present():
    assert "https://www.poreskauprava.gov.me/" in _params()["sources"]
