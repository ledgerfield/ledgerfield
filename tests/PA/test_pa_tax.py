"""Panama tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.PA.pa_gaap import PA_GAAP
from ledgerfield.tax.PA.cit import bereken_cit_panama

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_pa_schema_min_60_accounts():
    assert len(PA_GAAP) >= 60


# 2 — standard CIT rate = 25%
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 3 — flat 25% on 1,000,000 (no bruto) → 250,000, no CAIR
def test_standard_flat_25pct():
    result = bereken_cit_panama(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)
    assert result.cair_toegepast is False


# 4 — CAIR: winst 100,000, bruto 10,000,000 → 4.67% × 10M = 467,000 > 25,000
def test_cair_applies_when_greater():
    result = bereken_cit_panama(100_000.0, 2025, bruto_inkomen=10_000_000.0)
    assert result.cair_toegepast is True
    assert result.cit_totaal == pytest.approx(467_000.0)


# 5 — CAIR not applied when 25% of net is greater:
#     winst 1,000,000, bruto 2,000,000 → 93,400 < 250,000
def test_cair_not_applied_when_regular_greater():
    result = bereken_cit_panama(1_000_000.0, 2025, bruto_inkomen=2_000_000.0)
    assert result.cair_toegepast is False
    assert result.cit_totaal == pytest.approx(250_000.0)


# 6 — CAIR only above the USD 1.5m gross-income threshold
def test_cair_below_threshold_not_applied():
    result = bereken_cit_panama(100_000.0, 2025, bruto_inkomen=1_000_000.0)
    assert result.cair_toegepast is False
    assert result.cit_totaal == pytest.approx(25_000.0)
    assert _params()["cit"]["cair"]["gross_income_threshold_usd"] == 1_500_000


# 7 — VAT (ITBMS) = 7%
def test_vat_7pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.07)
    assert _params()["vat"]["implemented"] is True


# 8 — territorial system documented
def test_territorial_system_note():
    territorial = _params()["territorial_system"]
    assert territorial["applies"] is True
    assert "territorial" in territorial["note"].lower()


# 9 — free zones documented
def test_free_zones_note():
    assert "free" in _params()["free_zones"]["note"].lower()


# 10 — official source URL (DGI)
def test_official_source_url():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://dgi.mef.gob.pa/" in urls


# 11 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_panama(0.0, 2025).cit_totaal == pytest.approx(0.0)
    result = bereken_cit_panama(-50_000.0, 2025, bruto_inkomen=10_000_000.0)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.cair_toegepast is False
