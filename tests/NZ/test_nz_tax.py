"""New Zealand tax property tests — 5 tests."""
import json
import os

import pytest

from ledgerfield.schemas.NZ.schema import NZ_GAAP
from ledgerfield.tax.NZ.cit import bereken_cit_nz

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NZ/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_nz_schema_min_60_accounts():
    assert len(NZ_GAAP) >= 60


# 2 — CIT rate = 28%
def test_cit_rate_28pct():
    assert _params()["cit"]["rate"] == pytest.approx(0.28)


# 3 — GST rate = 15%
def test_gst_rate_15pct():
    assert _params()["gst"]["rate"] == pytest.approx(0.15)


# 4 — NZD 1M at 28% = NZD 280,000
def test_bereken_cit_nz_1m_at_28pct():
    result = bereken_cit_nz(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(280_000.0)


# 5 — zero profit returns zero CIT
def test_bereken_cit_nz_zero_winst():
    result = bereken_cit_nz(0.0, 2025)
    assert result.cit_totaal == pytest.approx(0.0)
