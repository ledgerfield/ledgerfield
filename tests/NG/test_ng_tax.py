"""Federal Republic of Nigeria tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.NG.ng_gaap import NG_GAAP
from ledgerfield.tax.NG.cit import bereken_cit_nigeria

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. VAT accounts)
def test_ng_schema_min_60_accounts():
    assert len(NG_GAAP) >= 60
    names = [a.name for a in NG_GAAP]
    assert any("Input VAT" in n for n in names)
    assert any("Output VAT" in n for n in names)


# 2 — large company: 30% CIT + 3% TET = 330,000 on 1,000,000
def test_large_company_cit_plus_tet():
    result = bereken_cit_nigeria(1_000_000.0, 2025, company_size="large")
    assert result.cit_bedrag == pytest.approx(300_000.0)
    assert result.tet_bedrag == pytest.approx(30_000.0)
    assert result.totaal_bedrag == pytest.approx(330_000.0)


# 3 — medium company: 20% CIT + 3% TET
def test_medium_company_cit_plus_tet():
    result = bereken_cit_nigeria(1_000_000.0, 2025, company_size="medium")
    assert result.cit_bedrag == pytest.approx(200_000.0)
    assert result.tet_bedrag == pytest.approx(30_000.0)
    assert result.totaal_bedrag == pytest.approx(230_000.0)


# 4 — small company (turnover ≤ ₦25m): exempt from CIT and TET
def test_small_company_exempt():
    result = bereken_cit_nigeria(1_000_000.0, 2025, company_size="small")
    assert result.cit_bedrag == pytest.approx(0.0)
    assert result.tet_bedrag == pytest.approx(0.0)
    assert result.totaal_bedrag == pytest.approx(0.0)


# 5 — unknown company size is rejected
def test_unknown_company_size_raises():
    with pytest.raises(ValueError):
        bereken_cit_nigeria(1_000_000.0, 2025, company_size="mega")


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_nigeria(0.0, 2025).totaal_bedrag == pytest.approx(0.0)
    assert bereken_cit_nigeria(-500_000.0, 2025).totaal_bedrag == pytest.approx(0.0)


# 7 — params CIT rates by turnover-based company size
def test_params_cit_rates_by_size():
    rates = _params()["cit"]["rates_by_company_size"]
    assert rates["small"] == pytest.approx(0.0)
    assert rates["medium"] == pytest.approx(0.20)
    assert rates["large"] == pytest.approx(0.30)


# 8 — VAT = 7.5%
def test_vat_7_5pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.075)
    assert _params()["vat"]["implemented"] is True


# 9 — TET = 3% of assessable profit for medium/large
def test_tet_3pct_medium_large():
    tet = _params()["tertiary_education_tax"]
    assert tet["rate"] == pytest.approx(0.03)
    assert set(tet["applies_to"]) == {"medium", "large"}


# 10 — 2025 Tax Reform Acts note (effective 2026) is documented
def test_2026_reform_note_present():
    note = _params()["reform_2025"]["note"]
    assert "2026" in note
    assert "Development Levy" in note


# 11 — official FIRS source URL
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"] == "https://www.firs.gov.ng/" for s in sources)


# 12 — effectief_tarief is computed on the total (CIT + TET)
def test_effectief_tarief_on_totaal():
    result = bereken_cit_nigeria(1_000_000.0, 2025, company_size="large")
    assert result.effectief_tarief == pytest.approx(0.33)
    medium = bereken_cit_nigeria(1_000_000.0, 2025, company_size="medium")
    assert medium.effectief_tarief == pytest.approx(0.23)
