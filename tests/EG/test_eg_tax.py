"""Arab Republic of Egypt tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.EG.eg_gaap import EG_GAAP
from ledgerfield.tax.EG.cit import bereken_cit_egypte

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/EG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_eg_schema_min_60_accounts():
    assert len(EG_GAAP) >= 60


# 2 — standard CIT rate = 22.5%
def test_cit_standard_rate_22_5pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.225)


# 3 — standard sector: 1,000,000 → 225,000
def test_standard_sector_cit():
    result = bereken_cit_egypte(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(225_000.0)
    assert result.sector == "standard"


# 4 — oil & gas exploration/production: 40.55%
def test_oil_gas_sector_cit():
    result = bereken_cit_egypte(1_000_000.0, 2025, sector="oil_gas")
    assert result.cit_totaal == pytest.approx(405_500.0)
    assert result.cit_rate == pytest.approx(0.4055)


# 5 — state entities (Suez Canal Authority / EGPC / CBE): 40%
def test_state_entities_sector_cit():
    result = bereken_cit_egypte(1_000_000.0, 2025, sector="state_entities")
    assert result.cit_totaal == pytest.approx(400_000.0)
    assert result.cit_rate == pytest.approx(0.40)


# 6 — unknown sector is rejected
def test_unknown_sector_raises():
    with pytest.raises(ValueError):
        bereken_cit_egypte(1_000_000.0, 2025, sector="freezone")


# 7 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_egypte(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_egypte(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_egypte(-25_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 8 — VAT standard rate = 14%
def test_vat_14pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.14)
    assert _params()["vat"]["implemented"] is True


# 9 — small-enterprise turnover regime (Law 6/2025) documented
def test_small_enterprise_regime_note():
    regime = _params()["small_enterprise_regime"]
    assert regime["turnover_threshold_egp"] == 20_000_000
    assert regime["turnover_rate_range"] == [pytest.approx(0.004), pytest.approx(0.015)]
    assert "Law No. 6 of 2025" in regime["note"]


# 10 — official source URL (Egyptian Tax Authority)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"] == "https://www.eta.gov.eg/" for s in sources)


# 11 — effectief tarief equals statutory rate on positive profit
def test_effectief_tarief():
    result = bereken_cit_egypte(2_500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.225)
