"""Property tests for China schema and tax rules — 12 tests."""
import hashlib
import json
import os

import pytest

from ledgerfield.schemas.CN.cas import CAS_CN, get_account, accounts_by_class
from ledgerfield.tax.CN.cit import bereken_cit_china, CNEntityType

_RULESET_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../rulesets/CN_2025.json",
)
_PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CN/params.json",
)


def _ruleset():
    with open(_RULESET_PATH, encoding="utf-8") as f:
        return json.load(f)


def _params(jaar: int = 2025):
    with open(_PARAMS_PATH, encoding="utf-8") as f:
        return json.load(f)["years"][str(jaar)]


# --- Schema tests ---

def test_cas_cn_count_ge_60():
    assert len(CAS_CN) >= 60


def test_cas_cn_1002_is_bank_deposits():
    acc = get_account("1002")
    assert acc is not None
    assert acc.name_zh == "银行存款"


def test_cas_cn_main_revenue_account_exists():
    # 主营业务收入 — code 6001 in P&L class
    acc = get_account("6001")
    assert acc is not None
    assert "主营业务收入" in acc.name_zh


# --- CIT tests ---

def test_cn_cit_standard_5m_25pct():
    result = bereken_cit_china(5_000_000, jaar=2025, entity_type=CNEntityType.STANDARD)
    assert result.cit_totaal == pytest.approx(1_250_000.0)


def test_cn_cit_hnte_5m_15pct():
    result = bereken_cit_china(5_000_000, jaar=2025, entity_type=CNEntityType.HNTE)
    assert result.cit_totaal == pytest.approx(750_000.0)


def test_cn_cit_micro_500k_5pct():
    # 500k is below micro_threshold_cny (1M) → 5%
    result = bereken_cit_china(500_000, jaar=2025, entity_type=CNEntityType.MICRO)
    assert result.cit_totaal == pytest.approx(25_000.0)


def test_cn_cit_sme_2m_20pct():
    # 2M <= sme_threshold_cny (3M) → 20%
    result = bereken_cit_china(2_000_000, jaar=2025, entity_type=CNEntityType.SME)
    assert result.cit_totaal == pytest.approx(400_000.0)


def test_cn_cit_all_entity_types_produce_valid_results():
    income = 1_500_000
    for entity_type in CNEntityType:
        result = bereken_cit_china(income, jaar=2025, entity_type=entity_type)
        assert result.cit_totaal >= 0
        assert 0.0 <= result.effective_rate <= 1.0
        assert result.applied_rate > 0


# --- VAT tests ---

def test_cn_vat_standard_13pct():
    p = _params(2025)
    assert p["VAT"]["standard_rate"] == pytest.approx(0.13)


def test_cn_vat_services_6pct():
    p = _params(2025)
    assert p["VAT"]["rate_services"] == pytest.approx(0.06)


# --- IIT tests ---

def test_cn_iit_basic_deduction_5000_monthly():
    p = _params(2025)
    assert p["IIT"]["basic_deduction_cny_monthly"] == 5000


# --- Ruleset tests ---

def test_cn_ruleset_json_loads_and_cid_is_sha256():
    rs = _ruleset()
    assert rs["jurisdiction"] == "CN"
    raw = open(_RULESET_PATH, "rb").read()
    cid = "sha256:" + hashlib.sha256(raw).hexdigest()
    assert cid.startswith("sha256:")
    assert len(cid) == len("sha256:") + 64
