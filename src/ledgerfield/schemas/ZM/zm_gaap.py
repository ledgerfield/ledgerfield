"""Republic of Zambia chart of accounts (IFRS as applied in Zambia).

Zambian companies report under IFRS, overseen by the Zambia Institute of
Chartered Accountants (ZICA). This chart layers Zambia-specific tax and
payroll accounts on top of an IFRS structure:

CIT   = Corporate Income Tax (30% standard, Income Tax Act Cap. 323).
VAT   = Value Added Tax (16% standard rate).
PAYE  = Pay As You Earn withholding on employment income.
NAPSA = National Pension Scheme Authority contributions.
NHIMA = National Health Insurance Management Authority contributions.
Skills Development Levy = 0.5% payroll levy.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ZMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


ZM_GAAP: list[ZMGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ZMGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1020", "Zanaco Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1021", "Stanbic Bank Zambia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1022", "Absa Bank Zambia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1023", "FNB Zambia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1025", "Mobile Money Float (Airtel Money / MTN MoMo / Zamtel Kwacha)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZMGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ZMGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ZMGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    ZMGAAPAccount("1120", "Staff Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ZMGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ZMGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ZMGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    ZMGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    ZMGAAPAccount("1180", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    ZMGAAPAccount("1190", "Withholding Tax Credits (ZRA)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ZMGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ZMGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ZMGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ZMGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    ZMGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ZMGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ZMGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ZMGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ZMGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    ZMGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ZMGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ZMGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    ZMGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ZMGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    ZMGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ZMGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    ZMGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    ZMGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    ZMGAAPAccount("2110", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    ZMGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    ZMGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    ZMGAAPAccount("2140", "Skills Development Levy Payable", "Liability", "Tax Payable", "Credit"),
    ZMGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    ZMGAAPAccount("2210", "NAPSA Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    ZMGAAPAccount("2220", "NHIMA Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    ZMGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ZMGAAPAccount("2240", "Gratuity Provision", "Liability", "Employee Benefits", "Credit"),
    ZMGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ZMGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ZMGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    ZMGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    ZMGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ZMGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    ZMGAAPAccount("3100", "General Reserve", "Equity", "Reserves", "Credit"),
    ZMGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    ZMGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ZMGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ZMGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    ZMGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    ZMGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    ZMGAAPAccount("4030", "Revenue — Farming and Agro-Processing", "Revenue", "Operating Revenue", "Credit"),
    ZMGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ZMGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ZMGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ZMGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ZMGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ZMGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ZMGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ZMGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ZMGAAPAccount("6010", "NAPSA Employer Contribution", "Expense", "Staff Costs", "Debit"),
    ZMGAAPAccount("6020", "NHIMA Employer Contribution", "Expense", "Staff Costs", "Debit"),
    ZMGAAPAccount("6030", "Skills Development Levy Expense", "Expense", "Staff Costs", "Debit"),
    ZMGAAPAccount("6040", "Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    ZMGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    ZMGAAPAccount("6110", "Utilities (ZESCO / Water Utilities)", "Expense", "Occupancy Costs", "Debit"),
    ZMGAAPAccount("6200", "Business Licence and Registration Fees (PACRA)", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6210", "Government and Council Fees", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6230", "Telecommunications (Airtel / MTN / Zamtel)", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    ZMGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    ZMGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    ZMGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
