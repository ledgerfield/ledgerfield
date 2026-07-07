"""Costa Rica tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CR.cr_gaap import CR_GAAP
from ledgerfield.tax.CR.cit import bereken_cit_costarica

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CR/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_cr_schema_min_60_accounts():
    assert len(CR_GAAP) >= 60


# 2 — standard CIT rate = 30%
def test_cit_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)


# 3 — standard regime: flat 30% on 1,000,000 → 300,000
def test_standard_flat_30pct():
    result = bereken_cit_costarica(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)
    assert result.effectief_tarief == pytest.approx(0.30)


# 4 — SME regime, multi-slice: winst 10,000,000 across documented 2025 slices
#     5% × 5,761,000 + 10% × 2,882,000 + 15% × 1,357,000 = 779,800
def test_sme_bracket_math_multi_slice():
    result = bereken_cit_costarica(10_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(779_800.0)


# 5 — SME regime, first slice only: 4,000,000 at 5% → 200,000
def test_sme_first_slice_5pct():
    result = bereken_cit_costarica(4_000_000.0, 2025, sme=True)
    assert result.cit_totaal == pytest.approx(200_000.0)


# 6 — SME gross-income ceiling documented as CRC 122,145,000 (2025)
def test_sme_gross_income_ceiling():
    ceiling = _params()["cit"]["sme_regime"]["gross_income_ceiling_crc"]
    assert ceiling == 122_145_000


# 7 — VAT (IVA) = 13%
def test_vat_13pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.13)
    assert _params()["vat"]["implemented"] is True


# 8 — territorial system documented
def test_territorial_system_note():
    territorial = _params()["territorial_system"]
    assert territorial["applies"] is True
    assert "territorial" in territorial["note"].lower()


# 9 — official source URL (Ministerio de Hacienda)
def test_official_source_url():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.hacienda.go.cr/" in urls


# 10 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_costarica(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_costarica(-50_000.0, 2025, sme=True).cit_totaal == pytest.approx(0.0)


# 11 — effective date range covers 2025
def test_effective_date_range_2025():
    date_range = _params()["metadata"]["effective_date_range"]
    assert date_range["start"] == "2025-01-01"
    assert date_range["end"] == "2025-12-31"
