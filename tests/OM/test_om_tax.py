"""Sultanate of Oman tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.OM.om_gaap import OM_GAAP
from ledgerfield.tax.OM.cit import bereken_cit_oman

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/OM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (includes VAT accounts)
def test_om_schema_min_60_accounts():
    assert len(OM_GAAP) >= 60
    names = " | ".join(a.name for a in OM_GAAP)
    assert "VAT" in names


# 2 — CIT standard rate = 15%
def test_cit_standard_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — standard mode: 1,000,000 profit → 150,000 tax
def test_standard_mode_15pct():
    result = bereken_cit_oman(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(150_000.0)


# 4 — SME mode: 1,000,000 profit → 30,000 tax at 3%
def test_sme_mode_3pct():
    result = bereken_cit_oman(1_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(30_000.0)


# 5 — zero/negative profit yields zero tax in both modes
def test_non_positive_profit_zero_tax_both_modes():
    assert bereken_cit_oman(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oman(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oman(0.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oman(-25_000.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)


# 6 — VAT implemented at 5% (Royal Decree No. 121/2020)
def test_vat_5pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.05)
    assert _params()["vat"]["implemented"] is True


# 7 — no personal income tax (as of 2025)
def test_no_personal_income_tax():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.0)


# 8 — WHT on non-resident payments = 10%
def test_wht_10pct():
    p = _params()
    assert p["wht"]["non_resident_dividends_interest_royalties_services"] == pytest.approx(0.10)


# 9 — petroleum income special rate = 55%
def test_petroleum_special_rate_55pct():
    assert _params()["cit"]["special_rates"]["petroleum_income"] == pytest.approx(0.55)


# 10 — official source URL + effective-rate consistency
def test_official_source_and_effective_rate():
    sources = _params()["metadata"]["official_sources"]
    assert any("tms.taxoman.gov.om" in s["url"] for s in sources)
    assert bereken_cit_oman(500_000.0, 2025).effectief_tarief == pytest.approx(0.15)
    assert bereken_cit_oman(80_000.0, 2025, sme=True).effectief_tarief == pytest.approx(0.03)
