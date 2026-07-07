"""Republic of Guatemala chart of accounts (IFRS/NIIF as applied in Guatemala).

Guatemalan companies generally report under NIIF (IFRS) / NIIF para PYMES.
This chart layers Guatemala-specific tax and labour accounts on top of an
IFRS structure:

ISR = Impuesto Sobre la Renta (25% profits regime, Decreto 10-2012).
ISO = Impuesto de Solidaridad (~1% minimum tax, creditable against ISR).
IVA = Impuesto al Valor Agregado (12%).
IGSS = Instituto Guatemalteco de Seguridad Social (social security).
Aguinaldo / Bono 14 = statutory 13th and 14th month salary bonuses.
Indemnización = statutory severance provision (Código de Trabajo).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GTGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


GT_GAAP: list[GTGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    GTGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1020", "Banco Industrial Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1021", "Banrural Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1022", "Banco G&T Continental Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1023", "BAM (Banco Agromercantil) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    GTGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    GTGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GTGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    GTGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    GTGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    GTGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    GTGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    GTGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    GTGAAPAccount("1170", "IVA Credit (Crédito Fiscal)", "Asset", "Tax Receivable", "Debit"),
    GTGAAPAccount("1180", "ISO Solidarity Tax Credit (Creditable Against ISR)", "Asset", "Tax Receivable", "Debit"),
    GTGAAPAccount("1190", "ISR Withheld by Customers (Retenciones)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    GTGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    GTGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    GTGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    GTGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    GTGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    GTGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    GTGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    GTGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    GTGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    GTGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    GTGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    GTGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    GTGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    GTGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    GTGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    GTGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    GTGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    GTGAAPAccount("2100", "IVA Payable (Débito Fiscal)", "Liability", "Tax Payable", "Credit"),
    GTGAAPAccount("2110", "ISR (Corporate Income Tax) Payable", "Liability", "Tax Payable", "Credit"),
    GTGAAPAccount("2115", "ISO Solidarity Tax Payable", "Liability", "Tax Payable", "Credit"),
    GTGAAPAccount("2130", "Withholding Tax Payable (Retenciones ISR)", "Liability", "Tax Payable", "Credit"),
    GTGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    GTGAAPAccount("2210", "IGSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    GTGAAPAccount("2220", "Aguinaldo (13th Month) Provision", "Liability", "Employee Benefits", "Credit"),
    GTGAAPAccount("2225", "Bono 14 (14th Month) Provision", "Liability", "Employee Benefits", "Credit"),
    GTGAAPAccount("2230", "Indemnización (Severance) Provision", "Liability", "Employee Benefits", "Credit"),
    GTGAAPAccount("2240", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    GTGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    GTGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    GTGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    GTGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    GTGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    GTGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    GTGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    GTGAAPAccount("3100", "Legal Reserve (Reserva Legal 5%)", "Equity", "Reserves", "Credit"),
    GTGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    GTGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    GTGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    GTGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    GTGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    GTGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    GTGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    GTGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    GTGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    GTGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    GTGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    GTGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    GTGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    GTGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    GTGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    GTGAAPAccount("6010", "IGSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    GTGAAPAccount("6020", "Aguinaldo Expense", "Expense", "Staff Costs", "Debit"),
    GTGAAPAccount("6025", "Bono 14 Expense", "Expense", "Staff Costs", "Debit"),
    GTGAAPAccount("6030", "Indemnización (Severance) Expense", "Expense", "Staff Costs", "Debit"),
    GTGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    GTGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    GTGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6210", "Municipal and Government Fees", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6220", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    GTGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    GTGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    GTGAAPAccount("6400", "ISR (Corporate Income Tax) Expense", "Expense", "Tax Expense", "Debit"),
    GTGAAPAccount("6410", "ISO Solidarity Tax Expense", "Expense", "Tax Expense", "Debit"),
]
