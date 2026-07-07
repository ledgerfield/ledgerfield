"""Republic of Ghana chart of accounts (IFRS as applied in Ghana).

Ghanaian companies report under IFRS. This chart layers Ghana-specific tax and
levy accounts on top of an IFRS structure:

CIT = Corporate Income Tax (25% standard; 35% mining/upstream petroleum;
      22% hotels — Income Tax Act, 2015, Act 896).
GSL = Growth & Sustainability Levy (5% of profit before tax, 2023-2025).
VAT = Value Added Tax 15% plus NHIL 2.5%, GETFund 2.5% and COVID-19 levy 1%
      (levies are non-deductible as input tax; effective rate ~21.9%).
SSNIT = Social Security and National Insurance Trust contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GHGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


GH_GAAP: list[GHGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    GHGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1020", "GCB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1021", "Ecobank Ghana Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1022", "Absa Bank Ghana Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1023", "Stanbic Bank Ghana Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1025", "Mobile Money Float (MTN MoMo)", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    GHGAAPAccount("1040", "Fixed Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    GHGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GHGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    GHGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    GHGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GHGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    GHGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    GHGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    GHGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    GHGAAPAccount("1180", "VAT Input (Deductible)", "Asset", "Tax Receivable", "Debit"),
    GHGAAPAccount("1185", "Withholding Tax Credit Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    GHGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    GHGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    GHGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    GHGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    GHGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    GHGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    GHGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    GHGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    GHGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    GHGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    GHGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    GHGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    GHGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    GHGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    GHGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    GHGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    GHGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    GHGAAPAccount("2100", "VAT Output Payable (15%)", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2105", "NHIL Payable (2.5%)", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2106", "GETFund Levy Payable (2.5%)", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2107", "COVID-19 Levy Payable (1%)", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2125", "Growth & Sustainability Levy Payable", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2140", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    GHGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    GHGAAPAccount("2210", "SSNIT Contributions Payable (Tier 1)", "Liability", "Employee Benefits", "Credit"),
    GHGAAPAccount("2215", "Occupational Pension Payable (Tier 2)", "Liability", "Employee Benefits", "Credit"),
    GHGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    GHGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    GHGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    GHGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    GHGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    GHGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    GHGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    GHGAAPAccount("3000", "Stated Capital", "Equity", "Contributed Capital", "Credit"),
    GHGAAPAccount("3100", "Capital Surplus", "Equity", "Reserves", "Credit"),
    GHGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    GHGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    GHGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    GHGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    GHGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    GHGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    GHGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    GHGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    GHGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    GHGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    GHGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    GHGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    GHGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    GHGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    GHGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    GHGAAPAccount("5030", "Non-Deductible Input Levies (NHIL/GETFund/COVID)", "Expense", "Cost of Sales", "Debit"),
    GHGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    GHGAAPAccount("6010", "SSNIT Employer Contribution (13%)", "Expense", "Staff Costs", "Debit"),
    GHGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    GHGAAPAccount("6040", "Staff Training and Welfare", "Expense", "Staff Costs", "Debit"),
    GHGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    GHGAAPAccount("6110", "Utilities (ECG / Ghana Water)", "Expense", "Occupancy Costs", "Debit"),
    GHGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    GHGAAPAccount("6200", "Business Operating Permit Fees", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6230", "Telecommunications (MTN / Telecel)", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    GHGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    GHGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    GHGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
    GHGAAPAccount("6410", "Growth & Sustainability Levy Expense", "Expense", "Tax Expense", "Debit"),
]
