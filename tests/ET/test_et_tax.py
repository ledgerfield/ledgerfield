"""Federal Democratic Republic of Ethiopia tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.ET.et_gaap import ET_GAAP
from ledgerfield.tax.ET.cit import bereken_cit_ethiopie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/ET/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_et_schema_min_60_accounts():
    assert len(ET_GAAP) >= 60


# 2 — CIT rate = 30% flat
def test_cit_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — 1,000,000 → 300,000
def test_flat_cit_on_profit():
    result = bereken_cit_ethiopie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.cit_rate == pytest.approx(0.30)


# 4 — statutory basis: Income Tax Proclamation 979/2016
def test_cit_basis_proclamation():
    assert "979/2016" in _params()["cit"]["basis"]


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_ethiopie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_ethiopie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_ethiopie(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 6 — VAT standard rate = 15%
def test_vat_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)
    assert _params()["vat"]["implemented"] is True


# 7 — VAT modernization note references Proclamation 1341/2024
def test_vat_proclamation_note():
    assert "1341/2024" in _params()["vat"]["note"]


# 8 — Turnover Tax (TOT) 2% goods / 10% services documented
def test_turnover_tax_note():
    tot = _params()["turnover_tax"]
    assert tot["goods_rate"] == pytest.approx(0.02)
    assert tot["services_rate"] == pytest.approx(0.10)
    assert "VAT registration threshold" in tot["note"]


# 9 — official source URL (Ministry of Revenues)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"] == "https://mor.gov.et/" for s in sources)


# 10 — effectief tarief equals statutory 30% on positive profit
def test_effectief_tarief():
    result = bereken_cit_ethiopie(2_500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.30)


# 11 — result carries winst and jaar through
def test_result_fields_roundtrip():
    result = bereken_cit_ethiopie(500_000.0, 2025)
    assert result.winst == pytest.approx(500_000.0)
    assert result.jaar == 2025
