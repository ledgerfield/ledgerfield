"""Republic of Uganda chart of accounts (IFRS as applied in Uganda).

Ugandan companies report under IFRS. This chart layers Uganda-specific tax and
statutory accounts on top of an IFRS structure:

CIT = Corporate Income Tax (30%, Income Tax Act Cap 340).
VAT = Value Added Tax (18% standard rate, VAT Act Cap 349).
PAYE = Pay As You Earn (employee income tax withheld by employer).
NSSF = National Social Security Fund; LST = Local Service Tax.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


UG_GAAP: list[UGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    UGGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1020", "Stanbic Bank Uganda Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1021", "Centenary Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1022", "dfcu Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1023", "Absa Bank Uganda Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1024", "Mobile Money Wallet (MTN / Airtel)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UGGAAPAccount("1040", "Fixed Deposit Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    UGGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UGGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    UGGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    UGGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UGGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    UGGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    UGGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    UGGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    UGGAAPAccount("1180", "VAT Input (Deductible)", "Asset", "Tax Receivable", "Debit"),
    UGGAAPAccount("1185", "Withholding Tax Credits (Advance Tax)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    UGGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    UGGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    UGGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    UGGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    UGGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    UGGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    UGGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    UGGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    UGGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    UGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    UGGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    UGGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    UGGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    UGGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    UGGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    UGGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    UGGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    UGGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    UGGAAPAccount("2110", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    UGGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    UGGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    UGGAAPAccount("2140", "Presumptive Tax Payable", "Liability", "Tax Payable", "Credit"),
    UGGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    UGGAAPAccount("2210", "NSSF Payable", "Liability", "Employee Benefits", "Credit"),
    UGGAAPAccount("2220", "Local Service Tax Payable", "Liability", "Employee Benefits", "Credit"),
    UGGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    UGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    UGGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    UGGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    UGGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    UGGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    UGGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    UGGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    UGGAAPAccount("3100", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    UGGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    UGGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    UGGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    UGGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    UGGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    UGGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    UGGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    UGGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    UGGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    UGGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    UGGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    UGGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    UGGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    UGGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    UGGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    UGGAAPAccount("6010", "NSSF Employer Contribution (10%)", "Expense", "Staff Costs", "Debit"),
    UGGAAPAccount("6020", "Staff Medical Insurance", "Expense", "Staff Costs", "Debit"),
    UGGAAPAccount("6030", "Staff Training and Welfare", "Expense", "Staff Costs", "Debit"),
    UGGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    UGGAAPAccount("6110", "Utilities (Umeme / NWSC)", "Expense", "Occupancy Costs", "Debit"),
    UGGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    UGGAAPAccount("6200", "Trading Licence and Permit Fees", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6210", "KCCA / Local Government Fees", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6230", "Telecommunications (MTN / Airtel)", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6250", "Bank and Mobile Money Charges", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    UGGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    UGGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    UGGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
