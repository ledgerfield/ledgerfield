"""Slovak Republic tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.SK.sk_gaap import SK_GAAP
from ledgerfield.tax.SK.cit import bereken_cit_slowakije

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/SK/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_sk_schema_min_60_accounts():
    assert len(SK_GAAP) >= 60


# 2 — standard CIT rate = 21%
def test_cit_standard_rate_21pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.21)


# 3 — standard company: 21% on EUR 1,000,000
def test_standard_company_21pct():
    result = bereken_cit_slowakije(1_000_000.0, 2025, company_size="standard")
    assert result.cit_totaal == pytest.approx(210_000.0)


# 4 — small company (taxable revenue <= EUR 100,000): 10%
def test_small_company_10pct():
    result = bereken_cit_slowakije(1_000_000.0, 2025, company_size="small")
    assert result.cit_totaal == pytest.approx(100_000.0)
    assert _params()["cit"]["small_taxable_revenue_threshold_eur"] == 100_000


# 5 — large company (tax base > EUR 5,000,000): 24%
def test_large_company_24pct():
    result = bereken_cit_slowakije(1_000_000.0, 2025, company_size="large")
    assert result.cit_totaal == pytest.approx(240_000.0)
    assert _params()["cit"]["large_tax_base_threshold_eur"] == 5_000_000


# 6 — unknown company_size is rejected
def test_unknown_company_size_raises():
    with pytest.raises(ValueError):
        bereken_cit_slowakije(1_000_000.0, 2025, company_size="mega")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_slowakije(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_slowakije(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT standard rate 23% effective 1 January 2025 (raised from 20%)
def test_vat_23pct_from_2025():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.23)
    assert vat["effective_from"] == "2025-01-01"
    assert vat["previous_standard_rate"] == pytest.approx(0.20)


# 9 — reduced VAT rates 19% and 5%
def test_vat_reduced_rates():
    assert _params()["vat"]["reduced_rates"] == [0.19, 0.05]


# 10 — OSS eligible (EU One Stop Shop)
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 11 — official source is Finančná správa
def test_official_source_financna_sprava():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.financnasprava.sk/" in urls


# 12 — effectief tarief equals the applied band rate
def test_effectief_tarief():
    result = bereken_cit_slowakije(2_000_000.0, 2025, company_size="standard")
    assert result.effectief_tarief == pytest.approx(0.21)
    assert result.effectief_tarief == pytest.approx(result.cit_totaal / result.winst)
