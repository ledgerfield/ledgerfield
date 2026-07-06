"""Republic of the Philippines tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.PH.ph_gaap import PH_GAAP
from ledgerfield.tax.PH.cit import bereken_cit_filipijnen

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PH/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage, incl. VAT input/output accounts
def test_ph_schema_min_60_accounts():
    assert len(PH_GAAP) >= 60
    names = [a.name for a in PH_GAAP]
    assert any("Input VAT" in n for n in names)
    assert any("Output VAT" in n for n in names)


# 2 — standard CIT rate = 25%
def test_cit_standard_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — standard company: 1,000,000 → 250,000
def test_standard_company_25pct():
    result = bereken_cit_filipijnen(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 4 — qualifying SME: 1,000,000 → 200,000
def test_sme_20pct():
    result = bereken_cit_filipijnen(1_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 5 — non-positive profit yields zero tax (defensive guard), both regimes
def test_non_positive_profit_zero_tax():
    assert bereken_cit_filipijnen(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_filipijnen(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_filipijnen(0.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_filipijnen(-25_000.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)


# 6 — VAT = 12%
def test_vat_12pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.12)
    assert _params()["vat"]["implemented"] is True


# 7 — MCIT 2% of gross income noted in params
def test_mcit_2pct_note_present():
    mcit = _params()["cit"]["mcit"]
    assert mcit["rate"] == pytest.approx(0.02)
    assert "gross income" in mcit["note"]


# 8 — CREATE Act named in the CIT basis
def test_create_act_named_in_basis():
    assert "CREATE Act" in _params()["cit"]["basis"]


# 9 — official BIR source URL present
def test_official_source_url():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.bir.gov.ph/" in urls


# 10 — effectief tarief consistency: 0.25 standard / 0.20 SME
def test_effectief_tarief_consistency():
    assert bereken_cit_filipijnen(2_500_000.0, 2025).effectief_tarief == pytest.approx(0.25)
    assert bereken_cit_filipijnen(2_500_000.0, 2025, sme=True).effectief_tarief == pytest.approx(0.20)


# 11 — SME rate and twin thresholds in params
def test_sme_rate_and_thresholds():
    cit = _params()["cit"]
    assert cit["sme_rate"] == pytest.approx(0.20)
    assert cit["sme_conditions"]["max_net_taxable_income_php"] == 5_000_000
    assert cit["sme_conditions"]["max_total_assets_php"] == 100_000_000


# 12 — WHT on dividends to NRFC: 25% / 15% tax-sparing; PIT top rate 35% (TRAIN)
def test_wht_and_pit():
    p = _params()
    assert p["wht"]["dividends_to_nrfc"] == pytest.approx(0.25)
    assert p["wht"]["dividends_to_nrfc_tax_sparing"] == pytest.approx(0.15)
    assert p["personal_income_tax"]["max_rate"] == pytest.approx(0.35)
