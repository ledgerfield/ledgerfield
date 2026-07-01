"""US GAAP Chart of Accounts — standard for corporations and LLCs.

~90 accounts covering Assets (1000-1999), Liabilities (2000-2999),
Equity (3000-3999), Revenue (4000-4999), COGS (5000-5999),
Operating Expenses (6000-6999), and Other (7000+).
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Literal

__all__ = [
    "AccountCategory",
    "AccountType",
    "USGAAPAccount",
    "US_GAAP",
    "get_account",
    "accounts_for_entity_type",
    "write_json_schema",
]


class AccountCategory(Enum):
    ASSETS = "Assets"
    LIABILITIES = "Liabilities"
    EQUITY = "Equity"
    REVENUE = "Revenue"
    COGS = "Cost of Goods Sold"
    OPERATING_EXPENSES = "Operating Expenses"
    OTHER = "Other"


class AccountType(Enum):
    DEBIT = "debit"    # normal balance is debit (assets, expenses)
    CREDIT = "credit"  # normal balance is credit (liabilities, equity, revenue)


@dataclass(frozen=True)
class USGAAPAccount:
    number: int
    name: str
    category: AccountCategory
    normal_balance: AccountType
    description: str = ""
    # entity_types: which entity types include this account
    # None means all; otherwise a frozenset of "corp", "llc", "sole"
    entity_types: frozenset[str] | None = None

    @property
    def is_asset(self) -> bool:
        return self.category == AccountCategory.ASSETS

    @property
    def is_liability(self) -> bool:
        return self.category == AccountCategory.LIABILITIES

    @property
    def is_equity(self) -> bool:
        return self.category == AccountCategory.EQUITY

    @property
    def is_revenue(self) -> bool:
        return self.category == AccountCategory.REVENUE

    @property
    def is_expense(self) -> bool:
        return self.category in (
            AccountCategory.COGS,
            AccountCategory.OPERATING_EXPENSES,
            AccountCategory.OTHER,
        )

    def applies_to(self, entity: str) -> bool:
        if self.entity_types is None:
            return True
        return entity in self.entity_types

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "name": self.name,
            "category": self.category.value,
            "normal_balance": self.normal_balance.value,
            "description": self.description,
            "entity_types": sorted(self.entity_types) if self.entity_types else None,
        }


# Shorthand constructors
def _a(number, name, description="", entity_types=None):
    """Asset account (debit normal balance)."""
    return USGAAPAccount(number, name, AccountCategory.ASSETS, AccountType.DEBIT,
                         description, entity_types)

def _l(number, name, description="", entity_types=None):
    """Liability account (credit normal balance)."""
    return USGAAPAccount(number, name, AccountCategory.LIABILITIES, AccountType.CREDIT,
                         description, entity_types)

def _e(number, name, description="", entity_types=None):
    """Equity account (credit normal balance)."""
    return USGAAPAccount(number, name, AccountCategory.EQUITY, AccountType.CREDIT,
                         description, entity_types)

def _r(number, name, description="", entity_types=None):
    """Revenue account (credit normal balance)."""
    return USGAAPAccount(number, name, AccountCategory.REVENUE, AccountType.CREDIT,
                         description, entity_types)

def _c(number, name, description="", entity_types=None):
    """COGS account (debit normal balance)."""
    return USGAAPAccount(number, name, AccountCategory.COGS, AccountType.DEBIT,
                         description, entity_types)

def _x(number, name, description="", entity_types=None):
    """Operating expense account (debit normal balance)."""
    return USGAAPAccount(number, name, AccountCategory.OPERATING_EXPENSES, AccountType.DEBIT,
                         description, entity_types)

def _o(number, name, description="", entity_types=None):
    """Other income/expense account."""
    normal = AccountType.DEBIT if number >= 7100 else AccountType.CREDIT
    return USGAAPAccount(number, name, AccountCategory.OTHER, normal,
                         description, entity_types)


_CORP = frozenset({"corp"})
_LLC = frozenset({"llc"})
_CORP_LLC = frozenset({"corp", "llc"})
_ALL = None  # all entity types

_ACCOUNTS_LIST: list[USGAAPAccount] = [
    # ── ASSETS: Current ─────────────────────────────────────────────────────
    _a(1000, "Cash and Cash Equivalents",   "Total cash header",                          _ALL),
    _a(1010, "Checking Account",            "Primary operating checking account",          _ALL),
    _a(1020, "Savings Account",             "Business savings / money market",             _ALL),
    _a(1030, "Petty Cash",                  "On-hand petty cash fund",                    _ALL),
    _a(1040, "Restricted Cash",             "Cash restricted for specific purpose",        _ALL),
    _a(1100, "Accounts Receivable",         "Trade receivables header",                   _ALL),
    _a(1110, "Accounts Receivable",         "Amounts owed by customers",                  _ALL),
    _a(1120, "Allowance for Doubtful Accounts", "Contra-asset for estimated uncollectible", _ALL),
    _a(1130, "Notes Receivable (current)",  "Short-term notes receivable",                _ALL),
    _a(1200, "Inventory",                   "Merchandise / finished goods inventory",     _ALL),
    _a(1210, "Raw Materials",               "Raw material inventory",                     _ALL),
    _a(1220, "Work in Progress",            "WIP inventory",                              _ALL),
    _a(1230, "Finished Goods",              "Completed product ready for sale",           _ALL),
    _a(1400, "Prepaid Expenses",            "Prepaid expenses header",                    _ALL),
    _a(1410, "Prepaid Expenses",            "Prepaid insurance, rent, subscriptions",     _ALL),
    _a(1420, "Prepaid Insurance",           "Insurance paid in advance",                  _ALL),
    _a(1430, "Employee Advances",           "Advances paid to employees",                 _ALL),
    # ── ASSETS: Fixed / Long-term ───────────────────────────────────────────
    _a(1500, "Property, Plant & Equipment", "PP&E header (gross)",                        _ALL),
    _a(1510, "Land",                        "Land (not depreciated)",                     _ALL),
    _a(1520, "Buildings",                   "Buildings and improvements",                 _ALL),
    _a(1525, "Accumulated Depreciation – Buildings", "Contra-asset",                      _ALL),
    _a(1530, "Equipment",                   "Machinery, furniture, fixtures",             _ALL),
    _a(1535, "Accumulated Depreciation – Equipment", "Contra-asset",                      _ALL),
    _a(1540, "Vehicles",                    "Company vehicles",                           _ALL),
    _a(1545, "Accumulated Depreciation – Vehicles",  "Contra-asset",                      _ALL),
    _a(1550, "Leasehold Improvements",      "Tenant improvements",                        _ALL),
    _a(1555, "Accumulated Amortization – Leasehold", "Contra-asset",                      _ALL),
    # ── ASSETS: Intangible ──────────────────────────────────────────────────
    _a(1600, "Intangible Assets",           "Intangibles header",                         _ALL),
    _a(1610, "Patents",                     "Capitalized patent costs",                   _ALL),
    _a(1620, "Goodwill",                    "Goodwill from acquisitions",                 _CORP_LLC),
    _a(1630, "Trademarks",                  "Registered trademarks",                      _ALL),
    _a(1640, "Customer Lists",              "Acquired customer relationship intangibles",  _ALL),
    _a(1650, "Software Development Costs",  "Capitalized internal-use software",          _ALL),
    # ── ASSETS: Other ───────────────────────────────────────────────────────
    _a(1700, "Other Assets",               "Long-term assets not elsewhere classified",   _ALL),
    _a(1710, "Security Deposits",          "Deposits paid to landlords/utilities",        _ALL),
    _a(1720, "Long-Term Investments",      "Equity investments, bonds held to maturity",  _ALL),
    _a(1730, "Notes Receivable (long-term)", "Long-term notes receivable",               _ALL),

    # ── LIABILITIES: Current ────────────────────────────────────────────────
    _l(2010, "Accounts Payable",           "Amounts owed to vendors/suppliers",           _ALL),
    _l(2020, "Accrued Liabilities",        "Accrued expenses not yet invoiced",           _ALL),
    _l(2030, "Sales Tax Payable",          "Sales tax collected, owed to state",          _ALL),
    _l(2040, "Payroll Liabilities",        "Wages, taxes, benefits withheld",             _ALL),
    _l(2041, "Federal Payroll Taxes Payable", "FICA and FUTA payable",                   _ALL),
    _l(2042, "State Payroll Taxes Payable",   "State unemployment and income tax withheld", _ALL),
    _l(2050, "Federal Income Tax Payable", "Corporate/estimated federal income tax",      _CORP),
    _l(2060, "State Income Tax Payable",   "State income tax payable",                   _CORP),
    _l(2070, "Customer Deposits",          "Advance payments from customers",             _ALL),
    _l(2080, "Current Portion of Long-Term Debt", "LTD due within 12 months",            _ALL),
    # ── LIABILITIES: Long-term ──────────────────────────────────────────────
    _l(2100, "Notes Payable (short-term)", "Short-term borrowings and lines of credit",  _ALL),
    _l(2200, "Long-Term Notes Payable",   "Long-term bank loans and bonds payable",      _ALL),
    _l(2210, "Mortgage Payable",          "Mortgage on real property",                   _ALL),
    _l(2300, "Deferred Revenue",          "Revenue received but not yet earned",          _ALL),
    _l(2400, "Deferred Tax Liability",    "Temporary differences – deferred taxes",       _CORP),
    _l(2900, "Other Long-Term Liabilities", "Other non-current liabilities",             _ALL),

    # ── EQUITY ──────────────────────────────────────────────────────────────
    _e(3010, "Common Stock",              "Par value of issued common shares",            _CORP),
    _e(3015, "Preferred Stock",           "Par value of issued preferred shares",         _CORP),
    _e(3020, "Additional Paid-In Capital","Capital in excess of par value",              _CORP),
    _e(3025, "Member Contributions",      "Capital contributed by LLC members",           _LLC),
    _e(3030, "Retained Earnings",         "Accumulated undistributed net income",         _CORP),
    _e(3035, "Member Equity",             "LLC accumulated equity",                       _LLC),
    _e(3040, "Treasury Stock",            "Repurchased shares (contra-equity)",           _CORP),
    _e(3050, "Current Year Net Income",   "Plug account for current period P&L",         _ALL),
    _e(3060, "Owner's Drawings",          "Distributions to owners/members",             _ALL),
    _e(3070, "Dividends Declared",        "Dividends declared to shareholders",           _CORP),

    # ── REVENUE ─────────────────────────────────────────────────────────────
    _r(4010, "Product Sales",             "Revenue from sale of physical goods",          _ALL),
    _r(4015, "Sales Returns & Allowances","Contra-revenue: returns and price adjustments",_ALL),
    _r(4017, "Sales Discounts",           "Contra-revenue: early-pay discounts granted",  _ALL),
    _r(4020, "Service Revenue",           "Revenue from services rendered",               _ALL),
    _r(4030, "Interest Income",           "Interest earned on deposits and investments",  _ALL),
    _r(4040, "Other Income",              "Miscellaneous income not elsewhere classified", _ALL),
    _r(4050, "Gain on Sale of Assets",   "Gain realized on disposal of assets",          _ALL),

    # ── COST OF GOODS SOLD ──────────────────────────────────────────────────
    _c(5010, "Cost of Goods Sold",        "Direct cost of merchandise sold",              _ALL),
    _c(5020, "Direct Labor",              "Wages directly tied to production",            _ALL),
    _c(5030, "Manufacturing Overhead",    "Indirect production costs allocated to COGS",  _ALL),
    _c(5040, "Freight-In",               "Inbound shipping costs for inventory",          _ALL),
    _c(5050, "Purchase Discounts",        "Contra-COGS: discounts received from vendors", _ALL),

    # ── OPERATING EXPENSES: Payroll ─────────────────────────────────────────
    _x(6010, "Salaries & Wages Expense",  "Gross wages for employees",                   _ALL),
    _x(6020, "Payroll Tax Expense",       "Employer share of FICA, FUTA, SUTA",          _ALL),
    _x(6030, "Employee Benefits Expense", "Health, dental, vision, retirement match",    _ALL),
    _x(6040, "Officer Compensation",      "Salaries paid to officers/owners",             _CORP_LLC),
    # ── Operating Expenses: Facilities ──────────────────────────────────────
    _x(6110, "Rent Expense",              "Office, warehouse, or retail lease",           _ALL),
    _x(6120, "Utilities Expense",         "Electric, gas, water, internet",               _ALL),
    _x(6130, "Office Supplies Expense",   "Consumable office supplies",                   _ALL),
    _x(6140, "Insurance Expense",         "Business liability, property, auto insurance", _ALL),
    _x(6150, "Repairs & Maintenance",     "Routine repairs to premises and equipment",    _ALL),
    # ── Operating Expenses: Sales & Marketing ───────────────────────────────
    _x(6210, "Advertising & Marketing",   "Digital ads, print, SEO, marketing campaigns", _ALL),
    _x(6220, "Travel Expense",            "Airfare, lodging, ground transport",           _ALL),
    _x(6230, "Meals & Entertainment",     "50% deductible meals and client entertainment",_ALL),
    _x(6240, "Vehicle Expense",           "Gas, maintenance, tolls for business vehicles",_ALL),
    # ── Operating Expenses: Depreciation & Amortization ─────────────────────
    _x(6310, "Depreciation Expense",      "Periodic depreciation of PP&E",               _ALL),
    _x(6320, "Amortization Expense",      "Periodic amortization of intangible assets",  _ALL),
    # ── Operating Expenses: Professional & Tech ──────────────────────────────
    _x(6410, "Professional Fees",         "Legal, accounting, consulting fees",           _ALL),
    _x(6420, "Software & Subscriptions",  "SaaS, cloud, software licenses",               _ALL),
    _x(6430, "Bank & Merchant Fees",      "Bank charges, credit card processing fees",   _ALL),
    _x(6440, "Licenses & Permits",        "Business licenses, permits, regulatory fees",  _ALL),
    _x(6450, "Research & Development",    "R&D costs expensed in current period",         _ALL),
    _x(6490, "Miscellaneous Expense",     "Other operating expenses not classified above",_ALL),

    # ── OTHER INCOME / EXPENSE ───────────────────────────────────────────────
    _o(7010, "Interest Expense",          "Interest on loans, lines of credit, bonds",   _ALL),
    _o(7020, "Loss on Sale of Assets",    "Loss realized on disposal of assets",          _ALL),
    _o(7030, "Foreign Currency Loss",     "FX losses on transactions or translation",     _ALL),
    _o(7100, "Income Tax Expense – Federal","Federal corporate income tax provision",      _CORP),
    _o(7110, "Income Tax Expense – State", "State corporate income tax provision",         _CORP),
    _o(7120, "Deferred Tax Expense",      "Change in deferred tax asset/liability",       _CORP),
]

# Master dict: account number → USGAAPAccount
US_GAAP: dict[int, USGAAPAccount] = {acct.number: acct for acct in _ACCOUNTS_LIST}


def get_account(number: int) -> USGAAPAccount | None:
    """Return the USGAAPAccount for a given account number, or None."""
    return US_GAAP.get(number)


def accounts_for_entity_type(
    entity: Literal["corp", "llc", "sole"],
) -> dict[int, USGAAPAccount]:
    """Return the subset of US_GAAP accounts applicable to the given entity type."""
    return {n: a for n, a in US_GAAP.items() if a.applies_to(entity)}


# ── JSON schema export ───────────────────────────────────────────────────────

def _build_json_schema() -> dict:
    return {
        "schema": "US-GAAP",
        "version": "2024",
        "description": "Standard US GAAP chart of accounts for corporations and LLCs",
        "ranges": {
            "1000-1999": "Assets",
            "2000-2999": "Liabilities",
            "3000-3999": "Equity",
            "4000-4999": "Revenue",
            "5000-5999": "Cost of Goods Sold",
            "6000-6999": "Operating Expenses",
            "7000+":     "Other Income / Expense",
        },
        "accounts": [a.to_dict() for a in sorted(_ACCOUNTS_LIST, key=lambda x: x.number)],
    }


def write_json_schema(path: str | None = None) -> str:
    """Write the US GAAP schema JSON to ``path`` and return the output path."""

    if path is None:
        path = os.path.join(os.path.dirname(__file__), "us_gaap_schema.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(_build_json_schema(), f, indent=2, ensure_ascii=False)
    return path
