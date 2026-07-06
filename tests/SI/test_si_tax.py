"""Republic of Slovenia tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.SI.si_gaap import SI_GAAP
from ledgerfield.tax.SI.cit import bereken_cit_slovenie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/SI/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_si_schema_min_60_accounts():
    assert len(SI_GAAP) >= 60


# 2 — CIT rate = 22% (temporary 2024-2028 rate)
def test_cit_rate_22pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.22)


# 3 — flat 22% on EUR 1,000,000
def test_flat_22pct_on_1m():
    result = bereken_cit_slovenie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(220_000.0)
    assert result.cit_rate == pytest.approx(0.22)


# 4 — the 2024-2028 temporary-window is documented in params
def test_temporary_window_2024_2028():
    window = _params()["cit"]["temporary_rate_window"]
    assert window["start_year"] == 2024
    assert window["end_year"] == 2028
    assert _params()["cit"]["base_rate"] == pytest.approx(0.19)


# 5 — minimum tax base rules are noted
def test_minimum_tax_base_note_present():
    note = _params()["cit"]["minimum_tax_base_note"]
    assert "63%" in note


# 6 — Pillar Two note present
def test_pillar_two_note_present():
    assert "Pillar Two" in _params()["cit"]["pillar_two_note"]


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_slovenie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_slovenie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT standard rate 22%
def test_vat_22pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.22)


# 9 — reduced VAT rates 9.5% and 5%
def test_vat_reduced_rates():
    assert _params()["vat"]["reduced_rates"] == [0.095, 0.05]


# 10 — OSS eligible (EU One Stop Shop) + official source is FURS
def test_oss_eligible_and_furs_source():
    assert _params()["vat"]["oss_eligible"] is True
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.fu.gov.si/" in urls


# 11 — effectief tarief equals 22% for positive profit
def test_effectief_tarief():
    result = bereken_cit_slovenie(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.22)
    assert result.effectief_tarief == pytest.approx(result.cit_totaal / result.winst)
