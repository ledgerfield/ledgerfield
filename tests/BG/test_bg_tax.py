"""Bulgaria tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.BG.bg_gaap import BG_GAAP
from ledgerfield.tax.BG.cit import bereken_cit_bulgarije

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/BG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_bg_schema_min_60_accounts():
    assert len(BG_GAAP) >= 60


# 2 — CIT rate = 10% flat
def test_cit_rate_10pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.10)


# 3 — 1,000,000 profit → 100,000 CIT
def test_cit_1m_profit():
    result = bereken_cit_bulgarije(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(100_000.0)


# 4 — effectief tarief equals flat 10%
def test_effectief_tarief_flat():
    result = bereken_cit_bulgarije(750_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.10)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_bulgarije(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bulgarije(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bulgarije(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 6 — VAT standard rate 20%
def test_vat_standard_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)


# 7 — reduced 9% VAT for tourism accommodation
def test_vat_reduced_tourism_9pct():
    assert _params()["vat"]["reduced_rates"]["tourism_accommodation"] == pytest.approx(0.09)


# 8 — EU OSS eligible
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 9 — Pillar Two / QDMTT note present despite 10% CIT
def test_pillar_two_note():
    note = _params()["cit"]["pillar_two_note"]
    assert "Pillar Two" in note
    assert "QDMTT" in note


# 10 — flat 10% PIT and euro adoption 2026-01-01
def test_pit_flat_and_euro_adoption():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.10)
    assert _params()["currency_transition"]["euro_adoption_date"] == "2026-01-01"


# 11 — official source is the NRA
def test_official_source_nra():
    sources = _params()["metadata"]["official_sources"]
    assert any("nra.bg" in s["url"] for s in sources)
    assert _params()["metadata"]["effective_date_range"]["start"].startswith("2025")
