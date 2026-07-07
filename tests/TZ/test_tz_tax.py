"""United Republic of Tanzania tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.TZ.tz_gaap import TZ_GAAP
from ledgerfield.tax.TZ.cit import bereken_cit_tanzania

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_tz_schema_min_60_accounts():
    assert len(TZ_GAAP) >= 60


# 2 — standard CIT rate = 30%
def test_cit_standard_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — standard regime: 1,000,000 → 300,000
def test_standard_regime():
    result = bereken_cit_tanzania(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.cit_rate == pytest.approx(0.30)


# 4 — newly listed on DSE (>=30% public float): 25% for 3 years
def test_newly_listed_regime():
    result = bereken_cit_tanzania(1_000_000.0, 2025, regime="newly_listed")
    assert result.cit_totaal == pytest.approx(250_000.0)


# 5 — new manufacturer of pharmaceuticals/leather: 20%
def test_new_manufacturer_regime():
    result = bereken_cit_tanzania(1_000_000.0, 2025, regime="new_manufacturer")
    assert result.cit_totaal == pytest.approx(200_000.0)


# 6 — vehicle/tractor assembler: 10% → 100,000
def test_assembler_regime():
    result = bereken_cit_tanzania(1_000_000.0, 2025, regime="assembler")
    assert result.cit_totaal == pytest.approx(100_000.0)


# 7 — unknown regime is rejected
def test_unknown_regime_raises():
    with pytest.raises(ValueError):
        bereken_cit_tanzania(1_000_000.0, 2025, regime="offshore")


# 8 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_tanzania(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_tanzania(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_tanzania(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 9 — VAT = 18% (mainland), with Zanzibar 15% note
def test_vat_18pct_mainland():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.18)
    assert vat["implemented"] is True
    assert "Zanzibar" in vat["note"]


# 10 — alternative minimum tax 0.5% of turnover noted
def test_alternative_minimum_tax_note():
    amt = _params()["alternative_minimum_tax"]
    assert amt["rate"] == pytest.approx(0.005)
    assert amt["base"] == "turnover"
    assert "note" in amt


# 11 — official TRA source URL present
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("tra.go.tz" in s["url"] for s in sources)


# 12 — effectief_tarief equals the applied rate for positive profit
def test_effectief_tarief():
    result = bereken_cit_tanzania(2_500_000.0, 2025, regime="new_manufacturer")
    assert result.effectief_tarief == pytest.approx(0.20)
