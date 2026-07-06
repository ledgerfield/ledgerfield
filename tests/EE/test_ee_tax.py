"""Republic of Estonia tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.EE.ee_gaap import EE_GAAP
from ledgerfield.tax.EE.cit import bereken_cit_estland

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/EE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. käibemaks/VAT accounts)
def test_ee_schema_min_60_accounts():
    assert len(EE_GAAP) >= 60


# 2 — schema contains käibemaks/VAT accounts
def test_ee_schema_has_vat_accounts():
    names = " | ".join(a.name for a in EE_GAAP).lower()
    assert "käibemaks" in names
    assert "vat" in names


# 3 — Estonian-model core: retained/reinvested profit → 0 tax
def test_retained_profit_zero_tax():
    result = bereken_cit_estland(1_000_000.0, 2025, ingehouden=True)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.effectief_tarief == pytest.approx(0.0)
    assert _params()["cit"]["retained_profit_rate"] == pytest.approx(0.0)


# 4 — net distribution 780,000 → tax 220,000 (22/78 of net)
def test_distribution_780k_net():
    result = bereken_cit_estland(780_000.0, 2025)
    assert result.cit_totaal == pytest.approx(220_000.0)


# 5 — net distribution 78,000 → tax 22,000
def test_distribution_78k_net():
    result = bereken_cit_estland(78_000.0, 2025)
    assert result.cit_totaal == pytest.approx(22_000.0)


# 6 — effective rate on the net distribution ≈ 28.2% (22/78)
def test_effective_rate_on_net_22_78():
    result = bereken_cit_estland(100_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(22.0 / 78.0)
    assert result.effectief_tarief == pytest.approx(0.282, abs=0.001)


# 7 — zero / negative distribution → 0 tax (defensive guard)
def test_non_positive_distribution_zero_tax():
    assert bereken_cit_estland(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_estland(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 8 — VAT standard 22% in H1 2025, 24% from 1 July 2025
def test_vat_rates_2025():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.22)
    assert vat["rate_from_2025_07_01"] == pytest.approx(0.24)


# 9 — 2026 security-tax note: rate becomes 24/76
def test_2026_rate_note_present():
    note = _params()["cit"]["note_2026"]
    assert "24/76" in note
    assert "2026" in note


# 10 — OSS eligibility flag (EU One-Stop-Shop)
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 11 — official source is EMTA
def test_source_url_emta():
    urls = [s["url"] for s in _params()["metadata"]["official_sources"]]
    assert "https://www.emta.ee/" in urls


# 12 — gross-up documented and consistent: net 78 → gross 100 at 22% gross
def test_gross_up_documented():
    cit = _params()["cit"]
    assert cit["distribution_rate_fraction"] == "22/78"
    assert cit["distribution_rate_net"] == pytest.approx(22.0 / 78.0)
    assert cit["distribution_rate_gross"] == pytest.approx(0.22)
    # net + tax = gross; tax is 22% of the gross
    result = bereken_cit_estland(78_000.0, 2025)
    bruto = result.distributie_netto + result.cit_totaal
    assert result.cit_totaal == pytest.approx(0.22 * bruto)
