"""Kyrgyz Republic chart of accounts (IFRS as applied in Kyrgyzstan).

Kyrgyz companies report under IFRS. This chart layers Kyrgyzstan-specific tax
and payroll accounts on top of an IFRS structure:

CIT = Corporate Income (Profit) Tax (10% flat).
VAT = Value Added Tax (12% standard).
SALES TAX = Turnover-based sales tax on gross revenue.
Social Fund = mandatory social insurance contributions.

AI-estimated structure; verify against official State Tax Service guidance.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class KGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


KG_GAAP: list[KGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    KGGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1020", "Optima Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1021", "Demir Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1022", "RSK Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1023", "Bakai Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1024", "Aiyl Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    KGGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    KGGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KGGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    KGGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    KGGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KGGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    KGGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    KGGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    KGGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    KGGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    KGGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    KGGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    KGGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    KGGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    KGGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    KGGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    KGGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    KGGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    KGGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    KGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    KGGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    KGGAAPAccount("1620", "State Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    KGGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    KGGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    KGGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    KGGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    KGGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    KGGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    KGGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    KGGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    KGGAAPAccount("2110", "Sales Tax Payable", "Liability", "Tax Payable", "Credit"),
    KGGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    KGGAAPAccount("2130", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    KGGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    KGGAAPAccount("2220", "Social Fund Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    KGGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    KGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    KGGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    KGGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    KGGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    KGGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    KGGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    KGGAAPAccount("3000", "Charter Capital", "Equity", "Contributed Capital", "Credit"),
    KGGAAPAccount("3010", "Additional Paid-In Capital", "Equity", "Contributed Capital", "Credit"),
    KGGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    KGGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    KGGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    KGGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    KGGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    KGGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    KGGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    KGGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    KGGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    KGGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    KGGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    KGGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    KGGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    KGGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    KGGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    KGGAAPAccount("6020", "Social Fund Employer Contribution", "Expense", "Staff Costs", "Debit"),
    KGGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    KGGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    KGGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    KGGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    KGGAAPAccount("6200", "State Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6280", "Sales Tax Expense", "Expense", "Administrative Expenses", "Debit"),
    KGGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    KGGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    KGGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
