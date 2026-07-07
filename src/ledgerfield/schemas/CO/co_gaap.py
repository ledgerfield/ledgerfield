"""Republic of Colombia chart of accounts (NIIF / IFRS as applied in Colombia).

Colombian companies report under NIIF (IFRS as adopted in Colombia, Ley 1314
de 2009); the statutory chart of accounts follows the PUC (Plan Único de
Cuentas). This chart layers Colombia-specific tax and labour accounts on top
of an IFRS structure:

CIT  = Corporate income tax / impuesto sobre la renta (35%; financial
       institutions 40% incl. surtax through 2027).
IVA  = Value Added Tax (19%): IVA Descontable (input) and IVA Generado
       (output), settled via DIAN returns.
ICA  = Municipal turnover tax (Impuesto de Industria y Comercio).
Retefuente / ReteIVA / ReteICA = Colombian withholding-at-source mechanisms.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class COGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CO_GAAP: list[COGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    COGAAPAccount("1010", "Cash on Hand (Caja)", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1015", "Petty Cash (Caja Menor)", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1020", "Bancolombia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1021", "Banco de Bogotá Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1022", "Davivienda Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1023", "BBVA Colombia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    COGAAPAccount("1040", "Fiduciary Investment (Fiducia / CDT)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    COGAAPAccount("1100", "Trade Receivables (Clientes)", "Asset", "Trade and Other Receivables", "Debit"),
    COGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    COGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    COGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    COGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    COGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    COGAAPAccount("1170", "IVA Descontable (Input VAT 19%)", "Asset", "Tax Receivable", "Debit"),
    COGAAPAccount("1175", "Withholding Tax Receivable (Retefuente Sufrida)", "Asset", "Tax Receivable", "Debit"),
    COGAAPAccount("1180", "ReteIVA Receivable (Retención de IVA Sufrida)", "Asset", "Tax Receivable", "Debit"),
    COGAAPAccount("1185", "ReteICA Receivable (Retención de ICA Sufrida)", "Asset", "Tax Receivable", "Debit"),
    COGAAPAccount("1190", "Income Tax Advance (Anticipo de Renta)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    COGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    COGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    COGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    COGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    COGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    COGAAPAccount("1500", "Land (Terrenos)", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    COGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    COGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    COGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    COGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    COGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    COGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    COGAAPAccount("1710", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    COGAAPAccount("2000", "Trade Payables (Proveedores)", "Liability", "Trade and Other Payables", "Credit"),
    COGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    COGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    COGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    COGAAPAccount("2100", "IVA Generado (Output VAT 19%)", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2110", "IVA Payable — DIAN Settlement", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2120", "Corporate Income Tax Payable (Impuesto de Renta)", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2130", "Withholding Tax Payable (Retefuente por Pagar)", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2135", "ReteIVA Payable (Retención de IVA Practicada)", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2140", "ICA Payable (Impuesto de Industria y Comercio)", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2145", "ReteICA Payable (Retención de ICA Practicada)", "Liability", "Tax Payable", "Credit"),
    COGAAPAccount("2200", "Salaries and Wages Payable (Nómina por Pagar)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2210", "Pension Contributions Payable (Colpensiones / AFP)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2220", "Health Contributions Payable (EPS)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2225", "Payroll Parafiscals Payable (SENA / ICBF / Caja de Compensación)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2230", "Severance Fund Payable (Cesantías)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2235", "Interest on Cesantías Payable", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2240", "Service Bonus Provision (Prima de Servicios)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2245", "Vacation Provision (Vacaciones)", "Liability", "Employee Benefits", "Credit"),
    COGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    COGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    COGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    COGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    COGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    COGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    COGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    COGAAPAccount("3200", "Retained Earnings (Utilidades Acumuladas)", "Equity", "Retained Earnings", "Credit"),
    COGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    COGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    COGAAPAccount("4000", "Revenue — Goods (Ventas)", "Revenue", "Operating Revenue", "Credit"),
    COGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    COGAAPAccount("4020", "Revenue — Exports (IVA Exempt / Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    COGAAPAccount("4100", "Sales Returns and Allowances (Devoluciones)", "Revenue", "Operating Revenue", "Debit"),
    COGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    COGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    COGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    COGAAPAccount("5000", "Cost of Goods Sold (Costo de Ventas)", "Expense", "Cost of Sales", "Debit"),
    COGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    COGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    COGAAPAccount("6000", "Salaries and Wages (Nómina)", "Expense", "Staff Costs", "Debit"),
    COGAAPAccount("6010", "Employer Social Security Contributions (Salud / Pensión / ARL)", "Expense", "Staff Costs", "Debit"),
    COGAAPAccount("6020", "Payroll Parafiscals (SENA / ICBF / Caja de Compensación)", "Expense", "Staff Costs", "Debit"),
    COGAAPAccount("6030", "Cesantías and Prima Expense", "Expense", "Staff Costs", "Debit"),
    COGAAPAccount("6100", "Office Rent (Arrendamiento)", "Expense", "Occupancy Costs", "Debit"),
    COGAAPAccount("6110", "Utilities (Servicios Públicos)", "Expense", "Occupancy Costs", "Debit"),
    COGAAPAccount("6200", "ICA Expense (Impuesto de Industria y Comercio)", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6210", "Financial Transactions Tax (GMF 4x1000)", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6220", "Professional and Audit Fees (Revisoría Fiscal)", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6230", "Chamber of Commerce Registration (Cámara de Comercio)", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6280", "Non-Recoverable IVA Expense", "Expense", "Administrative Expenses", "Debit"),
    COGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    COGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    COGAAPAccount("6400", "Corporate Income Tax Expense (Impuesto de Renta)", "Expense", "Tax Expense", "Debit"),
]
