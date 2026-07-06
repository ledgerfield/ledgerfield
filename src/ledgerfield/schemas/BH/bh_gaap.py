"""Kingdom of Bahrain chart of accounts (IFRS as applied in Bahrain).

Bahraini companies report under IFRS. This chart layers Bahrain-specific tax
and labour accounts on top of an IFRS structure:

VAT = Value Added Tax, 10% standard rate (raised from 5% on 1 January 2022),
administered by the National Bureau for Revenue (NBR).
SIO = Social Insurance Organization contributions (Bahraini nationals 7%/12%,
expatriates 1%/3%).
EOSB = End-of-Service Gratuity / Leaving Indemnity (Bahrain Labour Law).

Bahrain has no general corporate income tax; only oil & gas is taxed (46%),
and from 2025 a 15% DMTT applies to large MNEs (out of SME scope).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BHGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


BH_GAAP: list[BHGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    BHGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1020", "National Bank of Bahrain (NBB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1021", "Bank of Bahrain and Kuwait (BBK) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1022", "Ahli United Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1023", "Bahrain Islamic Bank (BisB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1024", "Al Salam Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BHGAAPAccount("1040", "Wakala Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    BHGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BHGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    BHGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    BHGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BHGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    BHGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    BHGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    BHGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    BHGAAPAccount("1180", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    BHGAAPAccount("1190", "VAT Refund Receivable (NBR)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    BHGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    BHGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    BHGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    BHGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    BHGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    BHGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    BHGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    BHGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    BHGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    BHGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    BHGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    BHGAAPAccount("1620", "Commercial Registration (CR) and Licences", "Asset", "Intangible Assets", "Debit"),
    BHGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    BHGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    BHGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    BHGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    BHGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    BHGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    BHGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    BHGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    BHGAAPAccount("2110", "VAT Payable to NBR (Net)", "Liability", "Tax Payable", "Credit"),
    BHGAAPAccount("2120", "Corporate Income Tax Payable (Oil & Gas)", "Liability", "Tax Payable", "Credit"),
    BHGAAPAccount("2130", "Excise Tax Payable", "Liability", "Tax Payable", "Credit"),
    BHGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    BHGAAPAccount("2210", "WPS Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    BHGAAPAccount("2220", "End-of-Service Gratuity Provision", "Liability", "Employee Benefits", "Credit"),
    BHGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    BHGAAPAccount("2240", "SIO Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    BHGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    BHGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    BHGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    BHGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    BHGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    BHGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    BHGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    BHGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    BHGAAPAccount("3100", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    BHGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    BHGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    BHGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    BHGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    BHGAAPAccount("4000", "Revenue — Goods (Standard-Rated 10%)", "Revenue", "Operating Revenue", "Credit"),
    BHGAAPAccount("4010", "Revenue — Services (Standard-Rated 10%)", "Revenue", "Operating Revenue", "Credit"),
    BHGAAPAccount("4020", "Revenue — Zero-Rated / Exports", "Revenue", "Operating Revenue", "Credit"),
    BHGAAPAccount("4030", "Revenue — VAT-Exempt Supplies", "Revenue", "Operating Revenue", "Credit"),
    BHGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    BHGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    BHGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    BHGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    BHGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    BHGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    BHGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    BHGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    BHGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    BHGAAPAccount("6010", "End-of-Service Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    BHGAAPAccount("6020", "SIO Employer Contribution", "Expense", "Staff Costs", "Debit"),
    BHGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    BHGAAPAccount("6040", "Work Permit and Visa Fees (LMRA)", "Expense", "Staff Costs", "Debit"),
    BHGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    BHGAAPAccount("6110", "Utilities (EWA)", "Expense", "Occupancy Costs", "Debit"),
    BHGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    BHGAAPAccount("6200", "Commercial Registration (CR) Renewal", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6230", "Telecommunications (Batelco / stc / Zain)", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6280", "Irrecoverable VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    BHGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    BHGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    BHGAAPAccount("6400", "Corporate Income Tax Expense (Oil & Gas)", "Expense", "Tax Expense", "Debit"),
]
