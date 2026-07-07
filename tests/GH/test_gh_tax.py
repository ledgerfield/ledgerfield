"""Republic of Ghana tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.GH.gh_gaap import GH_GAAP
from ledgerfield.tax.GH.cit import bereken_cit_ghana

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/GH/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT + levies accounts)
def test_gh_schema_min_60_accounts():
    assert len(GH_GAAP) >= 60
    names = " | ".join(a.name for a in GH_GAAP)
    assert "VAT" in names
    assert "NHIL" in names
    assert "GETFund" in names
    assert "COVID" in names


# 2 — standard sector: 25% CIT + 5% GSL = 300,000 on 1,000,000
def test_standard_sector_cit_plus_gsl():
    result = bereken_cit_ghana(1_000_000.0, 2025)
    assert result.cit_bedrag == pytest.approx(250_000.0)
    assert result.gsl_bedrag == pytest.approx(50_000.0)
    assert result.totaal_bedrag == pytest.approx(300_000.0)


# 3 — mining/upstream petroleum: 35% CIT + 5% GSL
def test_mining_petroleum_35pct():
    result = bereken_cit_ghana(1_000_000.0, 2025, sector="mining_petroleum")
    assert result.cit_bedrag == pytest.approx(350_000.0)
    assert result.gsl_bedrag == pytest.approx(50_000.0)
    assert result.totaal_bedrag == pytest.approx(400_000.0)


# 4 — hotels: 22% CIT + 5% GSL
def test_hotels_22pct():
    result = bereken_cit_ghana(1_000_000.0, 2025, sector="hotels")
    assert result.cit_bedrag == pytest.approx(220_000.0)
    assert result.gsl_bedrag == pytest.approx(50_000.0)
    assert result.totaal_bedrag == pytest.approx(270_000.0)


# 5 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_ghana(1_000_000.0, 2025, sector="banking")


# 6 — non-positive profit yields zero tax and zero GSL (defensive guard)
def test_non_positive_profit_zero_tax_and_gsl():
    for winst in (0.0, -25_000.0):
        result = bereken_cit_ghana(winst, 2025)
        assert result.cit_bedrag == pytest.approx(0.0)
        assert result.gsl_bedrag == pytest.approx(0.0)
        assert result.totaal_bedrag == pytest.approx(0.0)


# 7 — params: CIT standard rate = 25%
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 8 — params: GSL = 5% of profit before tax
def test_gsl_rate_5pct():
    assert _params()["growth_sustainability_levy"]["standard_rate"] == pytest.approx(0.05)


# 9 — params: VAT standard rate = 15%
def test_vat_standard_rate_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)


# 10 — params: VAT levies NHIL 2.5% / GETFund 2.5% / COVID 1%
def test_vat_levies():
    levies = _params()["vat"]["levies"]
    assert levies["nhil"] == pytest.approx(0.025)
    assert levies["getfund"] == pytest.approx(0.025)
    assert levies["covid_levy"] == pytest.approx(0.01)


# 11 — params: official GRA source URL
def test_official_source_url():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert any("gra.gov.gh" in url for url in urls)


# 12 — effective rate is computed on the CIT + GSL total
def test_effectief_tarief_on_totaal():
    result = bereken_cit_ghana(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.30)
