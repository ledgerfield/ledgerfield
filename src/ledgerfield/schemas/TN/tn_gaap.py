"""Tunisia chart of accounts (Systeme Comptable des Entreprises).

Tunisian companies report under the national Systeme Comptable des
Entreprises (SCE, Law 96-112), a plan-comptable-style framework. This chart
layers Tunisia-specific tax and payroll accounts on top of that structure:

IS   = Impot sur les Societes (CIT; standard 20% under Finance Law 2025).
TVA  = Taxe sur la Valeur Ajoutee (VAT; 19% standard, 13%/7% reduced).
CNSS = Caisse Nationale de Securite Sociale contributions.
TFP  = Taxe de Formation Professionnelle; FOPROLOS = housing levy.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TNGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TN_GAAP: list[TNGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    TNGAAPAccount("1010", "Cash on Hand (Caisse)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1020", "BIAT Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1021", "BNA Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1022", "STB Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1023", "Attijari Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1030", "Foreign Currency Account (EUR/USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TNGAAPAccount("1040", "Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    TNGAAPAccount("1100", "Trade Receivables (Clients)", "Asset", "Trade and Other Receivables", "Debit"),
    TNGAAPAccount("1110", "Allowance for Doubtful Receivables", "Asset", "Trade and Other Receivables", "Credit"),
    TNGAAPAccount("1120", "Notes Receivable (Effets a Recevoir)", "Asset", "Trade and Other Receivables", "Debit"),
    TNGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TNGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    TNGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    TNGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    TNGAAPAccount("1170", "TVA Deductible (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    TNGAAPAccount("1180", "CIT Instalments Paid (Acomptes Provisionnels)", "Asset", "Tax Receivable", "Debit"),
    TNGAAPAccount("1190", "Withholding Tax Credit (Retenue a la Source)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    TNGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    TNGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    TNGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    TNGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    TNGAAPAccount("1240", "Provision for Inventory Obsolescence", "Asset", "Inventories", "Credit"),
    # Non-current assets
    TNGAAPAccount("1500", "Land (Terrains)", "Asset", "Property, Plant and Equipment", "Debit"),
    TNGAAPAccount("1510", "Buildings (Constructions)", "Asset", "Property, Plant and Equipment", "Debit"),
    TNGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    TNGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    TNGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    TNGAAPAccount("1540", "Motor Vehicles (Materiel de Transport)", "Asset", "Property, Plant and Equipment", "Debit"),
    TNGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    TNGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    TNGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    TNGAAPAccount("1600", "Goodwill (Fonds Commercial)", "Asset", "Intangible Assets", "Debit"),
    TNGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    TNGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    TNGAAPAccount("2000", "Trade Payables (Fournisseurs)", "Liability", "Trade and Other Payables", "Credit"),
    TNGAAPAccount("2010", "Notes Payable (Effets a Payer)", "Liability", "Trade and Other Payables", "Credit"),
    TNGAAPAccount("2020", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    TNGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    TNGAAPAccount("2100", "TVA Collectee (Output VAT)", "Liability", "Tax Payable", "Credit"),
    TNGAAPAccount("2120", "Corporate Income Tax Payable (IS)", "Liability", "Tax Payable", "Credit"),
    TNGAAPAccount("2130", "Withholding Tax Payable (Retenue a la Source)", "Liability", "Tax Payable", "Credit"),
    TNGAAPAccount("2140", "TFP / FOPROLOS Payable", "Liability", "Tax Payable", "Credit"),
    TNGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    TNGAAPAccount("2210", "CNSS Contributions Payable", "Liability", "Employee Benefits", "Credit"),
    TNGAAPAccount("2220", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    TNGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    TNGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    TNGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    TNGAAPAccount("2410", "Leasing Liabilities", "Liability", "Non-Current Liabilities", "Credit"),
    TNGAAPAccount("2420", "Shareholder Loan (Compte Courant Associes)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    TNGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    TNGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    TNGAAPAccount("3100", "Legal Reserve (Reserve Legale)", "Equity", "Reserves", "Credit"),
    TNGAAPAccount("3110", "Statutory Reserves", "Equity", "Reserves", "Credit"),
    TNGAAPAccount("3200", "Retained Earnings (Resultats Reportes)", "Equity", "Retained Earnings", "Credit"),
    TNGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    TNGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    TNGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    TNGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    TNGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    TNGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    TNGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    TNGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    TNGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    TNGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    TNGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    TNGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    TNGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    TNGAAPAccount("6010", "CNSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    TNGAAPAccount("6020", "TFP (Vocational Training Tax)", "Expense", "Staff Costs", "Debit"),
    TNGAAPAccount("6030", "FOPROLOS (Housing Levy)", "Expense", "Staff Costs", "Debit"),
    TNGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    TNGAAPAccount("6110", "Utilities (STEG / SONEDE)", "Expense", "Occupancy Costs", "Debit"),
    TNGAAPAccount("6200", "Municipal Taxes (TCL)", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6210", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6220", "Telecommunications (Tunisie Telecom / Ooredoo)", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6230", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6240", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6250", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6260", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6270", "Stamp Duty (Droit de Timbre)", "Expense", "Administrative Expenses", "Debit"),
    TNGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    TNGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    TNGAAPAccount("6400", "Corporate Income Tax Expense (IS)", "Expense", "Tax Expense", "Debit"),
    TNGAAPAccount("6410", "Conjunctural Contribution Expense", "Expense", "Tax Expense", "Debit"),
]
