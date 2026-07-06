"""Thailand chart of accounts (TFRS — Thai Financial Reporting Standards).

Thai companies report under TFRS (converged with IFRS). This chart layers
Thailand-specific tax and labour accounts on top of an IFRS-style structure:

CIT = Corporate Income Tax (20% standard; SME progressive brackets).
VAT = Value Added Tax (7%, statutory 10% temporarily reduced by royal decree).
WHT = Withholding Tax (e.g. 10% dividends, 15% interest).
SSF = Social Security Fund (5% employee / 5% employer, capped wage base).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class THGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TH_GAAP: list[THGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    THGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1020", "Bangkok Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1021", "Kasikornbank (KBank) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1022", "Siam Commercial Bank (SCB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1023", "Krungthai Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    THGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    THGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    THGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    THGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    THGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    THGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    THGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    THGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    THGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    THGAAPAccount("1180", "Input VAT (Purchase VAT)", "Asset", "Tax Receivable", "Debit"),
    THGAAPAccount("1185", "Undue Input VAT", "Asset", "Tax Receivable", "Debit"),
    THGAAPAccount("1190", "Withholding Tax Deducted at Source (Prepaid CIT)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    THGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    THGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    THGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    THGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    THGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    THGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    THGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    THGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    THGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1570", "Right-of-Use Asset (TFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    THGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    THGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    THGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    THGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),
    THGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    THGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    THGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    THGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    THGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    THGAAPAccount("2100", "Output VAT (Sales VAT)", "Liability", "Tax Payable", "Credit"),
    THGAAPAccount("2105", "Undue Output VAT", "Liability", "Tax Payable", "Credit"),
    THGAAPAccount("2110", "VAT Payable (PP.30 Settlement)", "Liability", "Tax Payable", "Credit"),
    THGAAPAccount("2120", "Corporate Income Tax Payable (PND.50)", "Liability", "Tax Payable", "Credit"),
    THGAAPAccount("2130", "Withholding Tax Payable (PND.3/53)", "Liability", "Tax Payable", "Credit"),
    THGAAPAccount("2140", "Personal Income Tax Withheld (PND.1)", "Liability", "Tax Payable", "Credit"),
    THGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    THGAAPAccount("2210", "Social Security Fund Payable", "Liability", "Employee Benefits", "Credit"),
    THGAAPAccount("2220", "Severance Pay Provision (Labour Protection Act)", "Liability", "Employee Benefits", "Credit"),
    THGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    THGAAPAccount("2240", "Provident Fund Payable", "Liability", "Employee Benefits", "Credit"),
    THGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    THGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    THGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    THGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    THGAAPAccount("2410", "Lease Liability (TFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    THGAAPAccount("2420", "Director Loan", "Liability", "Non-Current Liabilities", "Credit"),
    THGAAPAccount("2430", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    THGAAPAccount("3000", "Share Capital (Paid-Up)", "Equity", "Contributed Capital", "Credit"),
    THGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    THGAAPAccount("3100", "Legal Reserve (Civil and Commercial Code)", "Equity", "Reserves", "Credit"),
    THGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    THGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    THGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    THGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    THGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    THGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    THGAAPAccount("4020", "Revenue — Exports (Zero-Rated VAT)", "Revenue", "Operating Revenue", "Credit"),
    THGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    THGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    THGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    THGAAPAccount("4210", "Interest Income", "Revenue", "Other Income", "Credit"),
    THGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    THGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    THGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    THGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    THGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    THGAAPAccount("6010", "Social Security Fund Employer Contribution", "Expense", "Staff Costs", "Debit"),
    THGAAPAccount("6020", "Provident Fund Employer Contribution", "Expense", "Staff Costs", "Debit"),
    THGAAPAccount("6030", "Severance Pay Expense", "Expense", "Staff Costs", "Debit"),
    THGAAPAccount("6040", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    THGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    THGAAPAccount("6110", "Utilities (MEA / PEA / MWA)", "Expense", "Occupancy Costs", "Debit"),
    THGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    THGAAPAccount("6200", "Company Registration and DBD Fees", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6230", "Telecommunications (AIS / True / NT)", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6280", "Non-Deductible Entertainment (Excess over Limit)", "Expense", "Administrative Expenses", "Debit"),
    THGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    THGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    THGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    THGAAPAccount("6410", "Deferred Tax Expense / (Income)", "Expense", "Tax Expense", "Debit"),
]
