"""Dominican Republic chart of accounts (IFRS / NIIF as applied in the DR).

Dominican companies report under IFRS (NIIF); SMEs commonly apply NIIF para
PYMES. This chart layers DR-specific tax and labour accounts on top of an
IFRS structure:

ISR = Impuesto Sobre la Renta (corporate income tax, 27%).
ITBIS = Impuesto sobre Transferencias de Bienes Industrializados y Servicios
        (VAT, 18% standard / 16% reduced).
TSS = Tesorería de la Seguridad Social (social security contributions).
INFOTEP = Instituto Nacional de Formación Técnico Profesional (1% payroll levy).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class DOGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


DO_GAAP: list[DOGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    DOGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1020", "Banco Popular Dominicano Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1021", "Banreservas Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1022", "Banco BHD Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1023", "Scotiabank República Dominicana Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    DOGAAPAccount("1040", "Term Deposits (Certificados Financieros)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    DOGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    DOGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    DOGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    DOGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    DOGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    DOGAAPAccount("1150", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    DOGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    DOGAAPAccount("1170", "ITBIS Input Credit (Adelantado)", "Asset", "Tax Receivable", "Debit"),
    DOGAAPAccount("1180", "ISR Advance Payments (Anticipos)", "Asset", "Tax Receivable", "Debit"),
    DOGAAPAccount("1190", "Withholding Tax Receivable (Retenciones)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    DOGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    DOGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    DOGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    DOGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    DOGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    DOGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    DOGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    DOGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    DOGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    DOGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    DOGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    DOGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    DOGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    DOGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    DOGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    DOGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    DOGAAPAccount("2100", "ITBIS Output Payable", "Liability", "Tax Payable", "Credit"),
    DOGAAPAccount("2110", "ITBIS Withheld Payable", "Liability", "Tax Payable", "Credit"),
    DOGAAPAccount("2120", "ISR (Corporate Income Tax) Payable", "Liability", "Tax Payable", "Credit"),
    DOGAAPAccount("2125", "Assets Tax (Impuesto sobre Activos) Payable", "Liability", "Tax Payable", "Credit"),
    DOGAAPAccount("2130", "Withholding Tax Payable (Retenciones ISR)", "Liability", "Tax Payable", "Credit"),
    DOGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    DOGAAPAccount("2210", "TSS Social Security Payable", "Liability", "Employee Benefits", "Credit"),
    DOGAAPAccount("2220", "INFOTEP Payable", "Liability", "Employee Benefits", "Credit"),
    DOGAAPAccount("2230", "Christmas Salary (Regalía Pascual) Provision", "Liability", "Employee Benefits", "Credit"),
    DOGAAPAccount("2240", "Severance (Prestaciones Laborales) Provision", "Liability", "Employee Benefits", "Credit"),
    DOGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    DOGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    DOGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    DOGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    DOGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    DOGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    DOGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    DOGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    DOGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    DOGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    DOGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    DOGAAPAccount("4020", "Revenue — Exports / Free Zone", "Revenue", "Operating Revenue", "Credit"),
    DOGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    DOGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    DOGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    DOGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    DOGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    DOGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    DOGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    DOGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    DOGAAPAccount("6010", "TSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    DOGAAPAccount("6020", "INFOTEP Contribution (1%)", "Expense", "Staff Costs", "Debit"),
    DOGAAPAccount("6030", "Christmas Salary (Regalía Pascual) Expense", "Expense", "Staff Costs", "Debit"),
    DOGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    DOGAAPAccount("6110", "Utilities (EDESUR / EDENORTE / EDEESTE)", "Expense", "Occupancy Costs", "Debit"),
    DOGAAPAccount("6200", "Mercantile Registry Renewal", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6210", "Government Fees and Stamps", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6230", "Telecommunications (Claro / Altice)", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    DOGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    DOGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    DOGAAPAccount("6400", "ISR (Corporate Income Tax) Expense", "Expense", "Tax Expense", "Debit"),
    DOGAAPAccount("6410", "Assets Tax Expense", "Expense", "Tax Expense", "Debit"),
]
