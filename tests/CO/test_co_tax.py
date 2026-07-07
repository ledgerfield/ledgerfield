"""Republic of Colombia tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CO.co_gaap import CO_GAAP
from ledgerfield.tax.CO.cit import bereken_cit_colombia

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. IVA accounts)
def test_co_schema_min_60_accounts():
    assert len(CO_GAAP) >= 60
    names = " ".join(a.name for a in CO_GAAP)
    assert "IVA" in names


# 2 — CIT rate = 35%
def test_cit_rate_35pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.35)


# 3 — general rate: 1,000,000 → 350,000
def test_general_rate_350k():
    result = bereken_cit_colombia(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(350_000.0)
    assert result.cit_rate == pytest.approx(0.35)


# 4 — financial institution surtax: 1,000,000 → 400,000
def test_financial_institution_400k():
    result = bereken_cit_colombia(1_000_000.0, 2025, financial_institution=True)
    assert result.cit_totaal == pytest.approx(400_000.0)
    assert result.cit_rate == pytest.approx(0.40)


# 5 — effectief tarief matches the applied rate
def test_effectief_tarief():
    assert bereken_cit_colombia(2_000_000.0, 2025).effectief_tarief == pytest.approx(0.35)
    assert bereken_cit_colombia(
        2_000_000.0, 2025, financial_institution=True
    ).effectief_tarief == pytest.approx(0.40)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_colombia(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_colombia(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_colombia(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — VAT (IVA) = 19%
def test_vat_19pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.19)
    assert _params()["vat"]["implemented"] is True


# 8 — financial-institution surtax note (+5pp through 2027)
def test_financial_surtax_note():
    cit = _params()["cit"]
    assert cit["financial_institution_surtax"] == pytest.approx(0.05)
    assert cit["financial_institution_rate"] == pytest.approx(0.40)
    assert "2027" in cit["financial_institution_note"]


# 9 — Pillar-Two-style domestic minimum effective tax rate 15% note
def test_minimum_effective_tax_note():
    met = _params()["cit"]["minimum_effective_tax"]
    assert met["rate"] == pytest.approx(0.15)
    assert "note" in met


# 10 — ICA municipal turnover tax note present
def test_ica_note_present():
    assert "municipal" in _params()["ica"]["note"].lower()


# 11 — official source is the DIAN, range 2025
def test_official_source_dian_and_range():
    meta = _params()["metadata"]
    assert any("dian.gov.co" in s["url"] for s in meta["official_sources"])
    assert meta["effective_date_range"]["start"] == "2025-01-01"
    assert meta["effective_date_range"]["end"] == "2025-12-31"
