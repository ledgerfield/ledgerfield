"""Republic of Albania chart of accounts (National Accounting Standards / IFRS).

Albanian companies report under the National Accounting Standards (Standardet
Kombetare te Kontabilitetit) or IFRS. This chart layers Albania-specific tax
and labour accounts on top of an IFRS-style structure:

CIT = Corporate Income Tax (Tatimi mbi Fitimin, 15%).
VAT = Value Added Tax (TVSH, 20%).

WARNING: rates referenced here are AI-estimated and must be source-verified
against the official tax authority before production filing.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ALGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AL_GAAP: list[ALGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ALGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1020", "Banka Kombetare Tregtare (BKT) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1021", "Raiffeisen Bank Albania Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1022", "Credins Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1023", "Intesa Sanpaolo Bank Albania Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1024", "OTP Bank Albania Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ALGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ALGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ALGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    ALGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    ALGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ALGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ALGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ALGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    ALGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    ALGAAPAccount("1180", "VAT Receivable (Input TVSH)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ALGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ALGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ALGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ALGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    ALGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ALGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ALGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ALGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ALGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    ALGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ALGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ALGAAPAccount("1620", "Business Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    ALGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    ALGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ALGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    ALGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ALGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    ALGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    ALGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    ALGAAPAccount("2100", "VAT Payable (Output TVSH)", "Liability", "Tax Payable", "Credit"),
    ALGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    ALGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    ALGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    ALGAAPAccount("2210", "Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    ALGAAPAccount("2220", "Severance Provision", "Liability", "Employee Benefits", "Credit"),
    ALGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ALGAAPAccount("2240", "Social and Health Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    ALGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ALGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ALGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    ALGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    ALGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    ALGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ALGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    ALGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    ALGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    ALGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    ALGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    ALGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ALGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ALGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    ALGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    ALGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    ALGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ALGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ALGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ALGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    ALGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ALGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ALGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ALGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ALGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ALGAAPAccount("6010", "Severance Expense", "Expense", "Staff Costs", "Debit"),
    ALGAAPAccount("6020", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    ALGAAPAccount("6030", "Employee Health Insurance", "Expense", "Staff Costs", "Debit"),
    ALGAAPAccount("6040", "Work Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    ALGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    ALGAAPAccount("6110", "Utilities (OSHEE)", "Expense", "Occupancy Costs", "Debit"),
    ALGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    ALGAAPAccount("6200", "Business Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    ALGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    ALGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    ALGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
