"""Republic of North Macedonia chart of accounts (national GAAP / IFRS).

North Macedonian companies report under national accounting rules aligned with
IFRS. This chart layers North Macedonia-specific tax and labour accounts on top
of an IFRS-style structure:

CIT = Corporate Income Tax (Danok na dobivka, 10%).
VAT = Value Added Tax (DDV, 18%).

WARNING: rates referenced here are AI-estimated and must be source-verified
against the official tax authority before production filing.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MKGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MK_GAAP: list[MKGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MKGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1020", "Komercijalna Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1021", "Stopanska Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1022", "NLB Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1023", "Halkbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1024", "ProCredit Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MKGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MKGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MKGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MKGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    MKGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MKGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MKGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MKGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MKGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MKGAAPAccount("1180", "VAT Receivable (Input DDV)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MKGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MKGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MKGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MKGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MKGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MKGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MKGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MKGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MKGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MKGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MKGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MKGAAPAccount("1620", "Business Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    MKGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MKGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MKGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MKGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MKGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MKGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MKGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    MKGAAPAccount("2100", "VAT Payable (Output DDV)", "Liability", "Tax Payable", "Credit"),
    MKGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    MKGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    MKGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MKGAAPAccount("2210", "Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    MKGAAPAccount("2220", "Severance Provision", "Liability", "Employee Benefits", "Credit"),
    MKGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MKGAAPAccount("2240", "Social and Health Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    MKGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MKGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MKGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MKGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MKGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MKGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MKGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    MKGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    MKGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    MKGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    MKGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MKGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MKGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MKGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MKGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MKGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    MKGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MKGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MKGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MKGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MKGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MKGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MKGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MKGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MKGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MKGAAPAccount("6010", "Severance Expense", "Expense", "Staff Costs", "Debit"),
    MKGAAPAccount("6020", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MKGAAPAccount("6030", "Employee Health Insurance", "Expense", "Staff Costs", "Debit"),
    MKGAAPAccount("6040", "Work Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    MKGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MKGAAPAccount("6110", "Utilities (EVN)", "Expense", "Occupancy Costs", "Debit"),
    MKGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MKGAAPAccount("6200", "Business Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MKGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MKGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MKGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
