"""Republic of Paraguay tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.PY.py_gaap import PY_GAAP
from ledgerfield.tax.PY.cit import bereken_cit_paraguay

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/PY/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_py_schema_min_60_accounts():
    assert len(PY_GAAP) >= 60


# 2 — schema includes IVA accounts (crédito + débito fiscal)
def test_py_schema_has_iva_accounts():
    names = [a.name for a in PY_GAAP]
    assert any("IVA Crédito Fiscal" in n for n in names)
    assert any("IVA Débito Fiscal" in n for n in names)


# 3 — IRE rate = 10% flat (Ley 6380/2019)
def test_ire_rate_10pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.10)


# 4 — 1,000,000 PYG profit → 100,000 IRE; lowest corporate rate in South America
def test_ire_on_one_million():
    result = bereken_cit_paraguay(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(100_000.0)
    # Documented notable: PY has the lowest corporate income tax rate in SA.
    assert "lowest corporate income tax rate in South America" in _params()["cit"]["basis"]


# 5 — effectief tarief is exactly the flat 10%
def test_effectief_tarief_10pct():
    result = bereken_cit_paraguay(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.10)
    assert result.cit_rate == pytest.approx(0.10)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_paraguay(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_paraguay(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_paraguay(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — VAT (IVA) standard 10%, reduced 5%
def test_iva_10pct_standard_5pct_reduced():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.10)
    assert vat["reduced_rate"] == pytest.approx(0.05)
    assert vat["implemented"] is True


# 8 — IDU dividend tax 8% resident / 15% non-resident
def test_idu_dividend_rates():
    idu = _params()["idu"]
    assert idu["resident_rate"] == pytest.approx(0.08)
    assert idu["non_resident_rate"] == pytest.approx(0.15)


# 9 — SIMPLE / RESIMPLE small-business regimes are noted
def test_simple_resimple_regimes_noted():
    note = _params()["small_business_regimes"]["note"]
    assert "SIMPLE" in note
    assert "RESIMPLE" in note


# 10 — official source is DNIT
def test_official_source_dnit():
    sources = _params()["metadata"]["official_sources"]
    assert any(s["url"].startswith("https://www.dnit.gov.py") for s in sources)


# 11 — params target 2025 range
def test_effective_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"


# 12 — result dataclass carries winst/jaar through
def test_result_roundtrip_fields():
    result = bereken_cit_paraguay(250_000.0, 2025)
    assert result.winst == pytest.approx(250_000.0)
    assert result.jaar == 2025
    assert result.cit_totaal == pytest.approx(25_000.0)
