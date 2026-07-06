"""State of Israel tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.IL.il_gaap import IL_GAAP
from ledgerfield.tax.IL.cit import bereken_cit_israel

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/IL/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT accounts)
def test_il_schema_min_60_accounts():
    assert len(IL_GAAP) >= 60
    names = " ".join(a.name for a in IL_GAAP)
    assert "VAT" in names  # input & output VAT accounts present


# 2 — CIT rate = 23%
def test_cit_rate_23pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.23)


# 3 — 1,000,000 profit → 230,000 CIT
def test_cit_on_one_million():
    result = bereken_cit_israel(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(230_000.0)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_israel(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_israel(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — VAT = 18% effective 1 January 2025 (raised from 17%)
def test_vat_18pct_from_2025():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.18)
    assert "1 January 2025" in vat["note"]


# 6 — 3% surtax (mas yesef) with threshold, under personal income tax
def test_surtax_under_personal_income_tax():
    pit = _params()["personal_income_tax"]
    assert pit["surtax_rate"] == pytest.approx(0.03)
    assert pit["surtax_threshold_nis"] > 0


# 7 — top marginal PIT 47% + surtax = 50% combined
def test_top_combined_pit_rate():
    pit = _params()["personal_income_tax"]
    assert pit["top_marginal_rate"] == pytest.approx(0.47)
    assert pit["top_combined_rate"] == pytest.approx(0.50)


# 8 — preferred enterprise special rates present (16% / 7.5% area A)
def test_preferred_enterprise_special_rates():
    special = _params()["cit"]["special_rates"]
    assert special["preferred_enterprise"] == pytest.approx(0.16)
    assert special["preferred_enterprise_development_area_a"] == pytest.approx(0.075)


# 9 — official Israel Tax Authority source referenced
def test_official_source_referenced():
    sources = _params()["metadata"]["official_sources"]
    assert any(
        s["url"] == "https://www.gov.il/en/departments/israel_tax_authority"
        for s in sources
    )


# 10 — effective rate equals flat 23% on positive profit
def test_effectief_tarief_flat_23pct():
    result = bereken_cit_israel(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.23)
