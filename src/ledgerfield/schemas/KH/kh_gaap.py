"""Kingdom of Cambodia chart of accounts (CIFRS for SMEs).

Cambodian companies report under Cambodian International Financial Reporting
Standards (CIFRS / CIFRS for SMEs). This chart layers Cambodia-specific tax
and labour accounts on top of an IFRS structure:

ToI  = Tax on Income (20% standard; 30% oil/gas & certain minerals).
VAT  = Value Added Tax (10% standard rate; 0% on exports).
PToI = Prepayment of Tax on Income (1% of monthly turnover, creditable).
NSSF = National Social Security Fund contributions.
Seniority indemnity = twice-yearly payment under the Cambodian Labour Law.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class KHGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


KH_GAAP: list[KHGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    KHGAAPAccount("1010", "Cash on Hand (KHR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1020", "ACLEDA Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1021", "Canadia Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1022", "ABA Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1023", "Vattanac Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    KHGAAPAccount("1040", "Fixed Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    KHGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KHGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    KHGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    KHGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    KHGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    KHGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    KHGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    KHGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    KHGAAPAccount("1180", "VAT Input (Receivable)", "Asset", "Tax Receivable", "Debit"),
    KHGAAPAccount("1185", "VAT Refund Claim Receivable", "Asset", "Tax Receivable", "Debit"),
    KHGAAPAccount("1190", "Prepayment of Tax on Income (PToI Credit)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    KHGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    KHGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    KHGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    KHGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    KHGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    KHGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    KHGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    KHGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    KHGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    KHGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    KHGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    KHGAAPAccount("1620", "Business Registration and Patent Tax Licences", "Asset", "Intangible Assets", "Debit"),
    KHGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    KHGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    KHGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    KHGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    KHGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    KHGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    KHGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    KHGAAPAccount("2110", "VAT Settlement Account", "Liability", "Tax Payable", "Credit"),
    KHGAAPAccount("2120", "Tax on Income (ToI) Payable", "Liability", "Tax Payable", "Credit"),
    KHGAAPAccount("2125", "Minimum Tax Payable (1% of Turnover)", "Liability", "Tax Payable", "Credit"),
    KHGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    KHGAAPAccount("2140", "Tax on Salary Payable", "Liability", "Tax Payable", "Credit"),
    KHGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    KHGAAPAccount("2210", "NSSF Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    KHGAAPAccount("2220", "Seniority Indemnity Provision", "Liability", "Employee Benefits", "Credit"),
    KHGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    KHGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    KHGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    KHGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    KHGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    KHGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    KHGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    KHGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    KHGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    KHGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    KHGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    KHGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    KHGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    KHGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    KHGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    KHGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    KHGAAPAccount("4020", "Revenue — Exports (VAT 0%)", "Revenue", "Operating Revenue", "Credit"),
    KHGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    KHGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    KHGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    KHGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    KHGAAPAccount("4220", "Foreign Exchange Gain (KHR/USD)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    KHGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    KHGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    KHGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    KHGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    KHGAAPAccount("6010", "Seniority Indemnity Expense", "Expense", "Staff Costs", "Debit"),
    KHGAAPAccount("6020", "NSSF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    KHGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    KHGAAPAccount("6040", "Work Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    KHGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    KHGAAPAccount("6110", "Utilities (EDC Electricity / Water)", "Expense", "Occupancy Costs", "Debit"),
    KHGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    KHGAAPAccount("6200", "Patent Tax and Business Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6230", "Telecommunications (Smart / Cellcard / Metfone)", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6280", "Irrecoverable VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    KHGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    KHGAAPAccount("6310", "Foreign Exchange Loss (KHR/USD)", "Expense", "Finance Costs", "Debit"),
    KHGAAPAccount("6400", "Tax on Income (ToI) Expense", "Expense", "Tax Expense", "Debit"),
    KHGAAPAccount("6410", "Minimum Tax Expense", "Expense", "Tax Expense", "Debit"),
]
