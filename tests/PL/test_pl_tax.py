import json, hashlib
from ledgerfield.schemas.PL.schema import PL_ACCOUNTS, get_account
from tests.ruleset_paths import load_ruleset


def test_schema_has_accounts():
    assert len(PL_ACCOUNTS) >= 20


def test_asset_account_exists():
    a = get_account("1010")
    assert a is not None and a.account_type == "asset"


def test_liability_account_exists():
    a = get_account("2010")
    assert a is not None and a.account_type == "liability"


def test_ruleset_json_valid():
    rs = load_ruleset("PL")
    assert rs["jurisdiction"] == "PL"
    assert "corporate_income_tax" in rs["parameters"]


def test_ruleset_cid_computable():
    rs = load_ruleset("PL")
    canonical = json.dumps(rs, sort_keys=True, separators=(',', ':'))
    cid = "sha256:" + hashlib.sha256(canonical.encode()).hexdigest()
    assert cid.startswith("sha256:")
