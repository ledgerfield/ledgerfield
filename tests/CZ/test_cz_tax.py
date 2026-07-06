"""Czech Republic tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CZ.cz_gaap import CZ_GAAP
from ledgerfield.tax.CZ.cit import bereken_cit_tsjechie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_cz_schema_min_60_accounts():
    assert len(CZ_GAAP) >= 60


# 2 — schema includes VAT (DPH) accounts
def test_cz_schema_has_vat_accounts():
    names = " | ".join(a.name for a in CZ_GAAP)
    assert "DPH" in names or "VAT" in names


# 3 — CIT rate = 21% (raised from 19% by the 2024 consolidation package)
def test_cit_rate_21pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.21)


# 4 — 1,000,000 CZK profit → 210,000 CZK CIT
def test_cit_million_profit():
    result = bereken_cit_tsjechie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(210_000.0)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_tsjechie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_tsjechie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — effective rate equals the flat 21% on positive profit
def test_effectief_tarief():
    result = bereken_cit_tsjechie(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.21)
    assert bereken_cit_tsjechie(-1.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — VAT: 21% standard + single reduced 12% (2024 reform)
def test_vat_rates():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.21)
    assert vat["reduced_rate"] == pytest.approx(0.12)


# 8 — EU One-Stop-Shop eligibility flagged
def test_vat_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 9 — windfall tax note present (60% surcharge, banks/energy, 2023-2025)
def test_windfall_tax_note():
    windfall = _params()["cit"]["windfall_tax"]
    assert windfall["surcharge_rate"] == pytest.approx(0.60)
    assert "2023-2025" in windfall["note"]


# 10 — Pillar Two note present (15% top-up, EUR 750m threshold)
def test_pillar_two_note():
    note = _params()["metadata"]["pillar_two_note"]
    assert "15%" in note
    assert "750 million" in note


# 11 — personal income tax 15% / 23%
def test_personal_income_tax_rates():
    pit = _params()["personal_income_tax"]
    assert pit["standard_rate"] == pytest.approx(0.15)
    assert pit["higher_rate"] == pytest.approx(0.23)


# 12 — official source is Financni sprava
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("financnisprava.cz" in s["url"] for s in sources)
