"""Republic of Paraguay chart of accounts (Paraguayan GAAP / IFRS-aligned).

Paraguayan companies report under local standards converging toward IFRS.
This chart layers Paraguay-specific tax and payroll accounts on top of an
IFRS-style structure:

IRE  = Impuesto a la Renta Empresarial (corporate income tax, 10% flat —
       the lowest corporate rate in South America; Ley 6380/2019).
IDU  = Impuesto a los Dividendos y a las Utilidades (dividend tax,
       8% resident / 15% non-resident).
IVA  = Impuesto al Valor Agregado (VAT, 10% standard / 5% reduced — also
       the lowest standard VAT rate in South America).
IPS  = Instituto de Previsión Social (social security).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PYGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


PY_GAAP: list[PYGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    PYGAAPAccount("1010", "Cash on Hand (Caja)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1015", "Petty Cash (Caja Chica)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1020", "Banco Nacional de Fomento Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1021", "Banco Itaú Paraguay Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1022", "Banco Continental Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1023", "Banco GNB Paraguay Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PYGAAPAccount("1040", "Certificados de Depósito de Ahorro (CDA)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    PYGAAPAccount("1100", "Trade Receivables (Deudores por Ventas)", "Asset", "Trade and Other Receivables", "Debit"),
    PYGAAPAccount("1110", "Allowance for Doubtful Accounts", "Asset", "Trade and Other Receivables", "Credit"),
    PYGAAPAccount("1120", "Notes Receivable (Documentos a Cobrar)", "Asset", "Trade and Other Receivables", "Debit"),
    PYGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PYGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    PYGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    PYGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    PYGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    PYGAAPAccount("1180", "IVA Crédito Fiscal (Input VAT Receivable)", "Asset", "Tax Receivable", "Debit"),
    PYGAAPAccount("1185", "IRE Advance Payments (Anticipos IRE)", "Asset", "Tax Receivable", "Debit"),
    PYGAAPAccount("1190", "Withholding Tax Receivable (Retenciones)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    PYGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    PYGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    PYGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    PYGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    PYGAAPAccount("1240", "Provision for Inventory Obsolescence", "Asset", "Inventories", "Credit"),
    # Non-current assets
    PYGAAPAccount("1500", "Land (Terrenos)", "Asset", "Property, Plant and Equipment", "Debit"),
    PYGAAPAccount("1510", "Buildings (Edificios)", "Asset", "Property, Plant and Equipment", "Debit"),
    PYGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    PYGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    PYGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    PYGAAPAccount("1540", "Motor Vehicles (Rodados)", "Asset", "Property, Plant and Equipment", "Debit"),
    PYGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    PYGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    PYGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    PYGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    PYGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    PYGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    PYGAAPAccount("2000", "Trade Payables (Proveedores)", "Liability", "Trade and Other Payables", "Credit"),
    PYGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    PYGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    PYGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    PYGAAPAccount("2100", "IVA Débito Fiscal (Output VAT Payable)", "Liability", "Tax Payable", "Credit"),
    PYGAAPAccount("2110", "IVA Settlement Account (10% / 5%)", "Liability", "Tax Payable", "Credit"),
    PYGAAPAccount("2120", "IRE Payable (Impuesto a la Renta Empresarial)", "Liability", "Tax Payable", "Credit"),
    PYGAAPAccount("2130", "IDU Payable (Dividend Tax 8% / 15%)", "Liability", "Tax Payable", "Credit"),
    PYGAAPAccount("2140", "Withholding Tax Payable (Retenciones DNIT)", "Liability", "Tax Payable", "Credit"),
    PYGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    PYGAAPAccount("2210", "IPS Social Security Payable", "Liability", "Employee Benefits", "Credit"),
    PYGAAPAccount("2220", "Aguinaldo (13th-Month Salary) Provision", "Liability", "Employee Benefits", "Credit"),
    PYGAAPAccount("2230", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    PYGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    PYGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    PYGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    PYGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    PYGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    PYGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    PYGAAPAccount("3110", "Revaluation Reserve (Revalúo)", "Equity", "Reserves", "Credit"),
    PYGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    PYGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    PYGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    PYGAAPAccount("4000", "Revenue — Goods (Gravado IVA 10%)", "Revenue", "Operating Revenue", "Credit"),
    PYGAAPAccount("4005", "Revenue — Goods (Gravado IVA 5%)", "Revenue", "Operating Revenue", "Credit"),
    PYGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    PYGAAPAccount("4020", "Revenue — Exports (Exonerado IVA)", "Revenue", "Operating Revenue", "Credit"),
    PYGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    PYGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    PYGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    PYGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    PYGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    PYGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    PYGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    PYGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    PYGAAPAccount("6010", "Aguinaldo (13th-Month Salary) Expense", "Expense", "Staff Costs", "Debit"),
    PYGAAPAccount("6020", "IPS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PYGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    PYGAAPAccount("6110", "Utilities (ANDE / ESSAP)", "Expense", "Occupancy Costs", "Debit"),
    PYGAAPAccount("6200", "Municipal Licences and Patente Fees", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6230", "Telecommunications (Tigo / Personal)", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6280", "Non-Creditable IVA Expense", "Expense", "Administrative Expenses", "Debit"),
    PYGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    PYGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    PYGAAPAccount("6400", "IRE Expense (Corporate Income Tax 10%)", "Expense", "Tax Expense", "Debit"),
]
