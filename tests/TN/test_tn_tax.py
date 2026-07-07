"""Tunisia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.TN.tn_gaap import TN_GAAP
from ledgerfield.tax.TN.cit import bereken_cit_tunesie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TN/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_tn_schema_min_60_accounts():
    assert len(TN_GAAP) >= 60


# 2 — standard CIT rate = 20% (Finance Law 2025)
def test_cit_standard_rate_20pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.20)


# 3 — standard case: 1,000,000 → 200,000
def test_standard_sector_reference_case():
    result = bereken_cit_tunesie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(200_000.0)
    assert result.effectief_tarief == pytest.approx(0.20)


# 4 — banks/insurance: 1,000,000 → 400,000
def test_banks_insurance_40pct():
    result = bereken_cit_tunesie(1_000_000.0, 2025, sector="banks_insurance")
    assert result.cit_totaal == pytest.approx(400_000.0)


# 5 — telecom/hydrocarbons: 35%
def test_telecom_hydrocarbons_35pct():
    result = bereken_cit_tunesie(1_000_000.0, 2025, sector="telecom_hydrocarbons")
    assert result.cit_totaal == pytest.approx(350_000.0)


# 6 — reduced regime: 1,000,000 → 100,000
def test_reduced_regime_10pct():
    result = bereken_cit_tunesie(1_000_000.0, 2025, sector="reduced")
    assert result.cit_totaal == pytest.approx(100_000.0)


# 7 — unknown sector raises ValueError
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_tunesie(1_000_000.0, 2025, sector="crypto_mining")


# 8 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_tunesie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    result = bereken_cit_tunesie(-75_000.0, 2025)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.effectief_tarief == pytest.approx(0.0)


# 9 — VAT: 19% standard, 13%/7% reduced
def test_vat_rates():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.19)
    assert 0.13 in vat["reduced_rates"]
    assert 0.07 in vat["reduced_rates"]


# 10 — Finance Law 2025 rate raise documented (15% → 20%, 35% → 40%)
def test_fl2025_rate_raise_documented():
    change = _params()["cit"]["fl2025_rate_change"]
    assert change["previous_standard_rate"] == pytest.approx(0.15)
    assert change["new_standard_rate"] == pytest.approx(0.20)
    assert change["previous_banks_insurance_rate"] == pytest.approx(0.35)
    assert change["new_banks_insurance_rate"] == pytest.approx(0.40)


# 11 — conjunctural contribution note + official source URL present
def test_conjunctural_note_and_source_url():
    params = _params()
    assert "conjoncturelle" in params["cit"]["conjunctural_contribution"]["note"]
    sources = params["metadata"]["official_sources"]
    assert any("impots.finances.gov.tn" in s["url"] for s in sources)


# 12 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
