"""Thailand tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.TH.th_gaap import TH_GAAP
from ledgerfield.tax.TH.cit import bereken_cit_thailand

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TH/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT accounts)
def test_th_schema_min_60_accounts():
    assert len(TH_GAAP) >= 60
    names = " ".join(a.name for a in TH_GAAP)
    assert "Input VAT" in names
    assert "Output VAT" in names


# 2 — standard CIT rate = 20%
def test_cit_standard_rate_20pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.20)


# 3 — standard regime: 1,000,000 → 200,000
def test_standard_regime_flat_20pct():
    result = bereken_cit_thailand(1_000_000.0, 2025, sme=False)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 4 — SME brackets: 1,000,000 → 0% * 300k + 15% * 700k = 105,000
def test_sme_bracket_math_1m():
    result = bereken_cit_thailand(1_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(105_000.0)


# 5 — SME brackets: 5,000,000 → 15% * 2.7M + 20% * 2M = 805,000
def test_sme_bracket_math_5m():
    result = bereken_cit_thailand(5_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(805_000.0)


# 6 — SME below exempt threshold: 250,000 → 0
def test_sme_below_exempt_threshold():
    result = bereken_cit_thailand(250_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(0.0)


# 7 — non-positive profit yields zero tax in both modes (defensive guard)
def test_non_positive_profit_zero_tax_both_modes():
    assert bereken_cit_thailand(0.0, 2025, sme=False).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_thailand(0.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_thailand(-25_000.0, 2025, sme=False).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_thailand(-25_000.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)


# 8 — VAT: current 7%, statutory 10% captured in params
def test_vat_7pct_with_statutory_10pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.07)
    assert vat["statutory_rate"] == pytest.approx(0.10)
    assert vat["implemented"] is True
    assert "10%" in vat["note"]


# 9 — WHT: dividends 10%, interest 15%
def test_wht_rates():
    wht = _params()["wht"]
    assert wht["dividends"] == pytest.approx(0.10)
    assert wht["interest"] == pytest.approx(0.15)


# 10 — PIT progressive 5–35%
def test_pit_progressive_5_to_35pct():
    pit = _params()["personal_income_tax"]
    assert pit["min_rate"] == pytest.approx(0.05)
    assert pit["max_rate"] == pytest.approx(0.35)


# 11 — official source URL (The Revenue Department)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"] == "https://www.rd.go.th/" for s in sources)


# 12 — effectief_tarief consistency in both modes
def test_effectief_tarief_consistency():
    std = bereken_cit_thailand(1_000_000.0, 2025, sme=False)
    assert std.effectief_tarief == pytest.approx(std.cit_totaal / std.winst)
    assert std.effectief_tarief == pytest.approx(0.20)
    sme = bereken_cit_thailand(5_000_000.0, 2025, sme=True)
    assert sme.effectief_tarief == pytest.approx(sme.cit_totaal / sme.winst)
    assert sme.effectief_tarief == pytest.approx(0.161)
