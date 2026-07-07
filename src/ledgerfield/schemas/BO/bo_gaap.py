"""Plurinational State of Bolivia chart of accounts (Bolivian GAAP / NC).

Bolivian companies report under national accounting standards (Normas de
Contabilidad issued by the CTNAC/CAUB), converging with IFRS. This chart
layers Bolivia-specific tax and labour accounts on top of that structure:

IUE = Impuesto sobre las Utilidades de las Empresas (25% corporate profits tax).
IVA = Impuesto al Valor Agregado (13% inside-price VAT; debito/credito fiscal).
IT  = Impuesto a las Transacciones (3% gross-receipts transactions tax).
RC-IVA = employee complementary VAT regime withheld through payroll.
Aguinaldo / prima = mandatory year-end bonus and profit-sharing bonus.
AFP/Gestora, CNS = pension and health social contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BOGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


BO_GAAP: list[BOGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    BOGAAPAccount("1010", "Cash on Hand (Bolivianos)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1020", "Banco Mercantil Santa Cruz Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1021", "Banco Nacional de Bolivia Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1022", "Banco Union Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1023", "Banco BISA Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1024", "BancoSol Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    BOGAAPAccount("1040", "Fixed-Term Deposits (DPF)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    BOGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BOGAAPAccount("1110", "Allowance for Doubtful Accounts", "Asset", "Trade and Other Receivables", "Credit"),
    BOGAAPAccount("1120", "Notes Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    BOGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    BOGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    BOGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    BOGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    BOGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    BOGAAPAccount("1180", "IVA Credito Fiscal (Input VAT, 13%)", "Asset", "Tax Receivable", "Debit"),
    BOGAAPAccount("1185", "IUE Paid Creditable Against IT", "Asset", "Tax Receivable", "Debit"),
    BOGAAPAccount("1190", "Tax Withholdings Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    BOGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    BOGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    BOGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    BOGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    BOGAAPAccount("1240", "Provision for Obsolete Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    BOGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    BOGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    BOGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    BOGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1570", "Fixed-Asset Revaluation (UFV Update)", "Asset", "Property, Plant and Equipment", "Debit"),
    BOGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    BOGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    BOGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    BOGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    BOGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    BOGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    BOGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    BOGAAPAccount("2100", "IVA Debito Fiscal (Output VAT, 13%)", "Liability", "Tax Payable", "Credit"),
    BOGAAPAccount("2110", "IT Payable (Transactions Tax, 3%)", "Liability", "Tax Payable", "Credit"),
    BOGAAPAccount("2120", "IUE Payable (Corporate Profits Tax, 25%)", "Liability", "Tax Payable", "Credit"),
    BOGAAPAccount("2130", "RC-IVA Withholdings Payable", "Liability", "Tax Payable", "Credit"),
    BOGAAPAccount("2140", "IUE-BE Withholdings Payable (Non-Resident Remittances)", "Liability", "Tax Payable", "Credit"),
    BOGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2210", "Aguinaldo (Year-End Bonus) Provision", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2220", "Prima (Profit-Sharing Bonus) Provision", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2230", "Indemnity / Severance Provision (Indemnizacion)", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2240", "CNS Health Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2250", "AFP / Gestora Publica Pension Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2260", "Provivienda Housing Contribution Payable", "Liability", "Employee Benefits", "Credit"),
    BOGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    BOGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    BOGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    BOGAAPAccount("2410", "Lease Liability", "Liability", "Non-Current Liabilities", "Credit"),
    BOGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    BOGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    BOGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    BOGAAPAccount("3110", "Equity Restatement Reserve (Ajuste de Capital, UFV)", "Equity", "Reserves", "Credit"),
    BOGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    BOGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    BOGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    BOGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    BOGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    BOGAAPAccount("4020", "Revenue — Exports (Zero-Rated IVA)", "Revenue", "Operating Revenue", "Credit"),
    BOGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    BOGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    BOGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    BOGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    BOGAAPAccount("4220", "Inflation Restatement Gain (UFV)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    BOGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    BOGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    BOGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    BOGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    BOGAAPAccount("6010", "Aguinaldo Expense", "Expense", "Staff Costs", "Debit"),
    BOGAAPAccount("6020", "Employer Social Contributions (CNS / Provivienda / Riesgo)", "Expense", "Staff Costs", "Debit"),
    BOGAAPAccount("6030", "Severance and Indemnity Expense", "Expense", "Staff Costs", "Debit"),
    BOGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    BOGAAPAccount("6110", "Utilities (Electricity / Water / Gas)", "Expense", "Occupancy Costs", "Debit"),
    BOGAAPAccount("6200", "IT (Transactions Tax) Expense", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6220", "Telecommunications (Entel / Tigo / Viva)", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    BOGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    BOGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    BOGAAPAccount("6320", "Inflation Restatement Loss (UFV)", "Expense", "Finance Costs", "Debit"),
    BOGAAPAccount("6400", "IUE (Corporate Profits Tax) Expense", "Expense", "Tax Expense", "Debit"),
]
