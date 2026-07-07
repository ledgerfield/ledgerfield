"""Republic of Rwanda chart of accounts (IFRS as applied in Rwanda).

Rwandan companies report under IFRS (IFRS for SMEs is permitted for smaller
entities). This chart layers Rwanda-specific tax and labour accounts on top
of an IFRS structure:

CIT = Corporate Income Tax (28%, 2023 Income Tax Law; roadmap to 26%).
VAT = Value Added Tax (18%), with EBM (Electronic Billing Machine) invoicing.
PAYE / RSSB = payroll withholding and Rwanda Social Security Board
contributions (pension, medical/CBHI, maternity leave).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RWGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


RW_GAAP: list[RWGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    RWGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1020", "Bank of Kigali Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1021", "Equity Bank Rwanda Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1022", "I&M Bank Rwanda Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1025", "Mobile Money Account (MTN MoMo / Airtel Money)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RWGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    RWGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    RWGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    RWGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    RWGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    RWGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    RWGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    RWGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    RWGAAPAccount("1180", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    RWGAAPAccount("1190", "WHT Credits (15% / 3% Public Tenders)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    RWGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    RWGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    RWGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    RWGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    RWGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    RWGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    RWGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    RWGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    RWGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    RWGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    RWGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    RWGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    RWGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    RWGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    RWGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    RWGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    RWGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    RWGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    RWGAAPAccount("2110", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    RWGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    RWGAAPAccount("2130", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    RWGAAPAccount("2140", "District Trading Licence Tax Payable", "Liability", "Tax Payable", "Credit"),
    RWGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    RWGAAPAccount("2210", "RSSB Pension Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    RWGAAPAccount("2220", "RSSB Medical / CBHI Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    RWGAAPAccount("2225", "RSSB Maternity Leave Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    RWGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    RWGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    RWGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    RWGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    RWGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    RWGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    RWGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    RWGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    RWGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    RWGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    RWGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    RWGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    RWGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    RWGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    RWGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    RWGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    RWGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    RWGAAPAccount("4210", "Interest Income", "Revenue", "Other Income", "Credit"),
    RWGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    RWGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    RWGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    RWGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    RWGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    RWGAAPAccount("6010", "RSSB Pension Employer Contribution", "Expense", "Staff Costs", "Debit"),
    RWGAAPAccount("6020", "RSSB Medical Employer Contribution", "Expense", "Staff Costs", "Debit"),
    RWGAAPAccount("6030", "RSSB Maternity Leave Employer Contribution", "Expense", "Staff Costs", "Debit"),
    RWGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    RWGAAPAccount("6110", "Utilities (EUCL / WASAC)", "Expense", "Occupancy Costs", "Debit"),
    RWGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    RWGAAPAccount("6200", "RDB Registration and Licence Fees", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6210", "District Trading Licence Tax", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6230", "Telecommunications (MTN Rwanda / Airtel)", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6255", "EBM (Electronic Billing Machine) Costs", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    RWGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    RWGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    RWGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
