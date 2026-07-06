"""Sri Lanka chart of accounts (SLFRS — Sri Lanka Financial Reporting Standards).

Sri Lankan companies report under SLFRS/LKAS, the local adoption of IFRS
issued by CA Sri Lanka. This chart layers Sri Lanka-specific tax and labour
accounts on top of an IFRS-style structure:

CIT  = Corporate Income Tax (30% standard; 15% export of services; 45%
       betting/gaming, liquor and tobacco) — Inland Revenue Act No. 24 of 2017.
VAT  = Value Added Tax, 18% from 1 January 2024 (up from 15%).
SSCL = Social Security Contribution Levy, 2.5% on turnover.
EPF  = Employees' Provident Fund (employee 8%, employer 12%).
ETF  = Employees' Trust Fund (employer 3%).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LKGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


LK_GAAP: list[LKGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    LKGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1020", "Bank of Ceylon Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1021", "People's Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1022", "Commercial Bank of Ceylon Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1023", "Hatton National Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1024", "Sampath Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    LKGAAPAccount("1040", "Fixed Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    LKGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LKGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    LKGAAPAccount("1120", "Export Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LKGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LKGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    LKGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    LKGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    LKGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    LKGAAPAccount("1180", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    LKGAAPAccount("1185", "SVAT Suspended VAT Receivable", "Asset", "Tax Receivable", "Debit"),
    LKGAAPAccount("1190", "WHT / AIT Credit Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    LKGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    LKGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    LKGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    LKGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    LKGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    LKGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    LKGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    LKGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    LKGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1570", "Right-of-Use Asset (SLFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    LKGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    LKGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    LKGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    LKGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    LKGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    LKGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    LKGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    LKGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    LKGAAPAccount("2100", "VAT Output Payable (18%)", "Liability", "Tax Payable", "Credit"),
    LKGAAPAccount("2110", "SSCL Payable (2.5% on Turnover)", "Liability", "Tax Payable", "Credit"),
    LKGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    LKGAAPAccount("2130", "WHT / AIT Payable", "Liability", "Tax Payable", "Credit"),
    LKGAAPAccount("2140", "APIT (PAYE) Payable", "Liability", "Tax Payable", "Credit"),
    LKGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    LKGAAPAccount("2210", "EPF Payable (Employee 8% + Employer 12%)", "Liability", "Employee Benefits", "Credit"),
    LKGAAPAccount("2220", "ETF Payable (Employer 3%)", "Liability", "Employee Benefits", "Credit"),
    LKGAAPAccount("2230", "Gratuity Provision (Payment of Gratuity Act)", "Liability", "Employee Benefits", "Credit"),
    LKGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    LKGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    LKGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    LKGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    LKGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    LKGAAPAccount("2410", "Lease Liability (SLFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    LKGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    LKGAAPAccount("3000", "Stated Capital", "Equity", "Contributed Capital", "Credit"),
    LKGAAPAccount("3100", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    LKGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    LKGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    LKGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    LKGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    LKGAAPAccount("4000", "Revenue — Goods (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    LKGAAPAccount("4010", "Revenue — Services (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    LKGAAPAccount("4020", "Revenue — Export of Goods", "Revenue", "Operating Revenue", "Credit"),
    LKGAAPAccount("4030", "Revenue — Export of Services (15% CIT)", "Revenue", "Operating Revenue", "Credit"),
    LKGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    LKGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    LKGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    LKGAAPAccount("4210", "Interest Income", "Revenue", "Other Income", "Credit"),
    LKGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    LKGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    LKGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    LKGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    LKGAAPAccount("5030", "Import Duties and CESS", "Expense", "Cost of Sales", "Debit"),
    LKGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    LKGAAPAccount("6010", "EPF Employer Contribution (12%)", "Expense", "Staff Costs", "Debit"),
    LKGAAPAccount("6020", "ETF Employer Contribution (3%)", "Expense", "Staff Costs", "Debit"),
    LKGAAPAccount("6030", "Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    LKGAAPAccount("6040", "Staff Welfare and Medical", "Expense", "Staff Costs", "Debit"),
    LKGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    LKGAAPAccount("6110", "Utilities (CEB / Water Board)", "Expense", "Occupancy Costs", "Debit"),
    LKGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    LKGAAPAccount("6200", "SSCL Expense (2.5% on Turnover)", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6230", "Telecommunications (SLT / Dialog)", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6280", "Irrecoverable VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    LKGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    LKGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    LKGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
