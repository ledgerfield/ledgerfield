import sys; sys.path.insert(0, '/tmp/ledgerfield/src')
import json, hashlib
from ledgerfield.schemas.NO.schema import NO_ACCOUNTS, get_account

def test_schema_has_accounts():
    assert len(NO_ACCOUNTS) >= 20

def test_asset_account_exists():
    a = get_account("1010")
    assert a is not None and a.account_type == "asset"

def test_liability_account_exists():
    a = get_account("2010")
    assert a is not None and a.account_type == "liability"

def test_ruleset_json_valid():
    rs = json.load(open('/tmp/ledgerfield/rulesets/NO_2025.json'))
    assert rs["jurisdiction"] == "NO"
    assert "corporate_income_tax" in rs["parameters"]

def test_ruleset_cid_computable():
    rs = json.load(open('/tmp/ledgerfield/rulesets/NO_2025.json'))
    canonical = json.dumps(rs, sort_keys=True, separators=(',', ':'))
    cid = "sha256:" + hashlib.sha256(canonical.encode()).hexdigest()
    assert cid.startswith("sha256:")
