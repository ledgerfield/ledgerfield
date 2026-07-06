"""Sri Lanka tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.LK.lk_gaap import LK_GAAP
from ledgerfield.tax.LK.cit import bereken_cit_srilanka

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/LK/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_lk_schema_min_60_accounts():
    assert len(LK_GAAP) >= 60


# 2 — schema includes VAT and SSCL accounts
def test_lk_schema_has_vat_and_sscl_accounts():
    names = " | ".join(a.name for a in LK_GAAP)
    assert "VAT" in names
    assert "SSCL" in names


# 3 — standard CIT rate = 30%
def test_cit_standard_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 4 — standard sector: 1,000,000 → 300,000
def test_standard_sector_30pct():
    result = bereken_cit_srilanka(1_000_000.0, 2025, sector="standard")
    assert result.cit_totaal == pytest.approx(300_000.0)


# 5 — export of services: 1,000,000 → 150,000 (15%, 2025 budget)
def test_export_services_15pct():
    result = bereken_cit_srilanka(1_000_000.0, 2025, sector="export_services")
    assert result.cit_totaal == pytest.approx(150_000.0)
    assert _params()["cit"]["sector_rates"]["export_services"] == pytest.approx(0.15)


# 6 — betting/gaming, liquor and tobacco: 1,000,000 → 450,000 (45% sector rate)
def test_betting_liquor_tobacco_45pct():
    result = bereken_cit_srilanka(1_000_000.0, 2025, sector="betting_liquor_tobacco")
    assert result.cit_totaal == pytest.approx(450_000.0)
    assert _params()["cit"]["sector_rates"]["betting_liquor_tobacco"] == pytest.approx(0.45)


# 7 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_srilanka(1_000_000.0, 2025, sector="offshore_banking")


# 8 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_srilanka(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_srilanka(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 9 — VAT = 18% effective 1 January 2024 (up from 15%)
def test_vat_18pct_from_2024():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.18)
    assert vat["implemented"] is True
    assert vat["effective_from"] == "2024-01-01"
    assert vat["previous_rate"] == pytest.approx(0.15)


# 10 — SSCL = 2.5% on turnover, with explanatory note
def test_sscl_2_5pct_on_turnover():
    sscl = _params()["sscl"]
    assert sscl["rate"] == pytest.approx(0.025)
    assert sscl["base"] == "turnover"
    assert "Social Security Contribution Levy" in sscl["note"]


# 11 — official source URL (Inland Revenue Department) and 2025 date range
def test_official_source_and_effective_dates():
    meta = _params()["metadata"]
    assert any(
        s["url"] == "https://www.ird.gov.lk/" for s in meta["official_sources"]
    )
    assert meta["effective_date_range"]["start"] == "2025-01-01"
    assert meta["effective_date_range"]["end"] == "2025-12-31"


# 12 — effectief_tarief consistency across sectors
def test_effectief_tarief_consistency():
    for sector, rate in [
        ("standard", 0.30),
        ("export_services", 0.15),
        ("betting_liquor_tobacco", 0.45),
    ]:
        result = bereken_cit_srilanka(2_500_000.0, 2025, sector=sector)
        assert result.effectief_tarief == pytest.approx(rate)
        assert result.cit_totaal == pytest.approx(result.winst * result.effectief_tarief)
