"""Slovak Republic chart of accounts (Slovak accounting standards / IFRS).

Slovak companies report under the Slovak Act on Accounting (zákon č. 431/2002
Z. z.) with a decree-based uniform chart of accounts; listed groups use IFRS.
This chart layers Slovakia-specific tax and payroll accounts on top of an
IFRS-style structure:

DPH  = Daň z pridanej hodnoty (VAT, 23% standard from 1 Jan 2025; 19%/5% reduced).
DzP  = Daň z príjmov (income tax; CIT 10%/21%/24% bands from 2025).
FTT  = Financial transaction tax (introduced by the 2025 consolidation package).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SKGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


SK_GAAP: list[SKGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    SKGAAPAccount("1010", "Cash on Hand (Pokladnica)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1020", "Slovenská sporiteľňa Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1021", "VÚB Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1022", "Tatra banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1023", "ČSOB Slovakia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SKGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    SKGAAPAccount("1100", "Trade Receivables (Pohľadávky z obchodného styku)", "Asset", "Trade and Other Receivables", "Debit"),
    SKGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    SKGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    SKGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    SKGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    SKGAAPAccount("1150", "Prepaid Expenses (Náklady budúcich období)", "Asset", "Prepayments", "Debit"),
    SKGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    SKGAAPAccount("1170", "Input VAT Receivable (DPH na vstupe)", "Asset", "Tax Receivable", "Debit"),
    SKGAAPAccount("1180", "Corporate Income Tax Prepayments (Preddavky DzP)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    SKGAAPAccount("1200", "Inventory — Raw Materials (Materiál)", "Asset", "Inventories", "Debit"),
    SKGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    SKGAAPAccount("1220", "Inventory — Finished Goods (Výrobky)", "Asset", "Inventories", "Debit"),
    SKGAAPAccount("1230", "Goods for Resale (Tovar)", "Asset", "Inventories", "Debit"),
    SKGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    SKGAAPAccount("1500", "Land (Pozemky)", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1510", "Buildings (Stavby)", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    SKGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    SKGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    SKGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    SKGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    SKGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    SKGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    SKGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),
    SKGAAPAccount("1720", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    SKGAAPAccount("2000", "Trade Payables (Záväzky z obchodného styku)", "Liability", "Trade and Other Payables", "Credit"),
    SKGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    SKGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    SKGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    SKGAAPAccount("2100", "Output VAT Payable (DPH na výstupe, 23%)", "Liability", "Tax Payable", "Credit"),
    SKGAAPAccount("2110", "VAT Settlement Account (DPH — zúčtovanie)", "Liability", "Tax Payable", "Credit"),
    SKGAAPAccount("2120", "Corporate Income Tax Payable (DzP právnických osôb)", "Liability", "Tax Payable", "Credit"),
    SKGAAPAccount("2130", "Withholding Tax Payable (Zrážková daň)", "Liability", "Tax Payable", "Credit"),
    SKGAAPAccount("2140", "Financial Transaction Tax Payable (FTT 2025)", "Liability", "Tax Payable", "Credit"),
    SKGAAPAccount("2200", "Salaries and Wages Payable (Mzdy)", "Liability", "Employee Benefits", "Credit"),
    SKGAAPAccount("2210", "Payroll Tax Withheld (Preddavky na daň zo mzdy)", "Liability", "Employee Benefits", "Credit"),
    SKGAAPAccount("2220", "Social Insurance Payable (Sociálna poisťovňa)", "Liability", "Employee Benefits", "Credit"),
    SKGAAPAccount("2230", "Health Insurance Payable (Zdravotné poistenie)", "Liability", "Employee Benefits", "Credit"),
    SKGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    SKGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    SKGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    SKGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    SKGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    SKGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    SKGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    SKGAAPAccount("3000", "Share Capital (Základné imanie)", "Equity", "Contributed Capital", "Credit"),
    SKGAAPAccount("3010", "Capital Contributions (Kapitálové fondy)", "Equity", "Contributed Capital", "Credit"),
    SKGAAPAccount("3100", "Legal Reserve Fund (Zákonný rezervný fond)", "Equity", "Reserves", "Credit"),
    SKGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    SKGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    SKGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    SKGAAPAccount("4000", "Revenue — Goods (Tržby za tovar)", "Revenue", "Operating Revenue", "Credit"),
    SKGAAPAccount("4010", "Revenue — Services (Tržby za služby)", "Revenue", "Operating Revenue", "Credit"),
    SKGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    SKGAAPAccount("4030", "Revenue — Exports (non-EU)", "Revenue", "Operating Revenue", "Credit"),
    SKGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    SKGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    SKGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    SKGAAPAccount("4210", "Government Grants and Subsidies", "Revenue", "Other Income", "Credit"),
    SKGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    SKGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    SKGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    SKGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    SKGAAPAccount("6000", "Salaries and Wages (Mzdové náklady)", "Expense", "Staff Costs", "Debit"),
    SKGAAPAccount("6010", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    SKGAAPAccount("6020", "Health Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    SKGAAPAccount("6030", "Meal Allowance (Stravné)", "Expense", "Staff Costs", "Debit"),
    SKGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    SKGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    SKGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    SKGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6210", "Government and Registration Fees", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6220", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6245", "Financial Transaction Tax Expense (FTT)", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    SKGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    SKGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    SKGAAPAccount("6400", "Corporate Income Tax Expense (DzP)", "Expense", "Tax Expense", "Debit"),
    SKGAAPAccount("6410", "Deferred Tax Expense", "Expense", "Tax Expense", "Debit"),
]
