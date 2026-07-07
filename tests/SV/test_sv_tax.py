"""Republic of El Salvador tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.SV.sv_gaap import SV_GAAP
from ledgerfield.tax.SV.cit import bereken_cit_elsalvador

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/SV/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_sv_schema_min_60_accounts():
    assert len(SV_GAAP) >= 60


# 2 — standard ISR rate = 30%, reduced = 25% up to USD 150,000
def test_isr_rates_in_params():
    cit = _params()["cit"]
    assert cit["standard_rate"] == pytest.approx(0.30)
    assert cit["reduced_rate"] == pytest.approx(0.25)
    assert cit["reduced_rate_threshold"] == 150_000


# 3 — 100,000 taxable income → reduced 25% → 25,000
def test_reduced_rate_25pct():
    result = bereken_cit_elsalvador(100_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.25)
    assert result.cit_totaal == pytest.approx(25_000.0)


# 4 — 1,000,000 taxable income → standard 30% → 300,000
def test_standard_rate_30pct():
    result = bereken_cit_elsalvador(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.30)
    assert result.cit_totaal == pytest.approx(300_000.0)


# 5 — cliff at exactly USD 150,000: whole base at 25% (Salvadoran practice)
def test_threshold_boundary_whole_base():
    at = bereken_cit_elsalvador(150_000.0, 2025)
    assert at.cit_rate == pytest.approx(0.25)
    assert at.cit_totaal == pytest.approx(37_500.0)
    above = bereken_cit_elsalvador(150_000.01, 2025)
    assert above.cit_rate == pytest.approx(0.30)
    assert above.cit_totaal == pytest.approx(45_000.003)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_elsalvador(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_elsalvador(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 7 — VAT (IVA) = 13%
def test_vat_13pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.13)
    assert _params()["vat"]["implemented"] is True


# 8 — 1% gross minimum tax is NOT applied (declared unconstitutional in 2015)
def test_minimum_tax_suspended():
    mt = _params()["cit"]["minimum_tax"]
    assert mt["rate"] == pytest.approx(0.01)
    assert mt["applied"] is False
    assert "unconstitutional" in mt["note"].lower()


# 9 — effective rate equals the applied whole-base rate
def test_effective_rate_matches_applied_rate():
    assert bereken_cit_elsalvador(80_000.0, 2025).effectief_tarief == pytest.approx(0.25)
    assert bereken_cit_elsalvador(500_000.0, 2025).effectief_tarief == pytest.approx(0.30)


# 10 — official source is the Ministerio de Hacienda
def test_official_source_hacienda():
    sources = _params()["metadata"]["official_sources"]
    assert any("mh.gob.sv" in s["url"] for s in sources)
    start = _params()["metadata"]["effective_date_range"]["start"]
    assert start.startswith("2025")


# 11 — currency is USD (dollarised economy)
def test_currency_usd():
    assert _params()["metadata"]["currency"] == "USD"
