"""Bolivarian Republic of Venezuela tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.VE.ve_gaap import VE_GAAP
from ledgerfield.tax.VE.cit import bereken_cit_venezuela

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/VE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ve_schema_min_60_accounts():
    assert len(VE_GAAP) >= 60


# 2 — standard company: 34% top band
def test_standard_company_34pct():
    result = bereken_cit_venezuela(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(340_000.0)


# 3 — banking / insurance: 40%
def test_banking_insurance_40pct():
    result = bereken_cit_venezuela(1_000_000.0, 2025, sector="banking_insurance")
    assert result.cit_totaal == pytest.approx(400_000.0)


# 4 — hydrocarbons: 50%
def test_hydrocarbons_50pct():
    result = bereken_cit_venezuela(1_000_000.0, 2025, sector="hydrocarbons")
    assert result.cit_totaal == pytest.approx(500_000.0)


# 5 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_venezuela(1_000_000.0, 2025, sector="agriculture")


# 6 — Tarifa 2 UT brackets documented (15/22/34 with UT hyperinflation caveat)
def test_ut_bracket_note_present():
    cit = _params()["cit"]
    note = cit["note"]
    assert "UT" in note and "2,000 UT" in note and "3,000 UT" in note
    rates = [b["rate"] for b in cit["tarifa_2_ut_brackets"]]
    assert rates == [pytest.approx(0.15), pytest.approx(0.22), pytest.approx(0.34)]


# 7 — inflation adjustment (API/RPA) documented
def test_inflation_adjustment_note_present():
    infl = _params()["inflation_adjustment"]
    assert infl["applies"] is True
    assert "API" in infl["note"] or "RPA" in infl["note"]


# 8 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_venezuela(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_venezuela(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 9 — VAT (IVA) standard rate = 16%
def test_vat_16pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.16)
    assert vat["implemented"] is True


# 10 — official SENIAT source referenced
def test_official_source_seniat():
    sources = _params()["metadata"]["official_sources"]
    assert any("seniat.gob.ve" in s["url"] for s in sources)


# 11 — effective rate equals sector rate for positive profit
def test_effectief_tarief_matches_rate():
    result = bereken_cit_venezuela(2_500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.34)
    assert result.cit_rate == pytest.approx(0.34)
