"""Republic of Azerbaijan chart of accounts (IFRS as applied in Azerbaijan).

Azerbaijani companies report under National Accounting Standards aligned with
IFRS. This chart layers Azerbaijan-specific tax and labour accounts on top of an
IFRS structure:

CIT = Corporate Profit Tax (20%).
VAT = Value Added Tax (18%).
SSC = State Social Protection Fund contributions (social insurance).

AI-estimated pack — see params.json (source_status = ai_estimated_needs_verification).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AZ_GAAP: list[AZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    AZGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1020", "International Bank of Azerbaijan Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1021", "Kapital Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1022", "PASHA Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1023", "ABB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1031", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    AZGAAPAccount("1040", "Short-Term Bank Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    AZGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AZGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    AZGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    AZGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AZGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    AZGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    AZGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    AZGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    AZGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    AZGAAPAccount("1185", "Prepaid Profit Tax", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    AZGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    AZGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    AZGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    AZGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    AZGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    AZGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    AZGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    AZGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    AZGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    AZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    AZGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    AZGAAPAccount("1620", "State Registration and Permits", "Asset", "Intangible Assets", "Debit"),
    AZGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    AZGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    AZGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    AZGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    AZGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    AZGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    AZGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    AZGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    AZGAAPAccount("2120", "Corporate Profit Tax Payable", "Liability", "Tax Payable", "Credit"),
    AZGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    AZGAAPAccount("2140", "Simplified Tax Payable", "Liability", "Tax Payable", "Credit"),
    AZGAAPAccount("2150", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    AZGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    AZGAAPAccount("2210", "Social Protection Fund Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    AZGAAPAccount("2220", "Unemployment Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    AZGAAPAccount("2230", "Mandatory Medical Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    AZGAAPAccount("2240", "Vacation Pay Accrual", "Liability", "Employee Benefits", "Credit"),
    AZGAAPAccount("2300", "Short-Term Bank Loans", "Liability", "Borrowings", "Credit"),
    AZGAAPAccount("2310", "Current Portion of Long-Term Debt", "Liability", "Borrowings", "Credit"),
    AZGAAPAccount("2320", "Lease Liability (IFRS 16) — Current", "Liability", "Borrowings", "Credit"),
    AZGAAPAccount("2500", "Long-Term Bank Loans", "Liability", "Non-Current Liabilities", "Credit"),
    AZGAAPAccount("2510", "Lease Liability (IFRS 16) — Non-Current", "Liability", "Non-Current Liabilities", "Credit"),
    AZGAAPAccount("2520", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),
    AZGAAPAccount("2530", "Provisions", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    AZGAAPAccount("3000", "Share Capital (Charter Capital)", "Equity", "Capital", "Credit"),
    AZGAAPAccount("3010", "Share Premium", "Equity", "Capital", "Credit"),
    AZGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    AZGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    AZGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    AZGAAPAccount("3210", "Current Year Result", "Equity", "Retained Earnings", "Credit"),
    AZGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    AZGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    AZGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    AZGAAPAccount("4020", "Revenue — Contracts/Projects", "Revenue", "Operating Revenue", "Credit"),
    AZGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Contra Revenue", "Debit"),
    AZGAAPAccount("4110", "Sales Discounts", "Revenue", "Contra Revenue", "Debit"),
    AZGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    AZGAAPAccount("4210", "Foreign Exchange Gains", "Revenue", "Other Income", "Credit"),
    AZGAAPAccount("4220", "Interest Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    AZGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    AZGAAPAccount("5010", "Cost of Services", "Expense", "Cost of Sales", "Debit"),
    AZGAAPAccount("5020", "Direct Materials", "Expense", "Cost of Sales", "Debit"),
    AZGAAPAccount("5030", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    AZGAAPAccount("6000", "Salaries and Wages", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6010", "Social Protection Fund Contributions (Employer)", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6020", "Staff Welfare and Training", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6100", "Rent Expense", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6110", "Utilities", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6120", "Telecommunications and Internet", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6130", "Repairs and Maintenance", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6140", "Office Supplies", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6150", "Depreciation Expense", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6160", "Amortisation Expense", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6170", "Insurance", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6180", "Professional and Legal Fees", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6190", "Marketing and Advertising", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6200", "Travel and Transportation", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6210", "Bank Charges", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6220", "Foreign Exchange Losses", "Expense", "Operating Expenses", "Debit"),
    AZGAAPAccount("6300", "Interest Expense", "Expense", "Finance Costs", "Debit"),
    AZGAAPAccount("6400", "Corporate Profit Tax Expense", "Expense", "Tax Expense", "Debit"),
    AZGAAPAccount("6410", "Deferred Tax Expense", "Expense", "Tax Expense", "Debit"),
]
