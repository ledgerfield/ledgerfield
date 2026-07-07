"""Nepal tax property tests — 9 tests."""
import json
import os

import pytest

from ledgerfield.schemas.NP.np_gaap import NP_GAAP
from ledgerfield.tax.NP.cit import bereken_cit_nepal

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NP/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_np_schema_min_60_accounts():
    assert len(NP_GAAP) >= 60


# 2 — standard sector: 25%
def test_cit_standard_25pct():
    result = bereken_cit_nepal(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)
    assert result.cit_rate == pytest.approx(0.25)


# 3 — financial / telecom sector: 30%
def test_cit_financial_telecom_30pct():
    result = bereken_cit_nepal(1_000_000.0, 2025, sector="financial_telecom")
    assert result.cit_totaal == pytest.approx(300_000.0)


# 4 — special industry: 20%
def test_cit_special_industry_20pct():
    result = bereken_cit_nepal(1_000_000.0, 2025, sector="special_industry")
    assert result.cit_totaal == pytest.approx(200_000.0)


# 5 — unknown sector raises ValueError
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_nepal(1_000_000.0, 2025, sector="mining")


# 6 — VAT is 13%
def test_vat_13pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.13)


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_nepal(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_nepal(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — issue #39: needs verification flag + status
def test_needs_verification_metadata():
    meta = _params()["metadata"]
    assert meta["needs_verification"] is True
    assert meta["source_status"] == "ai_estimated_needs_verification"


# 9 — issue #39: official source URL present
def test_sources_url_present():
    sources = _params()["sources"]
    assert any(s["url"] == "https://ird.gov.np/" for s in sources)
