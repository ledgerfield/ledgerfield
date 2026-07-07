"""Montenegro chart of accounts (IFRS as applied in Montenegro).

Montenegrin companies report under IFRS / IFRS for SMEs. This chart layers
Montenegro-specific tax and payroll accounts on an IFRS structure:

CIT = Corporate Income Tax (porez na dobit, progressive 9% / 12% / 15%).
PDV = Value Added Tax (VAT, 21% standard / 7% reduced).
WHT = Withholding Tax (porez po odbitku) on certain non-resident payments.

Montenegro uses the euro (EUR) as its currency.

NOTE: Accounts and associated rates are AI-estimated and require verification.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


ME_GAAP: list[MEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MEGAAPAccount("1010", "Cash on Hand (Blagajna)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1020", "Crnogorska Komercijalna Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1021", "NLB Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1022", "Erste Bank Montenegro Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1023", "Hipotekarna Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1024", "Prva Banka Crne Gore Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MEGAAPAccount("1040", "Short-Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MEGAAPAccount("1100", "Trade Receivables (Kupci)", "Asset", "Trade and Other Receivables", "Debit"),
    MEGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MEGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    MEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MEGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MEGAAPAccount("1180", "Input VAT Receivable (Ulazni PDV)", "Asset", "Tax Receivable", "Debit"),
    MEGAAPAccount("1185", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MEGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MEGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MEGAAPAccount("1620", "Business Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    MEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MEGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MEGAAPAccount("2000", "Trade Payables (Dobavljači)", "Liability", "Trade and Other Payables", "Credit"),
    MEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MEGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    MEGAAPAccount("2100", "Output VAT Payable (Izlazni PDV)", "Liability", "Tax Payable", "Credit"),
    MEGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    MEGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    MEGAAPAccount("2140", "Personal Income Tax Payable (Payroll)", "Liability", "Tax Payable", "Credit"),
    MEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MEGAAPAccount("2210", "Social Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    MEGAAPAccount("2220", "Employee Leave Provision", "Liability", "Employee Benefits", "Credit"),
    MEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MEGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MEGAAPAccount("3000", "Share Capital (Osnovni kapital)", "Equity", "Contributed Capital", "Credit"),
    MEGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    MEGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    MEGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    MEGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MEGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MEGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MEGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MEGAAPAccount("4020", "Revenue — Tourism and Hospitality", "Revenue", "Operating Revenue", "Credit"),
    MEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MEGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MEGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MEGAAPAccount("6010", "Social Contributions Employer", "Expense", "Staff Costs", "Debit"),
    MEGAAPAccount("6020", "Employee Meal and Transport Allowance", "Expense", "Staff Costs", "Debit"),
    MEGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    MEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MEGAAPAccount("6110", "Utilities (EPCG / Water)", "Expense", "Occupancy Costs", "Debit"),
    MEGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MEGAAPAccount("6200", "Business Registration Renewal (CRPS)", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MEGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MEGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
