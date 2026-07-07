"""Republic of Kenya chart of accounts (IFRS as applied in Kenya).

Kenyan companies report under IFRS. This chart layers Kenya-specific tax and
statutory accounts on top of an IFRS structure:

CIT = Corporate Income Tax (30% resident / 37.5% non-resident branch).
VAT = Value Added Tax (16% standard rate, VAT Act 2013).
PAYE = Pay As You Earn (employee income tax withheld by employer).
NSSF = National Social Security Fund; SHIF = Social Health Insurance Fund.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class KEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


KE_GAAP: list[KEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    KEGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1020", "KCB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1021", "Equity Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1022", "Co-operative Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1023", "Absa Bank Kenya Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1024", "M-Pesa Business Wallet", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    KEGAAPAccount("1040", "Fixed Deposit Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    KEGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KEGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    KEGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    KEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    KEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    KEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    KEGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    KEGAAPAccount("1180", "VAT Input (Deductible)", "Asset", "Tax Receivable", "Debit"),
    KEGAAPAccount("1185", "Withholding Tax Credits (Advance Tax)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    KEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    KEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    KEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    KEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    KEGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    KEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    KEGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    KEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    KEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    KEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    KEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    KEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    KEGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    KEGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    KEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    KEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    KEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    KEGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    KEGAAPAccount("2110", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    KEGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    KEGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    KEGAAPAccount("2140", "Turnover Tax Payable", "Liability", "Tax Payable", "Credit"),
    KEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    KEGAAPAccount("2210", "NSSF Payable", "Liability", "Employee Benefits", "Credit"),
    KEGAAPAccount("2220", "SHIF Payable", "Liability", "Employee Benefits", "Credit"),
    KEGAAPAccount("2230", "Affordable Housing Levy Payable", "Liability", "Employee Benefits", "Credit"),
    KEGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    KEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    KEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    KEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    KEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    KEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    KEGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    KEGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    KEGAAPAccount("3100", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    KEGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    KEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    KEGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    KEGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    KEGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    KEGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    KEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    KEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    KEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    KEGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    KEGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    KEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    KEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    KEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    KEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    KEGAAPAccount("6010", "NSSF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    KEGAAPAccount("6020", "SHIF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    KEGAAPAccount("6030", "Affordable Housing Levy (Employer)", "Expense", "Staff Costs", "Debit"),
    KEGAAPAccount("6040", "Staff Medical Insurance", "Expense", "Staff Costs", "Debit"),
    KEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    KEGAAPAccount("6110", "Utilities (Kenya Power / Water)", "Expense", "Occupancy Costs", "Debit"),
    KEGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    KEGAAPAccount("6200", "Business Permit and Licence Fees", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6210", "County Government Fees", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6230", "Telecommunications (Safaricom / Airtel)", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6250", "Bank and M-Pesa Charges", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    KEGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    KEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    KEGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
