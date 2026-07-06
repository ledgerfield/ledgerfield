"""Republic of Malta tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.MT.mt_gaap import MT_GAAP
from ledgerfield.tax.MT.cit import bereken_cit_malta

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/MT/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_mt_schema_min_60_accounts():
    assert len(MT_GAAP) >= 60


# 2 — statutory CIT rate = 35%
def test_cit_rate_35pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.35)


# 3 — EUR 1,000,000 → 35% → EUR 350,000 company-level
def test_company_level_1m():
    result = bereken_cit_malta(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(350_000.0)
    assert result.effectief_tarief == pytest.approx(0.35)


# 4 — no refund requested → refund fields stay None
def test_no_refund_fields_none():
    result = bereken_cit_malta(1_000_000.0, 2025)
    assert result.refund_bedrag is None
    assert result.effectieve_druk is None


# 5 — 6/7 refund: EUR 1,000,000 → refund EUR 300,000
def test_refund_6_7_amount():
    result = bereken_cit_malta(1_000_000.0, 2025, refund_6_7=True)
    assert result.cit_totaal == pytest.approx(350_000.0)
    assert result.refund_bedrag == pytest.approx(300_000.0)


# 6 — 6/7 refund: effective burden = 5%
def test_refund_6_7_effective_rate_5pct():
    result = bereken_cit_malta(1_000_000.0, 2025, refund_6_7=True)
    assert result.effectieve_druk == pytest.approx(0.05)


# 7 — refund is documented as shareholder-level
def test_refund_is_shareholder_level():
    result = bereken_cit_malta(1_000_000.0, 2025, refund_6_7=True)
    assert "shareholder-level" in result.note
    assert "shareholder-level" in _params()["cit"]["imputation_refund"]["note"]


# 8 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_malta(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_malta(-75_000.0, 2025).cit_totaal == pytest.approx(0.0)
    result = bereken_cit_malta(-75_000.0, 2025, refund_6_7=True)
    assert result.refund_bedrag == pytest.approx(0.0)


# 9 — VAT standard rate = 18%
def test_vat_standard_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)


# 10 — VAT reduced rates 12/7/5 and OSS eligibility
def test_vat_reduced_rates_and_oss():
    vat = _params()["vat"]
    assert vat["reduced_rates"] == [0.12, 0.07, 0.05]
    assert vat["oss_eligible"] is True


# 11 — Pillar Two: Malta elected the 6-year QDMTT deferral
def test_pillar_two_deferral_note():
    p2 = _params()["pillar_two"]
    assert p2["qdmtt_deferral"] is True
    assert "6-year deferral" in p2["note"]


# 12 — official source URL (CFR)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("cfr.gov.mt" in s["url"] for s in sources)
