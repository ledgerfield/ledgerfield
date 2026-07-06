"""State of Israel chart of accounts (Israeli GAAP / IFRS as applied in Israel).

Israeli public companies report under IFRS; private companies commonly apply
Israeli GAAP (Israel Accounting Standards Board). This chart layers
Israel-specific tax and labour accounts on top of an IFRS-style structure:

CIT = Corporate Income Tax (23% flat, Income Tax Ordinance).
VAT = Value Added Tax (Ma'am) — 18% effective 1 January 2025 (raised from 17%).
Bituach Leumi = National Insurance (plus health insurance) contributions.
Severance = statutory severance pay provision (Severance Pay Law 5723-1963,
often funded via Section 14 arrangements).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ILGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


IL_GAAP: list[ILGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ILGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1020", "Bank Hapoalim Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1021", "Bank Leumi Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1022", "Mizrahi-Tefahot Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1023", "Israel Discount Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ILGAAPAccount("1040", "Short-Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ILGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ILGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    ILGAAPAccount("1120", "Checks Receivable (Post-Dated)", "Asset", "Trade and Other Receivables", "Debit"),
    ILGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ILGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ILGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ILGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    ILGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    ILGAAPAccount("1180", "Input VAT Receivable (Ma'am Tshumot)", "Asset", "Tax Receivable", "Debit"),
    ILGAAPAccount("1190", "Income Tax Advances (Mikdamot)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ILGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ILGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ILGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ILGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    ILGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ILGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ILGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ILGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ILGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    ILGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ILGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ILGAAPAccount("1620", "Capitalised Development Costs", "Asset", "Intangible Assets", "Debit"),
    ILGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    ILGAAPAccount("1710", "Severance Fund Deposits (Kupat Pitzuim)", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ILGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    ILGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ILGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    ILGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    ILGAAPAccount("2040", "Checks Payable (Post-Dated)", "Liability", "Trade and Other Payables", "Credit"),
    ILGAAPAccount("2100", "Output VAT Payable (Ma'am Askaot)", "Liability", "Tax Payable", "Credit"),
    ILGAAPAccount("2110", "VAT Settlement Account", "Liability", "Tax Payable", "Credit"),
    ILGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    ILGAAPAccount("2130", "Payroll Tax Withheld (Nikuy Mas)", "Liability", "Tax Payable", "Credit"),
    ILGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    ILGAAPAccount("2210", "Bituach Leumi Payable (National Insurance)", "Liability", "Employee Benefits", "Credit"),
    ILGAAPAccount("2220", "Severance Pay Provision (Pitzuim)", "Liability", "Employee Benefits", "Credit"),
    ILGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ILGAAPAccount("2240", "Pension Fund Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    ILGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ILGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ILGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    ILGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    ILGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    ILGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ILGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    ILGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    ILGAAPAccount("3100", "Capital Reserves", "Equity", "Reserves", "Credit"),
    ILGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    ILGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ILGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ILGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    ILGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    ILGAAPAccount("4020", "Revenue — Exports (Zero-Rated VAT)", "Revenue", "Operating Revenue", "Credit"),
    ILGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ILGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ILGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ILGAAPAccount("4210", "Government Grants (Innovation Authority)", "Revenue", "Other Income", "Credit"),
    ILGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ILGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ILGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ILGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ILGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ILGAAPAccount("6010", "Severance Pay Expense (Pitzuim)", "Expense", "Staff Costs", "Debit"),
    ILGAAPAccount("6020", "Bituach Leumi Employer Contribution", "Expense", "Staff Costs", "Debit"),
    ILGAAPAccount("6030", "Pension and Provident Fund Contributions", "Expense", "Staff Costs", "Debit"),
    ILGAAPAccount("6040", "Advanced Study Fund (Keren Hishtalmut)", "Expense", "Staff Costs", "Debit"),
    ILGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    ILGAAPAccount("6110", "Utilities and Municipal Taxes (Arnona)", "Expense", "Occupancy Costs", "Debit"),
    ILGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    ILGAAPAccount("6200", "Company Registration and Annual Fees", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6210", "Government and Regulatory Fees", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6280", "Non-Deductible VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    ILGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    ILGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    ILGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
