"""Kingdom of Saudi Arabia tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.SA.sa_gaap import SA_GAAP
from ledgerfield.tax.SA.cit import bereken_cit_saudi

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/SA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_sa_schema_min_60_accounts():
    assert len(SA_GAAP) >= 60


# 2 — CIT rate = 20%
def test_cit_rate_20pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.20)


# 3 — Zakat rate = 2.5%
def test_zakat_rate_2_5pct():
    assert _params()["cit"]["zakat_rate"] == pytest.approx(0.025)


# 4 — wholly foreign-owned: CIT only, 20%, no Zakat
def test_wholly_foreign_owned_cit_only():
    result = bereken_cit_saudi(1_000_000.0, 2025, foreign_ownership_share=1.0)
    assert result.cit_totaal == pytest.approx(200_000.0)
    assert result.zakat_totaal == pytest.approx(0.0)


# 5 — wholly Saudi/GCC-owned: Zakat only, 2.5%, no CIT
def test_wholly_saudi_owned_zakat_only():
    result = bereken_cit_saudi(1_000_000.0, 2025, foreign_ownership_share=0.0)
    assert result.zakat_totaal == pytest.approx(25_000.0)
    assert result.cit_totaal == pytest.approx(0.0)


# 6 — 50/50 mixed ownership blends both levies
def test_mixed_ownership_blend():
    result = bereken_cit_saudi(1_000_000.0, 2025, foreign_ownership_share=0.5)
    assert result.cit_totaal == pytest.approx(100_000.0)
    assert result.zakat_totaal == pytest.approx(12_500.0)
    assert result.heffing_totaal == pytest.approx(112_500.0)


# 7 — VAT standard rate = 15%
def test_vat_rate_15pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.15)


# 8 — no personal income tax
def test_no_personal_income_tax():
    assert _params()["personal_income_tax"]["rate"] == pytest.approx(0.0)


# 9 — non-positive profit yields zero levies (defensive guard)
def test_non_positive_profit_zero_levies():
    r0 = bereken_cit_saudi(0.0, 2025, foreign_ownership_share=1.0)
    rneg = bereken_cit_saudi(-100_000.0, 2025, foreign_ownership_share=0.0)
    assert r0.heffing_totaal == pytest.approx(0.0)
    assert rneg.heffing_totaal == pytest.approx(0.0)


# 10 — invalid ownership share is rejected
def test_invalid_ownership_share_raises():
    with pytest.raises(ValueError):
        bereken_cit_saudi(1_000_000.0, 2025, foreign_ownership_share=1.5)
