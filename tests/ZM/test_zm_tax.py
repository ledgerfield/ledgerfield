"""Republic of Zambia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.ZM.zm_gaap import ZM_GAAP
from ledgerfield.tax.ZM.cit import bereken_cit_zambia

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/ZM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_zm_schema_min_60_accounts():
    assert len(ZM_GAAP) >= 60


# 2 — standard CIT rate = 30%
def test_cit_standard_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — standard sector: 1,000,000 → 300,000
def test_standard_sector():
    result = bereken_cit_zambia(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.cit_rate == pytest.approx(0.30)


# 4 — farming/agro-processing: 10% → 100,000
def test_farming_agro_sector():
    result = bereken_cit_zambia(1_000_000.0, 2025, sector="farming_agro")
    assert result.cit_totaal == pytest.approx(100_000.0)


# 5 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_zambia(1_000_000.0, 2025, sector="mining")


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_zambia(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_zambia(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_zambia(-75_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — VAT = 16%
def test_vat_16pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.16)
    assert vat["implemented"] is True


# 8 — turnover tax 5% up to K5m noted
def test_turnover_tax_note():
    tot = _params()["turnover_tax"]
    assert tot["rate"] == pytest.approx(0.05)
    assert tot["threshold_zmw"] == 5_000_000
    assert "note" in tot


# 9 — hotels/tourism 15% accommodation rate + mining regime notes present
def test_sector_notes_present():
    cit = _params()["cit"]
    assert cit["special_rates"]["hotels_tourism_accommodation"] == pytest.approx(0.15)
    assert "mining" in cit["note"].lower()
    assert "note" in _params()["mineral_royalty"]


# 10 — official ZRA source URL present
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("zra.org.zm" in s["url"] for s in sources)


# 11 — effectief_tarief equals the applied rate for positive profit
def test_effectief_tarief():
    result = bereken_cit_zambia(3_000_000.0, 2025, sector="farming_agro")
    assert result.effectief_tarief == pytest.approx(0.10)


# 12 — result carries sector and year through
def test_result_metadata_passthrough():
    result = bereken_cit_zambia(500_000.0, 2025, sector="standard")
    assert result.sector == "standard"
    assert result.jaar == 2025
    assert result.winst == pytest.approx(500_000.0)
