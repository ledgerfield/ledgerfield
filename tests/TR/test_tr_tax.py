"""Republic of Türkiye tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.TR.tr_gaap import TR_GAAP
from ledgerfield.tax.TR.cit import bereken_cit_turkije

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/TR/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT accounts)
def test_tr_schema_min_60_accounts():
    assert len(TR_GAAP) >= 60
    names = " ".join(a.name for a in TR_GAAP)
    assert "KDV" in names  # Turkish VAT accounts present


# 2 — CIT rate = 25%
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — standard company: 1,000,000 → 250,000
def test_standard_company_25pct():
    result = bereken_cit_turkije(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.25)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 4 — financial institution: 30% → 300,000
def test_financial_institution_30pct():
    result = bereken_cit_turkije(1_000_000.0, 2025, financial_institution=True)
    assert result.cit_rate == pytest.approx(0.30)
    assert result.cit_totaal == pytest.approx(300_000.0)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_turkije(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_turkije(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — inflation_adjusted flag defaults to False
def test_inflation_adjusted_defaults_false():
    result = bereken_cit_turkije(1_000_000.0, 2025)
    assert result.inflation_adjusted is False


# 7 — inflation_adjusted flag round-trips into the result (issue #31)
def test_inflation_adjusted_flag_round_trips():
    result = bereken_cit_turkije(1_000_000.0, 2025, inflation_adjusted=True)
    assert result.inflation_adjusted is True
    # Flag is record-only: it must not change the computation.
    assert result.cit_totaal == pytest.approx(250_000.0)


# 8 — inflation adjustment is documented as mandatory in params
def test_inflation_adjustment_params_note():
    infl = _params()["cit"]["inflation_adjustment"]
    assert infl["mandatory"] is True
    assert "298" in infl["note"]


# 9 — VAT standard rate = 20%
def test_vat_standard_rate_20pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.20)
    assert vat["implemented"] is True


# 10 — domestic minimum tax note present (Law No. 7524, 2025)
def test_domestic_minimum_tax_note():
    dmt = _params()["cit"]["domestic_minimum_tax"]
    assert dmt["rate"] == pytest.approx(0.10)
    assert "7524" in dmt["note"]


# 11 — official source URL (Gelir İdaresi Başkanlığı)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("gib.gov.tr" in s["url"] for s in sources)


# 12 — effectief_tarief consistency
def test_effectief_tarief_consistency():
    result = bereken_cit_turkije(2_400_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(result.cit_totaal / result.winst)
    assert result.effectief_tarief == pytest.approx(0.25)
    fin = bereken_cit_turkije(2_400_000.0, 2025, financial_institution=True)
    assert fin.effectief_tarief == pytest.approx(0.30)
