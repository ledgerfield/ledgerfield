"""Republic of Mauritius tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MU.mu_gaap import MU_GAAP
from ledgerfield.tax.MU.cit import bereken_cit_mauritius

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MU/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_mu_schema_min_60_accounts():
    assert len(MU_GAAP) >= 60


# 2 — CIT rate = 15%
def test_cit_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — standard company: 15% on full profit
def test_standard_company_15pct():
    result = bereken_cit_mauritius(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(150_000.0)
    assert result.cit_rate == pytest.approx(0.15)
    assert result.effectieve_druk == pytest.approx(0.15)


# 4 — GBC partial exemption: effective 3% on qualifying foreign income
def test_gbc_partial_exemption_effective_3pct():
    result = bereken_cit_mauritius(1_000_000.0, 2025, gbc_partial_exemption=True)
    assert result.cit_totaal == pytest.approx(30_000.0)
    assert result.effectieve_druk == pytest.approx(0.03)
    # Nominal rate stays 15%; the relief works via the 80% exempt slice.
    assert result.cit_rate == pytest.approx(0.15)


# 5 — GBC: 80% of profit is exempt
def test_gbc_exempt_deel_80pct():
    result = bereken_cit_mauritius(1_000_000.0, 2025, gbc_partial_exemption=True)
    assert result.exempt_deel == pytest.approx(800_000.0)
    assert result.belastbaar_deel == pytest.approx(200_000.0)


# 6 — params encode the 80% exemption and 3% effective GBC rate
def test_params_gbc_partial_exemption():
    gbc = _params()["cit"]["gbc_partial_exemption"]
    assert gbc["exemption_share"] == pytest.approx(0.80)
    assert gbc["effective_rate"] == pytest.approx(0.03)


# 7 — export of goods taxed at 3%
def test_export_of_goods_3pct():
    assert _params()["cit"]["special_rates"]["export_of_goods"] == pytest.approx(0.03)


# 8 — Corporate Climate Responsibility levy: 2% above Rs 50m turnover
def test_climate_levy_2pct_above_rs50m():
    ccr = _params()["cit"]["corporate_climate_responsibility_levy"]
    assert ccr["rate"] == pytest.approx(0.02)
    assert ccr["turnover_threshold_mur"] == 50_000_000


# 9 — VAT = 15%
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)
    assert _params()["vat"]["implemented"] is True


# 10 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_mauritius(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_mauritius(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    gbc = bereken_cit_mauritius(-25_000.0, 2025, gbc_partial_exemption=True)
    assert gbc.cit_totaal == pytest.approx(0.0)
    assert gbc.exempt_deel == pytest.approx(0.0)


# 11 — official source is the MRA
def test_official_source_mra():
    sources = _params()["metadata"]["official_sources"]
    assert any("https://www.mra.mu/" in s["url"] for s in sources)


# 12 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
