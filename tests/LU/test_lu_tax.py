"""Grand Duchy of Luxembourg tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.LU.lu_gaap import LU_GAAP
from ledgerfield.tax.LU.cit import bereken_cit_luxemburg

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/LU/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_lu_schema_min_60_accounts():
    assert len(LU_GAAP) >= 60


# 2 — standard CIT rate = 16% from 2025 (cut from 17%)
def test_cit_standard_rate_16pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.16)


# 3 — reduced rate: EUR 100,000 → 14% → EUR 14,000
def test_reduced_bracket_100k():
    result = bereken_cit_luxemburg(100_000.0, 2025)
    assert result.cit_totaal == pytest.approx(14_000.0)
    assert result.cit_rate == pytest.approx(0.14)


# 4 — standard rate: EUR 1,000,000 → 16% → EUR 160,000
def test_standard_bracket_1m():
    result = bereken_cit_luxemburg(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(160_000.0)
    assert result.cit_rate == pytest.approx(0.16)


# 5 — transition band 175k-200k001 is documented (simplified, not modelled)
def test_transition_band_documented():
    band = _params()["cit"]["transition_band"]
    assert band["lower"] == 175_000
    assert band["upper"] == 200_001
    result = bereken_cit_luxemburg(180_000.0, 2025)
    assert "transition band" in result.note


# 6 — aggregate effective rate Luxembourg City 2025 = 23.87%
def test_aggregate_effective_rate_luxembourg_city():
    assert _params()["cit"]["aggregate_effective_rate_luxembourg_city"] == pytest.approx(0.2387)


# 7 — result carries only the state CIT (surtax/ICC excluded)
def test_result_is_state_cit_only():
    result = bereken_cit_luxemburg(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.16)
    assert "solidarity surtax" in result.note


# 8 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_luxemburg(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_luxemburg(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 9 — VAT standard rate = 17% (lowest in the EU)
def test_vat_standard_17pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.17)


# 10 — VAT reduced rates 14/8/3 and OSS eligibility
def test_vat_reduced_rates_and_oss():
    vat = _params()["vat"]
    assert vat["reduced_rates"] == [0.14, 0.08, 0.03]
    assert vat["oss_eligible"] is True


# 11 — Pillar Two note present
def test_pillar_two_note():
    p2 = _params()["pillar_two"]
    assert p2["in_scope"] is True
    assert "15%" in p2["note"]


# 12 — official source URL (ACD)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("impotsdirects.public.lu" in s["url"] for s in sources)
