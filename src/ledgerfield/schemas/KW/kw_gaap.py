"""State of Kuwait chart of accounts (IFRS as applied in Kuwait).

Kuwaiti companies report under IFRS. This chart layers Kuwait-specific tax and
labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (15% on foreign non-GCC ownership share).
Contract retention = 5% withheld on contract payments until tax clearance.
EOSB = End-of-Service Indemnity (Kuwait Labour Law No. 6 of 2010).
PIFSS = Public Institution for Social Security (Kuwaiti nationals only).

Kuwait has not implemented VAT as of the target period, so no VAT accounts are
included. Zakat/NLST accounts are included for listed-company completeness.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class KWGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


KW_GAAP: list[KWGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    KWGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1020", "National Bank of Kuwait (NBK) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1021", "Kuwait Finance House (KFH) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1022", "Gulf Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1023", "Burgan Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1024", "Boubyan Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    KWGAAPAccount("1040", "Wakala Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    KWGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KWGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    KWGAAPAccount("1120", "Contract Retention Receivable (5% Tax Retention)", "Asset", "Trade and Other Receivables", "Debit"),
    KWGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KWGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    KWGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    KWGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    KWGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    KWGAAPAccount("1180", "Tax Clearance Deposits Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    KWGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    KWGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    KWGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    KWGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    KWGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    KWGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    KWGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    KWGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    KWGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    KWGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    KWGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    KWGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    KWGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    KWGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    KWGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    KWGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    KWGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    KWGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    KWGAAPAccount("2040", "Contract Retention Payable (5% Tax Retention)", "Liability", "Trade and Other Payables", "Credit"),
    KWGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    KWGAAPAccount("2130", "Zakat and NLST Payable (Listed Companies)", "Liability", "Tax Payable", "Credit"),
    KWGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    KWGAAPAccount("2210", "Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    KWGAAPAccount("2220", "End-of-Service Indemnity Provision", "Liability", "Employee Benefits", "Credit"),
    KWGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    KWGAAPAccount("2240", "PIFSS Social Security Payable (Kuwaiti Nationals)", "Liability", "Employee Benefits", "Credit"),
    KWGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    KWGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    KWGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    KWGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    KWGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    KWGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    KWGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    KWGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    KWGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    KWGAAPAccount("3110", "Voluntary Reserve", "Equity", "Reserves", "Credit"),
    KWGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    KWGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    KWGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    KWGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    KWGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    KWGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    KWGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    KWGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    KWGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    KWGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    KWGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    KWGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    KWGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    KWGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    KWGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    KWGAAPAccount("6010", "End-of-Service Indemnity Expense", "Expense", "Staff Costs", "Debit"),
    KWGAAPAccount("6020", "PIFSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    KWGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    KWGAAPAccount("6040", "Residence Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    KWGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    KWGAAPAccount("6110", "Utilities (MEW)", "Expense", "Occupancy Costs", "Debit"),
    KWGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    KWGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6230", "Telecommunications (Zain / Ooredoo / stc)", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    KWGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    KWGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    KWGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    KWGAAPAccount("6410", "Zakat and NLST Expense (Listed Companies)", "Expense", "Tax Expense", "Debit"),
]
