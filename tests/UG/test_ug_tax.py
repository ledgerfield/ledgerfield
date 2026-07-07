"""Republic of Uganda tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.UG.ug_gaap import UG_GAAP
from ledgerfield.tax.UG.cit import bereken_cit_oeganda

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/UG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ug_schema_min_60_accounts():
    assert len(UG_GAAP) >= 60


# 2 — CIT rate = 30%
def test_cit_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — flat 30% of 1,000,000 = 300,000
def test_flat_30pct():
    result = bereken_cit_oeganda(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.cit_rate == pytest.approx(0.30)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_oeganda(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oeganda(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — VAT standard rate = 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)
    assert _params()["vat"]["implemented"] is True


# 6 — presumptive turnover regime for small businesses documented
def test_presumptive_turnover_regime_note():
    note = _params()["presumptive_turnover_tax"]["note"]
    assert "presumptive" in note.lower()


# 7 — DST 5% on non-resident digital services
def test_dst_5pct_note():
    dst = _params()["digital_services_tax"]
    assert dst["rate"] == pytest.approx(0.05)
    assert "non-resident" in dst["note"].lower()


# 8 — official source is URA
def test_official_source_ura():
    sources = _params()["metadata"]["official_sources"]
    assert any("ura.go.ug" in s["url"] for s in sources)


# 9 — effective rate equals nominal rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_oeganda(4_200_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.30)


# 10 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"


# 11 — statutory basis references Income Tax Act Cap 340
def test_statutory_basis_cap_340():
    assert "Cap 340" in _params()["cit"]["basis"]
