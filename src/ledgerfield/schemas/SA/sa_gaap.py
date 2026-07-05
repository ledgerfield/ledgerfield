"""Kingdom of Saudi Arabia chart of accounts (IFRS as endorsed by SOCPA).

Saudi entities report under IFRS as endorsed by the Saudi Organization for
Chartered and Professional Accountants (SOCPA). This chart layers Saudi tax
and labour accounts on top of an IFRS structure:

VAT   = Value Added Tax (15%).
CIT   = Corporate Income Tax (20% on foreign ownership share).
Zakat = 2.5% levy on the Zakat base (Saudi/GCC ownership share).
GOSI  = General Organization for Social Insurance.
EOSB  = End-of-Service Benefits (Saudi Labour Law).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


SA_GAAP: list[SAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    SAGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1020", "Al Rajhi Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1021", "Saudi National Bank (SNB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1022", "Riyad Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1023", "Banque Saudi Fransi Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1024", "Arab National Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SAGAAPAccount("1040", "Murabaha Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    SAGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    SAGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    SAGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    SAGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    SAGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    SAGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    SAGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    SAGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    SAGAAPAccount("1180", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    SAGAAPAccount("1185", "VAT Refund Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    SAGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    SAGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    SAGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    SAGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    SAGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    SAGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    SAGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    SAGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    SAGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    SAGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    SAGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    SAGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    SAGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    SAGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    SAGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    SAGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    SAGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    SAGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    SAGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    SAGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    SAGAAPAccount("2110", "VAT Payable — Net", "Liability", "Tax Payable", "Credit"),
    SAGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    SAGAAPAccount("2125", "Zakat Payable", "Liability", "Tax Payable", "Credit"),
    SAGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    SAGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    SAGAAPAccount("2210", "WPS Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    SAGAAPAccount("2220", "End-of-Service Benefits Provision", "Liability", "Employee Benefits", "Credit"),
    SAGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    SAGAAPAccount("2240", "GOSI Payable", "Liability", "Employee Benefits", "Credit"),
    SAGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    SAGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    SAGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    SAGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    SAGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    SAGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    SAGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    SAGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    SAGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    SAGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    SAGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    SAGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    SAGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    SAGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    SAGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    SAGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    SAGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    SAGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    SAGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    SAGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    SAGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    SAGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    SAGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    SAGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    SAGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    SAGAAPAccount("6010", "End-of-Service Benefits Expense", "Expense", "Staff Costs", "Debit"),
    SAGAAPAccount("6020", "GOSI Employer Contribution", "Expense", "Staff Costs", "Debit"),
    SAGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    SAGAAPAccount("6040", "Iqama and Work Permit Fees", "Expense", "Staff Costs", "Debit"),
    SAGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    SAGAAPAccount("6110", "Utilities (SEC / Water)", "Expense", "Occupancy Costs", "Debit"),
    SAGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    SAGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6230", "Telecommunications (STC / Mobily)", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    SAGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    SAGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    SAGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    SAGAAPAccount("6410", "Zakat Expense", "Expense", "Tax Expense", "Debit"),
    SAGAAPAccount("6900", "Irrecoverable VAT", "Expense", "Administrative Expenses", "Debit"),
]
