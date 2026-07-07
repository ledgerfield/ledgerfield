"""Arab Republic of Egypt chart of accounts (Egyptian Accounting Standards).

Egyptian companies report under the Egyptian Accounting Standards (EAS),
which are closely aligned with IFRS. This chart layers Egypt-specific tax
and labour accounts on top of that structure:

CIT = Corporate Income Tax (22.5% standard, Law No. 91 of 2005).
VAT = Value Added Tax (14% standard, Law No. 67 of 2016).
WHT = Withholding Tax on certain domestic and non-resident payments.
Social insurance per the Social Insurance and Pensions Law No. 148 of 2019.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class EGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


EG_GAAP: list[EGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    EGGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1020", "National Bank of Egypt Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1021", "Banque Misr Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1022", "Commercial International Bank (CIB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1023", "Banque du Caire Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    EGGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    EGGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    EGGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    EGGAAPAccount("1120", "Notes Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    EGGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    EGGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    EGGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    EGGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    EGGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    EGGAAPAccount("1180", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    EGGAAPAccount("1190", "Withholding Tax Receivable (Prepaid CIT)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    EGGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    EGGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    EGGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    EGGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    EGGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    EGGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    EGGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    EGGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    EGGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1570", "Right-of-Use Asset", "Asset", "Property, Plant and Equipment", "Debit"),
    EGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    EGGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    EGGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    EGGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    EGGAAPAccount("1710", "Treasury Bills and Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    EGGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    EGGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    EGGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    EGGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    EGGAAPAccount("2040", "Notes Payable", "Liability", "Trade and Other Payables", "Credit"),
    EGGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    EGGAAPAccount("2110", "VAT Settlement Account", "Liability", "Tax Payable", "Credit"),
    EGGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    EGGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    EGGAAPAccount("2140", "Payroll Tax (Salary Tax) Payable", "Liability", "Tax Payable", "Credit"),
    EGGAAPAccount("2150", "Stamp Duty Payable", "Liability", "Tax Payable", "Credit"),
    EGGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    EGGAAPAccount("2210", "Social Insurance Payable (NOSI)", "Liability", "Employee Benefits", "Credit"),
    EGGAAPAccount("2220", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    EGGAAPAccount("2230", "End-of-Service Provision", "Liability", "Employee Benefits", "Credit"),
    EGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    EGGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    EGGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    EGGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    EGGAAPAccount("2410", "Lease Liability", "Liability", "Non-Current Liabilities", "Credit"),
    EGGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),
    EGGAAPAccount("2430", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    EGGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    EGGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    EGGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    EGGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    EGGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    EGGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    EGGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    EGGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    EGGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    EGGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    EGGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    EGGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    EGGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    EGGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    EGGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    EGGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    EGGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    EGGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    EGGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    EGGAAPAccount("6010", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    EGGAAPAccount("6020", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    EGGAAPAccount("6030", "Staff Training and Development", "Expense", "Staff Costs", "Debit"),
    EGGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    EGGAAPAccount("6110", "Utilities (Electricity / Water / Gas)", "Expense", "Occupancy Costs", "Debit"),
    EGGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    EGGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6210", "Government Fees and Stamp Duty", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    EGGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    EGGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    EGGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    EGGAAPAccount("6410", "Non-Recoverable VAT Expense", "Expense", "Tax Expense", "Debit"),
]
