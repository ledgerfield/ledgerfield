"""Ecuador chart of accounts (IFRS / NIIF, LedgerField codes).

Ecuadorian companies report under IFRS (NIIF) as required by the
Superintendencia de Compañías. This chart layers Ecuador-specific tax and
labour accounts on top of a LedgerField IFRS structure:

IR   = Impuesto a la Renta (CIT 25% standard / 28% tax-haven surcharge).
IVA  = Impuesto al Valor Agregado, 15% (raised from 12% in April 2024,
       Ley de Solidaridad).
ISD  = Impuesto a la Salida de Divisas (5% currency-exit tax).
IESS = social security; décimo tercero/cuarto and 15% workers' profit
       sharing are statutory Ecuadorian payroll items. Ecuador is fully
       dollarized (USD).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ECGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


EC_GAAP: list[ECGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ECGAAPAccount("1010", "Cash on Hand (Caja)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1015", "Petty Cash (Caja Chica)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1020", "Banco Pichincha Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1021", "Banco Guayaquil Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1022", "Produbanco Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1023", "Banco del Pacífico Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1030", "Foreign Bank Account (Abroad)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ECGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ECGAAPAccount("1100", "Trade Receivables (Cuentas por Cobrar Clientes)", "Asset", "Trade and Other Receivables", "Debit"),
    ECGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    ECGAAPAccount("1120", "Notes Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    ECGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    ECGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ECGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ECGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    ECGAAPAccount("1170", "IVA Credit (Crédito Tributario IVA)", "Asset", "Tax Receivable", "Debit"),
    ECGAAPAccount("1175", "Income Tax Withholdings Receivable (Retenciones en la Fuente)", "Asset", "Tax Receivable", "Debit"),
    ECGAAPAccount("1180", "Income Tax Advance Payments (Anticipo IR)", "Asset", "Tax Receivable", "Debit"),
    ECGAAPAccount("1185", "ISD Tax Credit Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ECGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ECGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ECGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ECGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    ECGAAPAccount("1240", "Provision for Inventory Obsolescence", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ECGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ECGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ECGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ECGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    ECGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ECGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ECGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    ECGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ECGAAPAccount("2000", "Trade Payables (Cuentas por Pagar Proveedores)", "Liability", "Trade and Other Payables", "Credit"),
    ECGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ECGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    ECGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    ECGAAPAccount("2100", "IVA Payable (15%)", "Liability", "Tax Payable", "Credit"),
    ECGAAPAccount("2110", "IVA Withholdings Payable (Retenciones IVA)", "Liability", "Tax Payable", "Credit"),
    ECGAAPAccount("2120", "Income Tax Payable (Impuesto a la Renta)", "Liability", "Tax Payable", "Credit"),
    ECGAAPAccount("2130", "Income Tax Withholdings Payable (Retenciones en la Fuente)", "Liability", "Tax Payable", "Credit"),
    ECGAAPAccount("2140", "ISD Payable (Currency-Exit Tax 5%)", "Liability", "Tax Payable", "Credit"),
    ECGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    ECGAAPAccount("2210", "IESS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    ECGAAPAccount("2220", "13th Salary Provision (Décimo Tercero)", "Liability", "Employee Benefits", "Credit"),
    ECGAAPAccount("2230", "14th Salary Provision (Décimo Cuarto)", "Liability", "Employee Benefits", "Credit"),
    ECGAAPAccount("2240", "Reserve Funds Payable (Fondos de Reserva)", "Liability", "Employee Benefits", "Credit"),
    ECGAAPAccount("2250", "Workers' Profit Sharing Payable (15% Participación Trabajadores)", "Liability", "Employee Benefits", "Credit"),
    ECGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ECGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ECGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    ECGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    ECGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ECGAAPAccount("3000", "Share Capital (Capital Suscrito)", "Equity", "Contributed Capital", "Credit"),
    ECGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    ECGAAPAccount("3200", "Retained Earnings (Resultados Acumulados)", "Equity", "Retained Earnings", "Credit"),
    ECGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ECGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ECGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    ECGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    ECGAAPAccount("4020", "Revenue — Exports (IVA zero-rated)", "Revenue", "Operating Revenue", "Credit"),
    ECGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ECGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ECGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ECGAAPAccount("4210", "Interest Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ECGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ECGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ECGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ECGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ECGAAPAccount("6010", "IESS Employer Contribution (12.15%)", "Expense", "Staff Costs", "Debit"),
    ECGAAPAccount("6020", "13th and 14th Salary Expense", "Expense", "Staff Costs", "Debit"),
    ECGAAPAccount("6030", "Reserve Funds Expense", "Expense", "Staff Costs", "Debit"),
    ECGAAPAccount("6040", "Workers' Profit Sharing Expense (15%)", "Expense", "Staff Costs", "Debit"),
    ECGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    ECGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    ECGAAPAccount("6200", "Municipal Patente and 1.5 per Mille Tax", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6210", "Superintendencia de Compañías Contribution", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6255", "ISD Expense (Currency-Exit Tax)", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    ECGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    ECGAAPAccount("6400", "Income Tax Expense (Impuesto a la Renta)", "Expense", "Tax Expense", "Debit"),
]
