"""Papua New Guinea chart of accounts (IFRS as applied in PNG).

PNG companies report under IFRS. This chart layers PNG-specific tax and labour
accounts on top of an IFRS structure:

CIT = Corporate Income Tax (30% resident / 48% non-resident).
GST = Goods and Services Tax (10%).
Nasfund / NamBawan = superannuation (retirement) contributions.

NOTE: Tax rates referenced here are AI-estimated and require verification
against official IRC guidance.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


PG_GAAP: list[PGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    PGGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1020", "BSP (Bank South Pacific) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1021", "Kina Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1022", "ANZ PNG Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1023", "Westpac PNG Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PGGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    PGGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PGGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    PGGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    PGGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PGGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    PGGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    PGGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    PGGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    PGGAAPAccount("1180", "GST Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    PGGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    PGGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    PGGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    PGGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    PGGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    PGGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    PGGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    PGGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    PGGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    PGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    PGGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    PGGAAPAccount("1620", "Mining / Exploration Rights", "Asset", "Intangible Assets", "Debit"),
    PGGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    PGGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    PGGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    PGGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    PGGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    PGGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    PGGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    PGGAAPAccount("2100", "GST Output (Payable)", "Liability", "Tax Payable", "Credit"),
    PGGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    PGGAAPAccount("2130", "Salary/Wages Tax (PAYE) Payable", "Liability", "Tax Payable", "Credit"),
    PGGAAPAccount("2140", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    PGGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    PGGAAPAccount("2210", "Superannuation (Nasfund) Payable", "Liability", "Employee Benefits", "Credit"),
    PGGAAPAccount("2220", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    PGGAAPAccount("2230", "Long-Service Leave Provision", "Liability", "Employee Benefits", "Credit"),
    PGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    PGGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    PGGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    PGGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    PGGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    PGGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    PGGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    PGGAAPAccount("3010", "Shareholders' Current Account", "Equity", "Contributed Capital", "Credit"),
    PGGAAPAccount("3100", "General Reserve", "Equity", "Reserves", "Credit"),
    PGGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    PGGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    PGGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    PGGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    PGGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    PGGAAPAccount("4020", "Revenue — Resources / Commodities", "Revenue", "Operating Revenue", "Credit"),
    PGGAAPAccount("4030", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    PGGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    PGGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    PGGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    PGGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    PGGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    PGGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    PGGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    PGGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    PGGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    PGGAAPAccount("6010", "Superannuation Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PGGAAPAccount("6020", "Staff Training", "Expense", "Staff Costs", "Debit"),
    PGGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    PGGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    PGGAAPAccount("6110", "Electricity (PNG Power) and Water", "Expense", "Occupancy Costs", "Debit"),
    PGGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    PGGAAPAccount("6200", "Business Licence Renewal", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6210", "Government and Provincial Fees", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    PGGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    PGGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    PGGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
