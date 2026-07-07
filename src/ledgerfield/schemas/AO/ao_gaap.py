"""Republic of Angola chart of accounts (PGC-Angola oriented, IFRS-informed).

Angolan companies report under the Plano Geral de Contabilidade (PGC-Angola);
banks and larger entities align with IFRS. This chart layers Angola-specific
tax and labour accounts on top of a general structure:

Imposto Industrial = corporate income tax (25% standard; 35% banking/
insurance/telecom; 10% agriculture — Law 26/20).
IVA = value added tax at 14% standard (7% simplified/reduced bands).
INSS = Instituto Nacional de Segurança Social contributions (3% employee,
8% employer).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AOGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AO_GAAP: list[AOGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    AOGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1020", "Banco Angolano de Investimentos (BAI) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1021", "Banco de Fomento Angola (BFA) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1022", "Banco BIC Angola Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1023", "Banco Millennium Atlântico Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1024", "Standard Bank Angola Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    AOGAAPAccount("1040", "Term Deposits (Kwanza)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    AOGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AOGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    AOGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    AOGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    AOGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    AOGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    AOGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    AOGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    AOGAAPAccount("1180", "IVA Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    AOGAAPAccount("1190", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    AOGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    AOGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    AOGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    AOGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    AOGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    AOGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    AOGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    AOGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    AOGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    AOGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    AOGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    AOGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    AOGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    AOGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    AOGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    AOGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    AOGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    AOGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    AOGAAPAccount("2100", "IVA Payable (Output VAT 14%)", "Liability", "Tax Payable", "Credit"),
    AOGAAPAccount("2110", "IVA Settlement Account (AGT)", "Liability", "Tax Payable", "Credit"),
    AOGAAPAccount("2120", "Imposto Industrial Payable (CIT)", "Liability", "Tax Payable", "Credit"),
    AOGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    AOGAAPAccount("2140", "IRT Payable (Employment Income Tax Withheld)", "Liability", "Tax Payable", "Credit"),
    AOGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    AOGAAPAccount("2210", "INSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    AOGAAPAccount("2220", "Holiday and 13th-Month Pay Provision", "Liability", "Employee Benefits", "Credit"),
    AOGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    AOGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    AOGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    AOGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    AOGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    AOGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    AOGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    AOGAAPAccount("3010", "Supplementary Capital Contributions", "Equity", "Contributed Capital", "Credit"),
    AOGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    AOGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    AOGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    AOGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    AOGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    AOGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    AOGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    AOGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    AOGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    AOGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    AOGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    AOGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    AOGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    AOGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    AOGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    AOGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    AOGAAPAccount("5030", "Import Duties and Customs Charges", "Expense", "Cost of Sales", "Debit"),
    AOGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    AOGAAPAccount("6010", "INSS Employer Contribution (8%)", "Expense", "Staff Costs", "Debit"),
    AOGAAPAccount("6020", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    AOGAAPAccount("6030", "Staff Training", "Expense", "Staff Costs", "Debit"),
    AOGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    AOGAAPAccount("6110", "Utilities (ENDE / EPAL)", "Expense", "Occupancy Costs", "Debit"),
    AOGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    AOGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6230", "Telecommunications (Unitel / Movicel)", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6280", "Non-Deductible IVA Expense", "Expense", "Administrative Expenses", "Debit"),
    AOGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    AOGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    AOGAAPAccount("6400", "Imposto Industrial Expense (CIT)", "Expense", "Tax Expense", "Debit"),
]
