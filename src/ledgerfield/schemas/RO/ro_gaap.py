"""Romania chart of accounts (Romanian GAAP / OMFP 1802/2014, IFRS-aligned).

Romanian companies report under Romanian accounting regulations
(OMFP 1802/2014, based on the EU Accounting Directive); listed and banking
entities apply IFRS. This chart layers Romania-specific tax accounts on top
of a familiar structure:

CIT  = Corporate Income Tax / impozit pe profit (16%, Law 227/2015).
TVA  = Taxa pe Valoarea Adaugata (VAT): 19% standard in H1-2025,
       21% from 1 August 2025.
CAS/CASS = Social security / health insurance contributions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ROGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


RO_GAAP: list[ROGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    ROGAAPAccount("1010", "Cash on Hand (Casa in lei)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1020", "Banca Transilvania Account (RON)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1021", "BCR Account (RON)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1022", "BRD Account (RON)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1023", "ING Bank Romania Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ROGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    ROGAAPAccount("1100", "Trade Receivables (Clienti)", "Asset", "Trade and Other Receivables", "Debit"),
    ROGAAPAccount("1110", "Allowance for Doubtful Receivables", "Asset", "Trade and Other Receivables", "Credit"),
    ROGAAPAccount("1120", "Notes Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    ROGAAPAccount("1130", "Other Receivables (Debitori diversi)", "Asset", "Trade and Other Receivables", "Debit"),
    ROGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    ROGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    ROGAAPAccount("1160", "Prepaid Expenses (Cheltuieli in avans)", "Asset", "Prepayments", "Debit"),
    ROGAAPAccount("1170", "Input TVA Deductible (TVA deductibila 4426)", "Asset", "Tax Receivable", "Debit"),
    ROGAAPAccount("1175", "TVA Receivable (TVA de recuperat 4424)", "Asset", "Tax Receivable", "Debit"),
    ROGAAPAccount("1178", "Deferred Input TVA (TVA neexigibila)", "Asset", "Tax Receivable", "Debit"),
    ROGAAPAccount("1180", "Corporate Income Tax Prepayments", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    ROGAAPAccount("1200", "Inventory — Raw Materials (Materii prime)", "Asset", "Inventories", "Debit"),
    ROGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ROGAAPAccount("1220", "Inventory — Finished Goods (Produse finite)", "Asset", "Inventories", "Debit"),
    ROGAAPAccount("1230", "Merchandise (Marfuri)", "Asset", "Inventories", "Debit"),
    ROGAAPAccount("1240", "Provision for Inventory Impairment", "Asset", "Inventories", "Credit"),
    # Non-current assets
    ROGAAPAccount("1500", "Land (Terenuri)", "Asset", "Property, Plant and Equipment", "Debit"),
    ROGAAPAccount("1510", "Buildings (Constructii)", "Asset", "Property, Plant and Equipment", "Debit"),
    ROGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    ROGAAPAccount("1530", "Plant and Machinery (Echipamente tehnologice)", "Asset", "Property, Plant and Equipment", "Debit"),
    ROGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    ROGAAPAccount("1540", "Motor Vehicles (Mijloace de transport)", "Asset", "Property, Plant and Equipment", "Debit"),
    ROGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    ROGAAPAccount("1550", "Furniture and Office Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    ROGAAPAccount("1600", "Goodwill (Fond comercial)", "Asset", "Intangible Assets", "Debit"),
    ROGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    ROGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    ROGAAPAccount("1710", "Long-Term Deposits and Guarantees", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    ROGAAPAccount("2000", "Trade Payables (Furnizori)", "Liability", "Trade and Other Payables", "Credit"),
    ROGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    ROGAAPAccount("2020", "Other Payables (Creditori diversi)", "Liability", "Trade and Other Payables", "Credit"),
    ROGAAPAccount("2030", "Advances from Customers (Clienti creditori)", "Liability", "Trade and Other Payables", "Credit"),
    ROGAAPAccount("2100", "Output TVA Collected (TVA colectata 4427)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2105", "TVA Payable (TVA de plata 4423)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2108", "Deferred Output TVA (TVA neexigibila)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2120", "Corporate Income Tax Payable (Impozit pe profit 441)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2125", "Micro-Enterprise Tax Payable (Impozit micro)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2130", "Dividend Tax Payable (Impozit pe dividende)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2140", "Payroll Income Tax Payable (Impozit pe salarii 444)", "Liability", "Tax Payable", "Credit"),
    ROGAAPAccount("2200", "Salaries and Wages Payable (Salarii datorate 421)", "Liability", "Employee Benefits", "Credit"),
    ROGAAPAccount("2210", "Social Security Payable (CAS 4315)", "Liability", "Employee Benefits", "Credit"),
    ROGAAPAccount("2220", "Health Insurance Payable (CASS 4316)", "Liability", "Employee Benefits", "Credit"),
    ROGAAPAccount("2230", "Work Insurance Contribution Payable (CAM 436)", "Liability", "Employee Benefits", "Credit"),
    ROGAAPAccount("2240", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    ROGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ROGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    ROGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    ROGAAPAccount("2400", "Long-Term Loans (Credite bancare pe termen lung)", "Liability", "Non-Current Liabilities", "Credit"),
    ROGAAPAccount("2410", "Lease Liability", "Liability", "Non-Current Liabilities", "Credit"),
    ROGAAPAccount("2420", "Shareholder Loan (Imprumut asociat 455)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ROGAAPAccount("3000", "Share Capital (Capital social 101)", "Equity", "Contributed Capital", "Credit"),
    ROGAAPAccount("3100", "Legal Reserve (Rezerve legale 1061)", "Equity", "Reserves", "Credit"),
    ROGAAPAccount("3110", "Other Reserves", "Equity", "Reserves", "Credit"),
    ROGAAPAccount("3200", "Retained Earnings (Rezultatul reportat 117)", "Equity", "Retained Earnings", "Credit"),
    ROGAAPAccount("3210", "Current Year Profit / (Loss) (Rezultatul exercitiului 121)", "Equity", "Retained Earnings", "Credit"),
    ROGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ROGAAPAccount("4000", "Revenue — Goods (Venituri din vanzarea marfurilor 707)", "Revenue", "Operating Revenue", "Credit"),
    ROGAAPAccount("4010", "Revenue — Services (Venituri din prestari servicii 704)", "Revenue", "Operating Revenue", "Credit"),
    ROGAAPAccount("4020", "Revenue — Intra-EU and Export Sales", "Revenue", "Operating Revenue", "Credit"),
    ROGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ROGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    ROGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    ROGAAPAccount("4210", "Government Grants Income (Subventii)", "Revenue", "Other Income", "Credit"),
    ROGAAPAccount("4220", "Foreign Exchange Gain (Venituri din diferente de curs 765)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    ROGAAPAccount("5000", "Cost of Goods Sold (Cheltuieli privind marfurile 607)", "Expense", "Cost of Sales", "Debit"),
    ROGAAPAccount("5010", "Raw Materials Consumed (601)", "Expense", "Cost of Sales", "Debit"),
    ROGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    ROGAAPAccount("6000", "Salaries and Wages (Cheltuieli cu salariile 641)", "Expense", "Staff Costs", "Debit"),
    ROGAAPAccount("6010", "Employer Work Insurance Contribution (CAM 2.25%)", "Expense", "Staff Costs", "Debit"),
    ROGAAPAccount("6020", "Meal Vouchers (Tichete de masa)", "Expense", "Staff Costs", "Debit"),
    ROGAAPAccount("6100", "Office Rent (Cheltuieli cu chiriile 612)", "Expense", "Occupancy Costs", "Debit"),
    ROGAAPAccount("6110", "Utilities (Energie si apa 605)", "Expense", "Occupancy Costs", "Debit"),
    ROGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6210", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6220", "Marketing and Advertising (623)", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6230", "Bank Charges (627)", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6240", "Depreciation Expense (Cheltuieli cu amortizarea 6811)", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6250", "Repairs and Maintenance (611)", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6260", "Local Taxes and Duties (635)", "Expense", "Administrative Expenses", "Debit"),
    ROGAAPAccount("6300", "Finance Costs (Cheltuieli cu dobanzile 666)", "Expense", "Finance Costs", "Debit"),
    ROGAAPAccount("6310", "Foreign Exchange Loss (665)", "Expense", "Finance Costs", "Debit"),
    ROGAAPAccount("6400", "Corporate Income Tax Expense (Cheltuieli cu impozitul pe profit 691)", "Expense", "Tax Expense", "Debit"),
]
