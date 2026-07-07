"""Republic of Guatemala tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.GT.gt_gaap import GT_GAAP
from ledgerfield.tax.GT.cit import bereken_cit_guatemala

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/GT/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_gt_schema_min_60_accounts():
    assert len(GT_GAAP) >= 60


# 2 — profits regime CIT rate = 25%
def test_cit_profits_rate_25pct():
    assert _params()["cit"]["profits_regime"]["standard_rate"] == pytest.approx(0.25)


# 3 — profits regime: 1,000,000 → 250,000
def test_profits_regime_1m():
    result = bereken_cit_guatemala(1_000_000.0, 2025, regime="profits")
    assert result.cit_totaal == pytest.approx(250_000.0)


# 4 — effective rate equals 25% for positive profit
def test_effectief_tarief_25pct():
    result = bereken_cit_guatemala(400_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.25)


# 5 — simplified regime raises ValueError with the documented reason
#     (it is levied on gross revenue, a different base than net profit)
def test_simplified_regime_raises_gross_revenue_base():
    with pytest.raises(ValueError, match="gross revenue"):
        bereken_cit_guatemala(1_000_000.0, 2025, regime="simplified")


# 6 — any other unknown regime is also rejected
def test_unknown_regime_raises():
    with pytest.raises(ValueError):
        bereken_cit_guatemala(1_000_000.0, 2025, regime="flat")


# 7 — simplified regime documented in params: 5% / 7% on gross revenue,
#     GTQ 30,000 monthly threshold
def test_simplified_regime_documented_in_params():
    simplified = _params()["cit"]["simplified_optional_regime"]
    assert simplified["rate_lower"] == pytest.approx(0.05)
    assert simplified["rate_upper"] == pytest.approx(0.07)
    assert simplified["monthly_threshold_gtq"] == 30000
    assert "GROSS REVENUE" in simplified["basis"]


# 8 — ISO solidarity minimum tax note present (~1%, creditable)
def test_iso_solidarity_note_present():
    note = _params()["cit"]["profits_regime"]["iso_solidarity_note"]
    assert "ISO" in note
    assert "1%" in note


# 9 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_guatemala(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_guatemala(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_guatemala(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 10 — VAT (IVA) = 12%
def test_vat_12pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.12)


# 11 — official SAT source URL and 2025 range in params
def test_source_and_range():
    meta = _params()["metadata"]
    assert meta["official_sources"][0]["url"] == "https://portal.sat.gob.gt/"
    assert meta["effective_date_range"]["start"] == "2025-01-01"
    assert meta["effective_date_range"]["end"] == "2025-12-31"
