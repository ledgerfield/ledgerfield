"""Republic of Rwanda tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.RW.rw_gaap import RW_GAAP
from ledgerfield.tax.RW.cit import bereken_cit_rwanda

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/RW/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_rw_schema_min_60_accounts():
    assert len(RW_GAAP) >= 60


# 2 — CIT rate = 28%
def test_cit_rate_28pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.28)


# 3 — flat 28% on profit
def test_flat_28pct_on_profit():
    result = bereken_cit_rwanda(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(280_000.0)
    assert result.cit_rate == pytest.approx(0.28)
    assert result.effectief_tarief == pytest.approx(0.28)


# 4 — roadmap note: further reduction to 26%
def test_roadmap_to_26pct():
    roadmap = _params()["cit"]["roadmap"]
    assert roadmap["target_rate"] == pytest.approx(0.26)
    assert "26%" in roadmap["note"]


# 5 — rate was reduced from 30% by the 2023 Income Tax Law
def test_basis_mentions_reduction_from_30pct():
    basis = _params()["cit"]["basis"]
    assert "30%" in basis
    assert "2023" in basis


# 6 — small business flat/lump-sum regimes are noted
def test_small_business_regimes_noted():
    assert "lump-sum" in _params()["cit"]["small_business_regimes"]["note"]


# 7 — newly listed incentives: 25% / 20%
def test_newly_listed_incentives():
    rates = _params()["cit"]["newly_listed_incentives"]["rates"]
    assert rates == [pytest.approx(0.25), pytest.approx(0.20)]


# 8 — VAT = 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)
    assert _params()["vat"]["implemented"] is True


# 9 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_rwanda(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_rwanda(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_rwanda(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 10 — official source is the RRA
def test_official_source_rra():
    sources = _params()["metadata"]["official_sources"]
    assert any("https://www.rra.gov.rw/" in s["url"] for s in sources)


# 11 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
