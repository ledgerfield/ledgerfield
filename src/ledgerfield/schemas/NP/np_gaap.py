"""Nepal chart of accounts (NFRS / IFRS as applied in Nepal).

Nepalese companies report under Nepal Financial Reporting Standards (NFRS,
converged with IFRS). This chart layers Nepal-specific tax and payroll accounts
on top of an NFRS structure:

CIT = Corporate Income Tax (25% / 30% / 20% by sector).
VAT = Value Added Tax (13%).
SST = Social Security Fund / provident fund contributions.

Amounts are denominated in Nepalese rupees (NPR).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class NPGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


NP_GAAP: list[NPGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    NPGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1020", "Nabil Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1021", "Nepal Investment Mega Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1022", "Rastriya Banijya Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1023", "Global IME Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1024", "Nepal Bank Limited Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    NPGAAPAccount("1040", "Fixed Deposit Receipt", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    NPGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    NPGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    NPGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    NPGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    NPGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    NPGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    NPGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    NPGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    NPGAAPAccount("1180", "VAT Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    NPGAAPAccount("1185", "TDS Receivable (Withholding)", "Asset", "Tax Receivable", "Debit"),
    NPGAAPAccount("1190", "Advance Income Tax", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    NPGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    NPGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    NPGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    NPGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    NPGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    NPGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    NPGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    NPGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    NPGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1570", "Right-of-Use Asset (NFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    NPGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    NPGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    NPGAAPAccount("1620", "Company Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    NPGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    NPGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    NPGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    NPGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    NPGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    NPGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    NPGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    NPGAAPAccount("2100", "VAT Payable (Output VAT)", "Liability", "Tax Payable", "Credit"),
    NPGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    NPGAAPAccount("2130", "TDS Payable (Withholding)", "Liability", "Tax Payable", "Credit"),
    NPGAAPAccount("2140", "Personal Income Tax Payable (Payroll)", "Liability", "Tax Payable", "Credit"),
    NPGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    NPGAAPAccount("2210", "Provident Fund Payable", "Liability", "Employee Benefits", "Credit"),
    NPGAAPAccount("2220", "Social Security Fund (SSF) Payable", "Liability", "Employee Benefits", "Credit"),
    NPGAAPAccount("2230", "Gratuity Provision", "Liability", "Employee Benefits", "Credit"),
    NPGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    NPGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    NPGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    NPGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    NPGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    NPGAAPAccount("2410", "Lease Liability (NFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    NPGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    NPGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    NPGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    NPGAAPAccount("3100", "General Reserve", "Equity", "Reserves", "Credit"),
    NPGAAPAccount("3110", "Capital Reserve", "Equity", "Reserves", "Credit"),
    NPGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    NPGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    NPGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    NPGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    NPGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    NPGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    NPGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    NPGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    NPGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    NPGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    NPGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    NPGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    NPGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    NPGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    NPGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    NPGAAPAccount("6010", "Gratuity Expense", "Expense", "Staff Costs", "Debit"),
    NPGAAPAccount("6020", "Social Security / Provident Fund Contribution", "Expense", "Staff Costs", "Debit"),
    NPGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    NPGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    NPGAAPAccount("6110", "Utilities (Electricity and Water)", "Expense", "Occupancy Costs", "Debit"),
    NPGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    NPGAAPAccount("6200", "Company Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6230", "Telecommunications (NTC / Ncell)", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    NPGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    NPGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    NPGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
