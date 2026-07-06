"""Republic of Cyprus chart of accounts (IFRS as adopted by the EU).

Cypriot companies report under IFRS as adopted by the EU (Companies Law,
Cap. 113). This chart layers Cyprus-specific tax and payroll accounts on
top of an IFRS structure:

CIT = Corporate Income Tax (12.5%, Income Tax Law 118(I)/2002).
SDC = Special Defence Contribution (passive income: dividends/interest 17%).
VAT = Value Added Tax (19% standard; 9%/5%/3% reduced).
GHS = General Healthcare System (GeSY) contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CYGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CY_GAAP: list[CYGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    CYGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    CYGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    CYGAAPAccount("1020", "Bank of Cyprus Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CYGAAPAccount("1021", "Hellenic Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CYGAAPAccount("1022", "Eurobank Cyprus Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CYGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CYGAAPAccount("1040", "Fixed Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    CYGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    CYGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    CYGAAPAccount("1120", "Receivables from Related Parties", "Asset", "Trade and Other Receivables", "Debit"),
    CYGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    CYGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    CYGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    CYGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    CYGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    CYGAAPAccount("1180", "VAT Receivable", "Asset", "Tax Receivable", "Debit"),
    CYGAAPAccount("1190", "Corporate Income Tax Refundable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    CYGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    CYGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    CYGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    CYGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    CYGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    CYGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    CYGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    CYGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    CYGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    CYGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    CYGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    CYGAAPAccount("1620", "Qualifying IP Assets (IP Box)", "Asset", "Intangible Assets", "Debit"),
    CYGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    CYGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    CYGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    CYGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    CYGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    CYGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    CYGAAPAccount("2100", "VAT Payable", "Liability", "Tax Payable", "Credit"),
    CYGAAPAccount("2110", "OSS VAT Payable (EU One Stop Shop)", "Liability", "Tax Payable", "Credit"),
    CYGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    CYGAAPAccount("2130", "Special Defence Contribution Payable", "Liability", "Tax Payable", "Credit"),
    CYGAAPAccount("2140", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    CYGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    CYGAAPAccount("2210", "Social Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    CYGAAPAccount("2220", "GHS (GeSY) Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    CYGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    CYGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    CYGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    CYGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    CYGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    CYGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    CYGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    CYGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    CYGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    CYGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    CYGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    CYGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    CYGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    CYGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    CYGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    CYGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    CYGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    CYGAAPAccount("4030", "Revenue — Exports (non-EU)", "Revenue", "Operating Revenue", "Credit"),
    CYGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    CYGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    CYGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    CYGAAPAccount("4210", "Qualifying IP Royalty Income (IP Box)", "Revenue", "Other Income", "Credit"),
    CYGAAPAccount("4220", "Dividend Income", "Revenue", "Other Income", "Credit"),
    CYGAAPAccount("4230", "Interest Income", "Revenue", "Other Income", "Credit"),
    CYGAAPAccount("4240", "Rental Income", "Revenue", "Other Income", "Credit"),
    CYGAAPAccount("4250", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    CYGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    CYGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    CYGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    CYGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    CYGAAPAccount("6010", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    CYGAAPAccount("6020", "GHS (GeSY) Employer Contribution", "Expense", "Staff Costs", "Debit"),
    CYGAAPAccount("6030", "Provident Fund Contribution", "Expense", "Staff Costs", "Debit"),
    CYGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    CYGAAPAccount("6110", "Utilities (EAC / Water Board)", "Expense", "Occupancy Costs", "Debit"),
    CYGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    CYGAAPAccount("6200", "Annual Company Levy and Registrar Fees", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6220", "Telecommunications (CYTA / Epic)", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    CYGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    CYGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    CYGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    CYGAAPAccount("6410", "Special Defence Contribution Expense", "Expense", "Tax Expense", "Debit"),
]
