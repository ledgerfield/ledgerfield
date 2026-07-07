"""Trinidad and Tobago chart of accounts (IFRS as applied in T&T).

Trinidad and Tobago companies report under full IFRS; qualifying SMEs may use
IFRS for SMEs. This chart layers T&T-specific tax and payroll accounts on top
of an IFRS structure:

CIT = Corporation Tax (30% standard / 35% banks & petrochemical / 50% PPT).
VAT = Value Added Tax (12.5% standard).
Business levy (0.6% gross revenue) and green fund levy (0.3% gross revenue)
have dedicated liability and expense accounts. NIS = National Insurance
System (NIBTT); Health Surcharge is a payroll deduction.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TTGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TT_GAAP: list[TTGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    TTGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1020", "Republic Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1021", "First Citizens Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1022", "Scotiabank Trinidad and Tobago Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1023", "RBC Royal Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TTGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    TTGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TTGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    TTGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TTGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    TTGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    TTGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    TTGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    TTGAAPAccount("1170", "VAT Input Tax Credit", "Asset", "Tax Receivable", "Debit"),
    TTGAAPAccount("1180", "Corporation Tax Refund Receivable", "Asset", "Tax Receivable", "Debit"),
    TTGAAPAccount("1190", "Business Levy Credit (against Corporation Tax)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    TTGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    TTGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    TTGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    TTGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    TTGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    TTGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    TTGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    TTGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    TTGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    TTGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    TTGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    TTGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    TTGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    TTGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    TTGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    TTGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    TTGAAPAccount("2100", "VAT Output Tax Payable", "Liability", "Tax Payable", "Credit"),
    TTGAAPAccount("2120", "Corporation Tax Payable", "Liability", "Tax Payable", "Credit"),
    TTGAAPAccount("2125", "Business Levy Payable (0.6% Gross Revenue)", "Liability", "Tax Payable", "Credit"),
    TTGAAPAccount("2126", "Green Fund Levy Payable (0.3% Gross Revenue)", "Liability", "Tax Payable", "Credit"),
    TTGAAPAccount("2130", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    TTGAAPAccount("2140", "Health Surcharge Payable", "Liability", "Tax Payable", "Credit"),
    TTGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    TTGAAPAccount("2210", "NIS (NIBTT) Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    TTGAAPAccount("2220", "Vacation Leave Provision", "Liability", "Employee Benefits", "Credit"),
    TTGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    TTGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    TTGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    TTGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    TTGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    TTGAAPAccount("3100", "Capital Reserve", "Equity", "Reserves", "Credit"),
    TTGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    TTGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    TTGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    TTGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    TTGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    TTGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    TTGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    TTGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    TTGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    TTGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    TTGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    TTGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    TTGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    TTGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    TTGAAPAccount("6010", "NIS (NIBTT) Employer Contribution", "Expense", "Staff Costs", "Debit"),
    TTGAAPAccount("6020", "Group Health Insurance", "Expense", "Staff Costs", "Debit"),
    TTGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    TTGAAPAccount("6110", "Utilities (T&TEC / WASA)", "Expense", "Occupancy Costs", "Debit"),
    TTGAAPAccount("6200", "Companies Registry Annual Return Fees", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6210", "Government Fees and Stamp Duty", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6230", "Telecommunications (bmobile / Digicel)", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    TTGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    TTGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    TTGAAPAccount("6400", "Corporation Tax Expense", "Expense", "Tax Expense", "Debit"),
    TTGAAPAccount("6410", "Business Levy Expense", "Expense", "Tax Expense", "Debit"),
    TTGAAPAccount("6420", "Green Fund Levy Expense", "Expense", "Tax Expense", "Debit"),
]
