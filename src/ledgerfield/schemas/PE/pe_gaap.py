"""Peru chart of accounts (IFRS / PCGE-inspired, LedgerField codes).

Peruvian companies report under IFRS as adopted in Peru and book to the PCGE
(Plan Contable General Empresarial). This chart layers Peru-specific tax and
labour accounts on top of a LedgerField IFRS structure:

IR   = Impuesto a la Renta (CIT 29.5% general / MYPE Tributario brackets).
IGV  = Impuesto General a las Ventas, 18% (16% IGV + 2% IPM).
ITAN = Temporary Net Assets Tax (0.4%, creditable).
CTS / gratificaciones / EsSalud / ONP-AFP = statutory Peruvian payroll items.
Detracciones (SPOT) = mandatory deposit system on certain services.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


PE_GAAP: list[PEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    PEGAAPAccount("1010", "Cash on Hand (Caja)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1015", "Petty Cash (Caja Chica)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1020", "Banco de Crédito del Perú (BCP) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1021", "BBVA Perú Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1022", "Interbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1023", "Scotiabank Perú Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1025", "Banco de la Nación Detracciones (SPOT) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PEGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    PEGAAPAccount("1100", "Trade Receivables (Facturas por Cobrar)", "Asset", "Trade and Other Receivables", "Debit"),
    PEGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    PEGAAPAccount("1120", "Notes Receivable (Letras por Cobrar)", "Asset", "Trade and Other Receivables", "Debit"),
    PEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    PEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    PEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    PEGAAPAccount("1170", "IGV Credit (Crédito Fiscal IGV)", "Asset", "Tax Receivable", "Debit"),
    PEGAAPAccount("1180", "Income Tax Prepayments (Pagos a Cuenta IR)", "Asset", "Tax Receivable", "Debit"),
    PEGAAPAccount("1185", "ITAN Credit Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    PEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    PEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    PEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    PEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    PEGAAPAccount("1240", "Provision for Inventory Obsolescence", "Asset", "Inventories", "Credit"),
    # Non-current assets
    PEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    PEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    PEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    PEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    PEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    PEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    PEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    PEGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    PEGAAPAccount("2000", "Trade Payables (Facturas por Pagar)", "Liability", "Trade and Other Payables", "Credit"),
    PEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    PEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    PEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    PEGAAPAccount("2100", "IGV Payable (Débito Fiscal IGV)", "Liability", "Tax Payable", "Credit"),
    PEGAAPAccount("2110", "IPM Payable (Municipal Promotion Tax)", "Liability", "Tax Payable", "Credit"),
    PEGAAPAccount("2120", "Income Tax Payable (Impuesto a la Renta)", "Liability", "Tax Payable", "Credit"),
    PEGAAPAccount("2130", "Dividend Withholding Tax Payable (5%)", "Liability", "Tax Payable", "Credit"),
    PEGAAPAccount("2135", "Fourth-Category WHT Payable (Recibos por Honorarios)", "Liability", "Tax Payable", "Credit"),
    PEGAAPAccount("2140", "ITAN Payable", "Liability", "Tax Payable", "Credit"),
    PEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    PEGAAPAccount("2210", "EsSalud Contributions Payable (9%)", "Liability", "Employee Benefits", "Credit"),
    PEGAAPAccount("2220", "Pension Contributions Payable (ONP / AFP)", "Liability", "Employee Benefits", "Credit"),
    PEGAAPAccount("2230", "CTS Provision (Compensación por Tiempo de Servicios)", "Liability", "Employee Benefits", "Credit"),
    PEGAAPAccount("2240", "Statutory Gratuities Provision (Gratificaciones)", "Liability", "Employee Benefits", "Credit"),
    PEGAAPAccount("2250", "Workers' Profit Sharing Payable (Participación de Utilidades)", "Liability", "Employee Benefits", "Credit"),
    PEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    PEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    PEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    PEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    PEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    PEGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    PEGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    PEGAAPAccount("3200", "Retained Earnings (Resultados Acumulados)", "Equity", "Retained Earnings", "Credit"),
    PEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    PEGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    PEGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    PEGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    PEGAAPAccount("4020", "Revenue — Exports (IGV zero-rated)", "Revenue", "Operating Revenue", "Credit"),
    PEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    PEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    PEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    PEGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    PEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    PEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    PEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    PEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    PEGAAPAccount("6010", "EsSalud Employer Contribution", "Expense", "Staff Costs", "Debit"),
    PEGAAPAccount("6020", "CTS Expense", "Expense", "Staff Costs", "Debit"),
    PEGAAPAccount("6030", "Statutory Gratuities Expense", "Expense", "Staff Costs", "Debit"),
    PEGAAPAccount("6040", "Workers' Profit Sharing Expense", "Expense", "Staff Costs", "Debit"),
    PEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    PEGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    PEGAAPAccount("6200", "Municipal Licences and Fees", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6210", "ITAN Expense (non-credited portion)", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6250", "Bank Charges and ITF (Financial Transactions Tax)", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    PEGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    PEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    PEGAAPAccount("6400", "Income Tax Expense (Impuesto a la Renta)", "Expense", "Tax Expense", "Debit"),
]
