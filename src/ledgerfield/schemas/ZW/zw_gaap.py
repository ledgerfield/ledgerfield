"""Zimbabwe chart of accounts (IFRS as applied in Zimbabwe).

Zimbabwean companies report under IFRS. This chart layers Zimbabwe-specific
tax and payroll accounts on top of an IFRS structure:

CIT  = Corporate Income Tax (25% + 3% AIDS levy on the tax, effective 25.75%).
VAT  = Value Added Tax (15% standard rate).
IMTT = Intermediated Money Transfer Tax (2% on electronic transfers).
NSSA = National Social Security Authority contributions.

Zimbabwe operates a dual-currency regime (ZWG and USD), reflected in the
bank and foreign-currency accounts below.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ZWGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


ZW_GAAP: list[ZWGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ZWGAAPAccount("1010", "Cash on Hand (ZWG)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1015", "Cash on Hand (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1020", "CBZ Bank Account (ZWG)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1021", "Stanbic Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1022", "FBC Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1023", "Nostro FCA Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1024", "EcoCash Mobile Money Wallet", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZWGAAPAccount("1030", "Short-Term Money Market Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ZWGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ZWGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    ZWGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ZWGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ZWGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ZWGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    ZWGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    ZWGAAPAccount("1170", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    ZWGAAPAccount("1180", "Provisional Tax Paid (QPDs)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ZWGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ZWGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ZWGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ZWGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    ZWGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ZWGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ZWGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ZWGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ZWGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    ZWGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ZWGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ZWGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ZWGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    ZWGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ZWGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    ZWGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    ZWGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    ZWGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    ZWGAAPAccount("2125", "AIDS Levy Payable", "Liability", "Tax Payable", "Credit"),
    ZWGAAPAccount("2130", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    ZWGAAPAccount("2140", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    ZWGAAPAccount("2150", "IMTT Payable", "Liability", "Tax Payable", "Credit"),
    ZWGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    ZWGAAPAccount("2210", "NSSA Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    ZWGAAPAccount("2220", "ZIMDEF / Standards Levy Payable", "Liability", "Employee Benefits", "Credit"),
    ZWGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ZWGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ZWGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ZWGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    ZWGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    ZWGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ZWGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    ZWGAAPAccount("3100", "Non-Distributable Reserve", "Equity", "Reserves", "Credit"),
    ZWGAAPAccount("3110", "Currency Translation Reserve (ZWG/USD)", "Equity", "Reserves", "Credit"),
    ZWGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    ZWGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ZWGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ZWGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    ZWGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    ZWGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    ZWGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ZWGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ZWGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ZWGAAPAccount("4210", "Foreign Exchange Gain (ZWG/USD)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ZWGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ZWGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ZWGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ZWGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ZWGAAPAccount("6010", "NSSA Employer Contribution", "Expense", "Staff Costs", "Debit"),
    ZWGAAPAccount("6020", "ZIMDEF / Training Levy Expense", "Expense", "Staff Costs", "Debit"),
    ZWGAAPAccount("6030", "Employee Medical Aid", "Expense", "Staff Costs", "Debit"),
    ZWGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    ZWGAAPAccount("6110", "Utilities (ZESA / Municipal Water)", "Expense", "Occupancy Costs", "Debit"),
    ZWGAAPAccount("6200", "Licences and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6220", "Telecommunications (Econet / NetOne)", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6245", "IMTT Expense (2% Transfer Tax)", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    ZWGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    ZWGAAPAccount("6310", "Foreign Exchange Loss (ZWG/USD)", "Expense", "Finance Costs", "Debit"),
    ZWGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    ZWGAAPAccount("6410", "AIDS Levy Expense", "Expense", "Tax Expense", "Debit"),
]
