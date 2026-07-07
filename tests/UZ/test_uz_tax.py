"""Republic of Uzbekistan tax property tests."""
import json
import os

import pytest

from ledgerfield.schemas.UZ.uz_gaap import UZ_GAAP
from ledgerfield.tax.UZ.cit import bereken_cit_oezbekistan

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/UZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_uz_schema_min_60_accounts():
    assert len(UZ_GAAP) >= 60


# 2 — CIT rate = 15% standard
def test_cit_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — standard 15% on 1,000,000 → 150,000
def test_cit_standard_15pct():
    result = bereken_cit_oezbekistan(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(150_000.0)


# 4 — higher-rate sector (banks/mobile/cement) 20% → 200,000
def test_cit_hoger_tarief_sector_20pct():
    result = bereken_cit_oezbekistan(1_000_000.0, 2025, hoger_tarief_sector=True)
    assert result.cit_rate == pytest.approx(0.20)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_oezbekistan(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_oezbekistan(-25_000.0, 2025, hoger_tarief_sector=True).cit_totaal == pytest.approx(0.0)


# 6 — VAT = 12%
def test_vat_12pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.12)


# 7 — effective rate matches applicable rate
def test_effectief_tarief():
    assert bereken_cit_oezbekistan(500_000.0, 2025).effectief_tarief == pytest.approx(0.15)
    assert bereken_cit_oezbekistan(500_000.0, 2025, hoger_tarief_sector=True).effectief_tarief == pytest.approx(0.20)


# 8 — issue #39: needs verification + official source URL present
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert p["metadata"]["needs_verification"] is True
    urls = [s["url"] for s in p["sources"]]
    assert "https://soliq.uz/" in urls
