"""Republic of Fiji chart of accounts (IFRS as applied in Fiji).

Fijian companies report under IFRS. This chart layers Fiji-specific tax and
labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (20% resident / 25% non-resident).
VAT = Value Added Tax (15%).
FNPF = Fiji National Provident Fund (retirement contributions).

NOTE: Tax rates referenced here are AI-estimated and require verification
against official FRCS guidance.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FJGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


FJ_GAAP: list[FJGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    FJGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1020", "ANZ Fiji Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1021", "BSP (Bank South Pacific) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1022", "Westpac Fiji Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1023", "HFC Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    FJGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    FJGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    FJGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    FJGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    FJGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    FJGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    FJGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    FJGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    FJGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    FJGAAPAccount("1180", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    FJGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    FJGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    FJGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    FJGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    FJGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    FJGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    FJGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    FJGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    FJGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    FJGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    FJGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    FJGAAPAccount("1620", "Business Licences and Permits", "Asset", "Intangible Assets", "Debit"),
    FJGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    FJGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    FJGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    FJGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    FJGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    FJGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    FJGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    FJGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    FJGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    FJGAAPAccount("2130", "PAYE / Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    FJGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    FJGAAPAccount("2210", "FNPF Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    FJGAAPAccount("2220", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    FJGAAPAccount("2230", "Gratuity / Long-Service Provision", "Liability", "Employee Benefits", "Credit"),
    FJGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    FJGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    FJGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    FJGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    FJGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    FJGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    FJGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    FJGAAPAccount("3010", "Shareholders' Current Account", "Equity", "Contributed Capital", "Credit"),
    FJGAAPAccount("3100", "General Reserve", "Equity", "Reserves", "Credit"),
    FJGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    FJGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    FJGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    FJGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    FJGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    FJGAAPAccount("4020", "Revenue — Tourism and Hospitality", "Revenue", "Operating Revenue", "Credit"),
    FJGAAPAccount("4030", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    FJGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    FJGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    FJGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    FJGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    FJGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    FJGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    FJGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    FJGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    FJGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    FJGAAPAccount("6010", "FNPF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    FJGAAPAccount("6020", "Staff Training", "Expense", "Staff Costs", "Debit"),
    FJGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    FJGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    FJGAAPAccount("6110", "Electricity (EFL) and Water", "Expense", "Occupancy Costs", "Debit"),
    FJGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    FJGAAPAccount("6200", "Business Licence Renewal", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    FJGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    FJGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    FJGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
