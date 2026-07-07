"""Ecuador tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.EC.ec_gaap import EC_GAAP
from ledgerfield.tax.EC.cit import bereken_cit_ecuador

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/EC/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ec_schema_min_60_accounts():
    assert len(EC_GAAP) >= 60


# 2 — standard CIT rate = 25%
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — standard regime: 25% on USD 1,000,000
def test_standard_rate_on_million():
    result = bereken_cit_ecuador(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)
    assert result.effectief_tarief == pytest.approx(0.25)


# 4 — tax-haven shareholders (≥50%): +3pp → 28% → 280,000
def test_tax_haven_28pct_on_million():
    result = bereken_cit_ecuador(1_000_000.0, 2025, tax_haven_shareholders=True)
    assert result.cit_totaal == pytest.approx(280_000.0)
    assert result.cit_rate == pytest.approx(0.28)


# 5 — surcharge is exactly 3 percentage points (params consistency)
def test_surcharge_is_3pp():
    cit = _params()["cit"]
    surcharge = cit["tax_haven_surcharge"]
    assert surcharge["rate"] == pytest.approx(0.28)
    assert surcharge["rate"] - cit["standard_rate"] == pytest.approx(0.03)
    assert surcharge["threshold"] == pytest.approx(0.50)


# 6 — IVA 15%, raised from 12% in 2024 (Ley de Solidaridad)
def test_iva_15pct_raised_from_12():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.15)
    assert vat["implemented"] is True
    assert vat["raised"]["from"] == pytest.approx(0.12)
    assert vat["raised"]["to"] == pytest.approx(0.15)
    assert vat["raised"]["effective"].startswith("2024")
    assert "Solidaridad" in vat["raised"]["law"]


# 7 — ISD currency-exit tax = 5%
def test_isd_5pct():
    assert _params()["wht"]["isd_currency_exit_tax"] == pytest.approx(0.05)


# 8 — SME/microenterprise regimes documented as a note
def test_sme_regime_note_present():
    note = _params()["cit"]["sme_regimes_note"]
    assert "RIMPE" in note


# 9 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_ecuador(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_ecuador(
        -25_000.0, 2025, tax_haven_shareholders=True
    ).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_ecuador(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 10 — effective rate equals the applied statutory rate
def test_effectief_tarief_matches_rate():
    standard = bereken_cit_ecuador(300_000.0, 2025)
    haven = bereken_cit_ecuador(300_000.0, 2025, tax_haven_shareholders=True)
    assert standard.effectief_tarief == pytest.approx(0.25)
    assert haven.effectief_tarief == pytest.approx(0.28)


# 11 — official source URL (SRI) and 2025 effective range
def test_official_source_and_range():
    meta = _params()["metadata"]
    assert any(
        "sri.gob.ec" in src["url"] for src in meta["official_sources"]
    )
    assert meta["effective_date_range"]["start"] == "2025-01-01"
    assert meta["effective_date_range"]["end"] == "2025-12-31"
    assert meta["currency"] == "USD"


# 12 — result dataclass carries inputs through
def test_result_roundtrip_fields():
    result = bereken_cit_ecuador(200_000.0, 2025, tax_haven_shareholders=True)
    assert result.winst == pytest.approx(200_000.0)
    assert result.jaar == 2025
    assert result.tax_haven_shareholders is True
    assert result.cit_rate == pytest.approx(0.28)
