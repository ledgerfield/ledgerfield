"""Islamic Republic of Pakistan chart of accounts (IFRS as applied in Pakistan).

Pakistani companies report under IFRS as adopted by the Securities and
Exchange Commission of Pakistan (SECP), with the Companies Act 2017. This
chart layers Pakistan-specific tax and payroll accounts on top of an IFRS
structure:

CIT  = Corporate Income Tax (Income Tax Ordinance 2001; FBR).
GST  = Sales Tax on goods (Sales Tax Act 1990, 18% standard); provincial
       sales taxes on services (13-16%) are tracked separately.
WHT  = Withholding Tax — Pakistan runs a WHT-heavy regime, so both
       receivable (advance/adjustable) and payable accounts are included.
EOBI = Employees' Old-Age Benefits Institution contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PKGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


PK_GAAP: list[PKGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    PKGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1020", "Habib Bank (HBL) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1021", "United Bank (UBL) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1022", "MCB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1023", "Meezan Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1024", "National Bank of Pakistan Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PKGAAPAccount("1040", "Term Deposit Receipts (TDR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    PKGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PKGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    PKGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    PKGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PKGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    PKGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    PKGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    PKGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    PKGAAPAccount("1180", "Advance Income Tax (WHT Adjustable)", "Asset", "Tax Receivable", "Debit"),
    PKGAAPAccount("1185", "Input GST Receivable (Sales Tax)", "Asset", "Tax Receivable", "Debit"),
    PKGAAPAccount("1190", "Sales Tax Refund Claim", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    PKGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    PKGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    PKGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    PKGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    PKGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    PKGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    PKGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    PKGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    PKGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    PKGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    PKGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    PKGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    PKGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    PKGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    PKGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    PKGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    PKGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    PKGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    PKGAAPAccount("2100", "Output GST Payable (Sales Tax on Goods)", "Liability", "Tax Payable", "Credit"),
    PKGAAPAccount("2110", "Provincial Sales Tax on Services Payable", "Liability", "Tax Payable", "Credit"),
    PKGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    PKGAAPAccount("2125", "Super Tax Payable (s.4C)", "Liability", "Tax Payable", "Credit"),
    PKGAAPAccount("2130", "Withholding Tax Payable (as Withholding Agent)", "Liability", "Tax Payable", "Credit"),
    PKGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    PKGAAPAccount("2210", "Employee Income Tax Withheld Payable", "Liability", "Employee Benefits", "Credit"),
    PKGAAPAccount("2220", "Gratuity Provision", "Liability", "Employee Benefits", "Credit"),
    PKGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    PKGAAPAccount("2240", "EOBI Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    PKGAAPAccount("2250", "Provincial Social Security (PESSI/SESSI) Payable", "Liability", "Employee Benefits", "Credit"),
    PKGAAPAccount("2300", "Bank Overdraft / Running Finance", "Liability", "Borrowings", "Credit"),
    PKGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    PKGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    PKGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    PKGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    PKGAAPAccount("2420", "Director / Sponsor Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    PKGAAPAccount("3000", "Share Capital (Paid-Up)", "Equity", "Contributed Capital", "Credit"),
    PKGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    PKGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    PKGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    PKGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    PKGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    PKGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    PKGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    PKGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    PKGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    PKGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    PKGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    PKGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    PKGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    PKGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    PKGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    PKGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    PKGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    PKGAAPAccount("5030", "Import Duties and Customs Charges", "Expense", "Cost of Sales", "Debit"),
    PKGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    PKGAAPAccount("6010", "Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    PKGAAPAccount("6020", "EOBI Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PKGAAPAccount("6025", "Provincial Social Security Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PKGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    PKGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    PKGAAPAccount("6110", "Utilities (Electricity / Gas / Water)", "Expense", "Occupancy Costs", "Debit"),
    PKGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    PKGAAPAccount("6200", "SECP Filing and Registration Fees", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6230", "Telecommunications and Internet", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6280", "Non-Adjustable WHT Expense (Final Tax Regime)", "Expense", "Administrative Expenses", "Debit"),
    PKGAAPAccount("6300", "Finance Costs / Markup Expense", "Expense", "Finance Costs", "Debit"),
    PKGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    PKGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    PKGAAPAccount("6410", "Super Tax Expense (s.4C)", "Expense", "Tax Expense", "Debit"),
]
