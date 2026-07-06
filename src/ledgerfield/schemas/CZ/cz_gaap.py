"""Czech Republic chart of accounts (Czech GAAP / české účetní standardy).

Czech companies report under Czech accounting standards (Act No. 563/1991
Coll. on Accounting); listed groups use IFRS. This chart layers Czech-specific
tax and payroll accounts on top of an IFRS-style structure:

CIT = Corporate Income Tax (daň z příjmů právnických osob, 21%).
DPH = Value Added Tax (daň z přidané hodnoty, 21% standard / 12% reduced).
Social security and health insurance are administered by ČSSZ and the health
insurance funds.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CZ_GAAP: list[CZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    CZGAAPAccount("1010", "Cash on Hand (Pokladna)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1020", "Česká spořitelna Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1021", "ČSOB Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1022", "Komerční banka Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1023", "Raiffeisenbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    CZGAAPAccount("1040", "Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    CZGAAPAccount("1100", "Trade Receivables (Pohledávky z obchodních vztahů)", "Asset", "Trade and Other Receivables", "Debit"),
    CZGAAPAccount("1110", "Allowance for Doubtful Receivables (Opravné položky)", "Asset", "Trade and Other Receivables", "Credit"),
    CZGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    CZGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    CZGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    CZGAAPAccount("1150", "Prepaid Expenses (Náklady příštích období)", "Asset", "Prepayments", "Debit"),
    CZGAAPAccount("1160", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    CZGAAPAccount("1170", "Input VAT Receivable (DPH na vstupu)", "Asset", "Tax Receivable", "Debit"),
    CZGAAPAccount("1175", "Excess VAT Deduction Refundable (Nadměrný odpočet DPH)", "Asset", "Tax Receivable", "Debit"),
    CZGAAPAccount("1180", "Corporate Income Tax Prepayments (Zálohy na daň)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    CZGAAPAccount("1200", "Inventory — Raw Materials (Materiál)", "Asset", "Inventories", "Debit"),
    CZGAAPAccount("1210", "Inventory — Work in Progress (Nedokončená výroba)", "Asset", "Inventories", "Debit"),
    CZGAAPAccount("1220", "Inventory — Finished Goods (Výrobky)", "Asset", "Inventories", "Debit"),
    CZGAAPAccount("1230", "Merchandise (Zboží)", "Asset", "Inventories", "Debit"),
    CZGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    CZGAAPAccount("1500", "Land (Pozemky)", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1510", "Buildings (Stavby)", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    CZGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    CZGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    CZGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    CZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    CZGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    CZGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    CZGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    CZGAAPAccount("2000", "Trade Payables (Závazky z obchodních vztahů)", "Liability", "Trade and Other Payables", "Credit"),
    CZGAAPAccount("2010", "Accrued Expenses (Výdaje příštích období)", "Liability", "Trade and Other Payables", "Credit"),
    CZGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    CZGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    CZGAAPAccount("2100", "Output VAT Payable — Standard 21% (DPH na výstupu)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2105", "Output VAT Payable — Reduced 12% (DPH snížená sazba)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2110", "VAT Settlement Account (Zúčtování DPH)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2115", "VAT Reverse-Charge Clearing (Přenesení daňové povinnosti)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2120", "Corporate Income Tax Payable (Daň z příjmů PO)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2130", "Payroll Withholding Tax Payable (Záloha na daň ze mzdy)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2140", "Road Tax Payable (Silniční daň)", "Liability", "Tax Payable", "Credit"),
    CZGAAPAccount("2200", "Salaries and Wages Payable (Zaměstnanci)", "Liability", "Employee Benefits", "Credit"),
    CZGAAPAccount("2210", "Social Security Payable (ČSSZ)", "Liability", "Employee Benefits", "Credit"),
    CZGAAPAccount("2220", "Health Insurance Payable (Zdravotní pojišťovny)", "Liability", "Employee Benefits", "Credit"),
    CZGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    CZGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    CZGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    CZGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    CZGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    CZGAAPAccount("2410", "Lease Liability", "Liability", "Non-Current Liabilities", "Credit"),
    CZGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),
    CZGAAPAccount("2430", "Deferred Tax Liability (Odložená daň)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    CZGAAPAccount("3000", "Share Capital (Základní kapitál)", "Equity", "Contributed Capital", "Credit"),
    CZGAAPAccount("3010", "Capital Contributions (Příplatky mimo základní kapitál)", "Equity", "Contributed Capital", "Credit"),
    CZGAAPAccount("3100", "Statutory Reserve Fund (Rezervní fond)", "Equity", "Reserves", "Credit"),
    CZGAAPAccount("3110", "Other Reserves", "Equity", "Reserves", "Credit"),
    CZGAAPAccount("3200", "Retained Earnings (Nerozdělený zisk)", "Equity", "Retained Earnings", "Credit"),
    CZGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    CZGAAPAccount("3300", "Dividends Declared (Podíly na zisku)", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    CZGAAPAccount("4000", "Revenue — Goods (Tržby za zboží)", "Revenue", "Operating Revenue", "Credit"),
    CZGAAPAccount("4010", "Revenue — Services (Tržby za služby)", "Revenue", "Operating Revenue", "Credit"),
    CZGAAPAccount("4020", "Revenue — Intra-EU Supplies", "Revenue", "Operating Revenue", "Credit"),
    CZGAAPAccount("4030", "Revenue — Exports (Non-EU)", "Revenue", "Operating Revenue", "Credit"),
    CZGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    CZGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    CZGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    CZGAAPAccount("4210", "Foreign Exchange Gain (Kurzové zisky)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    CZGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    CZGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    CZGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    CZGAAPAccount("6000", "Salaries and Wages (Mzdové náklady)", "Expense", "Staff Costs", "Debit"),
    CZGAAPAccount("6010", "Social Security Employer Contribution (24.8%)", "Expense", "Staff Costs", "Debit"),
    CZGAAPAccount("6020", "Health Insurance Employer Contribution (9%)", "Expense", "Staff Costs", "Debit"),
    CZGAAPAccount("6030", "Meal Allowance (Stravenkový paušál)", "Expense", "Staff Costs", "Debit"),
    CZGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    CZGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    CZGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6210", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6220", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6230", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6240", "Depreciation Expense (Odpisy)", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6250", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6260", "Road Tax Expense (Silniční daň)", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6270", "Non-Deductible Representation Costs (Náklady na reprezentaci)", "Expense", "Administrative Expenses", "Debit"),
    CZGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    CZGAAPAccount("6310", "Foreign Exchange Loss (Kurzové ztráty)", "Expense", "Finance Costs", "Debit"),
    CZGAAPAccount("6400", "Corporate Income Tax Expense (Daň z příjmů — splatná)", "Expense", "Tax Expense", "Debit"),
    CZGAAPAccount("6410", "Deferred Tax Expense (Daň z příjmů — odložená)", "Expense", "Tax Expense", "Debit"),
]
