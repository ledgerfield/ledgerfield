"""Republic of Uzbekistan chart of accounts (IFRS as applied in Uzbekistan).

Uzbek companies increasingly report under IFRS. This chart layers
Uzbekistan-specific tax and payroll accounts on top of an IFRS structure:

CIT = Corporate Income Tax (15% standard; 20% for banks, mobile operators, cement).
VAT = Value Added Tax (QQS, 12%).
PIT = Personal Income Tax withheld from salaries (12% flat, indicative).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


UZ_GAAP: list[UZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    UZGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1020", "NBU Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1021", "Ipoteka Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1022", "Kapitalbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1023", "Hamkorbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UZGAAPAccount("1040", "Short-Term Bank Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    UZGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UZGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    UZGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    UZGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UZGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    UZGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    UZGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    UZGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    UZGAAPAccount("1180", "VAT Receivable (Input QQS)", "Asset", "Tax Receivable", "Debit"),
    UZGAAPAccount("1190", "CIT Advance Payments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    UZGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    UZGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    UZGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    UZGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    UZGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    UZGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    UZGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    UZGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    UZGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    UZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    UZGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    UZGAAPAccount("1620", "State Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    UZGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    UZGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    UZGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    UZGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    UZGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    UZGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    UZGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    UZGAAPAccount("2110", "VAT Payable (Output QQS)", "Liability", "Tax Payable", "Credit"),
    UZGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    UZGAAPAccount("2130", "Personal Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    UZGAAPAccount("2140", "Excise Tax Payable", "Liability", "Tax Payable", "Credit"),
    UZGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    UZGAAPAccount("2210", "Social Tax Payable", "Liability", "Employee Benefits", "Credit"),
    UZGAAPAccount("2220", "Pension Fund Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    UZGAAPAccount("2230", "Trade Union / Social Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    UZGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    UZGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    UZGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    UZGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    UZGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    UZGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    UZGAAPAccount("2420", "Founder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    UZGAAPAccount("3000", "Charter Capital", "Equity", "Contributed Capital", "Credit"),
    UZGAAPAccount("3010", "Founders' Contributions", "Equity", "Contributed Capital", "Credit"),
    UZGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    UZGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    UZGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    UZGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    UZGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    UZGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    UZGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    UZGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    UZGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    UZGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    UZGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    UZGAAPAccount("4210", "Interest Income", "Revenue", "Other Income", "Credit"),
    UZGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    UZGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    UZGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    UZGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    UZGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    UZGAAPAccount("6010", "Social Tax Expense", "Expense", "Staff Costs", "Debit"),
    UZGAAPAccount("6020", "Employer Pension Contributions", "Expense", "Staff Costs", "Debit"),
    UZGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    UZGAAPAccount("6040", "Business Travel and Per Diems", "Expense", "Staff Costs", "Debit"),
    UZGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    UZGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    UZGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    UZGAAPAccount("6200", "State Registration and Licence Fees", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6210", "Government and Local Fees", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    UZGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    UZGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    UZGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
