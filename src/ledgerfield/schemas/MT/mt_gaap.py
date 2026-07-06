"""Republic of Malta chart of accounts (GAPSME / IFRS as adopted by the EU).

Maltese companies report under GAPSME (General Accounting Principles for
Small and Medium-Sized Entities) or IFRS as adopted by the EU. This chart
layers Malta-specific tax and payroll accounts on top of an IFRS-style
structure:

CIT = Corporate Income Tax (35% statutory; shareholder 6/7 refund on
      distribution under the full-imputation system).
VAT = Value Added Tax (18% / 12% / 7% / 5%).
FSS = Final Settlement System (employee wage tax withholding).
SSC = Social Security Contributions (Class 1).

Malta's tax accounting requires profits to be allocated to tax accounts
(FTA, MTA, IPA, FIA, UA) which drive the shareholder refund — represented
here at summary level.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MTGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MT_GAAP: list[MTGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MTGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1020", "Bank of Valletta (BOV) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1021", "HSBC Malta Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1022", "APS Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1023", "Lombard Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MTGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MTGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MTGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MTGAAPAccount("1120", "Intra-Group Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MTGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MTGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MTGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MTGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MTGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MTGAAPAccount("1180", "Input VAT Receivable", "Asset", "Tax Receivable", "Debit"),
    MTGAAPAccount("1185", "Shareholder Tax Refund Receivable (6/7)", "Asset", "Tax Receivable", "Debit"),
    MTGAAPAccount("1190", "Provisional Tax Payments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MTGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MTGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MTGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MTGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MTGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MTGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MTGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MTGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MTGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MTGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MTGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MTGAAPAccount("1620", "Gaming / MFSA Licences", "Asset", "Intangible Assets", "Debit"),
    MTGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Financial Assets", "Debit"),
    MTGAAPAccount("1710", "Long-Term Loans to Group Companies", "Asset", "Financial Assets", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MTGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MTGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MTGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MTGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MTGAAPAccount("2100", "Output VAT Payable", "Liability", "Tax Payable", "Credit"),
    MTGAAPAccount("2110", "VAT Settlement Account (CFR)", "Liability", "Tax Payable", "Credit"),
    MTGAAPAccount("2120", "Corporate Income Tax Payable (35%)", "Liability", "Tax Payable", "Credit"),
    MTGAAPAccount("2130", "FSS Wage Tax Withheld Payable", "Liability", "Tax Payable", "Credit"),
    MTGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MTGAAPAccount("2210", "Social Security Contributions (SSC) Payable", "Liability", "Employee Benefits", "Credit"),
    MTGAAPAccount("2220", "Maternity Fund Contribution Payable", "Liability", "Employee Benefits", "Credit"),
    MTGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MTGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MTGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MTGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MTGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MTGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MTGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    MTGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    MTGAAPAccount("3100", "Other Reserves", "Equity", "Reserves", "Credit"),
    MTGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MTGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MTGAAPAccount("3220", "Maltese Taxed Account (MTA) — memo", "Equity", "Retained Earnings", "Credit"),
    MTGAAPAccount("3230", "Foreign Income Account (FIA) — memo", "Equity", "Retained Earnings", "Credit"),
    MTGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MTGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MTGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MTGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    MTGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    MTGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MTGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MTGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MTGAAPAccount("4210", "Dividend Income (Participation Exemption)", "Revenue", "Other Income", "Credit"),
    MTGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MTGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MTGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MTGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MTGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MTGAAPAccount("6010", "Social Security Employer Contribution (SSC)", "Expense", "Staff Costs", "Debit"),
    MTGAAPAccount("6020", "Maternity Fund Contribution", "Expense", "Staff Costs", "Debit"),
    MTGAAPAccount("6030", "Employee Insurance", "Expense", "Staff Costs", "Debit"),
    MTGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MTGAAPAccount("6110", "Utilities (Enemalta / WSC)", "Expense", "Occupancy Costs", "Debit"),
    MTGAAPAccount("6200", "MBR Filing and Registration Fees", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6210", "Government and Local Council Fees", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6230", "Telecommunications (GO / Epic / Melita)", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MTGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MTGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MTGAAPAccount("6400", "Corporate Income Tax Expense (35%)", "Expense", "Tax Expense", "Debit"),
]
