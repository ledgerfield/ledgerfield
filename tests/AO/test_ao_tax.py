"""Republic of Angola tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.AO.ao_gaap import AO_GAAP
from ledgerfield.tax.AO.cit import bereken_cit_angola

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ao_schema_min_60_accounts():
    assert len(AO_GAAP) >= 60


# 2 — schema includes IVA accounts
def test_ao_schema_has_iva_accounts():
    names = " ".join(account.name for account in AO_GAAP)
    assert "IVA Payable" in names
    assert "IVA Receivable" in names


# 3 — standard Imposto Industrial: 25% on 1,000,000
def test_standard_rate_25pct():
    result = bereken_cit_angola(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)
    assert result.cit_rate == pytest.approx(0.25)


# 4 — banking/insurance/telecom: 35%
def test_banking_insurance_telecom_35pct():
    result = bereken_cit_angola(1_000_000.0, 2025, sector="banking_insurance_telecom")
    assert result.cit_totaal == pytest.approx(350_000.0)


# 5 — agriculture/forestry/livestock: 10%
def test_agriculture_10pct():
    result = bereken_cit_angola(1_000_000.0, 2025, sector="agriculture")
    assert result.cit_totaal == pytest.approx(100_000.0)


# 6 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_angola(1_000_000.0, 2025, sector="mining")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_angola(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_angola(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT (IVA) standard rate = 14%
def test_vat_14pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.14)
    assert _params()["vat"]["implemented"] is True


# 9 — petroleum regime and simplified IVA band notes are present
def test_notes_present():
    params = _params()
    assert "petroleum" in params["cit"]["note"].lower()
    assert "7%" in params["vat"]["note"]


# 10 — official AGT source URL is referenced
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("agt.minfin.gov.ao" in source["url"] for source in sources)


# 11 — effective rate equals the sector rate for positive profit
def test_effectief_tarief():
    result = bereken_cit_angola(2_000_000.0, 2025, sector="banking_insurance_telecom")
    assert result.effectief_tarief == pytest.approx(0.35)
    assert bereken_cit_angola(-1.0, 2025).effectief_tarief == pytest.approx(0.0)
