"""United Arab Emirates tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.AE.ae_gaap import AE_GAAP
from ledgerfield.tax.AE.cit import bereken_cit_uae

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ae_schema_min_60_accounts():
    assert len(AE_GAAP) >= 60


# 2 — standard corporate tax rate = 9%
def test_standard_rate_9pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.09)


# 3 — zero band up to AED 375,000
def test_zero_band_limit_375k():
    assert _params()["cit"]["zero_band_limit_aed"] == 375_000


# 4 — profit within the 0% band pays no tax
def test_profit_within_zero_band_is_untaxed():
    result = bereken_cit_uae(300_000.0, 2025)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.effectief_tarief == pytest.approx(0.0)


# 5 — AED 1,375,000 profit → 9% on the AED 1,000,000 above the band = AED 90,000
def test_bereken_cit_uae_marginal_band():
    result = bereken_cit_uae(1_375_000.0, 2025)
    assert result.cit_totaal == pytest.approx(90_000.0)


# 6 — Qualifying Free Zone income is taxed at 0%
def test_free_zone_qualifying_is_zero_rated():
    result = bereken_cit_uae(5_000_000.0, 2025, free_zone_qualifying=True)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.cit_rate == pytest.approx(0.0)


# 7 — VAT standard rate = 5%
def test_vat_rate_5pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.05)


# 8 — no personal income tax
def test_no_personal_income_tax():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.0)


# 9 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_uae(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_uae(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 10 — effective rate stays below the 9% headline because of the 0% band
def test_effective_rate_below_headline():
    result = bereken_cit_uae(750_000.0, 2025)
    # 9% on 375,000 = 33,750 over 750,000 profit → 4.5% effective
    assert result.cit_totaal == pytest.approx(33_750.0)
    assert result.effectief_tarief < _params()["cit"]["standard_rate"]
