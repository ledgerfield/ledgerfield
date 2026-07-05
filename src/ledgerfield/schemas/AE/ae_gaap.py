"""United Arab Emirates chart of accounts (IFRS as applied in the UAE).

UAE-incorporated companies prepare financial statements under IFRS (there is no
separate national GAAP). This chart layers UAE-specific tax and labour accounts
on top of an IFRS structure:

VAT  = Value Added Tax (5%, standard/zero-rated/exempt).
CT   = Corporate Tax (0% up to AED 375,000, 9% above; Free Zone regime).
EOSB = End-of-Service Benefits / gratuity provision (UAE Labour Law).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AE_GAAP: list[AEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    # Cash and bank
    AEGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1020", "Emirates NBD Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1021", "First Abu Dhabi Bank (FAB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1022", "Abu Dhabi Commercial Bank (ADCB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1023", "Mashreq Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1024", "Dubai Islamic Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1025", "Abu Dhabi Islamic Bank (ADIB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    AEGAAPAccount("1040", "Term Deposit (Wakala)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    AEGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AEGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    AEGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    AEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    AEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    AEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    AEGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    AEGAAPAccount("1180", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    AEGAAPAccount("1185", "VAT Refund Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    AEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    AEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    AEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    AEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    AEGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    AEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    AEGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    AEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    AEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    AEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    AEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    AEGAAPAccount("1620", "Trade Licence and Establishment Card", "Asset", "Intangible Assets", "Debit"),
    AEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    AEGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    AEGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    AEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    AEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    AEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    AEGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    AEGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    AEGAAPAccount("2110", "VAT Payable — Net", "Liability", "Tax Payable", "Credit"),
    AEGAAPAccount("2120", "Corporate Tax Payable", "Liability", "Tax Payable", "Credit"),
    AEGAAPAccount("2130", "Corporate Tax Provision", "Liability", "Tax Payable", "Credit"),
    AEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    AEGAAPAccount("2210", "WPS Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    AEGAAPAccount("2220", "End-of-Service Benefits Provision (Gratuity)", "Liability", "Employee Benefits", "Credit"),
    AEGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    AEGAAPAccount("2240", "GPSSA Pension Payable (UAE Nationals)", "Liability", "Employee Benefits", "Credit"),
    AEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    AEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    AEGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    AEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    AEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    AEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    AEGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    AEGAAPAccount("3010", "Shareholder Current Account", "Equity", "Contributed Capital", "Credit"),
    AEGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    AEGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    AEGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    AEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    AEGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    AEGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    AEGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    AEGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    AEGAAPAccount("4030", "Revenue — Free Zone Qualifying Income", "Revenue", "Operating Revenue", "Credit"),
    AEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    AEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    AEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    AEGAAPAccount("4210", "Interest / Profit Income", "Revenue", "Other Income", "Credit"),
    AEGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    AEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    AEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    AEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    AEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    AEGAAPAccount("6010", "End-of-Service Benefits Expense", "Expense", "Staff Costs", "Debit"),
    AEGAAPAccount("6020", "Staff Visa and Labour Card Fees", "Expense", "Staff Costs", "Debit"),
    AEGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    AEGAAPAccount("6040", "Air Ticket Allowance", "Expense", "Staff Costs", "Debit"),
    AEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    AEGAAPAccount("6110", "Utilities (DEWA / SEWA)", "Expense", "Occupancy Costs", "Debit"),
    AEGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    AEGAAPAccount("6200", "Trade Licence Renewal", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6210", "Government and Immigration Fees", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6230", "Telecommunications (Etisalat / du)", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    AEGAAPAccount("6300", "Interest / Finance Costs", "Expense", "Finance Costs", "Debit"),
    AEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    AEGAAPAccount("6400", "Corporate Tax Expense", "Expense", "Tax Expense", "Debit"),
    AEGAAPAccount("6900", "Irrecoverable VAT", "Expense", "Administrative Expenses", "Debit"),
]
