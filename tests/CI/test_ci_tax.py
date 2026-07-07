"""Côte d'Ivoire tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CI import ci_gaap
from ledgerfield.schemas.CI.ci_gaap import CI_GAAP
from ledgerfield.tax._ohada.base import OHADACITBase
from ledgerfield.tax.CI.cit import CoteDivoireCIT, bereken_cit_ivoorkust

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CI/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ci_schema_min_60_accounts():
    assert len(CI_GAAP) >= 60


# 2 — schema documents the shared SYSCOHADA origin
def test_ci_schema_docstring_names_syscohada():
    assert "SYSCOHADA" in ci_gaap.__doc__


# 3 — CIT rate = 25% (CGI CI)
def test_cit_rate_25pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.25)
    assert CoteDivoireCIT.CIT_RATE == pytest.approx(0.25)


# 4 — 1,000,000 profit → 250,000 BIC
def test_cit_on_one_million():
    result = bereken_cit_ivoorkust(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(250_000.0)


# 5 — effectief tarief equals the flat rate for positive profit
def test_effectief_tarief_positive_profit():
    result = bereken_cit_ivoorkust(4_000_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.25)


# 6 — subclass of the shared OHADA base; land code carried on the result
def test_subclass_and_land():
    assert issubclass(CoteDivoireCIT, OHADACITBase)
    assert bereken_cit_ivoorkust(1_000_000.0, 2025).land == "CI"


# 7 — minimum tax (IMF) hook: 0.5% of turnover, bounds noted
def test_minimum_tax_imf_half_percent():
    assert _params()["cit"]["minimum_tax"]["rate_on_turnover"] == pytest.approx(0.005)
    assert CoteDivoireCIT.minimum_tax_op_omzet(20_000_000.0) == pytest.approx(100_000.0)
    assert "floor" in _params()["cit"]["minimum_tax"]["note"].lower()


# 8 — telecom sector rate = 30% (note)
def test_telecom_rate_30pct():
    assert _params()["cit"]["special_rates"]["telecom_it_communication"] == pytest.approx(0.30)
    assert CoteDivoireCIT.TELECOM_RATE == pytest.approx(0.30)


# 9 — VAT (TVA) = 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)
    assert _params()["vat"]["implemented"] is True


# 10 — non-positive profit yields zero tax (shared base guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_ivoorkust(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_ivoorkust(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 11 — official source (DGI) referenced
def test_official_source_dgi():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.dgi.gouv.ci/" in urls
