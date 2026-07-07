"""Mongolia tax property tests — 8 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MN.mn_gaap import MN_GAAP
from ledgerfield.tax.MN.cit import bereken_cit_mongolie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MN/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_mn_schema_min_60_accounts():
    assert len(MN_GAAP) >= 60


# 2 — lower band: 10% on income at/below MNT 6bn
def test_cit_lower_band_10pct():
    result = bereken_cit_mongolie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(100_000.0)
    assert result.band2_tax == pytest.approx(0.0)


# 3 — progressive bracket math above MNT 6bn
def test_cit_progressive_bracket_math():
    result = bereken_cit_mongolie(10_000_000_000.0, 2025)
    # 10% * 6bn + 25% * 4bn = 600,000,000 + 1,000,000,000
    assert result.band1_tax == pytest.approx(600_000_000.0)
    assert result.band2_tax == pytest.approx(1_000_000_000.0)
    assert result.cit_totaal == pytest.approx(1_600_000_000.0)


# 4 — exactly at threshold: still all lower band
def test_cit_at_threshold():
    result = bereken_cit_mongolie(6_000_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(600_000_000.0)
    assert result.band2_tax == pytest.approx(0.0)


# 5 — VAT is 10%
def test_vat_10pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.10)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_mongolie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_mongolie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 7 — issue #39: needs verification flag + status
def test_needs_verification_metadata():
    meta = _params()["metadata"]
    assert meta["needs_verification"] is True
    assert meta["source_status"] == "ai_estimated_needs_verification"


# 8 — issue #39: official source URL present
def test_sources_url_present():
    sources = _params()["sources"]
    assert any(s["url"] == "https://mta.mn/" for s in sources)
