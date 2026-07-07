"""Zimbabwe tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.ZW.zw_gaap import ZW_GAAP
from ledgerfield.tax.ZW.cit import bereken_cit_zimbabwe

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/ZW/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_zw_schema_min_60_accounts():
    assert len(ZW_GAAP) >= 60


# 2 — CIT rate = 25%
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — reference case: 1,000,000 → CIT 250,000
def test_cit_bedrag_reference_case():
    result = bereken_cit_zimbabwe(1_000_000.0, 2025)
    assert result.cit_bedrag == pytest.approx(250_000.0)


# 4 — AIDS levy is 3% of the TAX (not of profit): 250,000 * 0.03 = 7,500
def test_aids_levy_3pct_of_tax_not_profit():
    result = bereken_cit_zimbabwe(1_000_000.0, 2025)
    assert result.aids_levy_bedrag == pytest.approx(7_500.0)
    # explicitly NOT 3% of profit (which would be 30,000)
    assert result.aids_levy_bedrag != pytest.approx(30_000.0)


# 5 — total = CIT + AIDS levy = 257,500
def test_totaal_bedrag_reference_case():
    result = bereken_cit_zimbabwe(1_000_000.0, 2025)
    assert result.totaal_bedrag == pytest.approx(257_500.0)


# 6 — effective rate 25.75%
def test_effectief_tarief_2575():
    result = bereken_cit_zimbabwe(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.2575)
    assert _params()["cit"]["effective_rate"] == pytest.approx(0.2575)


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_zimbabwe(0.0, 2025).totaal_bedrag == pytest.approx(0.0)
    result = bereken_cit_zimbabwe(-50_000.0, 2025)
    assert result.cit_bedrag == pytest.approx(0.0)
    assert result.aids_levy_bedrag == pytest.approx(0.0)
    assert result.totaal_bedrag == pytest.approx(0.0)
    assert result.effectief_tarief == pytest.approx(0.0)


# 8 — VAT standard rate = 15%
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)


# 9 — IMTT 2% documented
def test_imtt_2pct_note():
    imtt = _params()["imtt"]
    assert imtt["rate"] == pytest.approx(0.02)
    assert "Intermediated Money Transfer Tax" in imtt["note"]


# 10 — dual-currency regime (ZWG/USD) documented
def test_dual_currency_note():
    regime = _params()["currency_regime"]
    assert "ZWG" in regime["currencies"]
    assert "USD" in regime["currencies"]


# 11 — ZIMRA source URL present
def test_zimra_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("zimra.co.zw" in s["url"] for s in sources)


# 12 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
