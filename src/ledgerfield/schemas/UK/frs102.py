"""FRS 102 — UK Standard Chart of Accounts for small/medium companies (Ltd, LLP).

~80 representative accounts across Balance Sheet and P&L, conforming to FRS 102
(Financial Reporting Standard applicable in the UK and Republic of Ireland).

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
    "FRSAccount",
    "FRS_UK",
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
class FRSAccount:
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


FRS_UK: dict[str, FRSAccount] = {
    # ─── 0: FIXED ASSETS ─────────────────────────────────────────────────────
    # Tangible
    "0010": FRSAccount("0010", "Tangible Fixed Assets",              _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0020": FRSAccount("0020", "Freehold Land & Buildings",          _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0030": FRSAccount("0030", "Leasehold Improvements",             _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0040": FRSAccount("0040", "Plant & Machinery",                  _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0050": FRSAccount("0050", "Motor Vehicles",                     _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0060": FRSAccount("0060", "Office Equipment & Furniture",       _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0070": FRSAccount("0070", "Computer Hardware & IT Equipment",   _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0080": FRSAccount("0080", "Accum. Depreciation — Buildings",    _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0085": FRSAccount("0085", "Accum. Depreciation — Plant",        _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0090": FRSAccount("0090", "Accum. Depreciation — Vehicles",     _BS, _G.FIXED_ASSETS_TANGIBLE),
    "0095": FRSAccount("0095", "Accum. Depreciation — IT",           _BS, _G.FIXED_ASSETS_TANGIBLE),
    # Intangible
    "0200": FRSAccount("0200", "Intangible Fixed Assets",            _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0210": FRSAccount("0210", "Goodwill",                           _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0220": FRSAccount("0220", "Intellectual Property / Patents",    _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0230": FRSAccount("0230", "Development Costs Capitalised",      _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0240": FRSAccount("0240", "Software (Capitalised)",             _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0280": FRSAccount("0280", "Accum. Amortisation — Goodwill",     _BS, _G.FIXED_ASSETS_INTANGIBLE),
    "0290": FRSAccount("0290", "Accum. Amortisation — Other Intang", _BS, _G.FIXED_ASSETS_INTANGIBLE),
    # Financial
    "0300": FRSAccount("0300", "Investments in Subsidiaries",        _BS, _G.FIXED_ASSETS_FINANCIAL),
    "0310": FRSAccount("0310", "Loans to Group Companies",           _BS, _G.FIXED_ASSETS_FINANCIAL),
    "0320": FRSAccount("0320", "Other Long-term Investments",        _BS, _G.FIXED_ASSETS_FINANCIAL),

    # ─── 1: CURRENT ASSETS ───────────────────────────────────────────────────
    "1000": FRSAccount("1000", "Stock / Inventories",                _BS, _G.CURRENT_ASSETS),
    "1010": FRSAccount("1010", "Raw Materials",                      _BS, _G.CURRENT_ASSETS),
    "1020": FRSAccount("1020", "Work in Progress",                   _BS, _G.CURRENT_ASSETS),
    "1030": FRSAccount("1030", "Finished Goods",                     _BS, _G.CURRENT_ASSETS),
    "1100": FRSAccount("1100", "Trade Debtors",                      _BS, _G.CURRENT_ASSETS),
    "1110": FRSAccount("1110", "Other Debtors",                      _BS, _G.CURRENT_ASSETS),
    "1120": FRSAccount("1120", "Prepayments",                        _BS, _G.CURRENT_ASSETS),
    "1130": FRSAccount("1130", "Accrued Income",                     _BS, _G.CURRENT_ASSETS),
    "1140": FRSAccount("1140", "VAT Recoverable",                    _BS, _G.CURRENT_ASSETS),
    "1150": FRSAccount("1150", "Corporation Tax Recoverable",        _BS, _G.CURRENT_ASSETS),
    "1160": FRSAccount("1160", "Loans to Directors / Officers",      _BS, _G.CURRENT_ASSETS),
    "1200": FRSAccount("1200", "Cash at Bank",                       _BS, _G.CURRENT_ASSETS),
    "1210": FRSAccount("1210", "Petty Cash",                         _BS, _G.CURRENT_ASSETS),
    "1220": FRSAccount("1220", "Short-term Deposits",                _BS, _G.CURRENT_ASSETS),

    # ─── 2: CREDITORS DUE WITHIN ONE YEAR ────────────────────────────────────
    "2000": FRSAccount("2000", "Trade Creditors",                    _BS, _G.CREDITORS_LT_1YR),
    "2010": FRSAccount("2010", "Accruals",                           _BS, _G.CREDITORS_LT_1YR),
    "2020": FRSAccount("2020", "Deferred Income",                    _BS, _G.CREDITORS_LT_1YR),
    "2030": FRSAccount("2030", "Bank Overdraft",                     _BS, _G.CREDITORS_LT_1YR),
    "2040": FRSAccount("2040", "Current Portion of Long-term Loans", _BS, _G.CREDITORS_LT_1YR),
    "2050": FRSAccount("2050", "VAT Payable",                        _BS, _G.CREDITORS_LT_1YR),
    "2060": FRSAccount("2060", "PAYE / NIC Payable",                 _BS, _G.CREDITORS_LT_1YR),
    "2070": FRSAccount("2070", "Corporation Tax Payable",            _BS, _G.CREDITORS_LT_1YR),
    "2080": FRSAccount("2080", "Dividend Payable",                   _BS, _G.CREDITORS_LT_1YR),
    "2090": FRSAccount("2090", "Directors' Loan Accounts",           _BS, _G.CREDITORS_LT_1YR),
    "2095": FRSAccount("2095", "Other Short-term Creditors",         _BS, _G.CREDITORS_LT_1YR),

    # ─── 3: CREDITORS DUE AFTER ONE YEAR ─────────────────────────────────────
    "3000": FRSAccount("3000", "Mortgage / Long-term Bank Loans",    _BS, _G.CREDITORS_GT_1YR),
    "3010": FRSAccount("3010", "Finance Lease Obligations",          _BS, _G.CREDITORS_GT_1YR),
    "3020": FRSAccount("3020", "Loans from Directors (>1yr)",        _BS, _G.CREDITORS_GT_1YR),
    "3030": FRSAccount("3030", "Debentures",                         _BS, _G.CREDITORS_GT_1YR),
    # Provisions 35xx
    "3500": FRSAccount("3500", "Provisions for Liabilities",         _BS, _G.PROVISIONS),
    "3510": FRSAccount("3510", "Deferred Tax Provision",             _BS, _G.PROVISIONS),
    "3520": FRSAccount("3520", "Warranty Provision",                 _BS, _G.PROVISIONS),
    "3530": FRSAccount("3530", "Restructuring Provision",            _BS, _G.PROVISIONS),

    # ─── 4: SHARE CAPITAL & RESERVES ─────────────────────────────────────────
    "4000": FRSAccount("4000", "Called-up Share Capital",            _BS, _G.SHARE_CAPITAL_RESERVES),
    "4010": FRSAccount("4010", "Share Premium Account",              _BS, _G.SHARE_CAPITAL_RESERVES),
    "4020": FRSAccount("4020", "Revaluation Reserve",                _BS, _G.SHARE_CAPITAL_RESERVES),
    "4030": FRSAccount("4030", "Capital Redemption Reserve",         _BS, _G.SHARE_CAPITAL_RESERVES),
    "4040": FRSAccount("4040", "Retained Earnings",                  _BS, _G.SHARE_CAPITAL_RESERVES),
    "4050": FRSAccount("4050", "Profit & Loss Account (current yr)", _BS, _G.SHARE_CAPITAL_RESERVES),

    # ─── 5: REVENUE ──────────────────────────────────────────────────────────
    "5000": FRSAccount("5000", "UK Sales",                           _PL, _G.REVENUE),
    "5010": FRSAccount("5010", "EU Sales (goods)",                   _PL, _G.REVENUE),
    "5020": FRSAccount("5020", "Export Sales (non-EU)",              _PL, _G.REVENUE),
    "5030": FRSAccount("5030", "Service Revenue",                    _PL, _G.REVENUE),
    "5040": FRSAccount("5040", "Rental Income",                      _PL, _G.REVENUE),
    "5050": FRSAccount("5050", "Grant Income",                       _PL, _G.REVENUE),
    "5060": FRSAccount("5060", "Other Operating Income",             _PL, _G.REVENUE),

    # ─── 6: COST OF SALES ────────────────────────────────────────────────────
    "6000": FRSAccount("6000", "Purchases — Materials",              _PL, _G.COST_OF_SALES),
    "6010": FRSAccount("6010", "Freight & Carriage Inward",          _PL, _G.COST_OF_SALES),
    "6020": FRSAccount("6020", "Direct Labour",                      _PL, _G.COST_OF_SALES),
    "6030": FRSAccount("6030", "Direct Overhead",                    _PL, _G.COST_OF_SALES),
    "6040": FRSAccount("6040", "Subcontractors",                     _PL, _G.COST_OF_SALES),
    "6050": FRSAccount("6050", "Opening Stock",                      _PL, _G.COST_OF_SALES),
    "6060": FRSAccount("6060", "Closing Stock",                      _PL, _G.COST_OF_SALES),

    # ─── 7: ADMIN & OVERHEAD ─────────────────────────────────────────────────
    "7000": FRSAccount("7000", "Directors' Remuneration",            _PL, _G.ADMIN_OVERHEAD),
    "7010": FRSAccount("7010", "Salaries & Wages",                   _PL, _G.ADMIN_OVERHEAD),
    "7020": FRSAccount("7020", "Employer NIC",                       _PL, _G.ADMIN_OVERHEAD),
    "7030": FRSAccount("7030", "Pension Contributions",              _PL, _G.ADMIN_OVERHEAD),
    "7040": FRSAccount("7040", "Rent & Rates",                       _PL, _G.ADMIN_OVERHEAD),
    "7050": FRSAccount("7050", "Light & Heat",                       _PL, _G.ADMIN_OVERHEAD),
    "7060": FRSAccount("7060", "Insurance",                          _PL, _G.ADMIN_OVERHEAD),
    "7070": FRSAccount("7070", "Repairs & Maintenance",              _PL, _G.ADMIN_OVERHEAD),
    "7080": FRSAccount("7080", "Telephone & Internet",               _PL, _G.ADMIN_OVERHEAD),
    "7090": FRSAccount("7090", "Postage & Stationery",               _PL, _G.ADMIN_OVERHEAD),
    "7100": FRSAccount("7100", "IT Costs & Software Licences",       _PL, _G.ADMIN_OVERHEAD),
    "7110": FRSAccount("7110", "Motor & Travel Expenses",            _PL, _G.ADMIN_OVERHEAD),
    "7120": FRSAccount("7120", "Subsistence & Entertaining",         _PL, _G.ADMIN_OVERHEAD),
    "7130": FRSAccount("7130", "Accountancy & Audit Fees",           _PL, _G.ADMIN_OVERHEAD),
    "7140": FRSAccount("7140", "Legal & Professional Fees",          _PL, _G.ADMIN_OVERHEAD),
    "7150": FRSAccount("7150", "Advertising & Marketing",            _PL, _G.ADMIN_OVERHEAD),
    "7160": FRSAccount("7160", "Bad Debts Written Off",              _PL, _G.ADMIN_OVERHEAD),
    "7170": FRSAccount("7170", "Depreciation — Tangible Assets",     _PL, _G.ADMIN_OVERHEAD),
    "7180": FRSAccount("7180", "Amortisation — Intangible Assets",   _PL, _G.ADMIN_OVERHEAD),
    "7190": FRSAccount("7190", "Sundry Expenses",                    _PL, _G.ADMIN_OVERHEAD),

    # ─── 8: FINANCE ──────────────────────────────────────────────────────────
    "8000": FRSAccount("8000", "Bank Interest Receivable",           _PL, _G.FINANCE),
    "8010": FRSAccount("8010", "Bank Interest Payable",              _PL, _G.FINANCE),
    "8020": FRSAccount("8020", "Loan Interest Payable",              _PL, _G.FINANCE),
    "8030": FRSAccount("8030", "Finance Lease Interest",             _PL, _G.FINANCE),
    "8040": FRSAccount("8040", "Bank Charges",                       _PL, _G.FINANCE),
    "8050": FRSAccount("8050", "Foreign Exchange Gains / (Losses)",  _PL, _G.FINANCE),

    # ─── 9: TAXATION ─────────────────────────────────────────────────────────
    "9000": FRSAccount("9000", "Corporation Tax Charge",             _PL, _G.TAXATION),
    "9010": FRSAccount("9010", "Deferred Tax (Charge) / Credit",     _PL, _G.TAXATION),
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_account(code: str) -> FRSAccount | None:
    """Return the FRSAccount for *code*, or None if not found."""
    return FRS_UK.get(code)


def accounts_by_group(group: str) -> list[FRSAccount]:
    """Return all accounts whose *group* matches the given string."""
    return [a for a in FRS_UK.values() if a.group == group]


# ── JSON export (side-effect on import: writes frs102_schema.json) ────────────

def _write_json() -> None:
    out = Path(__file__).with_name("frs102_schema.json")
    payload = [asdict(a) for a in FRS_UK.values()]
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


_write_json()
