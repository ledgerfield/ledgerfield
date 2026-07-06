"""Croatia chart of accounts (Croatian Financial Reporting Standards / IFRS).

Croatian companies report under the Croatian Financial Reporting Standards
(HSFI) or IFRS (listed/large entities). This chart layers Croatia-specific
tax and payroll accounts on top of an IFRS-style structure:

CIT = Corporate Income Tax (porez na dobit): 18% standard, 10% for annual
      revenue <= EUR 1,000,000.
PDV = Value Added Tax (porez na dodanu vrijednost): 25% standard, 13% and
      5% reduced rates.
Payroll: pension pillars I/II (HZMO) and health insurance (HZZO); PIT under
the municipal-rate system.

Croatia is a euro-area EU member state (EUR since 1 January 2023).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class HRGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


HR_GAAP: list[HRGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    HRGAAPAccount("1010", "Cash on Hand (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1020", "Zagrebacka banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1021", "Privredna banka Zagreb (PBZ) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1022", "Erste&Steiermarkische Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1023", "OTP banka Hrvatska Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    HRGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    HRGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    HRGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    HRGAAPAccount("1120", "Receivables from Related Parties", "Asset", "Trade and Other Receivables", "Debit"),
    HRGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    HRGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    HRGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    HRGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    HRGAAPAccount("1180", "VAT (PDV) Receivable / Input VAT", "Asset", "Tax Receivable", "Debit"),
    HRGAAPAccount("1190", "CIT Prepayments (Advance Instalments)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    HRGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    HRGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    HRGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    HRGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    HRGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    HRGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    HRGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    HRGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    HRGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    HRGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    HRGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    HRGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    HRGAAPAccount("1710", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    HRGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    HRGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    HRGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    HRGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    HRGAAPAccount("2100", "VAT (PDV) Payable — 25% Standard", "Liability", "Tax Payable", "Credit"),
    HRGAAPAccount("2110", "VAT (PDV) Payable — 13% Reduced", "Liability", "Tax Payable", "Credit"),
    HRGAAPAccount("2115", "VAT (PDV) Payable — 5% Reduced", "Liability", "Tax Payable", "Credit"),
    HRGAAPAccount("2120", "Corporate Income Tax Payable (Porezna uprava)", "Liability", "Tax Payable", "Credit"),
    HRGAAPAccount("2140", "Personal Income Tax Withheld (Municipal Rates)", "Liability", "Tax Payable", "Credit"),
    HRGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    HRGAAPAccount("2210", "Pension Contributions Payable (HZMO, Pillars I/II)", "Liability", "Employee Benefits", "Credit"),
    HRGAAPAccount("2220", "Health Insurance Contributions Payable (HZZO)", "Liability", "Employee Benefits", "Credit"),
    HRGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    HRGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    HRGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    HRGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    HRGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    HRGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    HRGAAPAccount("3000", "Share Capital (Temeljni kapital)", "Equity", "Contributed Capital", "Credit"),
    HRGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    HRGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    HRGAAPAccount("3110", "Other Reserves", "Equity", "Reserves", "Credit"),
    HRGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    HRGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    HRGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    HRGAAPAccount("4000", "Revenue — Goods (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    HRGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    HRGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    HRGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    HRGAAPAccount("4040", "Revenue — Tourism and Accommodation", "Revenue", "Operating Revenue", "Credit"),
    HRGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    HRGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    HRGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    HRGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    HRGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    HRGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    HRGAAPAccount("6010", "Health Insurance Employer Contribution (HZZO)", "Expense", "Staff Costs", "Debit"),
    HRGAAPAccount("6020", "Other Employee Benefits", "Expense", "Staff Costs", "Debit"),
    HRGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    HRGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    HRGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    HRGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    HRGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    HRGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    HRGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    HRGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    HRGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    HRGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
