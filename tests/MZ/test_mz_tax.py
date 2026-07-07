"""Republic of Mozambique tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MZ.mz_gaap import MZ_GAAP
from ledgerfield.tax.MZ.cit import bereken_cit_mozambique

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_mz_schema_min_60_accounts():
    assert len(MZ_GAAP) >= 60


# 2 — schema includes IVA accounts
def test_mz_schema_has_iva_accounts():
    names = " ".join(account.name for account in MZ_GAAP)
    assert "IVA Payable" in names
    assert "IVA Receivable" in names


# 3 — standard IRPC: 32% on 1,000,000
def test_standard_rate_32pct():
    result = bereken_cit_mozambique(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(320_000.0)
    assert result.cit_rate == pytest.approx(0.32)


# 4 — agriculture/aquaculture: 10%
def test_agriculture_10pct():
    result = bereken_cit_mozambique(1_000_000.0, 2025, sector="agriculture")
    assert result.cit_totaal == pytest.approx(100_000.0)


# 5 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_mozambique(1_000_000.0, 2025, sector="mining")


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_mozambique(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_mozambique(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 7 — VAT (IVA) standard rate = 16%
def test_vat_16pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.16)
    assert _params()["vat"]["implemented"] is True


# 8 — mining/petroleum regime and ISPC 3% notes are present
def test_notes_present():
    params = _params()
    assert "petroleum" in params["cit"]["note"].lower()
    assert "ISPC" in params["vat"]["note"]
    assert "3%" in params["vat"]["note"]


# 9 — official Autoridade Tributária source URL is referenced
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("at.gov.mz" in source["url"] for source in sources)


# 10 — effective rate equals the sector rate for positive profit
def test_effectief_tarief():
    result = bereken_cit_mozambique(2_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.32)
    assert bereken_cit_mozambique(-1.0, 2025).effectief_tarief == pytest.approx(0.0)


# 11 — params CIT rates match the calculator's rate table
def test_params_rates_match_calculator():
    params = _params()
    assert params["cit"]["standard_rate"] == pytest.approx(
        bereken_cit_mozambique(1.0, 2025).cit_rate
    )
    assert params["cit"]["special_rates"]["agriculture"] == pytest.approx(
        bereken_cit_mozambique(1.0, 2025, sector="agriculture").cit_rate
    )
