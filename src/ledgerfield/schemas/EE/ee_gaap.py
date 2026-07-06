"""Republic of Estonia chart of accounts (Estonian GAAP / IFRS for SMEs based).

Estonian companies report under Estonian financial reporting standard
(raamatupidamise seadus, based on IFRS for SMEs) or full IFRS. This chart
layers Estonia-specific tax and payroll accounts on top:

Käibemaks = VAT (standard 22% in H1 2025, 24% from 1 July 2025).
Tulumaks = income tax — under the Estonian model, corporate income tax is
    due only on profit DISTRIBUTION (22/78 of the net distribution from 2025);
    retained profit carries no tax, so the CIT accounts relate to
    distributions, fringe benefits and non-business expenses.
Sotsiaalmaks = 33% employer social tax.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class EEGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


EE_GAAP: list[EEGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    EEGAAPAccount("1010", "Cash on Hand (Kassa)", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1020", "Swedbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1021", "SEB Pank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1022", "LHV Pank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1023", "Luminor Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1024", "Coop Pank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    EEGAAPAccount("1040", "Short-Term Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    EEGAAPAccount("1100", "Trade Receivables (Nõuded ostjate vastu)", "Asset", "Trade and Other Receivables", "Debit"),
    EEGAAPAccount("1110", "Allowance for Doubtful Receivables", "Asset", "Trade and Other Receivables", "Credit"),
    EEGAAPAccount("1120", "Input VAT Receivable (Sisendkäibemaks)", "Asset", "Tax Receivable", "Debit"),
    EEGAAPAccount("1125", "VAT Refund Receivable from EMTA", "Asset", "Tax Receivable", "Debit"),
    EEGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    EEGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    EEGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    EEGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    EEGAAPAccount("1170", "Prepaid Taxes (EMTA Prepayment Account)", "Asset", "Prepayments", "Debit"),
    # Inventory
    EEGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    EEGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    EEGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    EEGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    EEGAAPAccount("1240", "Write-Down of Inventories", "Asset", "Inventories", "Credit"),
    # Non-current assets
    EEGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    EEGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    EEGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    EEGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    EEGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    EEGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    EEGAAPAccount("1620", "Development Costs", "Asset", "Intangible Assets", "Debit"),
    EEGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    EEGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    EEGAAPAccount("2000", "Trade Payables (Võlad tarnijatele)", "Liability", "Trade and Other Payables", "Credit"),
    EEGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    EEGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    EEGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    EEGAAPAccount("2100", "Output VAT Payable (Käibemaks müügilt)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2105", "VAT Payable to EMTA (Käibemaksukohustus)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2110", "VAT on EU Acquisitions (Reverse Charge)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2115", "OSS VAT Payable (EU One-Stop-Shop)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2120", "Income Tax Payable on Distributions (Tulumaks)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2130", "Income Tax Payable on Fringe Benefits (Erisoodustus)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2140", "Withholding Tax Payable (TSD)", "Liability", "Tax Payable", "Credit"),
    EEGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    EEGAAPAccount("2210", "Social Tax Payable (Sotsiaalmaks 33%)", "Liability", "Employee Benefits", "Credit"),
    EEGAAPAccount("2220", "Unemployment Insurance Payable (Töötuskindlustus)", "Liability", "Employee Benefits", "Credit"),
    EEGAAPAccount("2230", "Funded Pension Withholding Payable (Kogumispension)", "Liability", "Employee Benefits", "Credit"),
    EEGAAPAccount("2240", "Holiday Pay Provision", "Liability", "Employee Benefits", "Credit"),
    EEGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    EEGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    EEGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    EEGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    EEGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    EEGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    EEGAAPAccount("3000", "Share Capital (Osakapital)", "Equity", "Contributed Capital", "Credit"),
    EEGAAPAccount("3010", "Share Premium (Ülekurss)", "Equity", "Contributed Capital", "Credit"),
    EEGAAPAccount("3100", "Statutory Legal Reserve (Kohustuslik reservkapital)", "Equity", "Reserves", "Credit"),
    EEGAAPAccount("3200", "Retained Earnings (Untaxed until Distribution)", "Equity", "Retained Earnings", "Credit"),
    EEGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    EEGAAPAccount("3300", "Dividends Declared (Net Distribution)", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    EEGAAPAccount("4000", "Revenue — Goods (Domestic, VAT 22%/24%)", "Revenue", "Operating Revenue", "Credit"),
    EEGAAPAccount("4010", "Revenue — Services (Domestic)", "Revenue", "Operating Revenue", "Credit"),
    EEGAAPAccount("4020", "Revenue — Intra-EU Supplies (0% VAT)", "Revenue", "Operating Revenue", "Credit"),
    EEGAAPAccount("4030", "Revenue — Exports Outside EU (0% VAT)", "Revenue", "Operating Revenue", "Credit"),
    EEGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    EEGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    EEGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    EEGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    EEGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    EEGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    EEGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    EEGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    EEGAAPAccount("6010", "Social Tax Expense (Sotsiaalmaks 33%)", "Expense", "Staff Costs", "Debit"),
    EEGAAPAccount("6020", "Unemployment Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    EEGAAPAccount("6030", "Fringe Benefits (Erisoodustused)", "Expense", "Staff Costs", "Debit"),
    EEGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    EEGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    EEGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    EEGAAPAccount("6200", "State and Registry Fees (Riigilõiv)", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6230", "Telecommunications and IT Services", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6280", "Non-Business Expenses (Taxable, Tulumaks)", "Expense", "Administrative Expenses", "Debit"),
    EEGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    EEGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    EEGAAPAccount("6400", "Income Tax Expense on Distributions (22/78)", "Expense", "Tax Expense", "Debit"),
]
