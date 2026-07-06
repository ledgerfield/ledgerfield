"""Islamic Republic of Pakistan tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.PK.pk_gaap import PK_GAAP
from ledgerfield.tax.PK.cit import bereken_cit_pakistan

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PK/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_pk_schema_min_60_accounts():
    assert len(PK_GAAP) >= 60


# 2 — schema includes GST (sales tax) accounts
def test_pk_schema_has_gst_accounts():
    names = " | ".join(a.name for a in PK_GAAP)
    assert "GST" in names


# 3 — standard company: 29% → 1,000,000 → 290,000
def test_standard_company_29pct():
    result = bereken_cit_pakistan(1_000_000.0, 2025, company_type="standard")
    assert result.cit_totaal == pytest.approx(290_000.0)
    assert result.cit_rate == pytest.approx(0.29)


# 4 — small company: 20% → 1,000,000 → 200,000
def test_small_company_20pct():
    result = bereken_cit_pakistan(1_000_000.0, 2025, company_type="small")
    assert result.cit_totaal == pytest.approx(200_000.0)


# 5 — banking company: 39% → 1,000,000 → 390,000
def test_banking_company_39pct():
    result = bereken_cit_pakistan(1_000_000.0, 2025, company_type="banking")
    assert result.cit_totaal == pytest.approx(390_000.0)


# 6 — unknown company type is rejected
def test_unknown_company_type_raises():
    with pytest.raises(ValueError):
        bereken_cit_pakistan(1_000_000.0, 2025, company_type="cooperative")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_pakistan(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_pakistan(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — GST (sales tax on goods) standard rate = 18%
def test_gst_18pct():
    assert _params()["gst"]["standard_rate"] == pytest.approx(0.18)


# 9 — super tax (s.4C) note present in params
def test_super_tax_note_present():
    super_tax = _params()["cit"]["super_tax"]
    assert super_tax["section"] == "4C"
    assert super_tax["rate_range"] == [0.0, 0.10]
    assert "note" in super_tax


# 10 — official FBR source URL present
def test_source_url_fbr():
    sources = _params()["metadata"]["official_sources"]
    assert any("fbr.gov.pk" in s["url"] for s in sources)


# 11 — effectief_tarief consistency: cit_totaal / winst == effectief_tarief
def test_effectief_tarief_consistency():
    for company_type in ("standard", "small", "banking"):
        result = bereken_cit_pakistan(2_500_000.0, 2025, company_type=company_type)
        assert result.effectief_tarief == pytest.approx(result.cit_totaal / result.winst)
        assert result.effectief_tarief == pytest.approx(result.cit_rate)


# 12 — params CIT rates match calculator rates
def test_params_rates_match_calculator():
    params = _params()
    assert params["cit"]["standard_rate"] == pytest.approx(0.29)
    assert params["cit"]["special_rates"]["small_company"] == pytest.approx(0.20)
    assert params["cit"]["special_rates"]["banking_company"] == pytest.approx(0.39)
