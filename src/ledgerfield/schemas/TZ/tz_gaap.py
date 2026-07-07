"""United Republic of Tanzania chart of accounts (IFRS as applied in Tanzania).

Tanzanian companies report under IFRS (with IFRS for SMEs available for
smaller entities), overseen by the National Board of Accountants and Auditors
(NBAA). This chart layers Tanzania-specific tax and payroll accounts on top of
an IFRS structure:

CIT  = Corporate Income Tax (30% standard, Income Tax Act 2004).
VAT  = Value Added Tax (18% mainland standard rate).
SDL  = Skills and Development Levy (payroll levy).
NSSF = National Social Security Fund contributions.
WCF  = Workers Compensation Fund contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TZ_GAAP: list[TZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    TZGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1020", "CRDB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1021", "NMB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1022", "NBC Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1023", "Stanbic Bank Tanzania Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1025", "Mobile Money Float (M-Pesa / Tigo Pesa / Airtel Money)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TZGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    TZGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TZGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    TZGAAPAccount("1120", "Staff Advances", "Asset", "Trade and Other Receivables", "Debit"),
    TZGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TZGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    TZGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    TZGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    TZGAAPAccount("1180", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    TZGAAPAccount("1190", "Withholding Tax Credits (TRA)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    TZGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    TZGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    TZGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    TZGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    TZGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    TZGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    TZGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    TZGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    TZGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    TZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    TZGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    TZGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    TZGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    TZGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    TZGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    TZGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    TZGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    TZGAAPAccount("2100", "VAT Output (Payable)", "Liability", "Tax Payable", "Credit"),
    TZGAAPAccount("2110", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    TZGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    TZGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    TZGAAPAccount("2140", "Skills and Development Levy (SDL) Payable", "Liability", "Tax Payable", "Credit"),
    TZGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    TZGAAPAccount("2210", "NSSF Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    TZGAAPAccount("2220", "Workers Compensation Fund (WCF) Payable", "Liability", "Employee Benefits", "Credit"),
    TZGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    TZGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    TZGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    TZGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    TZGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    TZGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    TZGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    TZGAAPAccount("3100", "General Reserve", "Equity", "Reserves", "Credit"),
    TZGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    TZGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    TZGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    TZGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    TZGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    TZGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    TZGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    TZGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    TZGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    TZGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    TZGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    TZGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    TZGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    TZGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    TZGAAPAccount("6010", "NSSF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    TZGAAPAccount("6020", "Skills and Development Levy (SDL) Expense", "Expense", "Staff Costs", "Debit"),
    TZGAAPAccount("6030", "Workers Compensation Fund (WCF) Expense", "Expense", "Staff Costs", "Debit"),
    TZGAAPAccount("6040", "Employee Medical Insurance (NHIF)", "Expense", "Staff Costs", "Debit"),
    TZGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    TZGAAPAccount("6110", "Utilities (TANESCO / DAWASA)", "Expense", "Occupancy Costs", "Debit"),
    TZGAAPAccount("6200", "Business Licence and Registration Fees (BRELA)", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6230", "Telecommunications (Vodacom / Airtel / TTCL)", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    TZGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    TZGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    TZGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
