"""Republic of Honduras chart of accounts (IFRS/NIIF as applied in Honduras).

Honduran companies generally report under NIIF (IFRS) / NIIF para PYMES.
This chart layers Honduras-specific tax and labour accounts on top of an
IFRS structure:

ISR = Impuesto Sobre la Renta (25% CIT, Ley del ISR).
Aportación Solidaria = 5% solidarity contribution on net taxable income
above HNL 1,000,000.
ISV = Impuesto Sobre Ventas (sales tax, 15%; 18% alcohol/tobacco).
IHSS = Instituto Hondureño de Seguridad Social (social security).
RAP = Régimen de Aportaciones Privadas (private contributions regime).
Décimo Tercero / Décimo Cuarto = statutory 13th and 14th month salaries.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class HNGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


HN_GAAP: list[HNGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    HNGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1020", "Banco Atlántida Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1021", "BAC Honduras Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1022", "Banco Ficohsa Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1023", "Banco de Occidente Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    HNGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    HNGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    HNGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    HNGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    HNGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    HNGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    HNGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    HNGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    HNGAAPAccount("1170", "ISV Credit (Crédito Fiscal)", "Asset", "Tax Receivable", "Debit"),
    HNGAAPAccount("1180", "ISR Advance Payments (Pagos a Cuenta)", "Asset", "Tax Receivable", "Debit"),
    HNGAAPAccount("1190", "ISR Withheld by Customers (Retenciones)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    HNGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    HNGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    HNGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    HNGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    HNGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    HNGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    HNGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    HNGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    HNGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    HNGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    HNGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    HNGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    HNGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    HNGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    HNGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    HNGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    HNGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    HNGAAPAccount("2100", "ISV Payable (Débito Fiscal)", "Liability", "Tax Payable", "Credit"),
    HNGAAPAccount("2110", "ISR (Corporate Income Tax) Payable", "Liability", "Tax Payable", "Credit"),
    HNGAAPAccount("2115", "Aportación Solidaria Payable", "Liability", "Tax Payable", "Credit"),
    HNGAAPAccount("2130", "Withholding Tax Payable (Retenciones ISR)", "Liability", "Tax Payable", "Credit"),
    HNGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2210", "IHSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2215", "RAP Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2220", "Décimo Tercer Mes (13th Month) Provision", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2225", "Décimo Cuarto Mes (14th Month) Provision", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2230", "Severance (Prestaciones Laborales) Provision", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2240", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    HNGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    HNGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    HNGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    HNGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    HNGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    HNGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    HNGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    HNGAAPAccount("3100", "Legal Reserve (Reserva Legal 5%)", "Equity", "Reserves", "Credit"),
    HNGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    HNGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    HNGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    HNGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    HNGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    HNGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    HNGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    HNGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    HNGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    HNGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    HNGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    HNGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    HNGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    HNGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    HNGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    HNGAAPAccount("6010", "IHSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    HNGAAPAccount("6015", "RAP Employer Contribution", "Expense", "Staff Costs", "Debit"),
    HNGAAPAccount("6020", "Décimo Tercer Mes Expense", "Expense", "Staff Costs", "Debit"),
    HNGAAPAccount("6025", "Décimo Cuarto Mes Expense", "Expense", "Staff Costs", "Debit"),
    HNGAAPAccount("6030", "Severance (Prestaciones Laborales) Expense", "Expense", "Staff Costs", "Debit"),
    HNGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    HNGAAPAccount("6110", "Utilities (ENEE / SANAA)", "Expense", "Occupancy Costs", "Debit"),
    HNGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6210", "Municipal and Government Fees", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6220", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    HNGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    HNGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    HNGAAPAccount("6400", "ISR (Corporate Income Tax) Expense", "Expense", "Tax Expense", "Debit"),
    HNGAAPAccount("6410", "Aportación Solidaria Expense", "Expense", "Tax Expense", "Debit"),
]
