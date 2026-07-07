"""Papua New Guinea tax property tests — 9 tests."""
import json
import os

import pytest

from ledgerfield.schemas.PG.pg_gaap import PG_GAAP
from ledgerfield.tax.PG.cit import bereken_cit_png

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_pg_schema_min_60_accounts():
    assert len(PG_GAAP) >= 60


# 2 — resident CIT: 30% on 1,000,000 → 300,000
def test_resident_cit_30pct():
    result = bereken_cit_png(1_000_000.0, 2025)
    assert result.cit_rate == pytest.approx(0.30)
    assert result.cit_totaal == pytest.approx(300_000.0)


# 3 — non-resident CIT: 48% on 1,000,000 → 480,000
def test_non_resident_cit_48pct():
    result = bereken_cit_png(1_000_000.0, 2025, non_resident=True)
    assert result.cit_rate == pytest.approx(0.48)
    assert result.cit_totaal == pytest.approx(480_000.0)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_png(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_png(-75_000.0, 2025, non_resident=True).cit_totaal == pytest.approx(0.0)


# 5 — GST is 10%
def test_gst_10pct():
    assert _params()["gst"]["standard_rate"] == pytest.approx(0.10)


# 6 — issue #39: needs_verification flag + source URL present
def test_needs_verification_and_source():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    assert "https://irc.gov.pg/" in p["sources"]


# 7 — effective rate equals statutory rate on positive profit
def test_effectief_tarief():
    assert bereken_cit_png(500_000.0, 2025).effectief_tarief == pytest.approx(0.30)
    assert bereken_cit_png(500_000.0, 2025, non_resident=True).effectief_tarief == pytest.approx(0.48)


# 8 — mining/petroleum resource-sector regime noted
def test_mining_petroleum_note_present():
    assert "mining_and_petroleum" in _params()["cit"]["special_rates"]


# 9 — all account codes are unique
def test_account_codes_unique():
    codes = [a.code for a in PG_GAAP]
    assert len(codes) == len(set(codes))
