"""South Africa tax property tests — 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.ZA.schema import ZA_GAAP
from ledgerfield.tax.ZA.cit import bereken_cit_south_africa

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/ZA/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_za_schema_min_60_accounts():
    assert len(ZA_GAAP) >= 60


# 2 — CIT rate = 27%
def test_cit_rate_27pct():
    assert _params()["cit"]["rate"] == pytest.approx(0.27)


# 3 — ZAR 1M at 27% = ZAR 270,000
def test_bereken_cit_south_africa_1m():
    result = bereken_cit_south_africa(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(270_000.0)


# 4 — VAT rate = 15%
def test_vat_rate_15pct():
    assert _params()["vat"]["rate"] == pytest.approx(0.15)


# 5 — Dividends tax = 20%
def test_dividends_tax_rate_20pct():
    assert _params()["dividends_tax"]["rate"] == pytest.approx(0.20)
