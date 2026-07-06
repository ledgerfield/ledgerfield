"""Malaysia chart of accounts (MFRS / Malaysian Financial Reporting Standards).

Malaysian companies report under MFRS (word-for-word IFRS as issued by the
MASB). This chart layers Malaysia-specific tax and payroll accounts on top of
an IFRS structure:

CIT = Corporate Income Tax (24% standard; 15%/17%/24% SME tiers, Income Tax
      Act 1967, administered by LHDN).
SST = Sales and Service Tax (two-tier: Sales Tax 5%/10% on manufactured and
      imported goods; Service Tax 8%, 6% retained for F&B, telecom, parking
      and logistics).
EPF = Employees Provident Fund; SOCSO = Social Security Organisation;
EIS = Employment Insurance System; HRD = Human Resources Development levy.

Malaysia has no VAT/GST (GST repealed 2018), so no VAT/GST accounts are
included — SST accounts are used instead.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MYGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MY_GAAP: list[MYGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MYGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1020", "Maybank Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1021", "CIMB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1022", "Public Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1023", "RHB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1024", "Bank Islam Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MYGAAPAccount("1040", "Fixed Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MYGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MYGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MYGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    MYGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MYGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MYGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MYGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MYGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MYGAAPAccount("1180", "CIT Instalments Paid (CP204)", "Asset", "Tax Receivable", "Debit"),
    MYGAAPAccount("1190", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MYGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MYGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MYGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MYGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MYGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MYGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MYGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MYGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MYGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1570", "Right-of-Use Asset (MFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MYGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MYGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MYGAAPAccount("1620", "Business Licences (SSM Registration)", "Asset", "Intangible Assets", "Debit"),
    MYGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MYGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MYGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MYGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MYGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MYGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MYGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    MYGAAPAccount("2100", "SST — Sales Tax Payable (5%/10%)", "Liability", "Tax Payable", "Credit"),
    MYGAAPAccount("2110", "SST — Service Tax Payable (8%)", "Liability", "Tax Payable", "Credit"),
    MYGAAPAccount("2115", "SST — Service Tax Payable (6% F&B/Telecom/Parking/Logistics)", "Liability", "Tax Payable", "Credit"),
    MYGAAPAccount("2120", "Corporate Income Tax Payable (LHDN)", "Liability", "Tax Payable", "Credit"),
    MYGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    MYGAAPAccount("2140", "PCB / MTD Payroll Tax Payable", "Liability", "Tax Payable", "Credit"),
    MYGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MYGAAPAccount("2210", "EPF Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    MYGAAPAccount("2220", "SOCSO Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    MYGAAPAccount("2225", "EIS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    MYGAAPAccount("2230", "HRD Levy Payable", "Liability", "Employee Benefits", "Credit"),
    MYGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MYGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MYGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MYGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MYGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MYGAAPAccount("2410", "Lease Liability (MFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MYGAAPAccount("2420", "Shareholder / Director Loan", "Liability", "Non-Current Liabilities", "Credit"),
    MYGAAPAccount("2430", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MYGAAPAccount("3000", "Share Capital (Ordinary Shares)", "Equity", "Contributed Capital", "Credit"),
    MYGAAPAccount("3010", "Share Premium / Capital Contribution", "Equity", "Contributed Capital", "Credit"),
    MYGAAPAccount("3100", "Capital Reserve", "Equity", "Reserves", "Credit"),
    MYGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    MYGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MYGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MYGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MYGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MYGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MYGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    MYGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MYGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MYGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MYGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MYGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MYGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MYGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MYGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MYGAAPAccount("5030", "Import Duties and Sales Tax on Inputs", "Expense", "Cost of Sales", "Debit"),
    MYGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MYGAAPAccount("6010", "EPF Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MYGAAPAccount("6020", "SOCSO Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MYGAAPAccount("6025", "EIS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MYGAAPAccount("6030", "HRD Levy Expense", "Expense", "Staff Costs", "Debit"),
    MYGAAPAccount("6040", "Employee Medical and Insurance", "Expense", "Staff Costs", "Debit"),
    MYGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MYGAAPAccount("6110", "Utilities (TNB / Water)", "Expense", "Occupancy Costs", "Debit"),
    MYGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MYGAAPAccount("6200", "SSM Annual Filing and Secretarial Fees", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6210", "Government and Local Council Fees", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6230", "Telecommunications (Service Tax 6%)", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6280", "Service Tax Expense (Non-Recoverable SST)", "Expense", "Administrative Expenses", "Debit"),
    MYGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MYGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MYGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    MYGAAPAccount("6410", "Deferred Tax Expense", "Expense", "Tax Expense", "Debit"),
]
