"""Republic of Latvia chart of accounts (Latvian Accounting Law / IFRS as
applied in Latvia).

Latvian companies report under the Law on Accounting and annual-report
legislation or IFRS. This chart layers Latvia-specific tax and payroll
accounts on top of an IFRS-style structure:

CIT  = Corporate Income Tax (uzņēmumu ienākuma nodoklis) — Estonian model:
       0% on retained profit, 20% of the grossed-up base on distribution
       (effectively 25% of the net distribution).
PVN  = Value Added Tax (pievienotās vērtības nodoklis, 21% standard).
VSAOI = State social insurance mandatory contributions.
IIN  = Personal income tax withheld on payroll (iedzīvotāju ienākuma nodoklis).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LVGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


LV_GAAP: list[LVGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    LVGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1020", "Swedbank Latvija Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1021", "SEB Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1022", "Citadele Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1023", "Luminor Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    LVGAAPAccount("1040", "Short-Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    LVGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LVGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    LVGAAPAccount("1120", "Intra-EU Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LVGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    LVGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    LVGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    LVGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    LVGAAPAccount("1170", "Input PVN (VAT) Receivable", "Asset", "Tax Receivable", "Debit"),
    LVGAAPAccount("1180", "Other Tax Receivable (VID)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    LVGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    LVGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    LVGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    LVGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    LVGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    LVGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    LVGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    LVGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    LVGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    LVGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    LVGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    LVGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    LVGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    LVGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    LVGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    LVGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    LVGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    LVGAAPAccount("2100", "Output PVN (VAT) Payable", "Liability", "Tax Payable", "Credit"),
    LVGAAPAccount("2110", "PVN Settlement Account (VID)", "Liability", "Tax Payable", "Credit"),
    LVGAAPAccount("2120", "CIT on Distributed Profit Payable (UIN)", "Liability", "Tax Payable", "Credit"),
    LVGAAPAccount("2130", "Payroll Income Tax Payable (IIN)", "Liability", "Tax Payable", "Credit"),
    LVGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    LVGAAPAccount("2210", "VSAOI Social Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    LVGAAPAccount("2220", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    LVGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    LVGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    LVGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    LVGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    LVGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    LVGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    LVGAAPAccount("3000", "Share Capital (Pamatkapitāls)", "Equity", "Contributed Capital", "Credit"),
    LVGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    LVGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    LVGAAPAccount("3110", "Other Reserves", "Equity", "Reserves", "Credit"),
    LVGAAPAccount("3200", "Retained Earnings (Untaxed Until Distribution)", "Equity", "Retained Earnings", "Credit"),
    LVGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    LVGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    LVGAAPAccount("4000", "Revenue — Goods (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    LVGAAPAccount("4010", "Revenue — Services (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    LVGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    LVGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    LVGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    LVGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    LVGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    LVGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    LVGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    LVGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    LVGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    LVGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    LVGAAPAccount("6010", "VSAOI Employer Contributions", "Expense", "Staff Costs", "Debit"),
    LVGAAPAccount("6020", "Vacation Pay Expense", "Expense", "Staff Costs", "Debit"),
    LVGAAPAccount("6030", "Employee Training and Benefits", "Expense", "Staff Costs", "Debit"),
    LVGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    LVGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    LVGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    LVGAAPAccount("6200", "Uzņēmumu Reģistrs and Government Fees", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6220", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6270", "Non-Business Expenses (Deemed Distribution Base)", "Expense", "Administrative Expenses", "Debit"),
    LVGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    LVGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    LVGAAPAccount("6400", "CIT Expense on Distributed Profit (UIN)", "Expense", "Tax Expense", "Debit"),
]
