"""Republic of Chile chart of accounts (IFRS as applied in Chile).

Chilean companies report under IFRS (full IFRS or IFRS for SMEs). This chart
layers Chile-specific tax and labour accounts on top of an IFRS structure:

CIT  = First Category Tax / Impuesto de Primera Categoría (27% / 25% Pro Pyme).
IVA  = Value Added Tax (19%): IVA Crédito Fiscal (input) and IVA Débito
       Fiscal (output), settled monthly via Form 29 (SII).
PPM  = Pagos Provisionales Mensuales (monthly CIT prepayments).
AFP / Fonasa-Isapre = mandatory pension and health contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CLGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CL_GAAP: list[CLGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    CLGAAPAccount("1010", "Cash on Hand (Caja)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1015", "Petty Cash (Caja Chica)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1020", "Banco de Chile Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1021", "BancoEstado Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1022", "Banco Santander Chile Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1023", "Banco BCI Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CLGAAPAccount("1040", "Time Deposits (Depósitos a Plazo)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    CLGAAPAccount("1100", "Trade Receivables (Clientes)", "Asset", "Trade and Other Receivables", "Debit"),
    CLGAAPAccount("1105", "Documents Receivable (Facturas por Cobrar)", "Asset", "Trade and Other Receivables", "Debit"),
    CLGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    CLGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    CLGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    CLGAAPAccount("1150", "Employee Advances (Anticipos al Personal)", "Asset", "Trade and Other Receivables", "Debit"),
    CLGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    CLGAAPAccount("1170", "IVA Crédito Fiscal (Input VAT 19%)", "Asset", "Tax Receivable", "Debit"),
    CLGAAPAccount("1175", "IVA Remanente (VAT Credit Carryforward)", "Asset", "Tax Receivable", "Debit"),
    CLGAAPAccount("1180", "PPM — Monthly CIT Prepayments (Pagos Provisionales Mensuales)", "Asset", "Tax Receivable", "Debit"),
    CLGAAPAccount("1185", "Income Tax Receivable (SII Refund)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    CLGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    CLGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    CLGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    CLGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    CLGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    CLGAAPAccount("1500", "Land (Terrenos)", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    CLGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    CLGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    CLGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    CLGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    CLGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    CLGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    CLGAAPAccount("1710", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    CLGAAPAccount("2000", "Trade Payables (Proveedores)", "Liability", "Trade and Other Payables", "Credit"),
    CLGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    CLGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    CLGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    CLGAAPAccount("2100", "IVA Débito Fiscal (Output VAT 19%)", "Liability", "Tax Payable", "Credit"),
    CLGAAPAccount("2110", "IVA Payable — Form 29 Settlement (SII)", "Liability", "Tax Payable", "Credit"),
    CLGAAPAccount("2120", "First Category Tax Payable (Impuesto de Primera Categoría)", "Liability", "Tax Payable", "Credit"),
    CLGAAPAccount("2130", "Withholding Tax Payable (Impuesto Adicional / Retenciones)", "Liability", "Tax Payable", "Credit"),
    CLGAAPAccount("2140", "Employee Income Tax Withheld (Impuesto Único Segunda Categoría)", "Liability", "Tax Payable", "Credit"),
    CLGAAPAccount("2200", "Salaries and Wages Payable (Remuneraciones por Pagar)", "Liability", "Employee Benefits", "Credit"),
    CLGAAPAccount("2210", "AFP Pension Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    CLGAAPAccount("2220", "Health Contributions Payable (Fonasa / Isapre)", "Liability", "Employee Benefits", "Credit"),
    CLGAAPAccount("2230", "Unemployment Insurance Payable (Seguro de Cesantía)", "Liability", "Employee Benefits", "Credit"),
    CLGAAPAccount("2240", "Vacation Provision (Provisión de Vacaciones)", "Liability", "Employee Benefits", "Credit"),
    CLGAAPAccount("2250", "Severance Provision (Indemnización por Años de Servicio)", "Liability", "Employee Benefits", "Credit"),
    CLGAAPAccount("2300", "Bank Overdraft (Línea de Crédito)", "Liability", "Borrowings", "Credit"),
    CLGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    CLGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    CLGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    CLGAAPAccount("2420", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    CLGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    CLGAAPAccount("3100", "Legal / Other Reserves", "Equity", "Reserves", "Credit"),
    CLGAAPAccount("3110", "Price-Level Restatement Reserve (Revalorización)", "Equity", "Reserves", "Credit"),
    CLGAAPAccount("3200", "Retained Earnings (Utilidades Acumuladas)", "Equity", "Retained Earnings", "Credit"),
    CLGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    CLGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    CLGAAPAccount("4000", "Revenue — Goods (Ventas)", "Revenue", "Operating Revenue", "Credit"),
    CLGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    CLGAAPAccount("4020", "Revenue — Exports (IVA Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    CLGAAPAccount("4100", "Sales Returns and Allowances (Notas de Crédito)", "Revenue", "Operating Revenue", "Debit"),
    CLGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    CLGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    CLGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    CLGAAPAccount("4230", "UF / Inflation Indexation Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    CLGAAPAccount("5000", "Cost of Goods Sold (Costo de Ventas)", "Expense", "Cost of Sales", "Debit"),
    CLGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    CLGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    CLGAAPAccount("6000", "Salaries and Wages (Remuneraciones)", "Expense", "Staff Costs", "Debit"),
    CLGAAPAccount("6010", "Employer Unemployment Insurance (Seguro de Cesantía)", "Expense", "Staff Costs", "Debit"),
    CLGAAPAccount("6020", "Employer Accident Insurance (Mutual de Seguridad)", "Expense", "Staff Costs", "Debit"),
    CLGAAPAccount("6030", "Statutory Bonus (Gratificación Legal)", "Expense", "Staff Costs", "Debit"),
    CLGAAPAccount("6100", "Office Rent (Arriendo)", "Expense", "Occupancy Costs", "Debit"),
    CLGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    CLGAAPAccount("6200", "Municipal Business Licence (Patente Municipal)", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6210", "Stamp Tax (Impuesto de Timbres y Estampillas)", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6280", "Non-Recoverable IVA Expense", "Expense", "Administrative Expenses", "Debit"),
    CLGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    CLGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    CLGAAPAccount("6400", "First Category Tax Expense (Impuesto a la Renta)", "Expense", "Tax Expense", "Debit"),
]
