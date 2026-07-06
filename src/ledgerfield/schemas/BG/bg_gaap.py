"""Bulgaria chart of accounts (National Accounting Standards / IFRS as applied in Bulgaria).

Bulgarian companies report under the National Accounting Standards (NSS) or
IFRS. This chart layers Bulgaria-specific tax and payroll accounts on top of
an IFRS-style structure:

CIT  = Corporate Income Tax (flat 10%, Corporate Income Tax Act / ZKPO).
DDS  = Value Added Tax (ДДС), 20% standard / 9% reduced (tourism).
NAP  = National Revenue Agency (НАП), the tax and social-security collector.
NOI  = National Social Security Institute (НОИ) contributions.

Note: Bulgaria adopts the euro on 1 January 2026; 2025 balances are in BGN.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


BG_GAAP: list[BGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    BGGAAPAccount("1010", "Cash on Hand (BGN)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1020", "UniCredit Bulbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1021", "DSK Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1022", "Eurobank Bulgaria (Postbank) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1023", "United Bulgarian Bank (UBB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BGGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    BGGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BGGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    BGGAAPAccount("1120", "Receivables from Related Parties", "Asset", "Trade and Other Receivables", "Debit"),
    BGGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BGGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    BGGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    BGGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    BGGAAPAccount("1180", "VAT (DDS) Receivable", "Asset", "Tax Receivable", "Debit"),
    BGGAAPAccount("1190", "CIT Prepayments (Advance Instalments)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    BGGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    BGGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    BGGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    BGGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    BGGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    BGGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    BGGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    BGGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    BGGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    BGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    BGGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    BGGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    BGGAAPAccount("1710", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    BGGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    BGGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    BGGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    BGGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    BGGAAPAccount("2100", "VAT (DDS) Payable — 20% Standard", "Liability", "Tax Payable", "Credit"),
    BGGAAPAccount("2110", "VAT (DDS) Payable — 9% Reduced (Tourism)", "Liability", "Tax Payable", "Credit"),
    BGGAAPAccount("2120", "Corporate Income Tax Payable (NAP)", "Liability", "Tax Payable", "Credit"),
    BGGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    BGGAAPAccount("2140", "Personal Income Tax Withheld (10% Flat)", "Liability", "Tax Payable", "Credit"),
    BGGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    BGGAAPAccount("2210", "Social Security Contributions Payable (NOI)", "Liability", "Employee Benefits", "Credit"),
    BGGAAPAccount("2220", "Health Insurance Contributions Payable (NZOK)", "Liability", "Employee Benefits", "Credit"),
    BGGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    BGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    BGGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    BGGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    BGGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    BGGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    BGGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    BGGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    BGGAAPAccount("3100", "Legal (Statutory) Reserve", "Equity", "Reserves", "Credit"),
    BGGAAPAccount("3110", "Other Reserves", "Equity", "Reserves", "Credit"),
    BGGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    BGGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    BGGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    BGGAAPAccount("4000", "Revenue — Goods (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    BGGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    BGGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    BGGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    BGGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    BGGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    BGGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    BGGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    BGGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    BGGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    BGGAAPAccount("6010", "Social Security Employer Contribution (NOI)", "Expense", "Staff Costs", "Debit"),
    BGGAAPAccount("6020", "Health Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    BGGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    BGGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    BGGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    BGGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    BGGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    BGGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    BGGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    BGGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    BGGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    BGGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
