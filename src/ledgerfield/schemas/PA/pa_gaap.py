"""Panama chart of accounts (IFRS/NIIF as applied in Panama).

Panamanian companies report under IFRS (NIIF). This chart layers
Panama-specific tax and labour accounts on top of an IFRS structure:

ISR   = Impuesto sobre la Renta (CIT, Código Fiscal; 25% flat, CAIR minimum).
ITBMS = Impuesto a la Transferencia de Bienes Corporales Muebles y la
        Prestación de Servicios (VAT, 7% standard).
CSS   = Caja de Seguro Social (social security).
Décimo Tercer Mes = mandatory 13th-month salary (three instalments);
Prima de Antigüedad = seniority premium provision.

Panama applies a territorial system (only Panama-source income is taxed)
and operates free-zone regimes (e.g. Zona Libre de Colón, Panamá Pacífico).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


PA_GAAP: list[PAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    PAGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1020", "Banco General Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1021", "Banistmo Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1022", "BAC Credomatic Panamá Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1023", "Banco Nacional de Panamá Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    PAGAAPAccount("1040", "Term Deposit (Depósito a Plazo Fijo)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    PAGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PAGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    PAGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    PAGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    PAGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    PAGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    PAGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    PAGAAPAccount("1180", "ITBMS Credit (Input VAT Receivable)", "Asset", "Tax Receivable", "Debit"),
    PAGAAPAccount("1190", "Income Tax Advance Payments (Adelanto ISR)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    PAGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    PAGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    PAGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    PAGAAPAccount("1230", "Goods in Transit (Colón Free Zone)", "Asset", "Inventories", "Debit"),
    PAGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    PAGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    PAGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    PAGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    PAGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    PAGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    PAGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    PAGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    PAGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    PAGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    PAGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    PAGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    PAGAAPAccount("2100", "ITBMS Payable (Output VAT 7%)", "Liability", "Tax Payable", "Credit"),
    PAGAAPAccount("2120", "Corporate Income Tax Payable (ISR)", "Liability", "Tax Payable", "Credit"),
    PAGAAPAccount("2130", "Dividend Tax / Complementary Tax Payable", "Liability", "Tax Payable", "Credit"),
    PAGAAPAccount("2140", "Municipal Tax Payable (Impuesto Municipal)", "Liability", "Tax Payable", "Credit"),
    PAGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    PAGAAPAccount("2210", "CSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    PAGAAPAccount("2220", "Décimo Tercer Mes Provision (13th-Month Salary)", "Liability", "Employee Benefits", "Credit"),
    PAGAAPAccount("2230", "Prima de Antigüedad Provision (Seniority Premium)", "Liability", "Employee Benefits", "Credit"),
    PAGAAPAccount("2240", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    PAGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    PAGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    PAGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    PAGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    PAGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    PAGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    PAGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    PAGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    PAGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    PAGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    PAGAAPAccount("4000", "Revenue — Goods (Panama Source)", "Revenue", "Operating Revenue", "Credit"),
    PAGAAPAccount("4010", "Revenue — Services (Panama Source)", "Revenue", "Operating Revenue", "Credit"),
    PAGAAPAccount("4020", "Revenue — Foreign Source (Territorial Exempt)", "Revenue", "Operating Revenue", "Credit"),
    PAGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    PAGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    PAGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    PAGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    PAGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    PAGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    PAGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    PAGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    PAGAAPAccount("6010", "Décimo Tercer Mes Expense (13th-Month Salary)", "Expense", "Staff Costs", "Debit"),
    PAGAAPAccount("6020", "CSS Employer Contributions", "Expense", "Staff Costs", "Debit"),
    PAGAAPAccount("6030", "Educational Insurance Tax (Seguro Educativo)", "Expense", "Staff Costs", "Debit"),
    PAGAAPAccount("6040", "Prima de Antigüedad Expense", "Expense", "Staff Costs", "Debit"),
    PAGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    PAGAAPAccount("6110", "Utilities (ENSA / Naturgy / IDAAN)", "Expense", "Occupancy Costs", "Debit"),
    PAGAAPAccount("6200", "Annual Franchise Tax (Tasa Única)", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6210", "Notice of Operation Tax (Aviso de Operación)", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6230", "Telecommunications (+Móvil / Tigo)", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    PAGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    PAGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    PAGAAPAccount("6400", "Corporate Income Tax Expense (ISR)", "Expense", "Tax Expense", "Debit"),
]
