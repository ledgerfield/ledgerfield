"""State of Kuwait tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.KW.kw_gaap import KW_GAAP
from ledgerfield.tax.KW.cit import bereken_cit_koeweit

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/KW/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_kw_schema_min_60_accounts():
    assert len(KW_GAAP) >= 60


# 2 — CIT rate = 15%
def test_cit_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — wholly foreign-owned: 15% on full profit
def test_wholly_foreign_owned_15pct():
    result = bereken_cit_koeweit(1_000_000.0, 2025, foreign_ownership_share=1.0)
    assert result.cit_totaal == pytest.approx(150_000.0)


# 4 — wholly Kuwaiti/GCC-owned: exempt (zero CIT)
def test_wholly_kuwaiti_owned_exempt():
    result = bereken_cit_koeweit(1_000_000.0, 2025, foreign_ownership_share=0.0)
    assert result.cit_totaal == pytest.approx(0.0)


# 5 — 40% foreign ownership → 15% on that share (pro-rata)
def test_partial_foreign_ownership():
    result = bereken_cit_koeweit(1_000_000.0, 2025, foreign_ownership_share=0.4)
    assert result.cit_totaal == pytest.approx(60_000.0)


# 6 — VAT not implemented (rate 0, implemented flag False)
def test_vat_not_implemented():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.0)
    assert _params()["vat"]["implemented"] is False


# 7 — no personal income tax
def test_no_personal_income_tax():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.0)


# 8 — no general WHT; 5% contract-payment retention until tax clearance
def test_wht_retention_5pct():
    assert _params()["wht"]["general_rate"] == pytest.approx(0.0)
    assert _params()["wht"]["contract_payment_retention"] == pytest.approx(0.05)


# 9 — non-positive profit yields zero tax and zero effective rate
def test_non_positive_profit_zero_tax():
    assert bereken_cit_koeweit(0.0, 2025).cit_totaal == pytest.approx(0.0)
    verlies = bereken_cit_koeweit(-25_000.0, 2025)
    assert verlies.cit_totaal == pytest.approx(0.0)
    assert verlies.effectief_tarief == pytest.approx(0.0)


# 10 — invalid ownership share is rejected
def test_invalid_ownership_share_raises():
    with pytest.raises(ValueError):
        bereken_cit_koeweit(1_000_000.0, 2025, foreign_ownership_share=-0.2)
    with pytest.raises(ValueError):
        bereken_cit_koeweit(1_000_000.0, 2025, foreign_ownership_share=1.2)


# 11 — official source referenced and effective-rate consistency
def test_official_source_and_effective_rate_consistency():
    sources = _params()["metadata"]["official_sources"]
    assert any("mof.gov.kw" in s["url"] for s in sources)
    result = bereken_cit_koeweit(800_000.0, 2025, foreign_ownership_share=0.6)
    assert result.effectief_tarief == pytest.approx(result.cit_totaal / result.winst)
    assert result.effectief_tarief == pytest.approx(0.6 * 0.15)
