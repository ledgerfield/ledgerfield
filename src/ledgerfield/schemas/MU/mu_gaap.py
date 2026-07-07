"""Republic of Mauritius chart of accounts (IFRS as applied in Mauritius).

Mauritian companies report under IFRS. This chart layers Mauritius-specific
tax and labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (15%; effective 3% under the GBC partial
      exemption regime for qualifying foreign-source income).
CCR = Corporate Climate Responsibility levy (2%, turnover > Rs 50m).
VAT = Value Added Tax (15%, Value Added Tax Act 1998).
PAYE / CSG / NSF = payroll withholding and social contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MUGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MU_GAAP: list[MUGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MUGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MUGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MUGAAPAccount("1020", "Mauritius Commercial Bank (MCB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MUGAAPAccount("1021", "SBM Bank (Mauritius) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MUGAAPAccount("1022", "Absa Bank (Mauritius) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MUGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MUGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MUGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MUGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MUGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MUGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MUGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MUGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MUGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MUGAAPAccount("1180", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    MUGAAPAccount("1190", "Advance Payment System (APS) Tax Credits", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MUGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MUGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MUGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MUGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MUGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MUGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MUGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MUGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MUGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MUGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MUGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MUGAAPAccount("1620", "Global Business Licence (FSC) Fees Capitalised", "Asset", "Intangible Assets", "Debit"),
    MUGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MUGAAPAccount("1710", "Foreign Portfolio Investments", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MUGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MUGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MUGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MUGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MUGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    MUGAAPAccount("2110", "Tax Deducted at Source (TDS) Payable", "Liability", "Tax Payable", "Credit"),
    MUGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    MUGAAPAccount("2125", "Corporate Climate Responsibility Levy Payable", "Liability", "Tax Payable", "Credit"),
    MUGAAPAccount("2130", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    MUGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MUGAAPAccount("2210", "CSG (Contribution Sociale Généralisée) Payable", "Liability", "Employee Benefits", "Credit"),
    MUGAAPAccount("2220", "NSF (National Savings Fund) Payable", "Liability", "Employee Benefits", "Credit"),
    MUGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MUGAAPAccount("2240", "Portable Retirement Gratuity Fund Provision", "Liability", "Employee Benefits", "Credit"),
    MUGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MUGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MUGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MUGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MUGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MUGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    MUGAAPAccount("3100", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    MUGAAPAccount("3110", "Foreign Currency Translation Reserve", "Equity", "Reserves", "Credit"),
    MUGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MUGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MUGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MUGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MUGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MUGAAPAccount("4020", "Revenue — Export of Goods (3% CIT)", "Revenue", "Operating Revenue", "Credit"),
    MUGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MUGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MUGAAPAccount("4200", "Foreign Dividend Income (Partial Exemption)", "Revenue", "Other Income", "Credit"),
    MUGAAPAccount("4210", "Foreign Interest Income (Partial Exemption)", "Revenue", "Other Income", "Credit"),
    MUGAAPAccount("4220", "Ship and Aircraft Leasing Income (Partial Exemption)", "Revenue", "Other Income", "Credit"),
    MUGAAPAccount("4230", "CIS Management Fee Income (Partial Exemption)", "Revenue", "Other Income", "Credit"),
    MUGAAPAccount("4240", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MUGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MUGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MUGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MUGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MUGAAPAccount("6010", "CSG Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MUGAAPAccount("6020", "NSF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MUGAAPAccount("6030", "HRDC Training Levy", "Expense", "Staff Costs", "Debit"),
    MUGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MUGAAPAccount("6110", "Utilities (CEB / CWA)", "Expense", "Occupancy Costs", "Debit"),
    MUGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MUGAAPAccount("6200", "FSC and Registrar of Companies Fees", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6210", "Management Company (Corporate Services) Fees", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6230", "Telecommunications (Mauritius Telecom)", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MUGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MUGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MUGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    MUGAAPAccount("6410", "Corporate Climate Responsibility Levy Expense", "Expense", "Tax Expense", "Debit"),
]
