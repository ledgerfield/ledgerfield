"""Bosnia and Herzegovina chart of accounts (IFRS as applied in BiH).

Companies in Bosnia and Herzegovina report under accounting rules aligned with
IFRS at entity level. This chart layers BiH-specific tax and labour accounts on
top of an IFRS structure:

CIT = Corporate Income Tax (10%, both FBiH and Republika Srpska).
VAT = Value Added Tax (17%, state-level via UINO/ITA).

AI-estimated pack — see params.json (source_status = ai_estimated_needs_verification).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


BA_GAAP: list[BAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    BAGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1020", "UniCredit Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1021", "Raiffeisen Bank BiH Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1022", "NLB Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1023", "Intesa Sanpaolo Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1031", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BAGAAPAccount("1040", "Short-Term Bank Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    BAGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BAGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    BAGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    BAGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BAGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    BAGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    BAGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    BAGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    BAGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    BAGAAPAccount("1185", "Prepaid Profit Tax", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    BAGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    BAGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    BAGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    BAGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    BAGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    BAGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    BAGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    BAGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    BAGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    BAGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    BAGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    BAGAAPAccount("1620", "Court Registration and Permits", "Asset", "Intangible Assets", "Debit"),
    BAGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    BAGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    BAGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    BAGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    BAGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    BAGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    BAGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    BAGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    BAGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    BAGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    BAGAAPAccount("2150", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    BAGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    BAGAAPAccount("2210", "Pension and Disability Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    BAGAAPAccount("2220", "Health Insurance Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    BAGAAPAccount("2230", "Unemployment Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    BAGAAPAccount("2240", "Vacation Pay Accrual", "Liability", "Employee Benefits", "Credit"),
    BAGAAPAccount("2300", "Short-Term Bank Loans", "Liability", "Borrowings", "Credit"),
    BAGAAPAccount("2310", "Current Portion of Long-Term Debt", "Liability", "Borrowings", "Credit"),
    BAGAAPAccount("2320", "Lease Liability (IFRS 16) — Current", "Liability", "Borrowings", "Credit"),
    BAGAAPAccount("2500", "Long-Term Bank Loans", "Liability", "Non-Current Liabilities", "Credit"),
    BAGAAPAccount("2510", "Lease Liability (IFRS 16) — Non-Current", "Liability", "Non-Current Liabilities", "Credit"),
    BAGAAPAccount("2520", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),
    BAGAAPAccount("2530", "Provisions", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    BAGAAPAccount("3000", "Share Capital", "Equity", "Capital", "Credit"),
    BAGAAPAccount("3010", "Share Premium", "Equity", "Capital", "Credit"),
    BAGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    BAGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    BAGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    BAGAAPAccount("3210", "Current Year Result", "Equity", "Retained Earnings", "Credit"),
    BAGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    BAGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    BAGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    BAGAAPAccount("4020", "Revenue — Contracts/Projects", "Revenue", "Operating Revenue", "Credit"),
    BAGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Contra Revenue", "Debit"),
    BAGAAPAccount("4110", "Sales Discounts", "Revenue", "Contra Revenue", "Debit"),
    BAGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    BAGAAPAccount("4210", "Foreign Exchange Gains", "Revenue", "Other Income", "Credit"),
    BAGAAPAccount("4220", "Interest Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    BAGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    BAGAAPAccount("5010", "Cost of Services", "Expense", "Cost of Sales", "Debit"),
    BAGAAPAccount("5020", "Direct Materials", "Expense", "Cost of Sales", "Debit"),
    BAGAAPAccount("5030", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    BAGAAPAccount("6000", "Salaries and Wages", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6010", "Social Contributions (Employer)", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6020", "Staff Welfare and Training", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6100", "Rent Expense", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6110", "Utilities", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6120", "Telecommunications and Internet", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6130", "Repairs and Maintenance", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6140", "Office Supplies", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6150", "Depreciation Expense", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6160", "Amortisation Expense", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6170", "Insurance", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6180", "Professional and Legal Fees", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6190", "Marketing and Advertising", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6200", "Travel and Transportation", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6210", "Bank Charges", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6220", "Foreign Exchange Losses", "Expense", "Operating Expenses", "Debit"),
    BAGAAPAccount("6300", "Interest Expense", "Expense", "Finance Costs", "Debit"),
    BAGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    BAGAAPAccount("6410", "Deferred Tax Expense", "Expense", "Tax Expense", "Debit"),
]
