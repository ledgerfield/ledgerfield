"""Bolivarian Republic of Venezuela chart of accounts (VEN-NIF).

Venezuelan companies report under VEN-NIF (IFRS as adopted in Venezuela,
including inflation-adjusted reporting under BA VEN-NIF). This chart layers
Venezuela-specific tax and labour accounts on top of an IFRS structure:

ISLR = Impuesto sobre la Renta (corporate income tax, Tarifa 2 top band 34%).
IVA  = Impuesto al Valor Agregado (VAT, 16% standard).
UT   = Unidad Tributaria (tax unit; bolivar value re-fixed by SENIAT).
INCES/IVSS/FAOV = payroll parafiscal and social security contributions.
Prestaciones sociales = employee severance guarantee (LOTTT).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class VEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


VE_GAAP: list[VEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    VEGAAPAccount("1010", "Cash on Hand (Bolivares)", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1020", "Banco de Venezuela Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1021", "Banesco Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1022", "Banco Mercantil Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1023", "BBVA Provincial Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1024", "Bancaribe Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    VEGAAPAccount("1040", "Short-Term Placements", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    VEGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    VEGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    VEGAAPAccount("1120", "Receivables in Foreign Currency", "Asset", "Trade and Other Receivables", "Debit"),
    VEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    VEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    VEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    VEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    VEGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    VEGAAPAccount("1180", "IVA Credito Fiscal (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    VEGAAPAccount("1185", "IVA Withheld by Customers (Retenciones IVA)", "Asset", "Tax Receivable", "Debit"),
    VEGAAPAccount("1190", "ISLR Advance Payments and Withholdings", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    VEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    VEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    VEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    VEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    VEGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    VEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    VEGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    VEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    VEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1580", "Inflation Revaluation of Non-Monetary Assets (API)", "Asset", "Property, Plant and Equipment", "Debit"),
    VEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    VEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    VEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    VEGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    VEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    VEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    VEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    VEGAAPAccount("2100", "IVA Debito Fiscal (Output VAT, 16%)", "Liability", "Tax Payable", "Credit"),
    VEGAAPAccount("2110", "IVA Withholdings Payable (Retenciones IVA)", "Liability", "Tax Payable", "Credit"),
    VEGAAPAccount("2120", "ISLR Payable (Corporate Income Tax)", "Liability", "Tax Payable", "Credit"),
    VEGAAPAccount("2130", "ISLR Withholdings Payable (Retenciones ISLR)", "Liability", "Tax Payable", "Credit"),
    VEGAAPAccount("2140", "Municipal Business Tax Payable (Actividades Economicas)", "Liability", "Tax Payable", "Credit"),
    VEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2210", "Prestaciones Sociales Provision (LOTTT)", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2220", "Utilidades (Profit-Sharing Bonus) Provision", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2230", "Vacation and Vacation Bonus Provision", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2240", "IVSS Social Security Payable", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2250", "FAOV Housing Fund Payable", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2260", "INCES Training Contribution Payable", "Liability", "Employee Benefits", "Credit"),
    VEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    VEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    VEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    VEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    VEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    VEGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    VEGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    VEGAAPAccount("3110", "Inflation Adjustment Reserve (RPA)", "Equity", "Reserves", "Credit"),
    VEGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    VEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    VEGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    VEGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    VEGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    VEGAAPAccount("4020", "Revenue — Exports (Zero-Rated IVA)", "Revenue", "Operating Revenue", "Credit"),
    VEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    VEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    VEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    VEGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    VEGAAPAccount("4220", "Monetary Position Gain (Inflation)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    VEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    VEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    VEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    VEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    VEGAAPAccount("6010", "Prestaciones Sociales Expense", "Expense", "Staff Costs", "Debit"),
    VEGAAPAccount("6020", "Utilidades (Profit-Sharing) Expense", "Expense", "Staff Costs", "Debit"),
    VEGAAPAccount("6030", "IVSS/FAOV/INCES Employer Contributions", "Expense", "Staff Costs", "Debit"),
    VEGAAPAccount("6040", "Cestaticket (Food Benefit) Expense", "Expense", "Staff Costs", "Debit"),
    VEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    VEGAAPAccount("6110", "Utilities (Corpoelec / Hidrocapital)", "Expense", "Occupancy Costs", "Debit"),
    VEGAAPAccount("6200", "Municipal Business Tax Expense", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6220", "Telecommunications (CANTV / Movilnet / Digitel)", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6240", "Bank Charges and Financial Transaction Tax (IGTF)", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    VEGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    VEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    VEGAAPAccount("6320", "Monetary Position Loss (Inflation)", "Expense", "Finance Costs", "Debit"),
    VEGAAPAccount("6400", "ISLR (Corporate Income Tax) Expense", "Expense", "Tax Expense", "Debit"),
]
