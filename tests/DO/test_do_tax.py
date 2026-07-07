"""Dominican Republic tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.DO.do_gaap import DO_GAAP
from ledgerfield.tax.DO.cit import bereken_cit_dominicaanse

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/DO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_do_schema_min_60_accounts():
    assert len(DO_GAAP) >= 60


# 2 — CIT (ISR) rate = 27%
def test_cit_rate_27pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.27)


# 3 — 1,000,000 profit → 270,000 ISR
def test_cit_on_one_million():
    result = bereken_cit_dominicaanse(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(270_000.0)


# 4 — effectief tarief equals 27% on positive profit
def test_effectief_tarief_27pct():
    result = bereken_cit_dominicaanse(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.27)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_dominicaanse(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_dominicaanse(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — ITBIS standard rate = 18%
def test_itbis_standard_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)


# 7 — ITBIS reduced rate = 16%
def test_itbis_reduced_16pct():
    assert _params()["vat"]["reduced_rate"] == pytest.approx(0.16)


# 8 — 1% assets tax noted as alternative minimum
def test_assets_tax_alternative_minimum():
    amt = _params()["cit"]["assets_tax_alternative_minimum"]
    assert amt["rate"] == pytest.approx(0.01)
    assert "minimum" in amt["note"].lower()


# 9 — free-zone 0% regime noted
def test_free_zone_zero_rate_note():
    p = _params()["cit"]
    assert p["free_zone_rate"] == pytest.approx(0.0)
    assert "zona" in p["free_zone_note"].lower() or "free zone" in p["free_zone_note"].lower()


# 10 — official source is DGII
def test_official_source_dgii():
    sources = _params()["metadata"]["official_sources"]
    assert any("dgii.gov.do" in s["url"] for s in sources)
