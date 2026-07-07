"""Cameroon tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CM import cm_gaap
from ledgerfield.schemas.CM.cm_gaap import CM_GAAP
from ledgerfield.tax._ohada.base import OHADACITBase
from ledgerfield.tax.CM.cit import CameroonCIT, CITResultCM, bereken_cit_kameroen

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CM/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_cm_schema_min_60_accounts():
    assert len(CM_GAAP) >= 60


# 2 — schema documents the shared SYSCOHADA origin
def test_cm_schema_docstring_names_syscohada():
    assert "SYSCOHADA" in cm_gaap.__doc__


# 3 — effective CIT rate = 33% incl. CAC
def test_cit_rate_33pct_effective():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.33)
    assert CameroonCIT.CIT_RATE == pytest.approx(0.33)


# 4 — 33% decomposes as 30% principal + 10% CAC on the tax
def test_cit_decomposition_30_plus_10_cac():
    decomp = _params()["cit"]["decomposition"]
    assert decomp["principal_rate"] == pytest.approx(0.30)
    assert decomp["cac_rate_on_tax"] == pytest.approx(0.10)
    assert CameroonCIT.PRINCIPAL_RATE * (1 + CameroonCIT.CAC_RATE) == pytest.approx(
        CameroonCIT.CIT_RATE
    )


# 5 — 1,000,000 profit → 330,000 total (300,000 principal + 30,000 CAC)
def test_cit_on_one_million_with_cac():
    result = bereken_cit_kameroen(1_000_000.0, 2025)
    assert isinstance(result, CITResultCM)
    assert result.cit_totaal == pytest.approx(330_000.0)
    assert result.cit_principal == pytest.approx(300_000.0)
    assert result.cac_bedrag == pytest.approx(30_000.0)
    assert result.cit_principal + result.cac_bedrag == pytest.approx(result.cit_totaal)


# 6 — effectief tarief = 33% for positive profit
def test_effectief_tarief_positive_profit():
    result = bereken_cit_kameroen(5_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.33)


# 7 — subclass of the shared OHADA base; land code carried on the result
def test_subclass_and_land():
    assert issubclass(CameroonCIT, OHADACITBase)
    assert bereken_cit_kameroen(1_000_000.0, 2025).land == "CM"


# 8 — reduced regimes noted: 27.5% incl. CAC (25% principal), turnover band
def test_reduced_regimes_note():
    reduced = _params()["cit"]["reduced_regimes"]
    assert reduced["turnover_up_to_xaf_3bn_rate_incl_cac"] == pytest.approx(0.275)
    assert reduced["turnover_up_to_xaf_3bn_principal_rate"] == pytest.approx(0.25)


# 9 — VAT = 19.25% = 17.5% + 10% CAC (documented decomposition)
def test_vat_19_25pct_with_cac_decomposition():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.1925)
    assert vat["decomposition"]["principal_rate"] == pytest.approx(0.175)
    assert vat["decomposition"]["cac_rate_on_tax"] == pytest.approx(0.10)
    assert 0.175 * 1.10 == pytest.approx(0.1925)


# 10 — non-positive profit yields zero tax and zero CAC (shared base guard)
def test_non_positive_profit_zero_tax():
    for winst in (0.0, -100_000.0):
        result = bereken_cit_kameroen(winst, 2025)
        assert result.cit_totaal == pytest.approx(0.0)
        assert result.cit_principal == pytest.approx(0.0)
        assert result.cac_bedrag == pytest.approx(0.0)


# 11 — minimum tax on turnover (minimum de perception, 2.2% incl. CAC)
def test_minimum_tax_2_2pct():
    assert _params()["cit"]["minimum_tax"]["rate_on_turnover_incl_cac"] == pytest.approx(0.022)
    assert CameroonCIT.minimum_tax_op_omzet(10_000_000.0) == pytest.approx(220_000.0)


# 12 — official source (DGI Cameroun) referenced
def test_official_source_dgi_cm():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.impots.cm/" in urls
