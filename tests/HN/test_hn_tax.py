"""Republic of Honduras tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.HN.hn_gaap import HN_GAAP
from ledgerfield.tax.HN.cit import bereken_cit_honduras

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/HN/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_hn_schema_min_60_accounts():
    assert len(HN_GAAP) >= 60


# 2 — CIT rate = 25%
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — at the HNL 1,000,000 threshold: CIT 250,000, no solidarity, total 250,000
def test_1m_at_threshold_no_solidarity():
    result = bereken_cit_honduras(1_000_000.0, 2025)
    assert result.cit_bedrag == pytest.approx(250_000.0)
    assert result.solidariteit_bedrag == pytest.approx(0.0)
    assert result.totaal_bedrag == pytest.approx(250_000.0)


# 4 — 2,000,000: CIT 500,000 + solidarity 5% of the 1,000,000 excess = 550,000
def test_2m_with_solidarity():
    result = bereken_cit_honduras(2_000_000.0, 2025)
    assert result.cit_bedrag == pytest.approx(500_000.0)
    assert result.solidariteit_bedrag == pytest.approx(50_000.0)
    assert result.totaal_bedrag == pytest.approx(550_000.0)


# 5 — below the threshold only the 25% CIT applies
def test_below_threshold_only_cit():
    result = bereken_cit_honduras(400_000.0, 2025)
    assert result.solidariteit_bedrag == pytest.approx(0.0)
    assert result.totaal_bedrag == pytest.approx(100_000.0)
    assert result.effectief_tarief == pytest.approx(0.25)


# 6 — effective rate above the threshold exceeds 25% (2m → 27.5%)
def test_effectief_tarief_above_threshold():
    result = bereken_cit_honduras(2_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.275)


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_honduras(0.0, 2025).totaal_bedrag == pytest.approx(0.0)
    assert bereken_cit_honduras(-100_000.0, 2025).totaal_bedrag == pytest.approx(0.0)
    assert bereken_cit_honduras(-100_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 8 — VAT (ISV) = 15%, alcohol/tobacco 18%
def test_vat_15pct_and_18pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.15)
    assert vat["increased_rate_alcohol_tobacco"] == pytest.approx(0.18)


# 9 — solidarity contribution documented: 5% above HNL 1,000,000
def test_solidarity_params():
    sol = _params()["cit"]["solidarity_contribution"]
    assert sol["rate"] == pytest.approx(0.05)
    assert sol["threshold_hnl"] == 1_000_000


# 10 — alternative minimum (1.5% gross, > HNL 1bn) and territorial notes present
def test_alt_minimum_and_territorial_notes():
    cit = _params()["cit"]
    assert cit["alternative_minimum"]["rate"] == pytest.approx(0.015)
    assert cit["alternative_minimum"]["gross_revenue_threshold_hnl"] == 1_000_000_000
    assert "territorial" in cit["territorial_note"].lower()


# 11 — official SAR source URL and 2025 range in params
def test_source_and_range():
    meta = _params()["metadata"]
    assert meta["official_sources"][0]["url"] == "https://www.sar.gob.hn/"
    assert meta["effective_date_range"]["start"] == "2025-01-01"
    assert meta["effective_date_range"]["end"] == "2025-12-31"
