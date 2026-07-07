"""Republic of Serbia chart of accounts (IFRS as applied in Serbia).

Serbian companies report under IFRS / IFRS for SMEs, aligned with the national
Kontni okvir. This chart layers Serbia-specific tax and payroll accounts on an
IFRS structure:

CIT = Corporate Income Tax (porez na dobit, 15% flat).
PDV = Value Added Tax (VAT, 20% standard / 10% reduced).
WHT = Withholding Tax (porez po odbitku) on certain non-resident payments.

NOTE: Accounts and associated rates are AI-estimated and require verification.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RSGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


RS_GAAP: list[RSGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    RSGAAPAccount("1010", "Cash on Hand (Blagajna)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1020", "Banca Intesa Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1021", "OTP Banka Srbija Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1022", "Komercijalna Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1023", "UniCredit Bank Srbija Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1024", "Raiffeisen Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    RSGAAPAccount("1040", "Short-Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    RSGAAPAccount("1100", "Trade Receivables (Kupci)", "Asset", "Trade and Other Receivables", "Debit"),
    RSGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    RSGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    RSGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    RSGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    RSGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    RSGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    RSGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    RSGAAPAccount("1180", "Input VAT Receivable (Pretporez)", "Asset", "Tax Receivable", "Debit"),
    RSGAAPAccount("1185", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    RSGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    RSGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    RSGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    RSGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    RSGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    RSGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    RSGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    RSGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    RSGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    RSGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    RSGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    RSGAAPAccount("1620", "Business Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    RSGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    RSGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    RSGAAPAccount("2000", "Trade Payables (Dobavljači)", "Liability", "Trade and Other Payables", "Credit"),
    RSGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    RSGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    RSGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    RSGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    RSGAAPAccount("2100", "Output VAT Payable (PDV)", "Liability", "Tax Payable", "Credit"),
    RSGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    RSGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    RSGAAPAccount("2140", "Personal Income Tax Payable (Payroll)", "Liability", "Tax Payable", "Credit"),
    RSGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    RSGAAPAccount("2210", "Social Contributions Payable (PIO/RFZO)", "Liability", "Employee Benefits", "Credit"),
    RSGAAPAccount("2220", "Employee Leave Provision", "Liability", "Employee Benefits", "Credit"),
    RSGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    RSGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    RSGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    RSGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    RSGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    RSGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    RSGAAPAccount("3000", "Share Capital (Osnovni kapital)", "Equity", "Contributed Capital", "Credit"),
    RSGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    RSGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    RSGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    RSGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    RSGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    RSGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    RSGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    RSGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    RSGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    RSGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    RSGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    RSGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    RSGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    RSGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    RSGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    RSGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    RSGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    RSGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    RSGAAPAccount("6010", "Social Contributions Employer", "Expense", "Staff Costs", "Debit"),
    RSGAAPAccount("6020", "Employee Meal and Transport Allowance", "Expense", "Staff Costs", "Debit"),
    RSGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    RSGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    RSGAAPAccount("6110", "Utilities (EPS / Water)", "Expense", "Occupancy Costs", "Debit"),
    RSGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    RSGAAPAccount("6200", "Business Registration Renewal (APR)", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    RSGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    RSGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    RSGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
