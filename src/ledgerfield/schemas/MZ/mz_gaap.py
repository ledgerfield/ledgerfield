"""Republic of Mozambique chart of accounts (PGC-NIRF oriented, IFRS-informed).

Mozambican companies report under the Plano Geral de Contabilidade (PGC-NIRF,
IFRS-based). This chart layers Mozambique-specific tax and labour accounts on
top of a general structure:

IRPC = corporate income tax (32% standard; 10% agriculture/aquaculture —
Código do IRPC).
IVA = value added tax at 16% standard; small taxpayers may use the ISPC 3%
simplified turnover regime.
INSS = Instituto Nacional de Segurança Social contributions (3% employee,
4% employer).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MZ_GAAP: list[MZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MZGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1020", "Millennium BIM Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1021", "Banco Comercial e de Investimentos (BCI) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1022", "Standard Bank Moçambique Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1023", "Absa Bank Moçambique Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1024", "Moza Banco Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MZGAAPAccount("1040", "Term Deposits (Metical)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MZGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MZGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    MZGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    MZGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MZGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MZGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MZGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MZGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MZGAAPAccount("1180", "IVA Receivable (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    MZGAAPAccount("1190", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MZGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MZGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MZGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MZGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MZGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MZGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MZGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MZGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MZGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    MZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    MZGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MZGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    MZGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MZGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MZGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    MZGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MZGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MZGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MZGAAPAccount("2100", "IVA Payable (Output VAT 16%)", "Liability", "Tax Payable", "Credit"),
    MZGAAPAccount("2110", "IVA Settlement Account (Autoridade Tributária)", "Liability", "Tax Payable", "Credit"),
    MZGAAPAccount("2120", "IRPC Payable (CIT)", "Liability", "Tax Payable", "Credit"),
    MZGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    MZGAAPAccount("2140", "IRPS Payable (Employment Income Tax Withheld)", "Liability", "Tax Payable", "Credit"),
    MZGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MZGAAPAccount("2210", "INSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    MZGAAPAccount("2220", "Holiday and 13th-Month Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MZGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MZGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MZGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MZGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MZGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    MZGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MZGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    MZGAAPAccount("3010", "Supplementary Capital Contributions", "Equity", "Contributed Capital", "Credit"),
    MZGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    MZGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    MZGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    MZGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MZGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MZGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MZGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MZGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    MZGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MZGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MZGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MZGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MZGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MZGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MZGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MZGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MZGAAPAccount("5030", "Import Duties and Customs Charges", "Expense", "Cost of Sales", "Debit"),
    MZGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MZGAAPAccount("6010", "INSS Employer Contribution (4%)", "Expense", "Staff Costs", "Debit"),
    MZGAAPAccount("6020", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    MZGAAPAccount("6030", "Staff Training", "Expense", "Staff Costs", "Debit"),
    MZGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MZGAAPAccount("6110", "Utilities (EDM / FIPAG)", "Expense", "Occupancy Costs", "Debit"),
    MZGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    MZGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6210", "Government and Municipal Fees", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6230", "Telecommunications (Vodacom / Tmcel / Movitel)", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6280", "Non-Deductible IVA Expense", "Expense", "Administrative Expenses", "Debit"),
    MZGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MZGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MZGAAPAccount("6400", "IRPC Expense (CIT)", "Expense", "Tax Expense", "Debit"),
]
