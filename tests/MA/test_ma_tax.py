"""Kingdom of Morocco tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MA.ma_gaap import MA_GAAP
from ledgerfield.tax.MA.cit import bereken_cit_marokko

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ma_schema_min_60_accounts():
    assert len(MA_GAAP) >= 60


# 2 — schema includes TVA (VAT) accounts
def test_ma_schema_has_tva_accounts():
    names = " ".join(account.name for account in MA_GAAP)
    assert "TVA Collectée" in names
    assert "TVA Déductible" in names


# 3 — standard rate: MAD 1,000,000 → 200,000 (20%)
def test_standard_rate_20pct():
    result = bereken_cit_marokko(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(200_000.0)
    assert result.cit_rate == pytest.approx(0.20)


# 4 — high rate on WHOLE base: MAD 150,000,000 → 52,500,000 (35%)
def test_high_rate_whole_base():
    result = bereken_cit_marokko(150_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(52_500_000.0)
    assert result.cit_rate == pytest.approx(0.35)


# 5 — financial institution: 40% → MAD 1,000,000 → 400,000
def test_financial_institution_40pct():
    result = bereken_cit_marokko(1_000_000.0, 2025, financial_institution=True)
    assert result.cit_totaal == pytest.approx(400_000.0)
    assert result.cit_rate == pytest.approx(0.40)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_marokko(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_marokko(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 7 — VAT (TVA) standard rate = 20%
def test_vat_standard_rate_20pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.20)


# 8 — VAT reduced rates 14/10/7 documented
def test_vat_reduced_rates():
    assert _params()["vat"]["reduced_rates"] == [0.14, 0.10, 0.07]


# 9 — Finance Law 2023 convergence documented (2025 = year 3, target 2026)
def test_convergence_note_documented():
    note = _params()["cit"]["convergence_note"]
    assert "2026" in note
    assert "glide path" in note


# 10 — cotisation minimale 0.25% of turnover documented
def test_cotisation_minimale_documented():
    cm = _params()["cit"]["cotisation_minimale"]
    assert cm["rate"] == pytest.approx(0.0025)
    assert "cotisation minimale" in cm["note"]


# 11 — official DGI source URL present
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"] == "https://www.tax.gov.ma/" for s in sources)


# 12 — effectief tarief equals the applied rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_marokko(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.20)
    result_high = bereken_cit_marokko(150_000_000.0, 2025)
    assert result_high.effectief_tarief == pytest.approx(0.35)
