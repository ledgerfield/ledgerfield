"""Japan tax tests — 法人税/所得税/消費税 2024-2025. 12 tests."""
import json
import os

import pytest

from ledgerfield.tax.JP.cit import bereken_cit_japan, CITResult
from ledgerfield.schemas.JP.jgaap import JGAAP_JP, get_account, accounts_by_class

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/JP/params.json",
)


def _params(jaar):
    return json.load(open(PARAMS_PATH))["years"][str(jaar)]


# ── params.json structure ─────────────────────────────────────────────────────

def test_params_2025_cit_sme_rate():
    assert _params(2025)["CIT"]["sme_rate"] == pytest.approx(0.19)


def test_params_2025_cit_standard_rate():
    assert _params(2025)["CIT"]["standard_rate"] == pytest.approx(0.232)


def test_params_2025_consumption_standard():
    assert _params(2025)["consumption_tax"]["standard_rate"] == pytest.approx(0.10)


def test_params_2025_consumption_reduced():
    assert _params(2025)["consumption_tax"]["reduced_rate"] == pytest.approx(0.08)


def test_params_2025_iit_brackets_count():
    assert len(_params(2025)["IIT"]["brackets"]) == 7


# ── bereken_cit_japan ─────────────────────────────────────────────────────────

def test_cit_sme_below_threshold():
    """SME, income ≤ ¥8M → all taxed at 19%."""
    r = bereken_cit_japan(5_000_000, jaar=2025, capital=10_000_000)
    assert r.is_sme is True
    assert r.cit_tier1 == pytest.approx(5_000_000 * 0.19)
    assert r.cit_tier2 == pytest.approx(0.0)


def test_cit_sme_above_threshold():
    """SME, income > ¥8M → split rates."""
    r = bereken_cit_japan(12_000_000, jaar=2025, capital=10_000_000)
    assert r.cit_tier1 == pytest.approx(8_000_000 * 0.19)
    assert r.cit_tier2 == pytest.approx(4_000_000 * 0.232)


def test_cit_large_company():
    """Large company → flat 23.2%."""
    r = bereken_cit_japan(20_000_000, jaar=2025, capital=200_000_000)
    assert r.is_sme is False
    assert r.cit_tier1 == pytest.approx(0.0)
    assert r.cit_national == pytest.approx(20_000_000 * 0.232)


def test_cit_local_tax_estimate():
    """Local tax estimate ~10.7% of national tax."""
    r = bereken_cit_japan(10_000_000, jaar=2025)
    assert r.local_tax_estimate == pytest.approx(r.cit_national * 0.107)


def test_cit_zero_income():
    r = bereken_cit_japan(0, jaar=2025)
    assert r.cit_total == pytest.approx(0.0)
    assert r.effective_rate == pytest.approx(0.0)


@pytest.mark.parametrize(
    "capital,expected_is_sme",
    [(10_000_000, True), (200_000_000, False)],
)
def test_cit_negative_income_returns_zero_tax(capital, expected_is_sme):
    r = bereken_cit_japan(-1_000_000, jaar=2025, capital=capital)
    assert r.taxable_income == pytest.approx(-1_000_000.0)
    assert r.is_sme is expected_is_sme
    assert r.cit_tier1 == pytest.approx(0.0)
    assert r.cit_tier2 == pytest.approx(0.0)
    assert r.cit_national == pytest.approx(0.0)
    assert r.local_tax_estimate == pytest.approx(0.0)
    assert r.cit_total == pytest.approx(0.0)
    assert r.effective_rate == pytest.approx(0.0)


# ── J-GAAP schema ─────────────────────────────────────────────────────────────

def test_jgaap_account_count():
    assert len(JGAAP_JP) >= 70


def test_jgaap_get_account():
    acc = get_account("1010")
    assert acc.name_ja == "現金"
    assert acc.name_en == "Cash"


def test_jgaap_accounts_by_class():
    assets = accounts_by_class("流動資産")
    assert len(assets) >= 10
    assert all(a.is_asset for a in assets)
