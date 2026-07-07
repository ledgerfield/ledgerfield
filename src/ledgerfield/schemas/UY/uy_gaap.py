"""Oriental Republic of Uruguay chart of accounts (Uruguayan GAAP / IFRS-aligned).

Uruguayan companies report under Normas Contables Adecuadas, which adopt IFRS.
This chart layers Uruguay-specific tax and payroll accounts on top of an
IFRS-style structure:

IRAE = Impuesto a las Rentas de las Actividades Económicas (corporate income
       tax, 25% flat; Título 4).
IVA  = Impuesto al Valor Agregado (VAT, 22% standard / 10% reduced mínimo).
IP   = Impuesto al Patrimonio (net-wealth tax, 1.5% on corporate net worth).
BPS  = Banco de Previsión Social (social security).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UYGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


UY_GAAP: list[UYGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    UYGAAPAccount("1010", "Cash on Hand (Caja)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1015", "Petty Cash (Caja Chica)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1020", "Banco República (BROU) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1021", "Banco Itaú Uruguay Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1022", "Banco Santander Uruguay Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1023", "Scotiabank Uruguay Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    UYGAAPAccount("1040", "Term Deposits (Plazo Fijo)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    UYGAAPAccount("1100", "Trade Receivables (Deudores por Ventas)", "Asset", "Trade and Other Receivables", "Debit"),
    UYGAAPAccount("1110", "Allowance for Doubtful Accounts", "Asset", "Trade and Other Receivables", "Credit"),
    UYGAAPAccount("1120", "Notes Receivable (Documentos a Cobrar)", "Asset", "Trade and Other Receivables", "Debit"),
    UYGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    UYGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    UYGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    UYGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    UYGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    UYGAAPAccount("1180", "IVA Compras (Input VAT Receivable)", "Asset", "Tax Receivable", "Debit"),
    UYGAAPAccount("1185", "IRAE Advance Payments (Anticipos IRAE)", "Asset", "Tax Receivable", "Debit"),
    UYGAAPAccount("1190", "Withholding Tax Receivable (Retenciones DGI)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    UYGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    UYGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    UYGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    UYGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    UYGAAPAccount("1240", "Provision for Inventory Obsolescence", "Asset", "Inventories", "Credit"),
    # Non-current assets
    UYGAAPAccount("1500", "Land (Terrenos)", "Asset", "Property, Plant and Equipment", "Debit"),
    UYGAAPAccount("1510", "Buildings (Edificios)", "Asset", "Property, Plant and Equipment", "Debit"),
    UYGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    UYGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    UYGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    UYGAAPAccount("1540", "Motor Vehicles (Rodados)", "Asset", "Property, Plant and Equipment", "Debit"),
    UYGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    UYGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    UYGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    UYGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    UYGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    UYGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    UYGAAPAccount("2000", "Trade Payables (Proveedores)", "Liability", "Trade and Other Payables", "Credit"),
    UYGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    UYGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    UYGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    UYGAAPAccount("2100", "IVA Ventas (Output VAT Payable)", "Liability", "Tax Payable", "Credit"),
    UYGAAPAccount("2110", "IVA Settlement Account (22% / 10%)", "Liability", "Tax Payable", "Credit"),
    UYGAAPAccount("2120", "IRAE Payable (Corporate Income Tax)", "Liability", "Tax Payable", "Credit"),
    UYGAAPAccount("2130", "IP Payable (Impuesto al Patrimonio 1.5%)", "Liability", "Tax Payable", "Credit"),
    UYGAAPAccount("2140", "Withholding Tax Payable (Retenciones DGI)", "Liability", "Tax Payable", "Credit"),
    UYGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    UYGAAPAccount("2210", "BPS Social Security Payable", "Liability", "Employee Benefits", "Credit"),
    UYGAAPAccount("2220", "Aguinaldo (13th-Month Salary) Provision", "Liability", "Employee Benefits", "Credit"),
    UYGAAPAccount("2230", "Vacation Pay and Salario Vacacional Provision", "Liability", "Employee Benefits", "Credit"),
    UYGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    UYGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    UYGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    UYGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    UYGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    UYGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    UYGAAPAccount("3110", "Revaluation Reserve", "Equity", "Reserves", "Credit"),
    UYGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    UYGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    UYGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    UYGAAPAccount("4000", "Revenue — Goods (Gravado IVA 22%)", "Revenue", "Operating Revenue", "Credit"),
    UYGAAPAccount("4005", "Revenue — Goods (Tasa Mínima IVA 10%)", "Revenue", "Operating Revenue", "Credit"),
    UYGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    UYGAAPAccount("4020", "Revenue — Exports (Tasa Cero IVA)", "Revenue", "Operating Revenue", "Credit"),
    UYGAAPAccount("4030", "Revenue — Zona Franca Operations", "Revenue", "Operating Revenue", "Credit"),
    UYGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    UYGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    UYGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    UYGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    UYGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    UYGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    UYGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    UYGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    UYGAAPAccount("6010", "Aguinaldo (13th-Month Salary) Expense", "Expense", "Staff Costs", "Debit"),
    UYGAAPAccount("6020", "BPS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    UYGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    UYGAAPAccount("6110", "Utilities (UTE / OSE / Antel)", "Expense", "Occupancy Costs", "Debit"),
    UYGAAPAccount("6200", "Municipal Taxes and Licences", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6280", "Non-Creditable IVA Expense", "Expense", "Administrative Expenses", "Debit"),
    UYGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    UYGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    UYGAAPAccount("6400", "IRAE Expense (Corporate Income Tax 25%)", "Expense", "Tax Expense", "Debit"),
    UYGAAPAccount("6410", "IP Expense (Impuesto al Patrimonio)", "Expense", "Tax Expense", "Debit"),
]
