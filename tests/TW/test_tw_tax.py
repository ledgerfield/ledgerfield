"""Taiwan (TW) — schema + ruleset tests. 5 tests."""
import json
import hashlib
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from ledgerfield.schemas.TW.schema import TW_ACCOUNTS, get_account

RULESET_PATH = os.path.join(os.path.dirname(__file__), "../../rulesets/TW_2025.json")


def test_schema_has_accounts():
    assert len(TW_ACCOUNTS) >= 10


def test_asset_account_exists():
    a = get_account("1010")
    assert a.type == "asset"


def test_liability_account_exists():
    a = get_account("2010")
    assert a.type == "liability"


def test_ruleset_json_valid():
    d = json.load(open(RULESET_PATH))
    assert d["jurisdiction"] == "TW"
    assert "corporate_income_tax" in d["parameters"]


def test_ruleset_cid_computable():
    d = json.load(open(RULESET_PATH))
    cid = d["cid"]
    assert cid.startswith("sha256:")
