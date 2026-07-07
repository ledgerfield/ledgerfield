"""Federal Republic of Nigeria chart of accounts (IFRS as adopted in Nigeria).

Nigerian companies report under IFRS as adopted by the Financial Reporting
Council of Nigeria (FRCN). This chart layers Nigeria-specific tax and payroll
accounts on top of an IFRS structure:

CIT = Companies Income Tax (0% / 20% / 30% by turnover-based company size).
TET = Tertiary Education Tax (3% of assessable profit, medium/large companies).
VAT = Value Added Tax (7.5%, Finance Act 2019) — input and output VAT accounts
      are included.
WHT = Withholding Tax (creditable against CIT).
PAYE = Pay-As-You-Earn personal income tax withheld from employees.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class NGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


NG_GAAP: list[NGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    NGGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1020", "Zenith Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1021", "GTBank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1022", "Access Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1023", "First Bank of Nigeria Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1024", "United Bank for Africa (UBA) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1030", "Domiciliary Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    NGGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    NGGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    NGGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    NGGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    NGGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    NGGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    NGGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    NGGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    NGGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    NGGAAPAccount("1180", "Input VAT Receivable", "Asset", "Tax Receivable", "Debit"),
    NGGAAPAccount("1190", "Withholding Tax Credit Notes Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    NGGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    NGGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    NGGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    NGGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    NGGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    NGGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    NGGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    NGGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    NGGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1570", "Generators and Power Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1580", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    NGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    NGGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    NGGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    NGGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    NGGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    NGGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    NGGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    NGGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    NGGAAPAccount("2100", "Output VAT Payable", "Liability", "Tax Payable", "Credit"),
    NGGAAPAccount("2110", "VAT Remittance Account (FIRS)", "Liability", "Tax Payable", "Credit"),
    NGGAAPAccount("2120", "Companies Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    NGGAAPAccount("2125", "Tertiary Education Tax Payable", "Liability", "Tax Payable", "Credit"),
    NGGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    NGGAAPAccount("2140", "PAYE Payable (State IRS)", "Liability", "Tax Payable", "Credit"),
    NGGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    NGGAAPAccount("2210", "Pension Contributions Payable (PenCom)", "Liability", "Employee Benefits", "Credit"),
    NGGAAPAccount("2220", "NHF Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    NGGAAPAccount("2230", "NSITF / ECS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    NGGAAPAccount("2240", "ITF Levy Payable", "Liability", "Employee Benefits", "Credit"),
    NGGAAPAccount("2250", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    NGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    NGGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    NGGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    NGGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    NGGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    NGGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    NGGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    NGGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    NGGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    NGGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    NGGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    NGGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    NGGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    NGGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    NGGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    NGGAAPAccount("4020", "Revenue — Exports (Zero-Rated VAT)", "Revenue", "Operating Revenue", "Credit"),
    NGGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    NGGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    NGGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    NGGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    NGGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    NGGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    NGGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    NGGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    NGGAAPAccount("5030", "Import Duties and Clearing Charges", "Expense", "Cost of Sales", "Debit"),
    NGGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    NGGAAPAccount("6010", "Pension Employer Contribution (10%)", "Expense", "Staff Costs", "Debit"),
    NGGAAPAccount("6020", "NSITF / ECS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    NGGAAPAccount("6030", "ITF Training Levy Expense", "Expense", "Staff Costs", "Debit"),
    NGGAAPAccount("6040", "Employee Medical / HMO Expense", "Expense", "Staff Costs", "Debit"),
    NGGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    NGGAAPAccount("6110", "Electricity (DisCo) and Water", "Expense", "Occupancy Costs", "Debit"),
    NGGAAPAccount("6115", "Diesel and Generator Running Costs", "Expense", "Occupancy Costs", "Debit"),
    NGGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    NGGAAPAccount("6200", "CAC Annual Returns and Filing Fees", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6210", "Government Levies and Business Premises Fees", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6230", "Telecommunications and Internet", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6250", "Bank Charges and EMT Levy", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6280", "Irrecoverable Input VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    NGGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    NGGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    NGGAAPAccount("6400", "Companies Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    NGGAAPAccount("6410", "Tertiary Education Tax Expense", "Expense", "Tax Expense", "Debit"),
]
