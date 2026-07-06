"""Republic of Latvia tax property tests — 11 tests (Estonian model)."""
import json
import os

import pytest

from ledgerfield.schemas.LV.lv_gaap import LV_GAAP
from ledgerfield.tax.LV.cit import bereken_cit_letland

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/LV/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_lv_schema_min_60_accounts():
    assert len(LV_GAAP) >= 60


# 2 — Estonian-model core: retained profit 1,000,000 → 0 tax
def test_retained_profit_zero_tax():
    result = bereken_cit_letland(1_000_000.0, 2025, ingehouden=True)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.effectief_tarief_op_netto == pytest.approx(0.0)


# 3 — distribution 800,000 net → 200,000 CIT (= 800000 * 20/80)
def test_distribution_grossed_up_20_80():
    result = bereken_cit_letland(800_000.0, 2025)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 4 — effective rate on the NET distribution is 25%
def test_effective_rate_on_net_25pct():
    result = bereken_cit_letland(800_000.0, 2025)
    assert result.effectief_tarief_op_netto == pytest.approx(0.25)


# 5 — statutory rate on grossed-up base is 20%
def test_statutory_rate_on_grossed_up_base_20pct():
    assert _params()["cit"]["distribution_rate_on_grossed_up_base"] == pytest.approx(0.20)
    assert bereken_cit_letland(800_000.0, 2025).cit_rate == pytest.approx(0.20)


# 6 — params: retained-profit rate is 0% (Estonian model)
def test_params_retained_rate_zero():
    assert _params()["cit"]["retained_profit_rate"] == pytest.approx(0.0)
    assert _params()["cit"]["model"] == "estonian_distribution_only"


# 7 — gross-up consistency: CIT equals 20% of (net / 0.8)
def test_gross_up_consistency():
    net = 123_456.0
    result = bereken_cit_letland(net, 2025)
    assert result.cit_totaal == pytest.approx(0.20 * (net / 0.8))


# 8 — VAT (PVN) standard 21%
def test_vat_standard_21pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.21)


# 9 — OSS eligible (EU member state)
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 10 — non-positive distribution yields zero tax (defensive guard)
def test_non_positive_distribution_zero_tax():
    assert bereken_cit_letland(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_letland(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 11 — official source is VID
def test_official_source_vid():
    sources = _params()["metadata"]["official_sources"]
    assert any("vid.gov.lv" in s["url"] for s in sources)
