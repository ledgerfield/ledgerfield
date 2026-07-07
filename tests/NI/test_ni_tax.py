"""Republic of Nicaragua tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.NI.ni_gaap import NI_GAAP
from ledgerfield.tax.NI.cit import bereken_cit_nicaragua

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NI/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ni_schema_min_60_accounts():
    assert len(NI_GAAP) >= 60


# 2 — IR rate = 30%
def test_cit_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — 1,000,000 net income without bruto → 300,000 IR
def test_net_income_without_gross_30pct():
    result = bereken_cit_nicaragua(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.minimum_toegepast is False


# 4 — pago mínimo definitivo overrides: winst 100,000 + bruto 20,000,000
#     → minimum 600,000 > regular 30,000 → minimum applies
def test_pago_minimo_overrides_regular_ir():
    result = bereken_cit_nicaragua(100_000.0, 2025, bruto_inkomen=20_000_000.0)
    assert result.pago_minimo == pytest.approx(600_000.0)
    assert result.cit_regulier == pytest.approx(30_000.0)
    assert result.cit_totaal == pytest.approx(600_000.0)
    assert result.minimum_toegepast is True


# 5 — net LOSS with positive gross income still owes the gross minimum
#     (the pago mínimo is definitive and computed on gross, not on profit)
def test_net_loss_with_gross_still_owes_minimum():
    result = bereken_cit_nicaragua(-50_000.0, 2025, bruto_inkomen=1_000_000.0)
    assert result.cit_totaal == pytest.approx(30_000.0)
    assert result.minimum_toegepast is True


# 6 — regular IR wins when it exceeds the minimum
def test_regular_ir_wins_over_small_minimum():
    result = bereken_cit_nicaragua(1_000_000.0, 2025, bruto_inkomen=2_000_000.0)
    assert result.pago_minimo == pytest.approx(60_000.0)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.minimum_toegepast is False


# 7 — small-taxpayer tier: 1% minimum via minimum_pct
def test_small_taxpayer_1pct_minimum():
    result = bereken_cit_nicaragua(-10_000.0, 2025, bruto_inkomen=500_000.0, minimum_pct=0.01)
    assert result.cit_totaal == pytest.approx(5_000.0)
    assert result.minimum_toegepast is True


# 8 — non-positive profit WITHOUT bruto yields zero tax (defensive guard)
def test_non_positive_profit_without_gross_zero_tax():
    assert bereken_cit_nicaragua(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_nicaragua(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 9 — VAT (IVA) = 15%
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)
    assert _params()["vat"]["implemented"] is True


# 10 — pago mínimo tiers in params (1%–3% by taxpayer size)
def test_pago_minimo_tiers_in_params():
    pm = _params()["cit"]["pago_minimo_definitivo"]
    assert pm["rate_large_taxpayers"] == pytest.approx(0.03)
    assert pm["rate_medium_taxpayers"] == pytest.approx(0.02)
    assert pm["rate_small_taxpayers"] == pytest.approx(0.01)
    assert pm["base"] == "gross_income"


# 11 — official source is the DGI
def test_official_source_dgi():
    sources = _params()["metadata"]["official_sources"]
    assert any("dgi.gob.ni" in s["url"] for s in sources)
    start = _params()["metadata"]["effective_date_range"]["start"]
    assert start.startswith("2025")


# 12 — invalid inputs are rejected
def test_invalid_inputs_raise():
    with pytest.raises(ValueError):
        bereken_cit_nicaragua(100_000.0, 2025, bruto_inkomen=-1.0)
    with pytest.raises(ValueError):
        bereken_cit_nicaragua(100_000.0, 2025, bruto_inkomen=1_000.0, minimum_pct=1.5)
