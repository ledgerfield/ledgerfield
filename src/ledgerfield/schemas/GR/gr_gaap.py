"""Hellenic Republic (Greece) chart of accounts (Greek GAAP / ELP).

Greek companies report under Greek Accounting Standards (Law 4308/2014,
"Ellinika Logistika Protypa" / ELP); listed groups use IFRS as adopted by
the EU. This chart layers Greece-specific tax and payroll accounts on top
of an ELP/IFRS-compatible structure:

CIT = Corporate Income Tax (22%, Law 4172/2013; credit institutions 29%).
FPA = Value Added Tax (24% standard; 13%/6% reduced; island reductions).
EFKA = Unified Social Security Fund contributions.
myDATA = AADE electronic books platform.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GRGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


GR_GAAP: list[GRGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    GRGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1020", "National Bank of Greece Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1021", "Piraeus Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1022", "Alpha Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1023", "Eurobank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    GRGAAPAccount("1040", "Fixed Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    GRGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GRGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    GRGAAPAccount("1120", "Cheques Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    GRGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GRGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    GRGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    GRGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    GRGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    GRGAAPAccount("1180", "VAT (FPA) Receivable", "Asset", "Tax Receivable", "Debit"),
    GRGAAPAccount("1190", "Advance Corporate Income Tax Paid", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    GRGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    GRGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    GRGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    GRGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    GRGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    GRGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    GRGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    GRGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    GRGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    GRGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    GRGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    GRGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    GRGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    GRGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    GRGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    GRGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    GRGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    GRGAAPAccount("2040", "Cheques Payable", "Liability", "Trade and Other Payables", "Credit"),
    GRGAAPAccount("2100", "VAT (FPA) Payable", "Liability", "Tax Payable", "Credit"),
    GRGAAPAccount("2110", "OSS VAT Payable (EU One Stop Shop)", "Liability", "Tax Payable", "Credit"),
    GRGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    GRGAAPAccount("2130", "Withholding Taxes Payable", "Liability", "Tax Payable", "Credit"),
    GRGAAPAccount("2140", "Payroll Tax (FMY) Payable", "Liability", "Tax Payable", "Credit"),
    GRGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    GRGAAPAccount("2210", "EFKA Social Security Payable", "Liability", "Employee Benefits", "Credit"),
    GRGAAPAccount("2220", "Leave Pay and Bonus Provision (Doro)", "Liability", "Employee Benefits", "Credit"),
    GRGAAPAccount("2230", "Staff Retirement Indemnity Provision", "Liability", "Employee Benefits", "Credit"),
    GRGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    GRGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    GRGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    GRGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    GRGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    GRGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    GRGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    GRGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    GRGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    GRGAAPAccount("3110", "Tax-Free Reserves", "Equity", "Reserves", "Credit"),
    GRGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    GRGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    GRGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    GRGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    GRGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    GRGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    GRGAAPAccount("4030", "Revenue — Exports (non-EU)", "Revenue", "Operating Revenue", "Credit"),
    GRGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    GRGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    GRGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    GRGAAPAccount("4210", "Dividend Income", "Revenue", "Other Income", "Credit"),
    GRGAAPAccount("4220", "Interest Income", "Revenue", "Other Income", "Credit"),
    GRGAAPAccount("4230", "Rental Income", "Revenue", "Other Income", "Credit"),
    GRGAAPAccount("4240", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    GRGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    GRGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    GRGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    GRGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    GRGAAPAccount("6010", "EFKA Employer Contribution", "Expense", "Staff Costs", "Debit"),
    GRGAAPAccount("6020", "Holiday Bonuses (Easter/Christmas Doro)", "Expense", "Staff Costs", "Debit"),
    GRGAAPAccount("6030", "Staff Retirement Indemnity Expense", "Expense", "Staff Costs", "Debit"),
    GRGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    GRGAAPAccount("6110", "Utilities (DEI / EYDAP)", "Expense", "Occupancy Costs", "Debit"),
    GRGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    GRGAAPAccount("6200", "GEMI Registry and Chamber Fees", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6220", "myDATA / E-Invoicing Platform Fees", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6230", "Telecommunications (OTE / Cosmote)", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    GRGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    GRGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    GRGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    GRGAAPAccount("6410", "Non-Deductible Taxes and Levies", "Expense", "Tax Expense", "Debit"),
]
