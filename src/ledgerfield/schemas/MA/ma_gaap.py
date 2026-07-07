"""Kingdom of Morocco chart of accounts (CGNC-inspired, SME layout).

Moroccan companies report under the Code Général de Normalisation Comptable
(CGNC) / Plan Comptable Général Marocain. This chart layers Morocco-specific
tax and payroll accounts on top of an SME structure:

IS   = Impôt sur les Sociétés (corporate income tax; two-rate target system
       20%/35%, financial institutions 40%, per Finance Law 2023 convergence).
TVA  = Taxe sur la Valeur Ajoutée (VAT; 20% standard, 14/10/7% reduced).
CNSS = Caisse Nationale de Sécurité Sociale (social security).
IR   = Impôt sur le Revenu (payroll withholding on salaries).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


MA_GAAP: list[MAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    MAGAAPAccount("1010", "Cash on Hand (Caisse)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1020", "Attijariwafa Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1021", "Banque Populaire Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1022", "BMCE / Bank of Africa Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1023", "CIH Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    MAGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    MAGAAPAccount("1100", "Trade Receivables (Clients)", "Asset", "Trade and Other Receivables", "Debit"),
    MAGAAPAccount("1110", "Allowance for Doubtful Receivables", "Asset", "Trade and Other Receivables", "Credit"),
    MAGAAPAccount("1120", "Notes Receivable (Effets à recevoir)", "Asset", "Trade and Other Receivables", "Debit"),
    MAGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    MAGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    MAGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    MAGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    MAGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    MAGAAPAccount("1180", "TVA Déductible (Input VAT Recoverable)", "Asset", "Tax Receivable", "Debit"),
    MAGAAPAccount("1185", "TVA Credit Carryforward", "Asset", "Tax Receivable", "Debit"),
    MAGAAPAccount("1190", "IS Instalments Paid (Acomptes IS)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    MAGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    MAGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    MAGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    MAGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    MAGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    MAGAAPAccount("1500", "Land (Terrains)", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1510", "Buildings (Constructions)", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    MAGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    MAGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    MAGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    MAGAAPAccount("1600", "Goodwill (Fonds Commercial)", "Asset", "Intangible Assets", "Debit"),
    MAGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    MAGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    MAGAAPAccount("1710", "Long-Term Deposits and Guarantees", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    MAGAAPAccount("2000", "Trade Payables (Fournisseurs)", "Liability", "Trade and Other Payables", "Credit"),
    MAGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    MAGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    MAGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    MAGAAPAccount("2040", "Notes Payable (Effets à payer)", "Liability", "Trade and Other Payables", "Credit"),
    MAGAAPAccount("2100", "TVA Collectée (Output VAT)", "Liability", "Tax Payable", "Credit"),
    MAGAAPAccount("2110", "TVA Payable (VAT Settlement — État)", "Liability", "Tax Payable", "Credit"),
    MAGAAPAccount("2120", "Corporate Income Tax Payable (IS)", "Liability", "Tax Payable", "Credit"),
    MAGAAPAccount("2125", "Cotisation Minimale Payable", "Liability", "Tax Payable", "Credit"),
    MAGAAPAccount("2130", "Payroll Tax Withheld (IR sur salaires)", "Liability", "Tax Payable", "Credit"),
    MAGAAPAccount("2140", "Social Solidarity Contribution Payable", "Liability", "Tax Payable", "Credit"),
    MAGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    MAGAAPAccount("2210", "CNSS Payable", "Liability", "Employee Benefits", "Credit"),
    MAGAAPAccount("2220", "AMO Health Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    MAGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    MAGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    MAGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    MAGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    MAGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    MAGAAPAccount("2420", "Shareholder Loan (Compte Courant d'Associés)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    MAGAAPAccount("3000", "Share Capital (Capital Social)", "Equity", "Contributed Capital", "Credit"),
    MAGAAPAccount("3100", "Legal Reserve (Réserve Légale)", "Equity", "Reserves", "Credit"),
    MAGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    MAGAAPAccount("3200", "Retained Earnings (Report à Nouveau)", "Equity", "Retained Earnings", "Credit"),
    MAGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    MAGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    MAGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    MAGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    MAGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    MAGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    MAGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    MAGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    MAGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    MAGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    MAGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    MAGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    MAGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    MAGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    MAGAAPAccount("6010", "CNSS Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MAGAAPAccount("6020", "AMO Employer Contribution", "Expense", "Staff Costs", "Debit"),
    MAGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    MAGAAPAccount("6040", "Staff Training (incl. OFPPT levy)", "Expense", "Staff Costs", "Debit"),
    MAGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    MAGAAPAccount("6110", "Utilities (Water and Electricity)", "Expense", "Occupancy Costs", "Debit"),
    MAGAAPAccount("6200", "Business Licence Tax (Taxe Professionnelle)", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6230", "Telecommunications (Maroc Telecom / Orange / inwi)", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6280", "Non-Recoverable TVA Expense", "Expense", "Administrative Expenses", "Debit"),
    MAGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    MAGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    MAGAAPAccount("6400", "Corporate Income Tax Expense (IS)", "Expense", "Tax Expense", "Debit"),
    MAGAAPAccount("6410", "Cotisation Minimale Expense", "Expense", "Tax Expense", "Debit"),
]
