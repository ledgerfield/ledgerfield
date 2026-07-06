"""Republic of Slovenia chart of accounts (Slovenian Accounting Standards / IFRS).

Slovenian companies report under the Slovenian Accounting Standards (SRS 2016)
or IFRS. This chart layers Slovenia-specific tax and payroll accounts on top
of an IFRS-style structure:

DDV  = Davek na dodano vrednost (VAT, 22% standard; 9.5%/5% reduced).
DDPO = Davek od dohodkov pravnih oseb (CIT, 22% flat for 2024-2028).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SIGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


SI_GAAP: list[SIGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    SIGAAPAccount("1010", "Cash on Hand (Blagajna)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1020", "NLB Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1021", "Nova KBM Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1022", "SKB Banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1023", "UniCredit Banka Slovenija Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SIGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    SIGAAPAccount("1100", "Trade Receivables (Poslovne terjatve)", "Asset", "Trade and Other Receivables", "Debit"),
    SIGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    SIGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    SIGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    SIGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    SIGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    SIGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    SIGAAPAccount("1170", "Input VAT Receivable (Vstopni DDV)", "Asset", "Tax Receivable", "Debit"),
    SIGAAPAccount("1180", "Corporate Income Tax Prepayments (Akontacije DDPO)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    SIGAAPAccount("1200", "Inventory — Raw Materials (Material)", "Asset", "Inventories", "Debit"),
    SIGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    SIGAAPAccount("1220", "Inventory — Finished Goods (Proizvodi)", "Asset", "Inventories", "Debit"),
    SIGAAPAccount("1230", "Goods for Resale (Trgovsko blago)", "Asset", "Inventories", "Debit"),
    SIGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    SIGAAPAccount("1500", "Land (Zemljišča)", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1510", "Buildings (Zgradbe)", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    SIGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    SIGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    SIGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    SIGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    SIGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    SIGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    SIGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),
    SIGAAPAccount("1720", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    SIGAAPAccount("2000", "Trade Payables (Poslovne obveznosti)", "Liability", "Trade and Other Payables", "Credit"),
    SIGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    SIGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    SIGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    SIGAAPAccount("2100", "Output VAT Payable (Izstopni DDV, 22%)", "Liability", "Tax Payable", "Credit"),
    SIGAAPAccount("2110", "VAT Settlement Account (Obračun DDV)", "Liability", "Tax Payable", "Credit"),
    SIGAAPAccount("2120", "Corporate Income Tax Payable (DDPO)", "Liability", "Tax Payable", "Credit"),
    SIGAAPAccount("2130", "Withholding Tax Payable (Davčni odtegljaj)", "Liability", "Tax Payable", "Credit"),
    SIGAAPAccount("2200", "Salaries and Wages Payable (Plače)", "Liability", "Employee Benefits", "Credit"),
    SIGAAPAccount("2210", "Payroll Tax Withheld (Akontacija dohodnine)", "Liability", "Employee Benefits", "Credit"),
    SIGAAPAccount("2220", "Social Security Contributions Payable (Prispevki)", "Liability", "Employee Benefits", "Credit"),
    SIGAAPAccount("2230", "Leave Pay and Holiday Allowance Provision (Regres)", "Liability", "Employee Benefits", "Credit"),
    SIGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    SIGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    SIGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    SIGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    SIGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    SIGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    SIGAAPAccount("3000", "Share Capital (Osnovni kapital)", "Equity", "Contributed Capital", "Credit"),
    SIGAAPAccount("3010", "Capital Surplus (Kapitalske rezerve)", "Equity", "Contributed Capital", "Credit"),
    SIGAAPAccount("3100", "Legal Reserves (Zakonske rezerve)", "Equity", "Reserves", "Credit"),
    SIGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    SIGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    SIGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    SIGAAPAccount("4000", "Revenue — Goods (Prihodki od prodaje blaga)", "Revenue", "Operating Revenue", "Credit"),
    SIGAAPAccount("4010", "Revenue — Services (Prihodki od storitev)", "Revenue", "Operating Revenue", "Credit"),
    SIGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    SIGAAPAccount("4030", "Revenue — Exports (non-EU)", "Revenue", "Operating Revenue", "Credit"),
    SIGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    SIGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    SIGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    SIGAAPAccount("4210", "Government Grants and Subsidies", "Revenue", "Other Income", "Credit"),
    SIGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    SIGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    SIGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    SIGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    SIGAAPAccount("6000", "Salaries and Wages (Stroški plač)", "Expense", "Staff Costs", "Debit"),
    SIGAAPAccount("6010", "Social Security Employer Contributions (Prispevki delodajalca)", "Expense", "Staff Costs", "Debit"),
    SIGAAPAccount("6020", "Holiday Allowance Expense (Regres)", "Expense", "Staff Costs", "Debit"),
    SIGAAPAccount("6030", "Meal and Commute Allowances (Prehrana, prevoz)", "Expense", "Staff Costs", "Debit"),
    SIGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    SIGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    SIGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    SIGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6210", "Government and Registration Fees", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6220", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    SIGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    SIGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    SIGAAPAccount("6400", "Corporate Income Tax Expense (DDPO)", "Expense", "Tax Expense", "Debit"),
    SIGAAPAccount("6410", "Deferred Tax Expense", "Expense", "Tax Expense", "Debit"),
]
