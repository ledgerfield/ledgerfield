"""Georgia chart of accounts (IFRS as applied in Georgia).

Georgian entities report under IFRS. This chart layers Georgia-specific tax and
labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (Estonian model: 15% on distributed profit only).
VAT = Value Added Tax (18% standard).
PIT = Personal Income Tax withheld on payroll.

WARNING: Tax rates in this pack are AI-estimated and must be verified against
the Revenue Service (rs.ge) before production filing.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


GE_GAAP: list[GEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    GEGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1020", "TBC Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1021", "Bank of Georgia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1022", "Liberty Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1023", "ProCredit Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1031", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    GEGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    GEGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GEGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    GEGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    GEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    GEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    GEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    GEGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    GEGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    GEGAAPAccount("1185", "Advance Tax Payments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    GEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    GEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    GEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    GEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    GEGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    GEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    GEGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    GEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    GEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    GEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    GEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    GEGAAPAccount("1620", "State Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    GEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    GEGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    GEGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    GEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    GEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    GEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    GEGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    GEGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    GEGAAPAccount("2120", "Corporate Income Tax Payable (Distributed Profit)", "Liability", "Tax Payable", "Credit"),
    GEGAAPAccount("2130", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    GEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    GEGAAPAccount("2220", "Pension Contribution Payable", "Liability", "Employee Benefits", "Credit"),
    GEGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    GEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    GEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    GEGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    GEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    GEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    GEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    GEGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    GEGAAPAccount("3010", "Additional Paid-in Capital", "Equity", "Contributed Capital", "Credit"),
    GEGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    GEGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    GEGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    GEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    GEGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    GEGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    GEGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    GEGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    GEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    GEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    GEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    GEGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    GEGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    GEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    GEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    GEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    GEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    GEGAAPAccount("6020", "Pension Employer Contribution", "Expense", "Staff Costs", "Debit"),
    GEGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    GEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    GEGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    GEGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    GEGAAPAccount("6200", "State Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    GEGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    GEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    GEGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
