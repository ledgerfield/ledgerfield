"""Jamaica chart of accounts (IFRS as applied in Jamaica).

Jamaican companies report under full IFRS (adopted 2002); qualifying SMEs may
use IFRS for SMEs. This chart layers Jamaica-specific tax and payroll
accounts on top of an IFRS structure:

CIT = Corporate Income Tax (25% unregulated / 33 1/3% regulated).
GCT = General Consumption Tax (15% standard).
NIS = National Insurance Scheme; NHT = National Housing Trust;
HEART = HEART/NSTA Trust levy; Ed. Tax = Education Tax.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class JMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


JM_GAAP: list[JMGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    JMGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1020", "National Commercial Bank (NCB) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1021", "Scotiabank Jamaica Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1022", "Sagicor Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1023", "JMMB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    JMGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    JMGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    JMGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    JMGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    JMGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    JMGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    JMGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    JMGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    JMGAAPAccount("1170", "GCT Input Tax Credit", "Asset", "Tax Receivable", "Debit"),
    JMGAAPAccount("1180", "Income Tax Refund Receivable", "Asset", "Tax Receivable", "Debit"),
    JMGAAPAccount("1190", "Withholding Tax Credit", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    JMGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    JMGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    JMGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    JMGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    JMGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    JMGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    JMGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    JMGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    JMGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    JMGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    JMGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    JMGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    JMGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    JMGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    JMGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    JMGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    JMGAAPAccount("2100", "GCT Output Tax Payable", "Liability", "Tax Payable", "Credit"),
    JMGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    JMGAAPAccount("2130", "PAYE Payable", "Liability", "Tax Payable", "Credit"),
    JMGAAPAccount("2140", "Education Tax Payable", "Liability", "Tax Payable", "Credit"),
    JMGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    JMGAAPAccount("2210", "NIS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    JMGAAPAccount("2220", "NHT Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    JMGAAPAccount("2230", "HEART/NSTA Trust Levy Payable", "Liability", "Employee Benefits", "Credit"),
    JMGAAPAccount("2240", "Vacation Leave Provision", "Liability", "Employee Benefits", "Credit"),
    JMGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    JMGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    JMGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    JMGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    JMGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    JMGAAPAccount("3100", "Capital Reserve", "Equity", "Reserves", "Credit"),
    JMGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    JMGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    JMGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    JMGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    JMGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    JMGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    JMGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    JMGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    JMGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    JMGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    JMGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    JMGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    JMGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    JMGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    JMGAAPAccount("6010", "NIS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    JMGAAPAccount("6020", "NHT Employer Contribution", "Expense", "Staff Costs", "Debit"),
    JMGAAPAccount("6030", "HEART/NSTA Trust Levy Expense", "Expense", "Staff Costs", "Debit"),
    JMGAAPAccount("6040", "Education Tax (Employer Portion)", "Expense", "Staff Costs", "Debit"),
    JMGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    JMGAAPAccount("6110", "Utilities (JPS / NWC)", "Expense", "Occupancy Costs", "Debit"),
    JMGAAPAccount("6200", "Companies Office Annual Return Fees", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6210", "Government Fees and Stamp Duty", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6230", "Telecommunications (Flow / Digicel)", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    JMGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    JMGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    JMGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
