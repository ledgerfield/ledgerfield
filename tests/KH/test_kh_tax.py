"""Kingdom of Cambodia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.KH.kh_gaap import KH_GAAP
from ledgerfield.tax.KH.cit import bereken_toi_cambodja

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/KH/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_kh_schema_min_60_accounts():
    assert len(KH_GAAP) >= 60


# 2 — schema includes VAT accounts (Cambodia has 10% VAT)
def test_kh_schema_has_vat_accounts():
    names = " | ".join(a.name for a in KH_GAAP)
    assert "VAT Input" in names
    assert "VAT Output" in names


# 3 — ToI standard rate = 20%
def test_toi_rate_20pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.20)


# 4 — standard sector: 1,000,000 profit → 200,000 ToI
def test_standard_sector_20pct():
    result = bereken_toi_cambodja(1_000_000.0, 2025, sector="standard")
    assert result.cit_totaal == pytest.approx(200_000.0)


# 5 — oil/gas & minerals sector: 1,000,000 profit → 300,000 ToI
def test_oil_gas_minerals_30pct():
    result = bereken_toi_cambodja(1_000_000.0, 2025, sector="oil_gas_minerals")
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert _params()["cit"]["special_rates"]["oil_gas_minerals"] == pytest.approx(0.30)


# 6 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_toi_cambodja(1_000_000.0, 2025, sector="banking")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_toi_cambodja(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_toi_cambodja(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT standard rate = 10%
def test_vat_10pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.10)
    assert _params()["vat"]["implemented"] is True


# 9 — minimum tax 1% of turnover documented
def test_minimum_tax_1pct_note():
    mt = _params()["minimum_tax"]
    assert mt["rate_on_turnover"] == pytest.approx(0.01)
    assert "1%" in mt["note"]


# 10 — QIP exemption note documented (3-9 year ToI holidays)
def test_qip_exemption_note():
    note = _params()["cit"]["qip_note"]
    assert "Qualified Investment Project" in note
    assert "3 to 9" in note


# 11 — official source URL (General Department of Taxation)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("tax.gov.kh" in s["url"] for s in sources)


# 12 — effectief_tarief consistency with cit_rate
def test_effectief_tarief_consistency():
    for winst in (1.0, 50_000.0, 1_000_000.0, 9_999_999.99):
        for sector in ("standard", "oil_gas_minerals"):
            result = bereken_toi_cambodja(winst, 2025, sector=sector)
            assert result.effectief_tarief == pytest.approx(result.toi_rate)
            assert result.cit_totaal == pytest.approx(winst * result.toi_rate)
