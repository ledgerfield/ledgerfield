"""Peru tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.PE.pe_gaap import PE_GAAP
from ledgerfield.tax.PE.cit import bereken_cit_peru

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_pe_schema_min_60_accounts():
    assert len(PE_GAAP) >= 60


# 2 — general-regime CIT rate = 29.5%
def test_cit_rate_29_5pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.295)


# 3 — general regime: flat 29.5% on S/ 1,000,000
def test_general_regime_flat():
    result = bereken_cit_peru(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(295_000.0)
    assert result.effectief_tarief == pytest.approx(0.295)


# 4 — MYPE Tributario: bracket math on S/ 100,000
#     10% * 80,250 + 29.5% * 19,750 = 8,025 + 5,826.25 = 13,851.25
def test_mype_bracket_math():
    result = bereken_cit_peru(100_000.0, 2025, mype=True)
    assert result.cit_totaal == pytest.approx(13_851.25)


# 5 — MYPE fully within the 15-UIT bracket: pure 10%
def test_mype_within_first_bracket():
    result = bereken_cit_peru(50_000.0, 2025, mype=True)
    assert result.cit_totaal == pytest.approx(5_000.0)
    assert result.effectief_tarief == pytest.approx(0.10)


# 6 — MYPE threshold = 15 UIT = 15 × S/ 5,350 = S/ 80,250 (params consistency)
def test_mype_threshold_15_uit():
    mype = _params()["cit"]["mype_tributario"]
    assert mype["uit_2025"] == 5350
    assert mype["bracket_uit"] == 15
    assert mype["bracket_threshold"] == pytest.approx(15 * 5350)
    assert mype["lower_rate"] == pytest.approx(0.10)
    assert mype["upper_rate"] == pytest.approx(0.295)


# 7 — IGV 18%, decomposed as 16% IGV + 2% IPM
def test_igv_18pct_decomposition():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.18)
    assert vat["implemented"] is True
    assert vat["decomposition"]["igv"] == pytest.approx(0.16)
    assert vat["decomposition"]["ipm"] == pytest.approx(0.02)
    assert vat["decomposition"]["igv"] + vat["decomposition"]["ipm"] == pytest.approx(
        vat["standard_rate"]
    )


# 8 — dividend WHT = 5%
def test_dividend_wht_5pct():
    assert _params()["wht"]["dividends"] == pytest.approx(0.05)


# 9 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_peru(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_peru(-25_000.0, 2025, mype=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_peru(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 10 — MYPE effective rate is below the flat rate but above the lower rate
def test_mype_effective_rate_between_brackets():
    result = bereken_cit_peru(100_000.0, 2025, mype=True)
    assert 0.10 < result.effectief_tarief < 0.295
    assert result.effectief_tarief == pytest.approx(13_851.25 / 100_000.0)


# 11 — official source URL (SUNAT) and 2025 effective range
def test_official_source_and_range():
    meta = _params()["metadata"]
    assert any(
        "sunat.gob.pe" in src["url"] for src in meta["official_sources"]
    )
    assert meta["effective_date_range"]["start"] == "2025-01-01"
    assert meta["effective_date_range"]["end"] == "2025-12-31"
    assert meta["currency"] == "PEN"


# 12 — result dataclass carries inputs through
def test_result_roundtrip_fields():
    result = bereken_cit_peru(200_000.0, 2025, mype=True)
    assert result.winst == pytest.approx(200_000.0)
    assert result.jaar == 2025
    assert result.mype is True
    assert result.cit_rate == pytest.approx(0.295)
