"""New Zealand NZ IFRS / NZ GAAP chart of accounts.

NZ IFRS = New Zealand equivalents to IFRS (issued by XRB / NZASB).
NZ GAAP = for-profit entities applying NZ IFRS; not-for-profit use PBE standards.
GST = Goods and Services Tax (15%).
KiwiSaver = employer contributions (employer minimum 3%).
CIT = Corporate Income Tax (28% flat rate).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class NZGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


NZ_GAAP: list[NZGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    # Cash and bank
    NZGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    NZGAAPAccount("1020", "ASB Bank — Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NZGAAPAccount("1021", "ANZ Business Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NZGAAPAccount("1022", "BNZ Business Transaction Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NZGAAPAccount("1023", "Westpac Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    NZGAAPAccount("1030", "PayNow / EFTPOS Float", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Term deposits
    NZGAAPAccount("1040", "Term Deposits — Current (<=12 months)", "Asset", "Short-term Investments", "Debit"),
    NZGAAPAccount("1041", "Term Deposits — Non-current (>12 months)", "Asset", "Long-term Investments", "Debit"),
    # Trade receivables
    NZGAAPAccount("1100", "Accounts Receivable — Trade", "Asset", "Trade Receivables", "Debit"),
    NZGAAPAccount("1101", "Allowance for Doubtful Debts", "Asset", "Trade Receivables", "Credit"),
    NZGAAPAccount("1102", "Accounts Receivable — Related Parties", "Asset", "Trade Receivables", "Debit"),
    # GST
    NZGAAPAccount("1110", "GST Receivable (Input Tax Credits)", "Asset", "Tax Receivables", "Debit"),
    NZGAAPAccount("1111", "GST Claimable — Capital Purchases", "Asset", "Tax Receivables", "Debit"),
    # Inventory
    NZGAAPAccount("1200", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    NZGAAPAccount("1201", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    NZGAAPAccount("1202", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    NZGAAPAccount("1203", "Inventory Write-down Provision", "Asset", "Inventories", "Credit"),
    # Prepayments and other current assets
    NZGAAPAccount("1300", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    NZGAAPAccount("1301", "Prepaid Insurance", "Asset", "Prepayments", "Debit"),
    NZGAAPAccount("1302", "Prepaid Subscriptions / Licences", "Asset", "Prepayments", "Debit"),
    NZGAAPAccount("1310", "Other Current Assets", "Asset", "Other Current Assets", "Debit"),
    NZGAAPAccount("1320", "Loans to Directors / Shareholders", "Asset", "Other Receivables", "Debit"),
    NZGAAPAccount("1330", "Staff Advances", "Asset", "Other Receivables", "Debit"),
    NZGAAPAccount("1340", "R&D Tax Credit Receivable", "Asset", "Tax Receivables", "Debit"),
    # Property, Plant and Equipment
    NZGAAPAccount("1500", "Land and Buildings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    NZGAAPAccount("1501", "Land and Buildings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    NZGAAPAccount("1510", "Leasehold Improvements — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    NZGAAPAccount("1511", "Leasehold Improvements — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    NZGAAPAccount("1520", "Machinery and Equipment — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    NZGAAPAccount("1521", "Machinery and Equipment — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    NZGAAPAccount("1530", "Furniture and Fittings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    NZGAAPAccount("1531", "Furniture and Fittings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    NZGAAPAccount("1540", "Computer Hardware — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    NZGAAPAccount("1541", "Computer Hardware — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    NZGAAPAccount("1550", "Motor Vehicles — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    NZGAAPAccount("1551", "Motor Vehicles — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    NZGAAPAccount("1560", "Right-of-Use Assets (NZ IFRS 16) — Cost", "Asset", "Right-of-Use Assets", "Debit"),
    NZGAAPAccount("1561", "Right-of-Use Assets — Accumulated Depreciation", "Asset", "Right-of-Use Assets", "Credit"),
    # Intangibles
    NZGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    NZGAAPAccount("1601", "Computer Software — Cost", "Asset", "Intangible Assets", "Debit"),
    NZGAAPAccount("1602", "Computer Software — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    NZGAAPAccount("1603", "Trademarks and Patents — Cost", "Asset", "Intangible Assets", "Debit"),
    NZGAAPAccount("1604", "Trademarks and Patents — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    # Investments
    NZGAAPAccount("1700", "Investments — Equity Securities (FVTPL)", "Asset", "Financial Assets", "Debit"),
    NZGAAPAccount("1701", "Investments — Equity Securities (FVTOCI)", "Asset", "Financial Assets", "Debit"),
    NZGAAPAccount("1702", "Investments — Debt Instruments (Amortised Cost)", "Asset", "Financial Assets", "Debit"),
    NZGAAPAccount("1710", "Investment in Subsidiaries", "Asset", "Financial Assets", "Debit"),
    NZGAAPAccount("1720", "Investment in Associates", "Asset", "Financial Assets", "Debit"),
    # Deferred tax
    NZGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    # Trade payables
    NZGAAPAccount("2010", "Accounts Payable — Trade", "Liability", "Trade Payables", "Credit"),
    NZGAAPAccount("2011", "Accounts Payable — Related Parties", "Liability", "Trade Payables", "Credit"),
    # Tax payables
    NZGAAPAccount("2100", "GST Payable (Output Tax)", "Liability", "Tax Payables", "Credit"),
    NZGAAPAccount("2110", "Corporate Income Tax (CIT) Payable", "Liability", "Tax Payables", "Credit"),
    NZGAAPAccount("2111", "PAYE Withholding Payable", "Liability", "Tax Payables", "Credit"),
    NZGAAPAccount("2112", "FBT (Fringe Benefit Tax) Payable", "Liability", "Tax Payables", "Credit"),
    # KiwiSaver and payroll
    NZGAAPAccount("2120", "KiwiSaver Payable — Employer Contributions", "Liability", "Payroll Payables", "Credit"),
    NZGAAPAccount("2121", "Salaries and Wages Payable", "Liability", "Payroll Payables", "Credit"),
    NZGAAPAccount("2122", "Annual Leave Accrual", "Liability", "Employee Entitlements", "Credit"),
    NZGAAPAccount("2123", "Long Service Leave Accrual", "Liability", "Employee Entitlements", "Credit"),
    NZGAAPAccount("2124", "PAYE Withholding — Employee Tax", "Liability", "Payroll Payables", "Credit"),
    # Accruals and other
    NZGAAPAccount("2200", "Accrued Expenses", "Liability", "Accruals", "Credit"),
    NZGAAPAccount("2201", "Accrued Audit Fees", "Liability", "Accruals", "Credit"),
    NZGAAPAccount("2202", "Accrued Bonuses", "Liability", "Accruals", "Credit"),
    NZGAAPAccount("2210", "Deferred Revenue", "Liability", "Deferred Income", "Credit"),
    NZGAAPAccount("2220", "Customer Deposits Received", "Liability", "Other Payables", "Credit"),
    NZGAAPAccount("2230", "Dividends Payable", "Liability", "Other Payables", "Credit"),
    # Loans and lease
    NZGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    NZGAAPAccount("2310", "Bank Loan — Current Portion", "Liability", "Borrowings", "Credit"),
    NZGAAPAccount("2311", "Bank Loan — Non-current Portion", "Liability", "Borrowings", "Credit"),
    NZGAAPAccount("2320", "Director Loan", "Liability", "Borrowings", "Credit"),
    NZGAAPAccount("2330", "Lease Liability — Current (NZ IFRS 16)", "Liability", "Lease Liabilities", "Credit"),
    NZGAAPAccount("2331", "Lease Liability — Non-current (NZ IFRS 16)", "Liability", "Lease Liabilities", "Credit"),
    # Deferred tax
    NZGAAPAccount("2400", "Deferred Tax Liability", "Liability", "Deferred Tax", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    NZGAAPAccount("3010", "Share Capital — Ordinary Shares", "Equity", "Issued Capital", "Credit"),
    NZGAAPAccount("3020", "Share Premium", "Equity", "Issued Capital", "Credit"),
    NZGAAPAccount("3030", "Retained Earnings — Brought Forward", "Equity", "Retained Earnings", "Credit"),
    NZGAAPAccount("3040", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    NZGAAPAccount("3050", "Other Comprehensive Income Reserve", "Equity", "Reserves", "Credit"),
    NZGAAPAccount("3060", "Asset Revaluation Reserve", "Equity", "Reserves", "Credit"),
    NZGAAPAccount("3070", "Dividends Declared", "Equity", "Retained Earnings", "Debit"),
    NZGAAPAccount("3080", "Imputation Credits Reserve", "Equity", "Reserves", "Credit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    NZGAAPAccount("4010", "Sales of Goods", "Revenue", "Operating Revenue", "Credit"),
    NZGAAPAccount("4011", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    NZGAAPAccount("4020", "Service Revenue", "Revenue", "Operating Revenue", "Credit"),
    NZGAAPAccount("4030", "Rental Income", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4040", "Interest Income", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4050", "Dividend Income", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4060", "Gain on Disposal of Assets", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4070", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4080", "Government Grants (Callaghan Innovation / NZTE)", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4090", "R&D Tax Credit Income", "Revenue", "Other Income", "Credit"),
    NZGAAPAccount("4100", "Miscellaneous Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx ────────────────────────────────────────────────────────
    # Cost of sales
    NZGAAPAccount("5010", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    NZGAAPAccount("5020", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    NZGAAPAccount("5030", "Manufacturing Overhead", "Expense", "Cost of Sales", "Debit"),
    # Staff costs
    NZGAAPAccount("5100", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5101", "KiwiSaver — Employer Contributions (min 3%)", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5102", "Staff Bonuses", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5103", "Staff Benefits and Medical", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5104", "ACC Employer Levy", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5105", "Payroll Tax (Auckland / Wellington EI Levies)", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5106", "Staff Training and Development", "Expense", "Staff Costs", "Debit"),
    NZGAAPAccount("5107", "Fringe Benefit Tax (FBT)", "Expense", "Staff Costs", "Debit"),
    # Premises
    NZGAAPAccount("5200", "Rent — Operating Lease", "Expense", "Premises Costs", "Debit"),
    NZGAAPAccount("5201", "Depreciation — Right-of-Use Asset", "Expense", "Premises Costs", "Debit"),
    NZGAAPAccount("5202", "Interest on Lease Liability", "Expense", "Finance Costs", "Debit"),
    NZGAAPAccount("5210", "Utilities — Electricity", "Expense", "Premises Costs", "Debit"),
    NZGAAPAccount("5211", "Utilities — Gas and Water", "Expense", "Premises Costs", "Debit"),
    NZGAAPAccount("5212", "Maintenance and Repairs", "Expense", "Premises Costs", "Debit"),
    # Professional fees
    NZGAAPAccount("5300", "Audit Fees", "Expense", "Professional Fees", "Debit"),
    NZGAAPAccount("5301", "Tax Agent Fees", "Expense", "Professional Fees", "Debit"),
    NZGAAPAccount("5302", "Legal Fees", "Expense", "Professional Fees", "Debit"),
    NZGAAPAccount("5303", "Company Secretary Fees", "Expense", "Professional Fees", "Debit"),
    NZGAAPAccount("5304", "Consulting Fees", "Expense", "Professional Fees", "Debit"),
    # Depreciation and amortisation
    NZGAAPAccount("5400", "Depreciation — PPE", "Expense", "Depreciation and Amortisation", "Debit"),
    NZGAAPAccount("5401", "Amortisation — Intangibles", "Expense", "Depreciation and Amortisation", "Debit"),
    NZGAAPAccount("5402", "Impairment Loss", "Expense", "Depreciation and Amortisation", "Debit"),
    # Finance costs
    NZGAAPAccount("5500", "Interest Expense — Bank Loans", "Expense", "Finance Costs", "Debit"),
    NZGAAPAccount("5501", "Bank Charges and Fees", "Expense", "Finance Costs", "Debit"),
    # Tax
    NZGAAPAccount("5600", "Corporate Income Tax Expense", "Expense", "Taxation", "Debit"),
    NZGAAPAccount("5601", "Deferred Tax Expense / (Credit)", "Expense", "Taxation", "Debit"),
    # Other operating expenses
    NZGAAPAccount("5700", "Marketing and Advertising", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5701", "Travel and Entertainment", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5702", "IT Subscriptions and SaaS", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5703", "Office Supplies and Stationery", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5704", "Insurance Premiums", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5705", "Foreign Exchange Loss", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5706", "Bad Debt Written Off", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5707", "Charitable Donations", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5708", "Telecommunication Expenses", "Expense", "Other Operating Expenses", "Debit"),
    NZGAAPAccount("5709", "Miscellaneous Expenses", "Expense", "Other Operating Expenses", "Debit"),
]
