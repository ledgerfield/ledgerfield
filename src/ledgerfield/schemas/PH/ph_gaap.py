"""Republic of the Philippines chart of accounts (PFRS).

Philippine companies report under Philippine Financial Reporting Standards
(PFRS), the local adoption of IFRS. This chart layers Philippine-specific tax
and payroll accounts on top of a PFRS structure:

CIT = Corporate Income Tax (25% standard / 20% SME, CREATE Act RA 11534).
MCIT = Minimum Corporate Income Tax (2% of gross income from the 4th year).
VAT = Value-Added Tax (12%): input VAT and output VAT accounts included.
WHT = Withholding taxes (expanded/final/compensation) collected by the BIR.
SSS/PhilHealth/Pag-IBIG = mandatory employee social contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PHGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


PH_GAAP: list[PHGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    PHGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1020", "BDO Unibank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1021", "Bank of the Philippine Islands (BPI) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1022", "Metrobank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1023", "Land Bank of the Philippines Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PHGAAPAccount("1040", "Time Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    PHGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PHGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    PHGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    PHGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PHGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    PHGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    PHGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    PHGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    PHGAAPAccount("1180", "Input VAT", "Asset", "Tax Receivable", "Debit"),
    PHGAAPAccount("1185", "Deferred Input VAT", "Asset", "Tax Receivable", "Debit"),
    PHGAAPAccount("1190", "Creditable Withholding Tax (BIR Form 2307)", "Asset", "Tax Receivable", "Debit"),
    PHGAAPAccount("1195", "MCIT Carry-Forward Credit", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    PHGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    PHGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    PHGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    PHGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    PHGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    PHGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    PHGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    PHGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    PHGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1570", "Right-of-Use Asset (PFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    PHGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    PHGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    PHGAAPAccount("1620", "SEC / DTI Registration and Permits", "Asset", "Intangible Assets", "Debit"),
    PHGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    PHGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    PHGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    PHGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    PHGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    PHGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    PHGAAPAccount("2100", "Output VAT", "Liability", "Tax Payable", "Credit"),
    PHGAAPAccount("2110", "VAT Payable (BIR Form 2550)", "Liability", "Tax Payable", "Credit"),
    PHGAAPAccount("2120", "Corporate Income Tax Payable (BIR Form 1702)", "Liability", "Tax Payable", "Credit"),
    PHGAAPAccount("2130", "Expanded Withholding Tax Payable (BIR Form 0619-E)", "Liability", "Tax Payable", "Credit"),
    PHGAAPAccount("2140", "Final Withholding Tax Payable (BIR Form 0619-F)", "Liability", "Tax Payable", "Credit"),
    PHGAAPAccount("2150", "Withholding Tax on Compensation Payable (BIR Form 1601-C)", "Liability", "Tax Payable", "Credit"),
    PHGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    PHGAAPAccount("2210", "SSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    PHGAAPAccount("2220", "PhilHealth Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    PHGAAPAccount("2230", "Pag-IBIG (HDMF) Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    PHGAAPAccount("2240", "13th Month Pay Provision", "Liability", "Employee Benefits", "Credit"),
    PHGAAPAccount("2250", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    PHGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    PHGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    PHGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    PHGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    PHGAAPAccount("2410", "Lease Liability (PFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    PHGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    PHGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    PHGAAPAccount("3010", "Additional Paid-In Capital", "Equity", "Contributed Capital", "Credit"),
    PHGAAPAccount("3100", "Appropriated Retained Earnings", "Equity", "Reserves", "Credit"),
    PHGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    PHGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    PHGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    PHGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    PHGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    PHGAAPAccount("4020", "Revenue — Exports (VAT Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    PHGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    PHGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    PHGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    PHGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    PHGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    PHGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    PHGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    PHGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    PHGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    PHGAAPAccount("6010", "13th Month Pay Expense", "Expense", "Staff Costs", "Debit"),
    PHGAAPAccount("6020", "SSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PHGAAPAccount("6030", "PhilHealth Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PHGAAPAccount("6040", "Pag-IBIG (HDMF) Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PHGAAPAccount("6050", "Employee Medical Insurance (HMO)", "Expense", "Staff Costs", "Debit"),
    PHGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    PHGAAPAccount("6110", "Utilities (Meralco / Water)", "Expense", "Occupancy Costs", "Debit"),
    PHGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    PHGAAPAccount("6200", "Business Permit and Local Business Tax (LGU)", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6210", "BIR Annual Registration and Documentary Stamp Tax", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6230", "Telecommunications (PLDT / Globe)", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    PHGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    PHGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    PHGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    PHGAAPAccount("6410", "Minimum Corporate Income Tax (MCIT) Expense", "Expense", "Tax Expense", "Debit"),
]
