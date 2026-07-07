"""Trinidad and Tobago tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.TT.tt_gaap import TT_GAAP
from ledgerfield.tax.TT.cit import bereken_cit_trinidad

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TT/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_tt_schema_min_60_accounts():
    assert len(TT_GAAP) >= 60


# 2 — standard CIT rate = 30%
def test_cit_rate_30pct_standard():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — standard: 1,000,000 → 300,000
def test_standard_one_million():
    result = bereken_cit_trinidad(1_000_000.0, 2025, sector="standard")
    assert result.cit_totaal == pytest.approx(300_000.0)


# 4 — banks/petrochemical: 1,000,000 → 350,000
def test_banks_petrochemical_one_million():
    result = bereken_cit_trinidad(1_000_000.0, 2025, sector="banks_petrochemical")
    assert result.cit_totaal == pytest.approx(350_000.0)


# 5 — petroleum production (PPT regime): 1,000,000 → 500,000
def test_petroleum_one_million():
    result = bereken_cit_trinidad(1_000_000.0, 2025, sector="petroleum")
    assert result.cit_totaal == pytest.approx(500_000.0)


# 6 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_trinidad(1_000_000.0, 2025, sector="fintech")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_trinidad(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_trinidad(-25_000.0, 2025, sector="petroleum").cit_totaal == pytest.approx(0.0)


# 8 — VAT standard rate = 12.5%
def test_vat_12_5pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.125)


# 9 — business levy 0.6% of gross revenue noted
def test_business_levy_note():
    bl = _params()["business_levy"]
    assert bl["rate"] == pytest.approx(0.006)
    assert bl["base"] == "gross_revenue"


# 10 — green fund levy 0.3% of gross revenue noted
def test_green_fund_levy_note():
    gfl = _params()["green_fund_levy"]
    assert gfl["rate"] == pytest.approx(0.003)
    assert gfl["base"] == "gross_revenue"


# 11 — effectief tarief matches the sector rate; official source is IRD
def test_effectief_tarief_and_source():
    assert bereken_cit_trinidad(200_000.0, 2025).effectief_tarief == pytest.approx(0.30)
    assert bereken_cit_trinidad(200_000.0, 2025, sector="banks_petrochemical").effectief_tarief == pytest.approx(0.35)
    sources = _params()["metadata"]["official_sources"]
    assert any("ird.gov.tt" in s["url"] for s in sources)
