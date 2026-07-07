"""Plurinational State of Bolivia tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.BO.bo_gaap import BO_GAAP
from ledgerfield.tax.BO.cit import bereken_cit_bolivia

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/BO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_bo_schema_min_60_accounts():
    assert len(BO_GAAP) >= 60


# 2 — IUE flat 25%
def test_iue_25pct():
    result = bereken_cit_bolivia(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 3 — params IUE rate = 25%
def test_params_iue_rate():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 4 — financial sector AA-IUE surtax documented (25% when ROE > 6%)
def test_aa_iue_note_present():
    cit = _params()["cit"]
    assert cit["special_rates"]["financial_sector_aa_iue"] == pytest.approx(0.25)
    assert "AA-IUE" in cit["note"]
    assert "6%" in cit["note"]


# 5 — mining/hydrocarbons surtaxes documented (12.5% / up to 25%)
def test_mining_surtax_note_present():
    cit = _params()["cit"]
    assert cit["special_rates"]["mining_surtax"] == pytest.approx(0.125)
    assert cit["special_rates"]["mining_surtax_max_additional"] == pytest.approx(0.25)


# 6 — IT transactions tax 3% documented
def test_it_transactions_tax_3pct():
    it = _params()["it_transactions_tax"]
    assert it["rate"] == pytest.approx(0.03)
    assert "Impuesto a las Transacciones" in it["note"]


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_bolivia(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bolivia(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT (IVA) nominal rate = 13%
def test_vat_13pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.13)
    assert vat["implemented"] is True


# 9 — inside-price IVA: effective 14.94% on net price documented
def test_vat_effective_rate_note():
    vat = _params()["vat"]
    assert vat["effective_rate_on_net_price"] == pytest.approx(0.1494, abs=1e-4)
    assert "14.94%" in vat["note"]


# 10 — official SIN source referenced
def test_official_source_sin():
    sources = _params()["metadata"]["official_sources"]
    assert any("impuestos.gob.bo" in s["url"] for s in sources)


# 11 — effective rate equals 25% for positive profit
def test_effectief_tarief_matches_rate():
    result = bereken_cit_bolivia(4_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.25)
    assert result.cit_rate == pytest.approx(0.25)
