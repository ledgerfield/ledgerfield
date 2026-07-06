"""Bangladesh chart of accounts (IFRS as adopted in Bangladesh — BFRS/BAS).

Bangladeshi companies report under Bangladesh Financial Reporting Standards
(BFRS), which converge with IFRS. This chart layers Bangladesh-specific tax
and compliance accounts on top of an IFRS structure:

CIT = Corporate Income Tax (Income Tax Act 2023; 27.5% non-listed standard).
VAT = Value Added Tax (VAT & SD Act 2012; 15% standard, Mushak returns).
AIT = Advance Income Tax (withheld/collected at source, creditable).
SD  = Supplementary Duty.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BDGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


BD_GAAP: list[BDGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    BDGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1020", "Sonali Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1021", "BRAC Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1022", "Dutch-Bangla Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1023", "Islami Bank Bangladesh Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1024", "Mobile Financial Services (bKash/Nagad) Clearing", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BDGAAPAccount("1040", "Fixed Deposit Receipt (FDR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    BDGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BDGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    BDGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    BDGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BDGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    BDGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    BDGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    BDGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    BDGAAPAccount("1180", "VAT Input (Rebate) Receivable — Mushak", "Asset", "Tax Receivable", "Debit"),
    BDGAAPAccount("1185", "Advance Income Tax (AIT) Receivable", "Asset", "Tax Receivable", "Debit"),
    BDGAAPAccount("1190", "Tax Deducted at Source (TDS) Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    BDGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    BDGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    BDGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    BDGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    BDGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    BDGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    BDGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    BDGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    BDGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    BDGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    BDGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    BDGAAPAccount("1620", "Trade Licence and BIN Registration", "Asset", "Intangible Assets", "Debit"),
    BDGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    BDGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    BDGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    BDGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    BDGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    BDGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    BDGAAPAccount("2100", "VAT Output Payable — Mushak", "Liability", "Tax Payable", "Credit"),
    BDGAAPAccount("2110", "Supplementary Duty (SD) Payable", "Liability", "Tax Payable", "Credit"),
    BDGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    BDGAAPAccount("2130", "Tax Deducted at Source (TDS) Payable", "Liability", "Tax Payable", "Credit"),
    BDGAAPAccount("2140", "VAT Deducted at Source (VDS) Payable", "Liability", "Tax Payable", "Credit"),
    BDGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    BDGAAPAccount("2210", "Provident Fund Payable", "Liability", "Employee Benefits", "Credit"),
    BDGAAPAccount("2220", "Gratuity Provision", "Liability", "Employee Benefits", "Credit"),
    BDGAAPAccount("2230", "Workers' Profit Participation Fund (WPPF) Payable", "Liability", "Employee Benefits", "Credit"),
    BDGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    BDGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    BDGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    BDGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    BDGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    BDGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),
    BDGAAPAccount("2430", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    BDGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    BDGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    BDGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    BDGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    BDGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    BDGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    BDGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    BDGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    BDGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    BDGAAPAccount("4020", "Revenue — Exports (RMG and Other)", "Revenue", "Operating Revenue", "Credit"),
    BDGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    BDGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    BDGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    BDGAAPAccount("4210", "Cash Incentive on Exports", "Revenue", "Other Income", "Credit"),
    BDGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    BDGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    BDGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    BDGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    BDGAAPAccount("5030", "Customs Duty and Import Charges", "Expense", "Cost of Sales", "Debit"),
    BDGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    BDGAAPAccount("6010", "Provident Fund Employer Contribution", "Expense", "Staff Costs", "Debit"),
    BDGAAPAccount("6020", "Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    BDGAAPAccount("6030", "Employee Medical and Group Insurance", "Expense", "Staff Costs", "Debit"),
    BDGAAPAccount("6040", "Festival Bonus (Eid)", "Expense", "Staff Costs", "Debit"),
    BDGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    BDGAAPAccount("6110", "Utilities (DESCO / Titas / WASA)", "Expense", "Occupancy Costs", "Debit"),
    BDGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    BDGAAPAccount("6200", "Trade Licence Renewal", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6210", "Government and City Corporation Fees", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6230", "Telecommunications (Grameenphone / Robi / Banglalink)", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6280", "Non-Recoverable VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    BDGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    BDGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    BDGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    BDGAAPAccount("6410", "Minimum Tax on Gross Receipts Expense", "Expense", "Tax Expense", "Debit"),
    BDGAAPAccount("6420", "Deferred Tax Expense", "Expense", "Tax Expense", "Debit"),
]
