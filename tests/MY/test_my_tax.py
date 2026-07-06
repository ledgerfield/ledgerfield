"""Malaysia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MY.my_gaap import MY_GAAP
from ledgerfield.tax.MY.cit import bereken_cit_maleisie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MY/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_my_schema_min_60_accounts():
    assert len(MY_GAAP) >= 60


# 2 — schema has SST accounts but no VAT/GST accounts
def test_my_schema_sst_no_vat_gst():
    names = " | ".join(a.name.upper() for a in MY_GAAP)
    assert "SST" in names
    assert "SALES TAX" in names
    assert "SERVICE TAX" in names
    assert "VAT" not in names
    assert "GST" not in names


# 3 — standard CIT rate = 24%
def test_cit_standard_rate_24pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.24)
    result = bereken_cit_maleisie(1_000_000.0, 2025, sme=False)
    assert result.cit_totaal == pytest.approx(240_000.0)


# 4 — SME brackets: 1,000,000 → 15%*150k + 17%*450k + 24%*400k = 195,000
def test_sme_bracket_math_1m():
    result = bereken_cit_maleisie(1_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(22_500.0 + 76_500.0 + 96_000.0)
    assert result.cit_totaal == pytest.approx(195_000.0)


# 5 — SME fully within first bracket: 100,000 → 15,000
def test_sme_first_bracket_only():
    result = bereken_cit_maleisie(100_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(15_000.0)


# 6 — SME at exactly RM600,000 → 15%*150k + 17%*450k = 99,000
def test_sme_boundary_600k():
    result = bereken_cit_maleisie(600_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(99_000.0)


# 7 — zero and negative profit yield zero tax in both modes
def test_non_positive_profit_zero_tax():
    for sme in (False, True):
        assert bereken_cit_maleisie(0.0, 2025, sme=sme).cit_totaal == pytest.approx(0.0)
        assert bereken_cit_maleisie(-50_000.0, 2025, sme=sme).cit_totaal == pytest.approx(0.0)
        assert bereken_cit_maleisie(0.0, 2025, sme=sme).effectief_tarief == pytest.approx(0.0)


# 8 — SST two-tier present: sales tax 5%/10%, service tax 8%
def test_sst_two_tier_rates():
    sst = _params()["sst"]
    assert sst["implemented"] is True
    assert sst["sales_tax"]["rates"] == [pytest.approx(0.05), pytest.approx(0.10)]
    assert sst["service_tax"]["standard_rate"] == pytest.approx(0.08)
    assert "6%" in sst["service_tax"]["note"]


# 9 — no VAT: block marked not implemented
def test_no_vat_gst():
    assert _params()["vat"]["implemented"] is False


# 10 — WHT: interest 15%, royalties/technical 10%
def test_wht_rates():
    wht = _params()["wht"]
    assert wht["interest"] == pytest.approx(0.15)
    assert wht["royalties"] == pytest.approx(0.10)
    assert wht["technical_services"] == pytest.approx(0.10)


# 11 — official source URL (LHDN)
def test_source_url_lhdn():
    sources = _params()["metadata"]["official_sources"]
    assert any("hasil.gov.my" in s["url"] for s in sources)


# 12 — effectief_tarief consistency: cit_totaal / winst; SME below flat rate
def test_effectief_tarief_consistency():
    for winst in (100_000.0, 600_000.0, 1_000_000.0, 5_000_000.0):
        for sme in (False, True):
            r = bereken_cit_maleisie(winst, 2025, sme=sme)
            assert r.effectief_tarief == pytest.approx(r.cit_totaal / winst)
    standard = bereken_cit_maleisie(1_000_000.0, 2025, sme=False)
    sme_result = bereken_cit_maleisie(1_000_000.0, 2025, sme=True)
    assert standard.effectief_tarief == pytest.approx(0.24)
    assert sme_result.effectief_tarief < standard.effectief_tarief
