"""Republic of Indonesia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.ID.id_gaap import ID_GAAP
from ledgerfield.tax.ID.cit import bereken_cit_indonesie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/ID/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_id_schema_min_60_accounts():
    assert len(ID_GAAP) >= 60


# 2 — schema includes PPN input and output VAT accounts
def test_id_schema_has_ppn_accounts():
    names = [a.name for a in ID_GAAP]
    assert any("PPN Masukan" in n for n in names)
    assert any("PPN Keluaran" in n for n in names)


# 3 — CIT rate = 22% (UU HPP)
def test_cit_rate_22pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.22)


# 4 — standard company: 22% on profit
def test_standard_company_22pct():
    result = bereken_cit_indonesie(1_000_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(220_000_000.0)


# 5 — qualifying listed company: 3pp reduction → 19%
def test_public_listed_19pct():
    result = bereken_cit_indonesie(1_000_000_000.0, 2025, public_listed=True)
    assert result.cit_rate == pytest.approx(0.19)
    assert result.cit_totaal == pytest.approx(190_000_000.0)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_indonesie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_indonesie(-25_000_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_indonesie(-25_000_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — PPN standard rate 11%, luxury-only 12% nuance captured
def test_ppn_11pct_with_luxury_12_note():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.11)
    assert vat["implemented"] is True
    assert vat["luxury_goods_rate"] == pytest.approx(0.12)
    assert "LUXURY" in vat["note"] or "luxury" in vat["note"].lower()


# 8 — 0.5% small-business FINAL tax on turnover present as note-only param
def test_small_business_final_tax_note():
    final = _params()["cit"]["small_business_final_tax"]
    assert final["rate"] == pytest.approx(0.005)
    assert final["turnover_ceiling_idr"] == 4_800_000_000
    assert "TURNOVER" in final["note"] or "turnover" in final["note"].lower()


# 9 — Art. 31E 50% discount facility present as note-only param
def test_art_31e_facility_note():
    facility = _params()["cit"]["art_31e_facility"]
    assert facility["discount"] == pytest.approx(0.5)
    assert facility["turnover_ceiling_idr"] == 50_000_000_000


# 10 — WHT on dividends to foreign shareholders = 20%
def test_wht_dividends_foreign_20pct():
    assert _params()["wht"]["dividends_to_foreign_shareholders"] == pytest.approx(0.20)


# 11 — official source URL (Direktorat Jenderal Pajak)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("pajak.go.id" in s["url"] for s in sources)


# 12 — effectief_tarief consistency for positive profit
def test_effectief_tarief_consistency():
    for winst in (1.0, 4_800_000_000.0, 123_456_789.0):
        std = bereken_cit_indonesie(winst, 2025)
        assert std.effectief_tarief == pytest.approx(0.22)
        assert std.effectief_tarief == pytest.approx(std.cit_totaal / std.winst)
        listed = bereken_cit_indonesie(winst, 2025, public_listed=True)
        assert listed.effectief_tarief == pytest.approx(0.19)
