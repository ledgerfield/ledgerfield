"""Republic of Cyprus tax property tests — 12 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CY.cy_gaap import CY_GAAP
from ledgerfield.tax.CY.cit import bereken_cit_cyprus

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CY/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_cy_schema_min_60_accounts():
    assert len(CY_GAAP) >= 60


# 2 — CIT rate = 12.5%
def test_cit_rate_12_5pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.125)


# 3 — EUR 1,000,000 profit → EUR 125,000 CIT
def test_cit_one_million():
    result = bereken_cit_cyprus(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(125_000.0)


# 4 — effective rate equals 12.5% on positive profit
def test_effectief_tarief():
    result = bereken_cit_cyprus(400_000.0, 2025)
    assert result.effectief_tarief == pytest.approx(0.125)


# 5 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_cyprus(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_cyprus(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_cyprus(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 6 — VAT standard rate 19% with 9/5/3 reduced rates
def test_vat_rates():
    vat = _params()["vat"]
    assert vat["standard_rate"] == pytest.approx(0.19)
    assert vat["reduced_rates"] == [0.09, 0.05, 0.03]


# 7 — EU OSS eligible
def test_oss_eligible():
    assert _params()["vat"]["oss_eligible"] is True


# 8 — IP box: 80% exemption on qualifying IP profits noted
def test_ip_box_note():
    ip_box = _params()["cit"]["ip_box"]
    assert ip_box["qualifying_profit_exemption"] == pytest.approx(0.80)
    assert "IP box" in ip_box["note"]


# 9 — Special Defence Contribution: dividends and interest at 17%
def test_sdc_passive_income():
    sdc = _params()["sdc"]
    assert sdc["dividends_resident_domiciled"] == pytest.approx(0.17)
    assert sdc["interest"] == pytest.approx(0.17)
    assert "Special Defence Contribution" in sdc["note"]


# 10 — planned 15% CIT reform noted (announced, not yet law in range)
def test_reform_note():
    reform = _params()["cit"]["reform_note"]
    assert "15%" in reform
    assert "not yet law" in reform


# 11 — Pillar Two note present
def test_pillar_two_note():
    note = _params()["pillar_two"]["note"]
    assert "Pillar Two" in note
    assert "15%" in note


# 12 — official source URL (Tax Department)
def test_official_source_url():
    sources = _params()["metadata"]["official_sources"]
    assert any("mof.gov.cy" in s["url"] for s in sources)
