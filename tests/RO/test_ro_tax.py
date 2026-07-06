"""Romania tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.RO.ro_gaap import RO_GAAP
from ledgerfield.tax.RO.cit import bereken_cit_roemenie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/RO/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage, including TVA accounts
def test_ro_schema_min_60_accounts_with_tva():
    assert len(RO_GAAP) >= 60
    tva_accounts = [a for a in RO_GAAP if "TVA" in a.name]
    assert len(tva_accounts) >= 2


# 2 — CIT rate = 16%
def test_cit_rate_16pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.16)


# 3 — 1,000,000 profit → 160,000 tax
def test_cit_one_million():
    result = bereken_cit_roemenie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(160_000.0)


# 4 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_roemenie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_roemenie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 5 — VAT 19% standard with 21% mid-year change field (from 1 Aug 2025)
def test_vat_19pct_and_aug_2025_21pct():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.19)
    assert vat["rate_from_2025_08_01"] == pytest.approx(0.21)


# 6 — micro-enterprise regime documented (1%/3% of turnover, EUR 250k threshold)
def test_micro_enterprise_regime_note():
    micro = _params()["cit"]["micro_enterprise_regime"]
    assert micro["rate_low"] == pytest.approx(0.01)
    assert micro["rate_high"] == pytest.approx(0.03)
    assert micro["revenue_threshold_eur_2025"] == 250000
    assert "turnover" in micro["note"].lower()


# 7 — IMCA minimum turnover tax documented (1% above EUR 50m turnover)
def test_imca_minimum_turnover_tax_note():
    imca = _params()["cit"]["minimum_turnover_tax"]
    assert imca["rate"] == pytest.approx(0.01)
    assert imca["turnover_threshold_eur"] == 50000000


# 8 — OSS eligible (EU member state)
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 9 — dividend tax = 10% (raised from 8% in 2025)
def test_dividend_tax_10pct():
    assert _params()["dividend_tax"]["rate"] == pytest.approx(0.10)


# 10 — official source URL points to ANAF
def test_source_url_anaf():
    sources = _params()["metadata"]["official_sources"]
    assert any("anaf.ro" in s["url"] for s in sources)


# 11 — effective rate equals flat 16% for positive profit
def test_effectief_tarief():
    result = bereken_cit_roemenie(500_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.16)
    assert result.cit_rate == pytest.approx(0.16)
