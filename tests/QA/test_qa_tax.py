"""State of Qatar tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.QA.qa_gaap import QA_GAAP
from ledgerfield.tax.QA.cit import bereken_cit_qatar

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/QA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_qa_schema_min_60_accounts():
    assert len(QA_GAAP) >= 60


# 2 — CIT rate = 10%
def test_cit_rate_10pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.10)


# 3 — wholly foreign-owned: 10% on full profit
def test_wholly_foreign_owned_10pct():
    result = bereken_cit_qatar(1_000_000.0, 2025, foreign_ownership_share=1.0)
    assert result.cit_totaal == pytest.approx(100_000.0)


# 4 — wholly Qatari/GCC-owned: exempt
def test_wholly_qatari_owned_exempt():
    result = bereken_cit_qatar(1_000_000.0, 2025, foreign_ownership_share=0.0)
    assert result.cit_totaal == pytest.approx(0.0)


# 5 — 40% foreign ownership → 10% on that share
def test_partial_foreign_ownership():
    result = bereken_cit_qatar(1_000_000.0, 2025, foreign_ownership_share=0.4)
    assert result.cit_totaal == pytest.approx(40_000.0)


# 6 — VAT not implemented (rate 0, implemented flag False)
def test_vat_not_implemented():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.0)
    assert _params()["vat"]["implemented"] is False


# 7 — no personal income tax
def test_no_personal_income_tax():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.0)


# 8 — WHT on non-resident payments = 5%
def test_wht_5pct():
    assert _params()["wht"]["non_resident_services_and_royalties"] == pytest.approx(0.05)


# 9 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_qatar(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_qatar(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 10 — invalid ownership share is rejected
def test_invalid_ownership_share_raises():
    with pytest.raises(ValueError):
        bereken_cit_qatar(1_000_000.0, 2025, foreign_ownership_share=-0.2)
