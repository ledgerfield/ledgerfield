"""Federal Democratic Republic of Ethiopia chart of accounts (IFRS).

Ethiopian reporting entities apply IFRS under the Financial Reporting
Proclamation No. 847/2014 (overseen by AABE). This chart layers
Ethiopia-specific tax and labour accounts on top of an IFRS structure:

CIT = Business income tax on bodies (30%, Income Tax Proclamation 979/2016).
VAT = Value Added Tax (15%, VAT Proclamation 1341/2024).
TOT = Turnover Tax (2% goods / 10% services) for non-VAT-registered firms.
Pension contributions per the Private Organization Employees' Pension
Proclamation No. 1268/2022.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ETGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


ET_GAAP: list[ETGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ETGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1020", "Commercial Bank of Ethiopia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1021", "Awash Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1022", "Dashen Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1023", "Bank of Abyssinia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ETGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ETGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ETGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    ETGAAPAccount("1120", "Staff Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ETGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ETGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ETGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ETGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    ETGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    ETGAAPAccount("1180", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    ETGAAPAccount("1190", "Withholding Tax Receivable (Prepaid CIT)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ETGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ETGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ETGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ETGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    ETGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ETGAAPAccount("1500", "Land Use Rights (Lease)", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ETGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ETGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ETGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    ETGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ETGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ETGAAPAccount("1620", "Business Licences and Registrations", "Asset", "Intangible Assets", "Debit"),
    ETGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    ETGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ETGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    ETGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ETGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    ETGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    ETGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    ETGAAPAccount("2110", "Turnover Tax (TOT) Payable", "Liability", "Tax Payable", "Credit"),
    ETGAAPAccount("2120", "Business Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    ETGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    ETGAAPAccount("2140", "Employment Income Tax (PAYE) Payable", "Liability", "Tax Payable", "Credit"),
    ETGAAPAccount("2150", "Excise and Other Taxes Payable", "Liability", "Tax Payable", "Credit"),
    ETGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    ETGAAPAccount("2210", "Pension Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    ETGAAPAccount("2220", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ETGAAPAccount("2230", "Severance Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ETGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ETGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ETGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    ETGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    ETGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    ETGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ETGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    ETGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    ETGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    ETGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    ETGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    ETGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ETGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ETGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    ETGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    ETGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    ETGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ETGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ETGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ETGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    ETGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ETGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ETGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ETGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ETGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ETGAAPAccount("6010", "Pension Employer Contribution", "Expense", "Staff Costs", "Debit"),
    ETGAAPAccount("6020", "Employee Medical Costs", "Expense", "Staff Costs", "Debit"),
    ETGAAPAccount("6030", "Staff Training and Development", "Expense", "Staff Costs", "Debit"),
    ETGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    ETGAAPAccount("6110", "Utilities (Ethiopian Electric Utility / Water)", "Expense", "Occupancy Costs", "Debit"),
    ETGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    ETGAAPAccount("6200", "Business Licence Renewal", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6210", "Government Fees and Stamp Duty", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6230", "Telecommunications (Ethio Telecom / Safaricom)", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    ETGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    ETGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    ETGAAPAccount("6400", "Business Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    ETGAAPAccount("6410", "Turnover Tax Expense", "Expense", "Tax Expense", "Debit"),
]
