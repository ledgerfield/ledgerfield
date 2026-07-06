"""Kingdom of Bahrain tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.BH.bh_gaap import BH_GAAP
from ledgerfield.tax.BH.cit import bereken_cit_bahrein

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/BH/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT accounts, since Bahrain has 10% VAT)
def test_bh_schema_min_60_accounts():
    assert len(BH_GAAP) >= 60
    vat_accounts = [a for a in BH_GAAP if "VAT" in a.name]
    assert len(vat_accounts) >= 2


# 2 — general CIT standard rate = 0% (zero-CIT model)
def test_cit_standard_rate_zero():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.0)


# 3 — zero_cit flag works: positive profit, default mode → 0 tax
def test_zero_cit_positive_profit_no_tax():
    result = bereken_cit_bahrein(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.cit_rate == pytest.approx(0.0)


# 4 — oil & gas: 46% on 1,000,000 = 460,000 (Legislative Decree No. 22 of 1979)
def test_oil_and_gas_46pct():
    result = bereken_cit_bahrein(1_000_000.0, 2025, oil_and_gas=True)
    assert result.cit_totaal == pytest.approx(460_000.0)
    assert result.cit_rate == pytest.approx(0.46)


# 5 — non-positive profit yields zero tax in default (zero-CIT) mode
def test_non_positive_profit_zero_tax_default_mode():
    assert bereken_cit_bahrein(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bahrein(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — non-positive profit yields zero tax in oil & gas mode (defensive guard)
def test_non_positive_profit_zero_tax_oil_mode():
    assert bereken_cit_bahrein(0.0, 2025, oil_and_gas=True).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bahrein(-25_000.0, 2025, oil_and_gas=True).cit_totaal == pytest.approx(0.0)


# 7 — VAT standard rate = 10% (raised from 5% on 1 Jan 2022)
def test_vat_10pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.10)
    assert _params()["vat"]["implemented"] is True


# 8 — no personal income tax
def test_no_personal_income_tax():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.0)


# 9 — DMTT (Decree-Law No. 11 of 2024) mentioned in params note
def test_dmtt_mentioned_in_note():
    note = _params()["cit"]["note"]
    assert "DMTT" in note
    assert "Decree-Law No. 11 of 2024" in note


# 10 — official source (NBR) URL present
def test_official_source_nbr_url():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"] == "https://www.nbr.gov.bh/" for s in sources)


# 11 — effectief tarief: 0 in zero-CIT mode, 0.46 in oil & gas mode
def test_effectief_tarief_by_mode():
    assert bereken_cit_bahrein(500_000.0, 2025).effectief_tarief == pytest.approx(0.0)
    assert bereken_cit_bahrein(500_000.0, 2025, oil_and_gas=True).effectief_tarief == pytest.approx(0.46)
