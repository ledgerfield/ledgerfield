"""Tests for ledgerfield.schemas.NL.rgs — RGS NL accounts and NEN4400 checker."""
from ledgerfield.schemas.NL.rgs import RGS_NL, get_account, accounts_by_category
from ledgerfield.schemas.NL.nen4400 import NEN4400_ITEMS, NEN4400Checker, ComplianceStatus


def test_rgs_nl_len_ge_100():
    assert len(RGS_NL) >= 100


def test_get_account_1420_has_bank_in_name():
    acc = get_account("1420")
    assert acc is not None
    assert "Bank" in acc.name


def test_get_account_0100_is_asset():
    acc = get_account("0100")
    assert acc is not None
    assert acc.is_asset is True


def test_get_account_4020_is_liability():
    # Af te dragen BTW
    acc = get_account("4020")
    assert acc is not None
    assert acc.is_liability is True


def test_get_account_8010_is_revenue():
    acc = get_account("8010")
    assert acc is not None
    assert acc.is_revenue is True


def test_get_account_4110_is_expense():
    # DGA-salaris is W&V / Personeelskosten → not Opbrengsten → is_expense True
    acc = get_account("4110")
    assert acc is not None
    assert acc.is_expense is True


def test_accounts_by_category_activa_only_assets():
    activa = accounts_by_category("Activa")
    assert len(activa) > 0
    assert all(a.is_asset for a in activa)


def test_accounts_by_category_opbrengsten_only_revenue():
    opbrengsten = accounts_by_category("Opbrengsten")
    assert len(opbrengsten) > 0
    assert all(a.is_revenue for a in opbrengsten)


def test_nen4400_has_ge_15_items():
    assert len(NEN4400_ITEMS) >= 15


def test_nen4400_checker_initial_all_missing_and_score():
    checker = NEN4400Checker()
    # All items should start with MISSING status
    report = checker.report()
    assert all(item["status"] == ComplianceStatus.MISSING.value for item in report)
    # score = (0, n_mandatory)
    passed, total = checker.score()
    assert passed == 0
    mandatory_count = sum(1 for item in report if item["mandatory"])
    assert total == mandatory_count
