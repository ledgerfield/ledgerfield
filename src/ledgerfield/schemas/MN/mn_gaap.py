"""Mongolia chart of accounts (IFRS as applied in Mongolia).

Mongolian companies report under IFRS. This chart layers Mongolia-specific tax
and payroll accounts on top of an IFRS structure:

CIT = Corporate Income Tax (10% / 25% two-band progressive).
VAT = Value Added Tax (10%).
SI  = Social Insurance contributions.

Amounts are denominated in Mongolian tögrög (MNT).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MNGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MN_GAAP: list[MNGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MNGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1020", "Khan Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1021", "Golomt Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1022", "Trade and Development Bank (TDB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1023", "XacBank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1024", "State Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MNGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MNGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MNGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MNGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    MNGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MNGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MNGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MNGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MNGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MNGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    MNGAAPAccount("1185", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MNGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MNGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MNGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MNGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MNGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MNGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MNGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MNGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MNGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1580", "Mineral Exploration and Evaluation Assets", "Asset", "Property, Plant and Equipment", "Debit"),
    MNGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MNGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MNGAAPAccount("1620", "Mining and Exploration Licences", "Asset", "Intangible Assets", "Debit"),
    MNGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MNGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MNGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MNGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MNGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MNGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MNGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    MNGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    MNGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    MNGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    MNGAAPAccount("2140", "Personal Income Tax Payable (Payroll)", "Liability", "Tax Payable", "Credit"),
    MNGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MNGAAPAccount("2220", "Social Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    MNGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MNGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MNGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MNGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MNGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MNGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MNGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),
    MNGAAPAccount("2430", "Rehabilitation / Mine Closure Provision", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MNGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    MNGAAPAccount("3010", "Owners' Current Account", "Equity", "Contributed Capital", "Credit"),
    MNGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    MNGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    MNGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MNGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MNGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MNGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MNGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MNGAAPAccount("4020", "Revenue — Exports (Minerals)", "Revenue", "Operating Revenue", "Credit"),
    MNGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MNGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MNGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MNGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MNGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MNGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MNGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MNGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MNGAAPAccount("5030", "Royalties (Mineral Resources)", "Expense", "Cost of Sales", "Debit"),
    MNGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MNGAAPAccount("6020", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MNGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    MNGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MNGAAPAccount("6110", "Utilities (Heating and Electricity)", "Expense", "Occupancy Costs", "Debit"),
    MNGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MNGAAPAccount("6200", "State Registration and Licence Fees", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MNGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MNGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MNGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
