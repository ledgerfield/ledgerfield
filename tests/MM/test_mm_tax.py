"""Myanmar tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MM.mm_gaap import MM_GAAP
from ledgerfield.tax.MM.cit import bereken_cit_myanmar

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_mm_schema_min_60_accounts():
    assert len(MM_GAAP) >= 60


# 2 — Commercial Tax accounts present, no VAT accounts (Myanmar has no VAT)
def test_mm_schema_commercial_tax_no_vat_accounts():
    names = [a.name for a in MM_GAAP]
    assert any("Commercial Tax" in n for n in names)
    assert any("Specific Goods Tax" in n for n in names)
    assert not any("VAT" in n for n in names)


# 3 — standard CIT rate = 22% → 1,000,000 MMK → 220,000
def test_standard_cit_22pct():
    result = bereken_cit_myanmar(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.22)
    assert result.cit_totaal == pytest.approx(220_000.0)


# 4 — YSX-listed company → 17% → 170,000
def test_ysx_listed_17pct():
    result = bereken_cit_myanmar(1_000_000.0, 2025, ysx_listed=True)
    assert result.cit_rate == pytest.approx(0.17)
    assert result.cit_totaal == pytest.approx(170_000.0)


# 5 — zero profit yields zero tax (both variants)
def test_zero_profit_zero_tax():
    assert bereken_cit_myanmar(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_myanmar(0.0, 2025, ysx_listed=True).cit_totaal == pytest.approx(0.0)


# 6 — negative profit yields zero tax (both variants)
def test_negative_profit_zero_tax():
    assert bereken_cit_myanmar(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_myanmar(-50_000.0, 2025, ysx_listed=True).cit_totaal == pytest.approx(0.0)


# 7 — Commercial Tax standard rate 5% modelled in params
def test_commercial_tax_5pct():
    assert _params()["commercial_tax"]["standard_rate"] == pytest.approx(0.05)


# 8 — no VAT: block absent or explicitly not implemented
def test_no_vat_block():
    params = _params()
    assert "vat" not in params or params["vat"]["implemented"] is False


# 9 — SGT (Specific Goods Tax) note present in commercial_tax block
def test_sgt_note_present():
    assert "Specific Goods Tax" in _params()["commercial_tax"]["note"]


# 10 — fiscal year note: October-September (FY2024-25)
def test_fiscal_year_october_september():
    fy = _params()["fiscal_year"]
    assert fy["start"] == "10-01"
    assert fy["end"] == "09-30"
    assert "October" in fy["note"]


# 11 — official source URL: Internal Revenue Department
def test_official_source_ird():
    sources = _params()["metadata"]["official_sources"]
    assert any("ird.gov.mm" in s["url"] for s in sources)


# 12 — effectief_tarief consistency: cit_totaal / winst == effectief_tarief
def test_effectief_tarief_consistency():
    for winst, ysx in [(1_000_000.0, False), (1_000_000.0, True), (37_500.0, False)]:
        result = bereken_cit_myanmar(winst, 2025, ysx_listed=ysx)
        assert result.effectief_tarief == pytest.approx(result.cit_totaal / winst)
    assert bereken_cit_myanmar(-1.0, 2025).effectief_tarief == pytest.approx(0.0)
