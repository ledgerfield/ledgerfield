"""Ukraine chart of accounts (National Accounting Standards, P(S)BO).

Ukrainian entities report under National Accounting Standards (P(S)BO) or IFRS.
This chart layers Ukraine-specific tax and labour accounts on an IFRS-style
structure:

CIT = Corporate Income Tax (18% standard, 25% for banks).
VAT = PDV (Value Added Tax, 20% standard).
ESV = Unified Social Contribution (Yedynyi sotsialnyi vnesok, employer 22%).
PIT = Personal Income Tax (18%) plus military levy withheld from payroll.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


UA_GAAP: list[UAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    UAGAAPAccount("1010", "Cash on Hand (Kasa)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1020", "PrivatBank Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1021", "Oschadbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1022", "Raiffeisen Bank Aval Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1023", "Ukrgasbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1031", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UAGAAPAccount("1040", "Short-Term Bank Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    UAGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UAGAAPAccount("1110", "Allowance for Doubtful Debts", "Asset", "Trade and Other Receivables", "Credit"),
    UAGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UAGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    UAGAAPAccount("1140", "Employee Advances (Pidzvitni osoby)", "Asset", "Trade and Other Receivables", "Debit"),
    UAGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    UAGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    UAGAAPAccount("1170", "VAT Credit Receivable (Podatkovyi kredyt)", "Asset", "Tax Receivable", "Debit"),
    UAGAAPAccount("1180", "Corporate Income Tax Prepaid", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    UAGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    UAGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    UAGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    UAGAAPAccount("1230", "Goods for Resale", "Asset", "Inventories", "Debit"),
    UAGAAPAccount("1240", "Goods in Transit", "Asset", "Inventories", "Debit"),
    UAGAAPAccount("1250", "Provision for Obsolete Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    UAGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1510", "Buildings and Structures", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    UAGAAPAccount("1520", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1525", "Accumulated Depreciation — Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    UAGAAPAccount("1530", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1535", "Accumulated Depreciation — Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    UAGAAPAccount("1540", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1560", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    UAGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    UAGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    UAGAAPAccount("1620", "Trademarks and Patents", "Asset", "Intangible Assets", "Debit"),
    UAGAAPAccount("1700", "Long-Term Financial Investments", "Asset", "Investments", "Debit"),
    UAGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    UAGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    UAGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    UAGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    UAGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    UAGAAPAccount("2100", "VAT Payable (Podatkove zoboviazannia)", "Liability", "Tax Payable", "Credit"),
    UAGAAPAccount("2110", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    UAGAAPAccount("2120", "Single Tax Payable (Yedynyi podatok)", "Liability", "Tax Payable", "Credit"),
    UAGAAPAccount("2130", "Personal Income Tax Withheld", "Liability", "Tax Payable", "Credit"),
    UAGAAPAccount("2140", "Military Levy Withheld", "Liability", "Tax Payable", "Credit"),
    UAGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    UAGAAPAccount("2210", "Unified Social Contribution Payable (ESV)", "Liability", "Employee Benefits", "Credit"),
    UAGAAPAccount("2220", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    UAGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    UAGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    UAGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    UAGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    UAGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    UAGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 4xxx ──────────────────────────────────────────────────────────
    UAGAAPAccount("4000", "Registered (Share) Capital", "Equity", "Contributed Capital", "Credit"),
    UAGAAPAccount("4010", "Additional Paid-In Capital", "Equity", "Contributed Capital", "Credit"),
    UAGAAPAccount("4100", "Reserve Capital", "Equity", "Reserves", "Credit"),
    UAGAAPAccount("4110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    UAGAAPAccount("4200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    UAGAAPAccount("4210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    UAGAAPAccount("4300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 7xxx ─────────────────────────────────────────────────────────
    UAGAAPAccount("7000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    UAGAAPAccount("7010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    UAGAAPAccount("7020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    UAGAAPAccount("7100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    UAGAAPAccount("7110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    UAGAAPAccount("7200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    UAGAAPAccount("7210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    UAGAAPAccount("7220", "Interest Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 9xxx ────────────────────────────────────────────────────────
    UAGAAPAccount("9000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    UAGAAPAccount("9010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    UAGAAPAccount("9020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    UAGAAPAccount("9100", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    UAGAAPAccount("9110", "Unified Social Contribution Expense", "Expense", "Staff Costs", "Debit"),
    UAGAAPAccount("9120", "Vacation Pay Expense", "Expense", "Staff Costs", "Debit"),
    UAGAAPAccount("9200", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    UAGAAPAccount("9210", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    UAGAAPAccount("9300", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    UAGAAPAccount("9310", "Telecommunications and Internet", "Expense", "Administrative Expenses", "Debit"),
    UAGAAPAccount("9320", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    UAGAAPAccount("9330", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    UAGAAPAccount("9340", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    UAGAAPAccount("9350", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    UAGAAPAccount("9400", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    UAGAAPAccount("9410", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    UAGAAPAccount("9500", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
