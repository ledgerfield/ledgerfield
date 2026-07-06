"""Socialist Republic of Vietnam tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.VN.vn_gaap import VN_GAAP
from ledgerfield.tax.VN.cit import bereken_cit_vietnam

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/VN/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT accounts)
def test_vn_schema_min_60_accounts_with_vat():
    assert len(VN_GAAP) >= 60
    vat_accounts = [a for a in VN_GAAP if "VAT" in a.name]
    assert len(vat_accounts) >= 2


# 2 — CIT standard rate = 20%
def test_cit_standard_rate_20pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.20)


# 3 — standard: 1,000,000,000 VND → 200,000,000 VND
def test_standard_cit_1bn():
    result = bereken_cit_vietnam(1_000_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(200_000_000.0)


# 4 — hi-tech: 1,000,000,000 VND → 100,000,000 VND (10%)
def test_hi_tech_cit_1bn():
    result = bereken_cit_vietnam(1_000_000_000.0, 2025, hi_tech=True)
    assert result.cit_totaal == pytest.approx(100_000_000.0)
    assert result.cit_rate == pytest.approx(0.10)


# 5 — non-positive profit yields zero tax (both regimes)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_vietnam(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_vietnam(-25_000_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_vietnam(0.0, 2025, hi_tech=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_vietnam(-25_000_000.0, 2025, hi_tech=True).cit_totaal == pytest.approx(0.0)


# 6 — VAT standard 10% + temporary 8% reduction noted
def test_vat_10pct_with_8pct_reduction_note():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.10)
    assert vat["implemented"] is True
    assert "8%" in vat["note"]


# 7 — oil & gas special rates 32-50% noted
def test_oil_and_gas_special_rates():
    cit = _params()["cit"]
    assert cit["special_rates"]["oil_and_gas_min"] == pytest.approx(0.32)
    assert cit["special_rates"]["oil_and_gas_max"] == pytest.approx(0.50)
    assert "oil" in cit["note"].lower()


# 8 — hi-tech 10% for 15 years framing in basis / preferential params
def test_hi_tech_15_year_framing():
    cit = _params()["cit"]
    assert cit["preferential_rates"]["hi_tech_incentivized"] == pytest.approx(0.10)
    assert cit["preferential_rates"]["hi_tech_duration_years"] == 15
    assert "15 years" in cit["basis"]


# 9 — source URL is the General Department of Taxation
def test_source_url_gdt():
    sources = _params()["metadata"]["official_sources"]
    assert any("gdt.gov.vn" in s["url"] for s in sources)


# 10 — effectief_tarief consistency (standard and hi-tech)
def test_effectief_tarief_consistency():
    std = bereken_cit_vietnam(500_000_000.0, 2025)
    assert std.effectief_tarief == pytest.approx(std.cit_totaal / std.winst)
    assert std.effectief_tarief == pytest.approx(0.20)
    ht = bereken_cit_vietnam(500_000_000.0, 2025, hi_tech=True)
    assert ht.effectief_tarief == pytest.approx(ht.cit_totaal / ht.winst)
    assert ht.effectief_tarief == pytest.approx(0.10)


# 11 — PIT progressive 5-35%
def test_pit_5_to_35pct():
    pit = _params()["personal_income_tax"]
    assert pit["min_rate"] == pytest.approx(0.05)
    assert pit["max_rate"] == pytest.approx(0.35)


# 12 — small-enterprise 15%/17% (revised CIT Law, Oct 2025 / FY2026) note-only
def test_small_enterprise_tiers_note():
    cit = _params()["cit"]
    assert cit["preferential_rates"]["other_tiers"] == [0.15, 0.17]
    assert "15%/17%" in cit["note"]
    assert "FY2026" in cit["note"]
