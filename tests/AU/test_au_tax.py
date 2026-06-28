"""Australia tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.AU.au_gaap import AU_GAAP
from ledgerfield.tax.AU.cit import bereken_cit_australia

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/AU/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_au_schema_min_60_accounts():
    assert len(AU_GAAP) >= 60


# 2 — base rate entity CIT rate = 25%
def test_base_rate_entity_rate_25pct():
    assert _params()["cit"]["base_rate_entity_rate"] == pytest.approx(0.25)


# 3 — large company general rate = 30%
def test_general_rate_30pct():
    assert _params()["cit"]["general_rate"] == pytest.approx(0.30)


# 4 — AUD 1M at base rate (25%) = AUD 250,000
def test_bereken_cit_australia_1m_at_25pct():
    result = bereken_cit_australia(1_000_000.0, 2025, base_rate_entity=True)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 5 — GST rate = 10%
def test_gst_rate_10pct():
    assert _params()["gst"]["rate"] == pytest.approx(0.10)


# 6 — Superannuation guarantee from 1 July 2025 = 12%
def test_superannuation_rate_from_1_jul_2025_12pct():
    assert _params()["superannuation"]["employer_rate_from_1_jul_2025"] == pytest.approx(0.12)


# 7 — Medicare levy = 2%
def test_medicare_levy_2pct():
    assert _params()["medicare_levy"]["rate"] == pytest.approx(0.02)


# 8 — AUD 1M at general rate (30%) = AUD 300,000
def test_bereken_cit_australia_1m_large_at_30pct():
    result = bereken_cit_australia(1_000_000.0, 2025, base_rate_entity=False)
    assert result.cit_totaal == pytest.approx(300_000.0)


# 9 — zero profit returns zero CIT
def test_bereken_cit_australia_zero_winst():
    result = bereken_cit_australia(0.0, 2025, base_rate_entity=True)
    assert result.cit_totaal == pytest.approx(0.0)


# 10 — effective rate equals the applicable CIT rate for positive income
def test_effectief_tarief_equals_cit_rate():
    result = bereken_cit_australia(500_000.0, 2025, base_rate_entity=True)
    assert result.effectief_tarief == pytest.approx(result.cit_rate)
