"""Hashemite Kingdom of Jordan tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.JO.jo_gaap import JO_GAAP
from ledgerfield.tax.JO.cit import bereken_cit_jordanie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/JO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. GST accounts)
def test_jo_schema_min_60_accounts():
    assert len(JO_GAAP) >= 60
    names = " ".join(a.name for a in JO_GAAP)
    assert "GST" in names


# 2 — standard sector: 20% CIT + 1% national contribution
def test_standard_sector_20pct_plus_1pct_nc():
    result = bereken_cit_jordanie(1_000_000.0, 2025, sector="standard")
    assert result.cit == pytest.approx(200_000.0)
    assert result.national_contribution == pytest.approx(10_000.0)
    assert result.cit_totaal == pytest.approx(210_000.0)


# 3 — banking sector: 35% CIT + 3% national contribution
def test_banking_sector_35pct_plus_3pct_nc():
    result = bereken_cit_jordanie(1_000_000.0, 2025, sector="banking")
    assert result.cit == pytest.approx(350_000.0)
    assert result.national_contribution == pytest.approx(30_000.0)
    assert result.cit_totaal == pytest.approx(380_000.0)


# 4 — financial sector: 24% CIT + 4% national contribution
def test_financial_sector_24pct_plus_4pct_nc():
    result = bereken_cit_jordanie(1_000_000.0, 2025, sector="financial")
    assert result.cit_totaal == pytest.approx(280_000.0)


# 5 — unknown sector raises ValueError
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_jordanie(1_000_000.0, 2025, sector="hospitality")


# 6 — non-positive profit yields zero for all components (defensive guard)
def test_non_positive_profit_zero_all_components():
    for winst in (0.0, -25_000.0):
        result = bereken_cit_jordanie(winst, 2025)
        assert result.cit == pytest.approx(0.0)
        assert result.national_contribution == pytest.approx(0.0)
        assert result.cit_totaal == pytest.approx(0.0)
        assert result.effectief_tarief == pytest.approx(0.0)


# 7 — GST (VAT) standard rate = 16%
def test_gst_rate_16pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.16)
    assert _params()["vat"]["implemented"] is True


# 8 — SSC rates present: 7.5% employee / 14.25% employer
def test_ssc_rates_present():
    ssc = _params()["social_security"]
    assert ssc["employee_rate"] == pytest.approx(0.075)
    assert ssc["employer_rate"] == pytest.approx(0.1425)


# 9 — official ISTD source URL referenced
def test_official_source_istd():
    sources = _params()["metadata"]["official_sources"]
    assert any("istd.gov.jo" in s["url"] for s in sources)
    assert _params()["metadata"]["source_status"] == "official_sources_referenced_estimate"


# 10 — effective rate equals total / profit
def test_effectief_tarief_is_total_over_winst():
    result = bereken_cit_jordanie(750_000.0, 2025, sector="banking")
    assert result.effectief_tarief == pytest.approx(result.cit_totaal / result.winst)
    assert result.effectief_tarief == pytest.approx(0.38)


# 11 — params sector rates match calculator constants
def test_params_match_calculator_rates():
    params = _params()
    from ledgerfield.tax.JO.cit import NATIONAL_CONTRIBUTION, SECTOR_RATES
    assert params["cit"]["sector_rates"] == pytest.approx(SECTOR_RATES)
    assert params["national_contribution"]["sector_rates"] == pytest.approx(NATIONAL_CONTRIBUTION)
