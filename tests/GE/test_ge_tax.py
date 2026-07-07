"""Georgia tax property tests — Estonian (distributed-profit) model."""
import json
import os

import pytest

from ledgerfield.schemas.GE.ge_gaap import GE_GAAP
from ledgerfield.tax.GE.cit import bereken_cit_georgie

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/GE/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_ge_schema_min_60_accounts():
    assert len(GE_GAAP) >= 60


# 2 — CIT rate = 15%
def test_cit_rate_15pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.15)


# 3 — Estonian model CORE: retained/reinvested profit taxed at 0%
def test_retained_profit_zero_tax():
    result = bereken_cit_georgie(1_000_000.0, 2025, ingehouden=True)
    assert result.cit_totaal == pytest.approx(0.0)
    assert result.effectief_tarief == pytest.approx(0.0)


# 4 — distributed profit taxed at 15%
def test_distributed_profit_15pct():
    result = bereken_cit_georgie(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(150_000.0)
    assert result.effectief_tarief == pytest.approx(0.15)


# 5 — zero / negative distribution yields zero tax
def test_non_positive_distribution_zero_tax():
    assert bereken_cit_georgie(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_georgie(-25_000.0, 2025).cit_totaal == pytest.approx(0.0)


# 6 — VAT standard rate = 18%
def test_vat_18pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.18)


# 7 — Estonian model flagged in params
def test_estonian_model_flag():
    assert _params()["cit"]["model"] == "estonian_distributed_profit"
    assert _params()["cit"]["retained_profit_rate"] == pytest.approx(0.0)


# 8 — issue #39: needs_verification true and sources URL present
def test_needs_verification_and_source_url():
    p = _params()
    assert p["metadata"]["needs_verification"] is True
    assert p["metadata"]["source_status"] == "ai_estimated_needs_verification"
    urls = [s["url"] for s in p["sources"]]
    assert "https://www.rs.ge/" in urls
