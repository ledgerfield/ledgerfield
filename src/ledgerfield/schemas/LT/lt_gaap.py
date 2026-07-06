"""Republic of Lithuania chart of accounts (Lithuanian Business Accounting
Standards / IFRS as applied in Lithuania).

Lithuanian companies report under national Business Accounting Standards
(Verslo apskaitos standartai) or IFRS. This chart layers Lithuania-specific
tax and payroll accounts on top of an IFRS-style structure:

CIT  = Corporate Income Tax (pelno mokestis, 16% standard / 6% small / 0% first year).
PVM  = Value Added Tax (pridėtinės vertės mokestis, 21% standard; 9%/5% reduced).
Sodra = State Social Insurance Fund Board contributions.
GPM  = Personal income tax withheld on payroll (gyventojų pajamų mokestis).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LTGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


LT_GAAP: list[LTGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    LTGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1020", "SEB Bankas Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1021", "Swedbank Lietuva Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1022", "Luminor Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1023", "Šiaulių Bankas Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    LTGAAPAccount("1040", "Short-Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    LTGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LTGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    LTGAAPAccount("1120", "Intra-EU Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LTGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LTGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    LTGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    LTGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    LTGAAPAccount("1170", "Input PVM (VAT) Receivable", "Asset", "Tax Receivable", "Debit"),
    LTGAAPAccount("1180", "Corporate Income Tax Prepaid (Pelno Mokestis)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    LTGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    LTGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    LTGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    LTGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    LTGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    LTGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    LTGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    LTGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    LTGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    LTGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    LTGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    LTGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    LTGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    LTGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    LTGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    LTGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    LTGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    LTGAAPAccount("2100", "Output PVM (VAT) Payable", "Liability", "Tax Payable", "Credit"),
    LTGAAPAccount("2110", "PVM Settlement Account (VMI)", "Liability", "Tax Payable", "Credit"),
    LTGAAPAccount("2120", "Corporate Income Tax Payable (Pelno Mokestis)", "Liability", "Tax Payable", "Credit"),
    LTGAAPAccount("2130", "Payroll Income Tax Payable (GPM)", "Liability", "Tax Payable", "Credit"),
    LTGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    LTGAAPAccount("2210", "Sodra Social Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    LTGAAPAccount("2220", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    LTGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    LTGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    LTGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    LTGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    LTGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    LTGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    LTGAAPAccount("3000", "Share Capital (Įstatinis Kapitalas)", "Equity", "Contributed Capital", "Credit"),
    LTGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    LTGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    LTGAAPAccount("3110", "Other Reserves", "Equity", "Reserves", "Credit"),
    LTGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    LTGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    LTGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    LTGAAPAccount("4000", "Revenue — Goods (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    LTGAAPAccount("4010", "Revenue — Services (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    LTGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    LTGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    LTGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    LTGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    LTGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    LTGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    LTGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    LTGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    LTGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    LTGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    LTGAAPAccount("6010", "Sodra Employer Contributions", "Expense", "Staff Costs", "Debit"),
    LTGAAPAccount("6020", "Vacation Pay Expense", "Expense", "Staff Costs", "Debit"),
    LTGAAPAccount("6030", "Employee Training and Benefits", "Expense", "Staff Costs", "Debit"),
    LTGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    LTGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    LTGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    LTGAAPAccount("6200", "Registrų Centras and Government Fees", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6220", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6270", "Non-Deductible PVM Expense", "Expense", "Administrative Expenses", "Debit"),
    LTGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    LTGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    LTGAAPAccount("6400", "Corporate Income Tax Expense (Pelno Mokestis)", "Expense", "Tax Expense", "Debit"),
]
