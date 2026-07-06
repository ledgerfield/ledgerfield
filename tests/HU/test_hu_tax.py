"""Hungary tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.HU.hu_gaap import HU_GAAP
from ledgerfield.tax.HU.cit import bereken_cit_hongarije

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/HU/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage, including ÁFA/VAT accounts
def test_hu_schema_min_60_accounts():
    assert len(HU_GAAP) >= 60
    names = " ".join(a.name for a in HU_GAAP)
    assert "ÁFA" in names or "VAT" in names


# 2 — CIT rate = 9% (lowest in the EU)
def test_cit_rate_9pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.09)


# 3 — 1,000,000 profit → 90,000 tax
def test_cit_1m_profit():
    result = bereken_cit_hongarije(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(90_000.0)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_hongarije(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_hongarije(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — VAT standard rate = 27% (highest in the EU)
def test_vat_27pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.27)


# 6 — reduced VAT rates 18% and 5%
def test_vat_reduced_rates():
    reduced = _params()["vat"]["reduced_rates"]
    assert 0.18 in reduced
    assert 0.05 in reduced


# 7 — OSS eligible (EU member state)
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 8 — HIPA local business tax note (up to 2%, different base)
def test_hipa_note():
    hipa = _params()["local_business_tax"]
    assert hipa["max_rate"] == pytest.approx(0.02)
    assert "turnover" in hipa["note"].lower()


# 9 — KIVA alternative small-business regime at 10%
def test_kiva_note():
    kiva = _params()["kiva"]
    assert kiva["rate"] == pytest.approx(0.10)
    assert "KIVA" in kiva["note"] or "alternative" in kiva["note"].lower()


# 10 — Pillar Two QDMTT implemented despite 9% CIT
def test_pillar_two_note():
    p2 = _params()["pillar_two"]
    assert p2["implemented"] is True
    assert "QDMTT" in p2["note"]


# 11 — official source references NAV
def test_official_source_nav():
    sources = _params()["metadata"]["official_sources"]
    assert any("nav.gov.hu" in s["url"] for s in sources)


# 12 — effective rate equals the 9% flat rate for positive profit
def test_effectief_tarief_flat_9pct():
    result = bereken_cit_hongarije(5_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.09)
    assert result.cit_rate == pytest.approx(0.09)
