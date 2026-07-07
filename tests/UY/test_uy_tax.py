"""Oriental Republic of Uruguay tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.UY.uy_gaap import UY_GAAP
from ledgerfield.tax.UY.cit import bereken_cit_uruguay

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/UY/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_uy_schema_min_60_accounts():
    assert len(UY_GAAP) >= 60


# 2 — schema includes IVA accounts (compras + ventas)
def test_uy_schema_has_iva_accounts():
    names = [a.name for a in UY_GAAP]
    assert any("IVA Compras" in n for n in names)
    assert any("IVA Ventas" in n for n in names)


# 3 — IRAE rate = 25% flat (Título 4)
def test_irae_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)


# 4 — 1,000,000 UYU profit → 250,000 IRAE
def test_irae_on_one_million():
    result = bereken_cit_uruguay(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 5 — effectief tarief is exactly the flat 25%
def test_effectief_tarief_25pct():
    result = bereken_cit_uruguay(1_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.25)
    assert result.cit_rate == pytest.approx(0.25)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_uruguay(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_uruguay(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_uruguay(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — VAT (IVA) standard 22%, reduced (mínima) 10%
def test_iva_22pct_standard_10pct_reduced():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.22)
    assert vat["reduced_rate"] == pytest.approx(0.10)
    assert vat["implemented"] is True


# 8 — zona franca / software IRAE exemption is noted
def test_free_zone_exemption_noted():
    fz = _params()["free_zone"]
    assert fz["irae_rate"] == pytest.approx(0.0)
    assert "zona franca" in fz["note"].lower()
    assert "software" in fz["note"].lower()


# 9 — IMEBA agricultural alternative is noted
def test_imeba_alternative_noted():
    assert "IMEBA" in _params()["imeba"]["note"]


# 10 — IP net-wealth tax 1.5% is noted
def test_net_wealth_tax_1_5pct():
    assert _params()["net_wealth_tax"]["rate"] == pytest.approx(0.015)


# 11 — official source is DGI
def test_official_source_dgi():
    sources = _params()["metadata"]["official_sources"]
    assert any(
        s["url"].startswith("https://www.gub.uy/direccion-general-impositiva")
        for s in sources
    )


# 12 — params target 2025 range and result roundtrip
def test_effective_range_2025_and_roundtrip():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
    result = bereken_cit_uruguay(400_000.0, 2025)
    assert result.winst == pytest.approx(400_000.0)
    assert result.jaar == 2025
    assert result.cit_totaal == pytest.approx(100_000.0)
