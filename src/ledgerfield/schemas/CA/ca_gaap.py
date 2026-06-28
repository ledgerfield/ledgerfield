"""Canadian GAAP / IFRS chart of accounts.

Public companies use IFRS; private companies use ASPE
(Accounting Standards for Private Enterprises).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CAGAAPAccount:
    code: int
    name: str
    account_type: str


CA_GAAP: List[CAGAAPAccount] = [
    # ── Assets (1000-1999) ───────────────────────────────────────────────
    CAGAAPAccount(1010, "Cash and cash equivalents",        "asset"),
    CAGAAPAccount(1020, "GIC / term deposits",              "asset"),
    CAGAAPAccount(1110, "Accounts receivable",              "asset"),
    CAGAAPAccount(1120, "HST/GST receivable",               "asset"),
    CAGAAPAccount(1130, "Other receivables",                "asset"),
    CAGAAPAccount(1200, "Inventory",                        "asset"),
    CAGAAPAccount(1210, "Raw materials",                    "asset"),
    CAGAAPAccount(1220, "Work in progress",                 "asset"),
    CAGAAPAccount(1230, "Finished goods",                   "asset"),
    CAGAAPAccount(1300, "Prepaid expenses",                 "asset"),
    CAGAAPAccount(1310, "Deposits",                         "asset"),
    CAGAAPAccount(1500, "Property, plant and equipment",    "asset"),
    CAGAAPAccount(1510, "Land",                             "asset"),
    CAGAAPAccount(1520, "Buildings",                        "asset"),
    CAGAAPAccount(1530, "Equipment",                        "asset"),
    CAGAAPAccount(1540, "Leasehold improvements",           "asset"),
    CAGAAPAccount(1550, "Accumulated depreciation",         "contra_asset"),
    CAGAAPAccount(1600, "Intangible assets",                "asset"),
    CAGAAPAccount(1610, "Patents and trademarks",           "asset"),
    CAGAAPAccount(1620, "Goodwill",                         "asset"),
    CAGAAPAccount(1700, "Deferred tax asset",               "asset"),
    CAGAAPAccount(1800, "Long-term investments",            "asset"),

    # ── Liabilities (2000-2999) ──────────────────────────────────────────
    CAGAAPAccount(2010, "Accounts payable",                 "liability"),
    CAGAAPAccount(2020, "Accrued liabilities",              "liability"),
    CAGAAPAccount(2030, "HST/GST payable",                  "liability"),
    CAGAAPAccount(2040, "Income tax payable",               "liability"),
    CAGAAPAccount(2050, "Payroll liabilities (CPP/EI/tax)", "liability"),
    CAGAAPAccount(2060, "Deferred revenue",                 "liability"),
    CAGAAPAccount(2100, "Bank line of credit",              "liability"),
    CAGAAPAccount(2200, "Long-term debt",                   "liability"),
    CAGAAPAccount(2210, "Mortgage payable",                 "liability"),
    CAGAAPAccount(2300, "Lease liabilities (IFRS 16)",      "liability"),
    CAGAAPAccount(2400, "Deferred tax liability",           "liability"),

    # ── Equity (3000-3999) ───────────────────────────────────────────────
    CAGAAPAccount(3010, "Common shares",                    "equity"),
    CAGAAPAccount(3020, "Retained earnings",                "equity"),
    CAGAAPAccount(3030, "Contributed surplus",              "equity"),
    CAGAAPAccount(3040, "Accumulated OCI",                  "equity"),
    CAGAAPAccount(3050, "Current year net income",          "equity"),

    # ── Revenue (4000-4999) ──────────────────────────────────────────────
    CAGAAPAccount(4010, "Product sales",                    "revenue"),
    CAGAAPAccount(4020, "Service revenue",                  "revenue"),
    CAGAAPAccount(4030, "Grant income (SR&ED)",             "revenue"),
    CAGAAPAccount(4040, "Interest income",                  "revenue"),
    CAGAAPAccount(4050, "Other income",                     "revenue"),

    # ── Cost of Sales (5000-5999) ────────────────────────────────────────
    CAGAAPAccount(5010, "Cost of goods sold",               "cost_of_sales"),
    CAGAAPAccount(5020, "Direct labour",                    "cost_of_sales"),
    CAGAAPAccount(5030, "Manufacturing overhead",           "cost_of_sales"),

    # ── Operating Expenses (6000-6999) ───────────────────────────────────
    CAGAAPAccount(6010, "Salaries and wages",               "expense"),
    CAGAAPAccount(6020, "CPP employer contribution",        "expense"),
    CAGAAPAccount(6030, "EI employer premium",              "expense"),
    CAGAAPAccount(6040, "Employee benefits",                "expense"),
    CAGAAPAccount(6050, "Rent",                             "expense"),
    CAGAAPAccount(6060, "Utilities",                        "expense"),
    CAGAAPAccount(6070, "Office supplies",                  "expense"),
    CAGAAPAccount(6080, "Professional fees",                "expense"),
    CAGAAPAccount(6090, "Insurance",                        "expense"),
    CAGAAPAccount(6100, "Travel",                           "expense"),
    CAGAAPAccount(6110, "Marketing",                        "expense"),
    CAGAAPAccount(6120, "Depreciation and amortization",    "expense"),
    CAGAAPAccount(6130, "SR&ED (R&D)",                      "expense"),
    CAGAAPAccount(6140, "Bank charges",                     "expense"),
    CAGAAPAccount(6150, "Telephone and internet",           "expense"),

    # ── Other (7000+) ────────────────────────────────────────────────────
    CAGAAPAccount(7010, "Interest expense",                 "expense"),
    CAGAAPAccount(7020, "Income tax expense",               "expense"),
]
