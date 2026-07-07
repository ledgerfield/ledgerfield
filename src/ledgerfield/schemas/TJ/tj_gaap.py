"""Republic of Tajikistan chart of accounts (IFRS as applied in Tajikistan).

Tajik companies report under IFRS. This chart layers Tajikistan-specific tax
and payroll accounts on top of an IFRS structure:

CIT = Corporate (Profit) Income Tax (18% standard / 13% producers).
VAT = Value Added Tax (~14% standard).
Social Tax = mandatory social insurance contributions.

AI-estimated structure; verify against official Tax Committee guidance.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TJGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TJ_GAAP: list[TJGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    TJGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1020", "Amonatbonk Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1021", "Orienbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1022", "Eskhata Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1023", "Alif Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1024", "Spitamen Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TJGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    TJGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TJGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    TJGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    TJGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TJGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    TJGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    TJGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    TJGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    TJGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    TJGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    TJGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    TJGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    TJGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    TJGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    TJGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    TJGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    TJGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    TJGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    TJGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    TJGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    TJGAAPAccount("1620", "State Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    TJGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    TJGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    TJGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    TJGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    TJGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    TJGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    TJGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    TJGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    TJGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    TJGAAPAccount("2130", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    TJGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    TJGAAPAccount("2220", "Social Tax Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    TJGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    TJGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    TJGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    TJGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    TJGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    TJGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    TJGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    TJGAAPAccount("3000", "Charter Capital", "Equity", "Contributed Capital", "Credit"),
    TJGAAPAccount("3010", "Additional Paid-In Capital", "Equity", "Contributed Capital", "Credit"),
    TJGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    TJGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    TJGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    TJGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    TJGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    TJGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    TJGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    TJGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    TJGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    TJGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    TJGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    TJGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    TJGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    TJGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    TJGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    TJGAAPAccount("6020", "Social Tax Employer Contribution", "Expense", "Staff Costs", "Debit"),
    TJGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    TJGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    TJGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    TJGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    TJGAAPAccount("6200", "State Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    TJGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    TJGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    TJGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
