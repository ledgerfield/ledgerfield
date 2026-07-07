"""Turkmenistan chart of accounts (IFRS-aligned as applied in Turkmenistan).

This chart layers Turkmenistan-specific tax and payroll accounts on top of an
IFRS-aligned structure:

CIT = Corporate (Profit) Income Tax (8% private/domestic / 20% state or foreign).
VAT = Value Added Tax (15% standard).
Social Insurance = mandatory pension/social contributions.

AI-estimated structure; verify against official Main State Tax Service guidance.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TM_GAAP: list[TMGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    TMGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1020", "Turkmenbashi Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1021", "Halkbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1022", "Daykhanbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1023", "Senagat Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1024", "Rysgal Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TMGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    TMGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TMGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    TMGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    TMGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TMGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    TMGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    TMGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    TMGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    TMGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    TMGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    TMGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    TMGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    TMGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    TMGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    TMGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    TMGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    TMGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    TMGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    TMGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    TMGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    TMGAAPAccount("1620", "State Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    TMGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    TMGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    TMGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    TMGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    TMGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    TMGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    TMGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    TMGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    TMGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    TMGAAPAccount("2130", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    TMGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    TMGAAPAccount("2220", "Social Insurance Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    TMGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    TMGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    TMGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    TMGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    TMGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    TMGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    TMGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    TMGAAPAccount("3000", "Charter Capital", "Equity", "Contributed Capital", "Credit"),
    TMGAAPAccount("3010", "Additional Paid-In Capital", "Equity", "Contributed Capital", "Credit"),
    TMGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    TMGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    TMGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    TMGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    TMGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    TMGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    TMGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    TMGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    TMGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    TMGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    TMGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    TMGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    TMGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    TMGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    TMGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    TMGAAPAccount("6020", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    TMGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    TMGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    TMGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    TMGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    TMGAAPAccount("6200", "State Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    TMGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    TMGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    TMGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
