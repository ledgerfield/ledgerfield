"""Ireland tax property tests — 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.IE.schema import IE_GAAP
from ledgerfield.tax.IE.cit import bereken_cit_ireland

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/IE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ie_schema_min_60_accounts():
    assert len(IE_GAAP) >= 60


# 2 — trading CIT rate = 12.5%
def test_trading_cit_rate_12_5pct():
    assert _params()["cit"]["trading_rate"] == pytest.approx(0.125)


# 3 — EUR 1M at trading rate (12.5%) = EUR 125,000
def test_bereken_cit_ireland_1m_trading():
    result = bereken_cit_ireland(1_000_000.0, 2025, trading=True)
    assert result.cit_totaal == pytest.approx(125_000.0)


# 4 — VAT standard rate = 23%
def test_vat_standard_rate_23pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.23)


# 5 — zero profit returns zero CIT
def test_bereken_cit_ireland_zero_winst():
    result = bereken_cit_ireland(0.0, 2025, trading=True)
    assert result.cit_totaal == pytest.approx(0.0)
