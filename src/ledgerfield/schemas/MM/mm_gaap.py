"""Myanmar chart of accounts (Myanmar Financial Reporting Standards, MFRS/IFRS-based).

Myanmar companies report under the Myanmar Financial Reporting Standards
(aligned with IFRS). This chart layers Myanmar-specific tax and labour
accounts on top of an IFRS structure:

CIT = Corporate Income Tax (22% standard; 17% for YSX-listed companies).
CT  = Commercial Tax (generally 5%, 0-8% band) — Myanmar has no VAT, so no
      VAT accounts are included; Commercial Tax accounts take their place.
SGT = Specific Goods Tax (excise-like, on tobacco/liquor/vehicles).
WHT = Withholding Tax (e.g. 2.5% on payments to non-residents for
      goods/services; royalties 10%/15%).
SSB = Social Security Board contributions (Social Security Law 2012).

The fiscal year runs October-September (FY2024-25).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MM_GAAP: list[MMGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MMGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1020", "KBZ Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1021", "CB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1022", "AYA Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1023", "Yoma Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1024", "Myanma Economic Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MMGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MMGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MMGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MMGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    MMGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MMGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MMGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MMGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MMGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MMGAAPAccount("1180", "Commercial Tax Receivable (Offsetable Input CT)", "Asset", "Tax Receivable", "Debit"),
    MMGAAPAccount("1190", "Withholding Tax Receivable (Advance CIT Credit)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MMGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MMGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MMGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MMGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MMGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MMGAAPAccount("1500", "Land and Land-Use Rights", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MMGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MMGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MMGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MMGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MMGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MMGAAPAccount("1620", "DICA Registration and Business Licences", "Asset", "Intangible Assets", "Debit"),
    MMGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MMGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MMGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MMGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MMGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MMGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MMGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    MMGAAPAccount("2100", "Commercial Tax Payable", "Liability", "Tax Payable", "Credit"),
    MMGAAPAccount("2110", "Specific Goods Tax (SGT) Payable", "Liability", "Tax Payable", "Credit"),
    MMGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    MMGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    MMGAAPAccount("2140", "Personal Income Tax Withheld (PAYE) Payable", "Liability", "Tax Payable", "Credit"),
    MMGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MMGAAPAccount("2210", "Social Security Board (SSB) Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    MMGAAPAccount("2220", "Severance Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MMGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MMGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MMGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MMGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MMGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MMGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MMGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MMGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    MMGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    MMGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    MMGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    MMGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MMGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MMGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MMGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MMGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MMGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    MMGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MMGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MMGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MMGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MMGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MMGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MMGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MMGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MMGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MMGAAPAccount("6010", "Severance Pay Expense", "Expense", "Staff Costs", "Debit"),
    MMGAAPAccount("6020", "SSB Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MMGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    MMGAAPAccount("6040", "Work Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    MMGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MMGAAPAccount("6110", "Utilities (Electricity and Water)", "Expense", "Occupancy Costs", "Debit"),
    MMGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MMGAAPAccount("6200", "DICA Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6230", "Telecommunications (MPT / Telenor / Ooredoo)", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6280", "Commercial Tax Expense (Non-Offsetable)", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6290", "Specific Goods Tax (SGT) Expense", "Expense", "Administrative Expenses", "Debit"),
    MMGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MMGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MMGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
