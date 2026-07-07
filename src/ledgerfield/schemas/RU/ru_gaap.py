"""Russian Federation chart of accounts (RAS — Russian Accounting Standards).

Russian entities report under Russian Accounting Standards (RAS / RSBU, plan
schetov). This chart presents an IFRS-style structure with Russia-specific tax
and payroll accounts layered on top:

CIT = Corporate Profits Tax (25% standard from 2025, 5% for IT companies).
VAT = NDS (Value Added Tax, 20% standard).
INS = Unified social insurance contributions (employer, single 30% tariff).
PIT = Personal Income Tax (NDFL, progressive from 2025) withheld from payroll.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RUGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


RU_GAAP: list[RUGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    RUGAAPAccount("1010", "Cash on Hand (Kassa)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1020", "Sberbank Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1021", "VTB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1022", "Gazprombank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1023", "Alfa-Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1031", "Foreign Currency Account (CNY)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RUGAAPAccount("1040", "Short-Term Bank Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    RUGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    RUGAAPAccount("1110", "Allowance for Doubtful Debts", "Asset", "Trade and Other Receivables", "Credit"),
    RUGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    RUGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    RUGAAPAccount("1140", "Accountable Persons (Podotchetnye litsa)", "Asset", "Trade and Other Receivables", "Debit"),
    RUGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    RUGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    RUGAAPAccount("1170", "Input VAT Recoverable (NDS k vozmeshcheniyu)", "Asset", "Tax Receivable", "Debit"),
    RUGAAPAccount("1180", "Corporate Profits Tax Prepaid", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    RUGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    RUGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    RUGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    RUGAAPAccount("1230", "Goods for Resale", "Asset", "Inventories", "Debit"),
    RUGAAPAccount("1240", "Goods in Transit", "Asset", "Inventories", "Debit"),
    RUGAAPAccount("1250", "Provision for Obsolete Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    RUGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1510", "Buildings and Structures", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    RUGAAPAccount("1520", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1525", "Accumulated Depreciation — Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    RUGAAPAccount("1530", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1535", "Accumulated Depreciation — Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    RUGAAPAccount("1540", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1560", "Right-of-Use Asset (FSBU 25)", "Asset", "Property, Plant and Equipment", "Debit"),
    RUGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    RUGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    RUGAAPAccount("1620", "Trademarks and Patents", "Asset", "Intangible Assets", "Debit"),
    RUGAAPAccount("1700", "Long-Term Financial Investments", "Asset", "Investments", "Debit"),
    RUGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    RUGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    RUGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    RUGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    RUGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    RUGAAPAccount("2100", "Output VAT Payable (NDS k uplate)", "Liability", "Tax Payable", "Credit"),
    RUGAAPAccount("2110", "Corporate Profits Tax Payable", "Liability", "Tax Payable", "Credit"),
    RUGAAPAccount("2115", "Unified Tax Account Balance (ENS)", "Liability", "Tax Payable", "Credit"),
    RUGAAPAccount("2130", "Personal Income Tax Withheld (NDFL)", "Liability", "Tax Payable", "Credit"),
    RUGAAPAccount("2140", "Property Tax Payable", "Liability", "Tax Payable", "Credit"),
    RUGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    RUGAAPAccount("2210", "Social Insurance Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    RUGAAPAccount("2220", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    RUGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    RUGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    RUGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    RUGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    RUGAAPAccount("2410", "Lease Liability (FSBU 25)", "Liability", "Non-Current Liabilities", "Credit"),
    RUGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 4xxx ──────────────────────────────────────────────────────────
    RUGAAPAccount("4000", "Charter (Share) Capital (Ustavnyi kapital)", "Equity", "Contributed Capital", "Credit"),
    RUGAAPAccount("4010", "Additional Capital (Dobavochnyi kapital)", "Equity", "Contributed Capital", "Credit"),
    RUGAAPAccount("4100", "Reserve Capital (Rezervnyi kapital)", "Equity", "Reserves", "Credit"),
    RUGAAPAccount("4110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    RUGAAPAccount("4200", "Retained Earnings (Neraspredelennaya pribyl)", "Equity", "Retained Earnings", "Credit"),
    RUGAAPAccount("4210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    RUGAAPAccount("4300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 7xxx ─────────────────────────────────────────────────────────
    RUGAAPAccount("7000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    RUGAAPAccount("7010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    RUGAAPAccount("7020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    RUGAAPAccount("7100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    RUGAAPAccount("7110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    RUGAAPAccount("7200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    RUGAAPAccount("7210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    RUGAAPAccount("7220", "Interest Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 9xxx ────────────────────────────────────────────────────────
    RUGAAPAccount("9000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    RUGAAPAccount("9010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    RUGAAPAccount("9020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    RUGAAPAccount("9100", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    RUGAAPAccount("9110", "Social Insurance Contributions Expense", "Expense", "Staff Costs", "Debit"),
    RUGAAPAccount("9120", "Vacation Pay Expense", "Expense", "Staff Costs", "Debit"),
    RUGAAPAccount("9200", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    RUGAAPAccount("9210", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    RUGAAPAccount("9300", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    RUGAAPAccount("9310", "Telecommunications and Internet", "Expense", "Administrative Expenses", "Debit"),
    RUGAAPAccount("9320", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    RUGAAPAccount("9330", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    RUGAAPAccount("9340", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    RUGAAPAccount("9350", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    RUGAAPAccount("9400", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    RUGAAPAccount("9410", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    RUGAAPAccount("9500", "Corporate Profits Tax Expense", "Expense", "Tax Expense", "Debit"),
]
