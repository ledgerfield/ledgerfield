"""Senegal tax property tests (incl. shared OHADA-base tests) — 13 tests."""
import json
import os

import pytest

from ledgerfield.schemas.SN import sn_gaap
from ledgerfield.schemas.SN.sn_gaap import SN_GAAP
from ledgerfield.tax._ohada.base import CITResultOHADA, OHADACITBase
from ledgerfield.tax.CI.cit import CoteDivoireCIT
from ledgerfield.tax.CM.cit import CameroonCIT
from ledgerfield.tax.SN.cit import SenegalCIT, bereken_cit_senegal

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/SN/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_sn_schema_min_60_accounts():
    assert len(SN_GAAP) >= 60


# 2 — schema documents the shared SYSCOHADA origin
def test_sn_schema_docstring_names_syscohada():
    assert "SYSCOHADA" in sn_gaap.__doc__


# 3 — CIT rate = 30% (CGI Sénégal)
def test_cit_rate_30pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.30)
    assert SenegalCIT.CIT_RATE == pytest.approx(0.30)


# 4 — 1,000,000 profit → 300,000 IS
def test_cit_on_one_million():
    result = bereken_cit_senegal(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(300_000.0)


# 5 — effectief tarief equals the flat rate for positive profit
def test_effectief_tarief_positive_profit():
    result = bereken_cit_senegal(2_500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.30)


# 6 — result carries land/jaar metadata from the shared dataclass
def test_result_metadata():
    result = bereken_cit_senegal(1_000_000.0, 2025)
    assert isinstance(result, CITResultOHADA)
    assert result.land == "SN"
    assert result.jaar == 2025


# 7 — minimum tax (IMF) hook: 0.5% of turnover
def test_minimum_tax_imf_half_percent():
    assert _params()["cit"]["minimum_tax"]["rate_on_turnover"] == pytest.approx(0.005)
    assert SenegalCIT.minimum_tax_op_omzet(10_000_000.0) == pytest.approx(50_000.0)
    assert SenegalCIT.minimum_tax_op_omzet(0.0) == pytest.approx(0.0)


# 8 — VAT (TVA) = 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)
    assert _params()["vat"]["implemented"] is True


# 9 — non-positive profit yields zero tax (shared base guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_senegal(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_senegal(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 10 — official source (DGID) referenced
def test_official_source_dgid():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.dgid.sn/" in urls


# ── Shared OHADA-base tests (the bloc's abstract class) ─────────────────────

# 11 — all three country classes subclass OHADACITBase
def test_all_three_subclass_ohada_base():
    for cls in (SenegalCIT, CoteDivoireCIT, CameroonCIT):
        assert issubclass(cls, OHADACITBase)


# 12 — zero/negative guard behaviour is shared via the base for all three
def test_shared_base_guard_all_three():
    for cls in (SenegalCIT, CoteDivoireCIT, CameroonCIT):
        for winst in (0.0, -1.0, -1_000_000.0):
            result = cls.bereken(winst, 2025)
            assert isinstance(result, CITResultOHADA)
            assert result.cit_totaal == pytest.approx(0.0)
            assert result.effectief_tarief == pytest.approx(0.0)
            assert result.land == cls.LAND


# 13 — bereken is defined once on the base, not re-implemented per country
def test_bereken_defined_on_base():
    for cls in (SenegalCIT, CoteDivoireCIT, CameroonCIT):
        assert "bereken" not in cls.__dict__
    assert "bereken" in OHADACITBase.__dict__
