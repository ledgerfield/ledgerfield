"""Hellenic Republic (Greece) tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.GR.gr_gaap import GR_GAAP
from ledgerfield.tax.GR.cit import bereken_cit_griekenland

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/GR/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_gr_schema_min_60_accounts():
    assert len(GR_GAAP) >= 60


# 2 — CIT rate = 22%
def test_cit_rate_22pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.22)


# 3 — EUR 1,000,000 profit → EUR 220,000 CIT
def test_cit_one_million():
    result = bereken_cit_griekenland(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(220_000.0)


# 4 — credit institution → 29% → EUR 290,000
def test_credit_institution_29pct():
    result = bereken_cit_griekenland(1_000_000.0, 2025, credit_institution=True)
    assert result.cit_rate == pytest.approx(0.29)
    assert result.cit_totaal == pytest.approx(290_000.0)


# 5 — effective rate equals 22% on positive profit
def test_effectief_tarief():
    result = bereken_cit_griekenland(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.22)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_griekenland(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_griekenland(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_griekenland(
        -75_000.0, 2025, credit_institution=True
    ).cit_totaal == pytest.approx(0.0)


# 7 — VAT standard rate 24% with 13/6 reduced rates
def test_vat_rates():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.24)
    assert vat["reduced_rates"] == [0.13, 0.06]


# 8 — EU OSS eligible
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 9 — credit institutions 29% under deferred-tax framework noted
def test_credit_institutions_note():
    cit = _params()["cit"]
    assert cit["credit_institutions_rate"] == pytest.approx(0.29)
    assert "deferred-tax" in cit["credit_institutions_note"]


# 10 — Pillar Two note present
def test_pillar_two_note():
    note = _params()["pillar_two"]["note"]
    assert "Pillar Two" in note
    assert "15%" in note


# 11 — business tax (telos epitidevmatos) abolition-2025 note
def test_business_tax_abolition_note():
    note = _params()["business_tax"]["note"]
    assert "telos epitidevmatos" in note
    assert "2025" in note


# 12 — official source URL (AADE)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("aade.gr" in s["url"] for s in sources)
