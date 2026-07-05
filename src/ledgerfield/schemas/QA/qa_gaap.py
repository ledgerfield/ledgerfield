"""State of Qatar chart of accounts (IFRS as applied in Qatar).

Qatari companies report under IFRS. This chart layers Qatar-specific tax and
labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (10% on foreign ownership share).
WHT = Withholding Tax (5% on certain non-resident payments).
EOSB = End-of-Service Gratuity (Qatar Labour Law No. 14 of 2004).

Qatar has not implemented VAT as of the target period, so no VAT accounts are
included.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class QAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


QA_GAAP: list[QAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    QAGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1020", "Qatar National Bank (QNB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1021", "Commercial Bank of Qatar Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1022", "Doha Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1023", "Qatar Islamic Bank (QIB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1024", "Masraf Al Rayan Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    QAGAAPAccount("1040", "Wakala Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    QAGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    QAGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    QAGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    QAGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    QAGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    QAGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    QAGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    QAGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    QAGAAPAccount("1180", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    QAGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    QAGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    QAGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    QAGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    QAGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    QAGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    QAGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    QAGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    QAGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    QAGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    QAGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    QAGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    QAGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    QAGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    QAGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    QAGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    QAGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    QAGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    QAGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    QAGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    QAGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    QAGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    QAGAAPAccount("2210", "WPS Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    QAGAAPAccount("2220", "End-of-Service Gratuity Provision", "Liability", "Employee Benefits", "Credit"),
    QAGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    QAGAAPAccount("2240", "Social Insurance Payable (Qatari Nationals)", "Liability", "Employee Benefits", "Credit"),
    QAGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    QAGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    QAGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    QAGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    QAGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    QAGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    QAGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    QAGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    QAGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    QAGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    QAGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    QAGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    QAGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    QAGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    QAGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    QAGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    QAGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    QAGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    QAGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    QAGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    QAGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    QAGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    QAGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    QAGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    QAGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    QAGAAPAccount("6010", "End-of-Service Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    QAGAAPAccount("6020", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    QAGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    QAGAAPAccount("6040", "Residence Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    QAGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    QAGAAPAccount("6110", "Utilities (Kahramaa)", "Expense", "Occupancy Costs", "Debit"),
    QAGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    QAGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6230", "Telecommunications (Ooredoo / Vodafone)", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    QAGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    QAGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    QAGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
