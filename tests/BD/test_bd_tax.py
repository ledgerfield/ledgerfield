"""Bangladesh tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.BD.bd_gaap import BD_GAAP
from ledgerfield.tax.BD.cit import bereken_cit_bangladesh

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/BD/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT/Mushak accounts)
def test_bd_schema_min_60_accounts():
    assert len(BD_GAAP) >= 60
    names = " ".join(a.name for a in BD_GAAP)
    assert "Mushak" in names
    assert "VAT" in names


# 2 — non-listed company: 27.5% on 1,000,000 → 275,000
def test_non_listed_27_5pct():
    result = bereken_cit_bangladesh(1_000_000.0, 2025, company_type="non_listed")
    assert result.cit_totaal == pytest.approx(275_000.0)
    assert result.cit_rate == pytest.approx(0.275)


# 3 — listed company: 22.5% → 225,000
def test_listed_22_5pct():
    result = bereken_cit_bangladesh(1_000_000.0, 2025, company_type="listed")
    assert result.cit_totaal == pytest.approx(225_000.0)


# 4 — non-listed bank/insurance/NBFI: 40% → 400,000
def test_bank_non_listed_40pct():
    result = bereken_cit_bangladesh(1_000_000.0, 2025, company_type="bank_non_listed")
    assert result.cit_totaal == pytest.approx(400_000.0)


# 5 — mobile operator / tobacco: 45% → 450,000
def test_mobile_tobacco_45pct():
    result = bereken_cit_bangladesh(1_000_000.0, 2025, company_type="mobile_tobacco")
    assert result.cit_totaal == pytest.approx(450_000.0)


# 6 — unknown company type is rejected
def test_unknown_company_type_raises():
    with pytest.raises(ValueError):
        bereken_cit_bangladesh(1_000_000.0, 2025, company_type="offshore_fund")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_bangladesh(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_bangladesh(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT standard rate = 15% (VAT & SD Act 2012)
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)
    assert _params()["vat"]["implemented"] is True


# 9 — banking-channel 25% conditional rate is documented
def test_banking_channel_condition_note():
    conditions = _params()["cit"]["conditions"]
    assert conditions["banking_channel_reduced_rate"] == pytest.approx(0.25)
    assert "banking channel" in conditions["banking_channel_note"].lower()


# 10 — official source is the National Board of Revenue
def test_official_source_nbr():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"].startswith("https://nbr.gov.bd") for s in sources)


# 11 — effectief tarief equals the statutory rate for each company type
def test_effectief_tarief_consistency():
    for company_type in ("non_listed", "listed", "bank_listed", "bank_non_listed", "mobile_tobacco"):
        result = bereken_cit_bangladesh(2_500_000.0, 2025, company_type=company_type)
        assert result.effectief_tarief == pytest.approx(result.cit_rate)
        assert result.cit_totaal == pytest.approx(result.winst * result.cit_rate)


# 12 — minimum tax on gross receipts (0.6%) is documented
def test_minimum_tax_note():
    minimum = _params()["cit"]["minimum_tax"]
    assert minimum["gross_receipts_rate"] == pytest.approx(0.006)
    assert "gross receipts" in minimum["note"].lower()
