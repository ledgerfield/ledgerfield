"""Grand Duchy of Luxembourg chart of accounts (Lux GAAP / PCN).

Luxembourg companies report under Lux GAAP based on the Plan Comptable
Normalise (PCN 2020); IFRS is permitted for consolidated accounts. This chart
layers Luxembourg-specific tax and payroll accounts on top of a PCN-inspired
structure:

IRC  = Impot sur le revenu des collectivites (state CIT, 16%/14% from 2025).
ICC  = Impot commercial communal (municipal business tax, ~6.75% Lux City).
IF   = Impot sur la fortune (net wealth tax).
TVA  = Taxe sur la valeur ajoutee (VAT 17% / 14% / 8% / 3%).
CCSS = Centre commun de la securite sociale (social security).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LUGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


LU_GAAP: list[LUGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    LUGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1020", "BGL BNP Paribas Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1021", "Banque Internationale a Luxembourg (BIL) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1022", "Spuerkeess (BCEE) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1023", "Banque Raiffeisen Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    LUGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    LUGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LUGAAPAccount("1110", "Allowance for Doubtful Receivables", "Asset", "Trade and Other Receivables", "Credit"),
    LUGAAPAccount("1120", "Intra-Group Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LUGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LUGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    LUGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    LUGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    LUGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    LUGAAPAccount("1180", "Input VAT (TVA) Receivable", "Asset", "Tax Receivable", "Debit"),
    LUGAAPAccount("1190", "CIT (IRC) Advance Payments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    LUGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    LUGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    LUGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    LUGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    LUGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    LUGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    LUGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    LUGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    LUGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    LUGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    LUGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    LUGAAPAccount("1620", "IP — Patents and Trademarks", "Asset", "Intangible Assets", "Debit"),
    LUGAAPAccount("1700", "Participations (Subsidiaries)", "Asset", "Financial Assets", "Debit"),
    LUGAAPAccount("1710", "Long-Term Loans to Group Companies", "Asset", "Financial Assets", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    LUGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    LUGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    LUGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    LUGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    LUGAAPAccount("2100", "Output VAT (TVA) Payable", "Liability", "Tax Payable", "Credit"),
    LUGAAPAccount("2110", "VAT Settlement Account (AED)", "Liability", "Tax Payable", "Credit"),
    LUGAAPAccount("2120", "Corporate Income Tax (IRC) Payable", "Liability", "Tax Payable", "Credit"),
    LUGAAPAccount("2125", "Municipal Business Tax (ICC) Payable", "Liability", "Tax Payable", "Credit"),
    LUGAAPAccount("2130", "Net Wealth Tax (IF) Payable", "Liability", "Tax Payable", "Credit"),
    LUGAAPAccount("2140", "Wage Tax Withheld Payable", "Liability", "Tax Payable", "Credit"),
    LUGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    LUGAAPAccount("2210", "Social Security (CCSS) Payable", "Liability", "Employee Benefits", "Credit"),
    LUGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    LUGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    LUGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    LUGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    LUGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    LUGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    LUGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    LUGAAPAccount("3010", "Share Premium (Account 115 Contribution)", "Equity", "Contributed Capital", "Credit"),
    LUGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    LUGAAPAccount("3110", "Net Wealth Tax Reserve", "Equity", "Reserves", "Credit"),
    LUGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    LUGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    LUGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    LUGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    LUGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    LUGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    LUGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    LUGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    LUGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    LUGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    LUGAAPAccount("4210", "Dividend Income (Participation Exemption)", "Revenue", "Other Income", "Credit"),
    LUGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    LUGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    LUGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    LUGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    LUGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    LUGAAPAccount("6010", "Social Security Employer Contribution (CCSS)", "Expense", "Staff Costs", "Debit"),
    LUGAAPAccount("6020", "Meal Vouchers", "Expense", "Staff Costs", "Debit"),
    LUGAAPAccount("6030", "Employee Insurance", "Expense", "Staff Costs", "Debit"),
    LUGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    LUGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    LUGAAPAccount("6200", "RCS Filing and Registration Fees", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    LUGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    LUGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    LUGAAPAccount("6400", "Corporate Income Tax (IRC) Expense", "Expense", "Tax Expense", "Debit"),
    LUGAAPAccount("6410", "Municipal Business Tax (ICC) Expense", "Expense", "Tax Expense", "Debit"),
    LUGAAPAccount("6420", "Net Wealth Tax (IF) Expense", "Expense", "Tax Expense", "Debit"),
]
