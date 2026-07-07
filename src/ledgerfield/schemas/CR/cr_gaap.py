"""Costa Rica chart of accounts (IFRS/NIIF as applied in Costa Rica).

Costa Rican companies report under IFRS (NIIF). This chart layers Costa
Rica-specific tax and labour accounts on top of an IFRS structure:

ISU  = Impuesto sobre las Utilidades (CIT, Ley 7092; 30% standard, SME 5-20%).
IVA  = Impuesto al Valor Agregado (13% standard, Ley 9635).
CCSS = Caja Costarricense de Seguro Social (social security).
Aguinaldo = mandatory 13th-month salary; cesantía = severance provision.

Costa Rica applies a territorial system: only Costa Rican-source income is
taxed.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CRGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CR_GAAP: list[CRGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    CRGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1020", "Banco Nacional de Costa Rica Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1021", "Banco de Costa Rica (BCR) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1022", "BAC Credomatic Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1023", "Scotiabank Costa Rica Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CRGAAPAccount("1040", "Term Deposit (Certificado de Depósito)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    CRGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    CRGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    CRGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    CRGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    CRGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    CRGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    CRGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    CRGAAPAccount("1180", "IVA Credit (Input VAT Receivable)", "Asset", "Tax Receivable", "Debit"),
    CRGAAPAccount("1190", "Income Tax Advance Payments (Pagos Parciales ISU)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    CRGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    CRGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    CRGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    CRGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    CRGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    CRGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    CRGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    CRGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    CRGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    CRGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    CRGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    CRGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    CRGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    CRGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    CRGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    CRGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    CRGAAPAccount("2100", "IVA Payable (Output VAT 13%)", "Liability", "Tax Payable", "Credit"),
    CRGAAPAccount("2120", "Corporate Income Tax Payable (ISU)", "Liability", "Tax Payable", "Credit"),
    CRGAAPAccount("2130", "Withholding Tax Payable (Remesas al Exterior)", "Liability", "Tax Payable", "Credit"),
    CRGAAPAccount("2140", "Municipal Licence Tax Payable (Patente)", "Liability", "Tax Payable", "Credit"),
    CRGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    CRGAAPAccount("2210", "CCSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    CRGAAPAccount("2220", "Aguinaldo Provision (13th-Month Salary)", "Liability", "Employee Benefits", "Credit"),
    CRGAAPAccount("2230", "Cesantía Provision (Severance)", "Liability", "Employee Benefits", "Credit"),
    CRGAAPAccount("2240", "Vacation Pay Provision", "Liability", "Employee Benefits", "Credit"),
    CRGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    CRGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    CRGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    CRGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    CRGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    CRGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    CRGAAPAccount("3100", "Legal Reserve (Reserva Legal)", "Equity", "Reserves", "Credit"),
    CRGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    CRGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    CRGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    CRGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    CRGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    CRGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    CRGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    CRGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    CRGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    CRGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    CRGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    CRGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    CRGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    CRGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    CRGAAPAccount("6010", "Aguinaldo Expense (13th-Month Salary)", "Expense", "Staff Costs", "Debit"),
    CRGAAPAccount("6020", "CCSS Employer Contributions", "Expense", "Staff Costs", "Debit"),
    CRGAAPAccount("6030", "Cesantía Expense (Severance)", "Expense", "Staff Costs", "Debit"),
    CRGAAPAccount("6040", "INS Workers' Compensation Insurance", "Expense", "Staff Costs", "Debit"),
    CRGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    CRGAAPAccount("6110", "Utilities (ICE / AyA / CNFL)", "Expense", "Occupancy Costs", "Debit"),
    CRGAAPAccount("6200", "Municipal Licence Tax (Patente Municipal)", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6210", "Corporation Tax (Impuesto a las Personas Jurídicas)", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6230", "Telecommunications (Kölbi / Liberty)", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    CRGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    CRGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    CRGAAPAccount("6400", "Corporate Income Tax Expense (ISU)", "Expense", "Tax Expense", "Debit"),
]
