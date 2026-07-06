"""Hashemite Kingdom of Jordan chart of accounts (IFRS as applied in Jordan).

Jordanian companies report under IFRS. This chart layers Jordan-specific tax
and labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (sector-based, Income Tax Law No. 38 of 2018).
NC  = National Contribution Tax (Art. 11, Law 38/2018, on top of CIT).
GST = General Sales Tax (Jordan's VAT, standard 16%).
SSC = Social Security Corporation contributions (7.5% employee / 14.25% employer).

Administered by the Income and Sales Tax Department (ISTD).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class JOGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


JO_GAAP: list[JOGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    JOGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1020", "Arab Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1021", "Housing Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1022", "Jordan Kuwait Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1023", "Bank of Jordan Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1024", "Jordan Islamic Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    JOGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    JOGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    JOGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    JOGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    JOGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    JOGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    JOGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    JOGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    JOGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    JOGAAPAccount("1180", "GST (Sales Tax) Receivable — Input Tax", "Asset", "Tax Receivable", "Debit"),
    JOGAAPAccount("1190", "Income Tax Advance Payments (ISTD)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    JOGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    JOGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    JOGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    JOGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    JOGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    JOGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    JOGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    JOGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    JOGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    JOGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    JOGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    JOGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    JOGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    JOGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    JOGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    JOGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    JOGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    JOGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    JOGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    JOGAAPAccount("2100", "GST (Sales Tax) Payable — Output Tax", "Liability", "Tax Payable", "Credit"),
    JOGAAPAccount("2110", "GST Settlement Account (ISTD)", "Liability", "Tax Payable", "Credit"),
    JOGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    JOGAAPAccount("2125", "National Contribution Tax Payable", "Liability", "Tax Payable", "Credit"),
    JOGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    JOGAAPAccount("2140", "Payroll Income Tax Withheld (PIT)", "Liability", "Tax Payable", "Credit"),
    JOGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    JOGAAPAccount("2210", "SSC Payable — Employee Share (7.5%)", "Liability", "Employee Benefits", "Credit"),
    JOGAAPAccount("2220", "SSC Payable — Employer Share (14.25%)", "Liability", "Employee Benefits", "Credit"),
    JOGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    JOGAAPAccount("2240", "End-of-Service Indemnity Provision", "Liability", "Employee Benefits", "Credit"),
    JOGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    JOGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    JOGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    JOGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    JOGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    JOGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    JOGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    JOGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    JOGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    JOGAAPAccount("3110", "Voluntary Reserve", "Equity", "Reserves", "Credit"),
    JOGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    JOGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    JOGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    JOGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    JOGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    JOGAAPAccount("4020", "Revenue — Exports (GST Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    JOGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    JOGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    JOGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    JOGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    JOGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    JOGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    JOGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    JOGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    JOGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    JOGAAPAccount("6010", "SSC Employer Contribution (14.25%)", "Expense", "Staff Costs", "Debit"),
    JOGAAPAccount("6020", "End-of-Service Indemnity Expense", "Expense", "Staff Costs", "Debit"),
    JOGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    JOGAAPAccount("6040", "Work Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    JOGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    JOGAAPAccount("6110", "Utilities (Electricity and Water)", "Expense", "Occupancy Costs", "Debit"),
    JOGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    JOGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6230", "Telecommunications (Zain / Orange / Umniah)", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6280", "Irrecoverable GST Expense", "Expense", "Administrative Expenses", "Debit"),
    JOGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    JOGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    JOGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    JOGAAPAccount("6410", "National Contribution Tax Expense", "Expense", "Tax Expense", "Debit"),
]
