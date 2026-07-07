"""Jamaica tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.JM.jm_gaap import JM_GAAP
from ledgerfield.tax.JM.cit import bereken_cit_jamaica

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/JM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_jm_schema_min_60_accounts():
    assert len(JM_GAAP) >= 60


# 2 — unregulated CIT rate = 25%
def test_cit_rate_25pct_unregulated():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — unregulated: 1,000,000 → 250,000
def test_unregulated_one_million():
    result = bereken_cit_jamaica(1_000_000.0, 2025, regulated=False)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 4 — regulated (bank/insurer/securities dealer): 1,000,000 → 333,333.33 (1/3)
def test_regulated_one_million_one_third():
    result = bereken_cit_jamaica(1_000_000.0, 2025, regulated=True)
    assert result.cit_totaal == pytest.approx(333_333.33, abs=0.01)
    assert result.cit_rate == pytest.approx(1 / 3)


# 5 — regulated rate in params equals one third (IEEE-754 double)
def test_regulated_rate_param_one_third():
    assert _params()["cit"]["regulated_rate"] == pytest.approx(1 / 3)


# 6 — effectief tarief matches the applied rate
def test_effectief_tarief():
    assert bereken_cit_jamaica(400_000.0, 2025).effectief_tarief == pytest.approx(0.25)
    assert bereken_cit_jamaica(400_000.0, 2025, regulated=True).effectief_tarief == pytest.approx(1 / 3)


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_jamaica(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_jamaica(-25_000.0, 2025, regulated=True).cit_totaal == pytest.approx(0.0)


# 8 — GCT standard rate = 15%
def test_gct_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)


# 9 — Minimum Business Tax abolished
def test_mbt_abolished():
    mbt = _params()["minimum_business_tax"]
    assert mbt["abolished"] is True
    assert mbt["rate"] == pytest.approx(0.0)


# 10 — official source is TAJ
def test_official_source_taj():
    sources = _params()["metadata"]["official_sources"]
    assert any("jamaicatax.gov.jm" in s["url"] for s in sources)
