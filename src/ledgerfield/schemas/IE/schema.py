"""Irish GAAP (FRS 102 / IFRS) — Standard Chart of Accounts for Irish companies.

~80 representative accounts across Balance Sheet and P&L, conforming to Irish GAAP
(FRS 102 as adopted in the Republic of Ireland, also IFRS for larger entities).

FRS 102 is the same standard applicable in the UK and Republic of Ireland; Irish
companies file with the Companies Registration Office (CRO) and pay Corporation Tax
to the Revenue Commissioners.

Account groupings:
  0xxx  Fixed Assets (tangible + intangible)
  1xxx  Current Assets (stock, debtors, prepayments, cash)
  2xxx  Creditors due within one year
  3xxx  Creditors due after one year
  35xx  Provisions
  4xxx  Share Capital & Reserves
  5xxx  Sales / Revenue
  6xxx  Cost of Sales
  7xxx  Administrative & Overhead expenses
  8xxx  Finance income / charges
  9xxx  Taxation
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

__all__ = [
    "AccountGroup",
    "IEAccount",
    "IE_GAAP",
    "get_account",
    "accounts_by_group",
]


class AccountGroup:
    FIXED_ASSETS_TANGIBLE   = "Fixed Assets/Tangible"
    FIXED_ASSETS_INTANGIBLE = "Fixed Assets/Intangible"
    FIXED_ASSETS_FINANCIAL  = "Fixed Assets/Financial"
    CURRENT_ASSETS          = "Current Assets"
    CREDITORS_LT_1YR        = "Creditors <1yr"
    CREDITORS_GT_1YR        = "Creditors >1yr"
    PROVISIONS              = "Provisions"
    SHARE_CAPITAL_RESERVES  = "Share Capital & Reserves"
    REVENUE                 = "Revenue"
    COST_OF_SALES           = "Cost of Sales"
    ADMIN_OVERHEAD          = "Admin & Overhead"
    FINANCE                 = "Finance"
    TAXATION                = "Taxation"


@dataclass(frozen=True)
class IEAccount:
    code: str
    name: str
    statement: str   # "Balance Sheet" or "P&L"
    group: str       # one of AccountGroup constants

    @property
    def is_asset(self) -> bool:
        return self.statement == "Balance Sheet" and self.group.startswith("Fixed Assets") or \
               self.statement == "Balance Sheet" and self.group == "Current Assets"

    @property
    def is_liability(self) -> bool:
        return self.statement == "Balance Sheet" and self.group in (
            "Creditors <1yr", "Creditors >1yr", "Provisions"
        )

    @property
    def is_equity(self) -> bool:
        return self.group == "Share Capital & Reserves"

    @property
    def is_revenue(self) -> bool:
        return self.group == "Revenue"

    @property
    def is_expense(self) -> bool:
        return self.statement == "P&L" and not self.is_revenue


# ── Helper aliases ────────────────────────────────────────────────────────────
_BS = "Balance Sheet"
_PL = "P&L"
_G  = AccountGroup


IE_GAAP: dict[str, IEAccount] = {
    # ─── 0: FIXED ASSETS ─────────────────────────────────────────────────────
    # Tangible
    "0010": IEAccount("0010", "Tangible Fixed Assets",              _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0020": IEAccount("0020", "Freehold Land & Buildings",          _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0030": IEAccount("0030", "Leasehold Improvements",             _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0040": IEAccount("0040", "Plant & Machinery",                  _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0050": IEAccount("0050", "Motor Vehicles",                     _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0060": IEAccount("0060", "Office Equipment & Furniture",       _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0070": IEAccount("0070", "Computer Hardware & IT Equipment",   _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0080": IEAccount("0080", "Accum. Depreciation — Buildings",    _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0085": IEAccount("0085", "Accum. Depreciation — Plant",        _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0090": IEAccount("0090", "Accum. Depreciation — Vehicles",     _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0095": IEAccount("0095", "Accum. Depreciation — IT",           _BS, _G.FIXED_ASSETS_TANGIBLE),
    # Intangible
    "0200": IEAccount("0200", "Intangible Fixed Assets",            _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0210": IEAccount("0210", "Goodwill",                           _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0220": IEAccount("0220", "Intellectual Property / Patents",    _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0230": IEAccount("0230", "Development Costs Capitalised",      _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0240": IEAccount("0240", "Software (Capitalised)",             _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0280": IEAccount("0280", "Accum. Amortisation — Goodwill",     _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0290": IEAccount("0290", "Accum. Amortisation — Other Intang", _BS, _G.FIXED_ASSETS_INTANGIBLE),
    # Financial
    "0300": IEAccount("0300", "Investments in Subsidiaries",        _BS, _G.FIXED_ASSETS_FINANCIAL),
    "0310": IEAccount("0310", "Loans to Group Companies",           _BS, _G.FIXED_ASSETS_FINANCIAL),
    "0320": IEAccount("0320", "Other Long-term Investments",        _BS, _G.FIXED_ASSETS_FINANCIAL),

    # ─── 1: CURRENT ASSETS ───────────────────────────────────────────────────
    "1000": IEAccount("1000", "Stock / Inventories",                _BS, _G.CURRENT_ASSETS),
    "1010": IEAccount("1010", "Raw Materials",                      _BS, _G.CURRENT_ASSETS),
    "1020": IEAccount("1020", "Work in Progress",                   _BS, _G.CURRENT_ASSETS),
    "1030": IEAccount("1030", "Finished Goods",                     _BS, _G.CURRENT_ASSETS),
    "1100": IEAccount("1100", "Trade Debtors",                      _BS, _G.CURRENT_ASSETS),
    "1110": IEAccount("1110", "Other Debtors",                      _BS, _G.CURRENT_ASSETS),
    "1120": IEAccount("1120", "Prepayments",                        _BS, _G.CURRENT_ASSETS),
    "1130": IEAccount("1130", "Accrued Income",                     _BS, _G.CURRENT_ASSETS),
    "1140": IEAccount("1140", "VAT Recoverable",                    _BS, _G.CURRENT_ASSETS),
    "1150": IEAccount("1150", "Corporation Tax Recoverable",        _BS, _G.CURRENT_ASSETS),
    "1160": IEAccount("1160", "Loans to Directors / Officers",      _BS, _G.CURRENT_ASSETS),
    "1200": IEAccount("1200", "Cash at Bank",                       _BS, _G.CURRENT_ASSETS),
    "1210": IEAccount("1210", "Petty Cash",                         _BS, _G.CURRENT_ASSETS),
    "1220": IEAccount("1220", "Short-term Deposits",                _BS, _G.CURRENT_ASSETS),

    # ─── 2: CREDITORS DUE WITHIN ONE YEAR ────────────────────────────────────
    "2000": IEAccount("2000", "Trade Creditors",                    _BS, _G.CREDITORS_LT_1YR),
    "2010": IEAccount("2010", "Accruals",                           _BS, _G.CREDITORS_LT_1YR),
    "2020": IEAccount("2020", "Deferred Income",                    _BS, _G.CREDITORS_LT_1YR),
    "2030": IEAccount("2030", "Bank Overdraft",                     _BS, _G.CREDITORS_LT_1YR),
    "2040": IEAccount("2040", "Current Portion of Long-term Loans", _BS, _G.CREDITORS_LT_1YR),
    "2050": IEAccount("2050", "VAT Payable",                        _BS, _G.CREDITORS_LT_1YR),
    "2060": IEAccount("2060", "PAYE / PRSI Payable",                _BS, _G.CREDITORS_LT_1YR),
    "2070": IEAccount("2070", "Corporation Tax Payable",            _BS, _G.CREDITORS_LT_1YR),
    "2080": IEAccount("2080", "Dividend Payable",                   _BS, _G.CREDITORS_LT_1YR),
    "2090": IEAccount("2090", "Directors' Loan Accounts",           _BS, _G.CREDITORS_LT_1YR),
    "2095": IEAccount("2095", "Other Short-term Creditors",         _BS, _G.CREDITORS_LT_1YR),

    # ─── 3: CREDITORS DUE AFTER ONE YEAR ─────────────────────────────────────
    "3000": IEAccount("3000", "Mortgage / Long-term Bank Loans",    _BS, _G.CREDITORS_GT_1YR),
    "3010": IEAccount("3010", "Finance Lease Obligations",          _BS, _G.CREDITORS_GT_1YR),
    "3020": IEAccount("3020", "Loans from Directors (>1yr)",        _BS, _G.CREDITORS_GT_1YR),
    "3030": IEAccount("3030", "Debentures",                         _BS, _G.CREDITORS_GT_1YR),
    # Provisions 35xx
    "3500": IEAccount("3500", "Provisions for Liabilities",         _BS, _G.PROVISIONS),
    "3510": IEAccount("3510", "Deferred Tax Provision",             _BS, _G.PROVISIONS),
    "3520": IEAccount("3520", "Warranty Provision",                 _BS, _G.PROVISIONS),
    "3530": IEAccount("3530", "Restructuring Provision",            _BS, _G.PROVISIONS),

    # ─── 4: SHARE CAPITAL & RESERVES ─────────────────────────────────────────
    "4000": IEAccount("4000", "Called-up Share Capital",            _BS, _G.SHARE_CAPITAL_RESERVES),
    "4010": IEAccount("4010", "Share Premium Account",              _BS, _G.SHARE_CAPITAL_RESERVES),
    "4020": IEAccount("4020", "Revaluation Reserve",                _BS, _G.SHARE_CAPITAL_RESERVES),
    "4030": IEAccount("4030", "Capital Redemption Reserve",         _BS, _G.SHARE_CAPITAL_RESERVES),
    "4040": IEAccount("4040", "Retained Earnings",                  _BS, _G.SHARE_CAPITAL_RESERVES),
    "4050": IEAccount("4050", "Profit & Loss Account (current yr)", _BS, _G.SHARE_CAPITAL_RESERVES),

    # ─── 5: REVENUE ──────────────────────────────────────────────────────────
    "5000": IEAccount("5000", "Irish Sales",                        _PL, _G.REVENUE),
    "5010": IEAccount("5010", "EU Sales (goods)",                   _PL, _G.REVENUE),
    "5020": IEAccount("5020", "Export Sales (non-EU)",              _PL, _G.REVENUE),
    "5030": IEAccount("5030", "Service Revenue",                    _PL, _G.REVENUE),
    "5040": IEAccount("5040", "Rental Income",                      _PL, _G.REVENUE),
    "5050": IEAccount("5050", "Grant Income (Enterprise Ireland)",  _PL, _G.REVENUE),
    "5060": IEAccount("5060", "Other Operating Income",             _PL, _G.REVENUE),

    # ─── 6: COST OF SALES ────────────────────────────────────────────────────
    "6000": IEAccount("6000", "Purchases — Materials",              _PL, _G.COST_OF_SALES),
    "6010": IEAccount("6010", "Freight & Carriage Inward",          _PL, _G.COST_OF_SALES),
    "6020": IEAccount("6020", "Direct Labour",                      _PL, _G.COST_OF_SALES),
    "6030": IEAccount("6030", "Direct Overhead",                    _PL, _G.COST_OF_SALES),
    "6040": IEAccount("6040", "Subcontractors",                     _PL, _G.COST_OF_SALES),
    "6050": IEAccount("6050", "Opening Stock",                      _PL, _G.COST_OF_SALES),
    "6060": IEAccount("6060", "Closing Stock",                      _PL, _G.COST_OF_SALES),

    # ─── 7: ADMIN & OVERHEAD ─────────────────────────────────────────────────
    "7000": IEAccount("7000", "Directors' Remuneration",            _PL, _G.ADMIN_OVERHEAD),
    "7010": IEAccount("7010", "Salaries & Wages",                   _PL, _G.ADMIN_OVERHEAD),
    "7020": IEAccount("7020", "Employer PRSI",                      _PL, _G.ADMIN_OVERHEAD),
    "7030": IEAccount("7030", "Pension Contributions",              _PL, _G.ADMIN_OVERHEAD),
    "7040": IEAccount("7040", "Rent & Rates",                       _PL, _G.ADMIN_OVERHEAD),
    "7050": IEAccount("7050", "Light & Heat",                       _PL, _G.ADMIN_OVERHEAD),
    "7060": IEAccount("7060", "Insurance",                          _PL, _G.ADMIN_OVERHEAD),
    "7070": IEAccount("7070", "Repairs & Maintenance",              _PL, _G.ADMIN_OVERHEAD),
    "7080": IEAccount("7080", "Telephone & Internet",               _PL, _G.ADMIN_OVERHEAD),
    "7090": IEAccount("7090", "Postage & Stationery",               _PL, _G.ADMIN_OVERHEAD),
    "7100": IEAccount("7100", "IT Costs & Software Licences",       _PL, _G.ADMIN_OVERHEAD),
    "7110": IEAccount("7110", "Motor & Travel Expenses",            _PL, _G.ADMIN_OVERHEAD),
    "7120": IEAccount("7120", "Subsistence & Entertaining",         _PL, _G.ADMIN_OVERHEAD),
    "7130": IEAccount("7130", "Accountancy & Audit Fees",           _PL, _G.ADMIN_OVERHEAD),
    "7140": IEAccount("7140", "Legal & Professional Fees",          _PL, _G.ADMIN_OVERHEAD),
    "7150": IEAccount("7150", "Advertising & Marketing",            _PL, _G.ADMIN_OVERHEAD),
    "7160": IEAccount("7160", "Bad Debts Written Off",              _PL, _G.ADMIN_OVERHEAD),
    "7170": IEAccount("7170", "Depreciation — Tangible Assets",     _PL, _G.ADMIN_OVERHEAD),
    "7180": IEAccount("7180", "Amortisation — Intangible Assets",   _PL, _G.ADMIN_OVERHEAD),
    "7190": IEAccount("7190", "Sundry Expenses",                    _PL, _G.ADMIN_OVERHEAD),

    # ─── 8: FINANCE ──────────────────────────────────────────────────────────
    "8000": IEAccount("8000", "Bank Interest Receivable",           _PL, _G.FINANCE),
    "8010": IEAccount("8010", "Bank Interest Payable",              _PL, _G.FINANCE),
    "8020": IEAccount("8020", "Loan Interest Payable",              _PL, _G.FINANCE),
    "8030": IEAccount("8030", "Finance Lease Interest",             _PL, _G.FINANCE),
    "8040": IEAccount("8040", "Bank Charges",                       _PL, _G.FINANCE),
    "8050": IEAccount("8050", "Foreign Exchange Gains / (Losses)",  _PL, _G.FINANCE),

    # ─── 9: TAXATION ─────────────────────────────────────────────────────────
    "9000": IEAccount("9000", "Corporation Tax Charge",             _PL, _G.TAXATION),
    "9010": IEAccount("9010", "Deferred Tax (Charge) / Credit",     _PL, _G.TAXATION),
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_account(code: str) -> IEAccount | None:
    """Return the IEAccount for *code*, or None if not found."""
    return IE_GAAP.get(code)


def accounts_by_group(group: str) -> list[IEAccount]:
    """Return all accounts whose *group* matches the given string."""
    return [a for a in IE_GAAP.values() if a.group == group]


# ── JSON export (side-effect on import: writes ie_gaap_schema.json) ───────────

def _write_json() -> None:
    out = Path(__file__).with_name("ie_gaap_schema.json")
    payload = [asdict(a) for a in IE_GAAP.values()]
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


_write_json()
