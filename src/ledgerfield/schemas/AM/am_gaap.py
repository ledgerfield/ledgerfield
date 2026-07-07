"""Republic of Armenia chart of accounts (IFRS as applied in Armenia).

Armenian entities report under IFRS. This chart layers Armenia-specific tax and
labour accounts on top of an IFRS structure:

CIT = Corporate (Profit) Income Tax (18% on taxable profit).
VAT = Value Added Tax (20% standard).
PIT = Personal Income Tax withheld on payroll.

WARNING: Tax rates in this pack are AI-estimated and must be verified against
the State Revenue Committee (petekamutner.am) before production filing.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AM_GAAP: list[AMGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    AMGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1020", "Ardshinbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1021", "Ameriabank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1022", "Armbusinessbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1023", "Converse Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1031", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    AMGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    AMGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AMGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    AMGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    AMGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AMGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    AMGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    AMGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    AMGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    AMGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    AMGAAPAccount("1185", "Profit Tax Prepayments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    AMGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    AMGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    AMGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    AMGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    AMGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    AMGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    AMGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    AMGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    AMGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    AMGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    AMGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    AMGAAPAccount("1620", "State Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    AMGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    AMGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    AMGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    AMGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    AMGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    AMGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    AMGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    AMGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    AMGAAPAccount("2120", "Profit Tax Payable", "Liability", "Tax Payable", "Credit"),
    AMGAAPAccount("2130", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    AMGAAPAccount("2140", "Turnover Tax Payable", "Liability", "Tax Payable", "Credit"),
    AMGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    AMGAAPAccount("2220", "Social Payment (Pension) Payable", "Liability", "Employee Benefits", "Credit"),
    AMGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    AMGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    AMGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    AMGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    AMGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    AMGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    AMGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    AMGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    AMGAAPAccount("3010", "Additional Paid-in Capital", "Equity", "Contributed Capital", "Credit"),
    AMGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    AMGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    AMGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    AMGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    AMGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    AMGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    AMGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    AMGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    AMGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    AMGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    AMGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    AMGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    AMGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    AMGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    AMGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    AMGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    AMGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    AMGAAPAccount("6020", "Social Payment Employer Contribution", "Expense", "Staff Costs", "Debit"),
    AMGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    AMGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    AMGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    AMGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    AMGAAPAccount("6200", "State Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    AMGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    AMGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    AMGAAPAccount("6400", "Profit Tax Expense", "Expense", "Tax Expense", "Debit"),
]
