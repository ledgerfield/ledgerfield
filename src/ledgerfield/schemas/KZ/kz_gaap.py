"""Republic of Kazakhstan chart of accounts (IFRS as applied in Kazakhstan).

Kazakh companies report under IFRS / NSFO. This chart layers Kazakhstan-specific
tax and payroll accounts on top of an IFRS structure:

CIT = Corporate Income Tax (КПН, 20%).
VAT = Value Added Tax (НДС, 12%).
IIT = Individual Income Tax (ИПН) withheld from salaries.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class KZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


KZ_GAAP: list[KZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    KZGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1020", "Halyk Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1021", "Kaspi Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1022", "Forte Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1023", "Bank CenterCredit Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    KZGAAPAccount("1040", "Short-Term Bank Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    KZGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KZGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    KZGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    KZGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KZGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    KZGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    KZGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    KZGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    KZGAAPAccount("1180", "VAT Receivable (Input НДС)", "Asset", "Tax Receivable", "Debit"),
    KZGAAPAccount("1190", "CIT Advance Payments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    KZGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    KZGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    KZGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    KZGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    KZGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    KZGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    KZGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    KZGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    KZGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    KZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    KZGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    KZGAAPAccount("1620", "Subsurface Use Rights", "Asset", "Intangible Assets", "Debit"),
    KZGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    KZGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    KZGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    KZGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    KZGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    KZGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    KZGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    KZGAAPAccount("2110", "VAT Payable (Output НДС)", "Liability", "Tax Payable", "Credit"),
    KZGAAPAccount("2120", "Corporate Income Tax Payable (КПН)", "Liability", "Tax Payable", "Credit"),
    KZGAAPAccount("2130", "Individual Income Tax Payable (ИПН)", "Liability", "Tax Payable", "Credit"),
    KZGAAPAccount("2140", "Mineral Extraction Tax Payable", "Liability", "Tax Payable", "Credit"),
    KZGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    KZGAAPAccount("2210", "Social Tax Payable", "Liability", "Employee Benefits", "Credit"),
    KZGAAPAccount("2220", "Pension Contributions Payable (ОПВ)", "Liability", "Employee Benefits", "Credit"),
    KZGAAPAccount("2230", "Social Insurance Contributions Payable (СО)", "Liability", "Employee Benefits", "Credit"),
    KZGAAPAccount("2240", "Medical Insurance Contributions Payable (ОСМС)", "Liability", "Employee Benefits", "Credit"),
    KZGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    KZGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    KZGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    KZGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    KZGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    KZGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    KZGAAPAccount("3000", "Share Capital (Charter Capital)", "Equity", "Contributed Capital", "Credit"),
    KZGAAPAccount("3010", "Participants' Contributions", "Equity", "Contributed Capital", "Credit"),
    KZGAAPAccount("3100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    KZGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    KZGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    KZGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    KZGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    KZGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    KZGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    KZGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    KZGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    KZGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    KZGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    KZGAAPAccount("4210", "Interest Income", "Revenue", "Other Income", "Credit"),
    KZGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    KZGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    KZGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    KZGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    KZGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    KZGAAPAccount("6010", "Social Tax Expense", "Expense", "Staff Costs", "Debit"),
    KZGAAPAccount("6020", "Employer Social Contributions", "Expense", "Staff Costs", "Debit"),
    KZGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    KZGAAPAccount("6040", "Business Travel and Per Diems", "Expense", "Staff Costs", "Debit"),
    KZGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    KZGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    KZGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    KZGAAPAccount("6200", "State Registration and Licence Fees", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6210", "Government and Local Fees", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    KZGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    KZGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    KZGAAPAccount("6400", "Corporate Income Tax Expense (КПН)", "Expense", "Tax Expense", "Debit"),
]
