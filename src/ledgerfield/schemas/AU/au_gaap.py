"""Australia AASB (Australian Accounting Standards Board) chart of accounts.

AASB is aligned with IFRS as adopted by Australia.
GST = Goods and Services Tax (10%).
Super = Superannuation Guarantee (12% from 1 July 2025).
CIT = Corporate Income Tax (25% base rate / 30% general rate).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AUGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AU_GAAP: list[AUGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    # Cash and bank
    AUGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    AUGAAPAccount("1020", "Commonwealth Bank Cheque Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AUGAAPAccount("1021", "ANZ Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AUGAAPAccount("1022", "NAB Business Transaction Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AUGAAPAccount("1023", "Westpac Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    AUGAAPAccount("1030", "PayID / OSKO Float", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Term deposits
    AUGAAPAccount("1040", "Term Deposits — Current (<=12 months)", "Asset", "Short-term Investments", "Debit"),
    AUGAAPAccount("1041", "Term Deposits — Non-current (>12 months)", "Asset", "Long-term Investments", "Debit"),
    # Trade receivables
    AUGAAPAccount("1100", "Accounts Receivable — Trade", "Asset", "Trade Receivables", "Debit"),
    AUGAAPAccount("1101", "Allowance for Doubtful Debts", "Asset", "Trade Receivables", "Credit"),
    AUGAAPAccount("1102", "Accounts Receivable — Related Parties", "Asset", "Trade Receivables", "Debit"),
    # GST
    AUGAAPAccount("1110", "GST Receivable (Input Tax Credits)", "Asset", "Tax Receivables", "Debit"),
    AUGAAPAccount("1111", "GST Claimable — Capital Acquisitions", "Asset", "Tax Receivables", "Debit"),
    # Inventory
    AUGAAPAccount("1200", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    AUGAAPAccount("1201", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    AUGAAPAccount("1202", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    AUGAAPAccount("1203", "Inventory Write-down Provision", "Asset", "Inventories", "Credit"),
    # Prepayments and other current assets
    AUGAAPAccount("1300", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    AUGAAPAccount("1301", "Prepaid Insurance", "Asset", "Prepayments", "Debit"),
    AUGAAPAccount("1302", "Prepaid Subscriptions / Licences", "Asset", "Prepayments", "Debit"),
    AUGAAPAccount("1310", "Other Current Assets", "Asset", "Other Current Assets", "Debit"),
    AUGAAPAccount("1320", "Loans to Directors / Shareholders", "Asset", "Other Receivables", "Debit"),
    AUGAAPAccount("1330", "Staff Advances", "Asset", "Other Receivables", "Debit"),
    AUGAAPAccount("1340", "R&D Tax Offset Receivable", "Asset", "Tax Receivables", "Debit"),
    # Property, Plant and Equipment
    AUGAAPAccount("1500", "Land and Buildings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    AUGAAPAccount("1501", "Land and Buildings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    AUGAAPAccount("1510", "Leasehold Improvements — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    AUGAAPAccount("1511", "Leasehold Improvements — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    AUGAAPAccount("1520", "Machinery and Equipment — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    AUGAAPAccount("1521", "Machinery and Equipment — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    AUGAAPAccount("1530", "Furniture and Fittings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    AUGAAPAccount("1531", "Furniture and Fittings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    AUGAAPAccount("1540", "Computer Hardware — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    AUGAAPAccount("1541", "Computer Hardware — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    AUGAAPAccount("1550", "Motor Vehicles — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    AUGAAPAccount("1551", "Motor Vehicles — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    AUGAAPAccount("1560", "Right-of-Use Assets (AASB 16) — Cost", "Asset", "Right-of-Use Assets", "Debit"),
    AUGAAPAccount("1561", "Right-of-Use Assets — Accumulated Depreciation", "Asset", "Right-of-Use Assets", "Credit"),
    # Intangibles
    AUGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    AUGAAPAccount("1601", "Computer Software — Cost", "Asset", "Intangible Assets", "Debit"),
    AUGAAPAccount("1602", "Computer Software — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    AUGAAPAccount("1603", "Trademarks and Patents — Cost", "Asset", "Intangible Assets", "Debit"),
    AUGAAPAccount("1604", "Trademarks and Patents — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    # Investments
    AUGAAPAccount("1700", "Investments — Equity Securities (FVTPL)", "Asset", "Financial Assets", "Debit"),
    AUGAAPAccount("1701", "Investments — Equity Securities (FVTOCI)", "Asset", "Financial Assets", "Debit"),
    AUGAAPAccount("1702", "Investments — Debt Instruments (Amortised Cost)", "Asset", "Financial Assets", "Debit"),
    AUGAAPAccount("1710", "Investment in Subsidiaries", "Asset", "Financial Assets", "Debit"),
    AUGAAPAccount("1720", "Investment in Associates", "Asset", "Financial Assets", "Debit"),
    # Deferred tax
    AUGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    # Trade payables
    AUGAAPAccount("2010", "Accounts Payable — Trade", "Liability", "Trade Payables", "Credit"),
    AUGAAPAccount("2011", "Accounts Payable — Related Parties", "Liability", "Trade Payables", "Credit"),
    # Tax payables
    AUGAAPAccount("2100", "GST Payable (Output Tax)", "Liability", "Tax Payables", "Credit"),
    AUGAAPAccount("2110", "Corporate Income Tax (CIT) Payable", "Liability", "Tax Payables", "Credit"),
    AUGAAPAccount("2111", "PAYG Withholding Payable", "Liability", "Tax Payables", "Credit"),
    AUGAAPAccount("2112", "Fringe Benefits Tax Payable", "Liability", "Tax Payables", "Credit"),
    # Superannuation and payroll
    AUGAAPAccount("2120", "Superannuation Payable — Employer", "Liability", "Payroll Payables", "Credit"),
    AUGAAPAccount("2121", "Salaries and Wages Payable", "Liability", "Payroll Payables", "Credit"),
    AUGAAPAccount("2122", "Annual Leave Accrual", "Liability", "Employee Entitlements", "Credit"),
    AUGAAPAccount("2123", "Long Service Leave Accrual", "Liability", "Employee Entitlements", "Credit"),
    AUGAAPAccount("2124", "PAYG Withholding — Employee Tax", "Liability", "Payroll Payables", "Credit"),
    # Accruals and other
    AUGAAPAccount("2200", "Accrued Expenses", "Liability", "Accruals", "Credit"),
    AUGAAPAccount("2201", "Accrued Audit Fees", "Liability", "Accruals", "Credit"),
    AUGAAPAccount("2202", "Accrued Bonuses", "Liability", "Accruals", "Credit"),
    AUGAAPAccount("2210", "Deferred Revenue", "Liability", "Deferred Income", "Credit"),
    AUGAAPAccount("2220", "Customer Deposits Received", "Liability", "Other Payables", "Credit"),
    AUGAAPAccount("2230", "Dividends Payable", "Liability", "Other Payables", "Credit"),
    # Loans and lease
    AUGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    AUGAAPAccount("2310", "Bank Loan — Current Portion", "Liability", "Borrowings", "Credit"),
    AUGAAPAccount("2311", "Bank Loan — Non-current Portion", "Liability", "Borrowings", "Credit"),
    AUGAAPAccount("2320", "Director Loan", "Liability", "Borrowings", "Credit"),
    AUGAAPAccount("2330", "Lease Liability — Current (AASB 16)", "Liability", "Lease Liabilities", "Credit"),
    AUGAAPAccount("2331", "Lease Liability — Non-current (AASB 16)", "Liability", "Lease Liabilities", "Credit"),
    # Deferred tax
    AUGAAPAccount("2400", "Deferred Tax Liability", "Liability", "Deferred Tax", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    AUGAAPAccount("3010", "Share Capital — Ordinary Shares", "Equity", "Issued Capital", "Credit"),
    AUGAAPAccount("3020", "Share Premium", "Equity", "Issued Capital", "Credit"),
    AUGAAPAccount("3030", "Retained Earnings — Brought Forward", "Equity", "Retained Earnings", "Credit"),
    AUGAAPAccount("3040", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    AUGAAPAccount("3050", "Other Comprehensive Income Reserve", "Equity", "Reserves", "Credit"),
    AUGAAPAccount("3060", "Asset Revaluation Reserve", "Equity", "Reserves", "Credit"),
    AUGAAPAccount("3070", "Dividends Declared", "Equity", "Retained Earnings", "Debit"),
    AUGAAPAccount("3080", "Franking Credits Reserve", "Equity", "Reserves", "Credit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    AUGAAPAccount("4010", "Sales of Goods", "Revenue", "Operating Revenue", "Credit"),
    AUGAAPAccount("4011", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    AUGAAPAccount("4020", "Service Revenue", "Revenue", "Operating Revenue", "Credit"),
    AUGAAPAccount("4030", "Rental Income", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4040", "Interest Income", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4050", "Dividend Income (Unfranked)", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4051", "Dividend Income (Franked)", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4052", "Franking Credits on Dividends", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4060", "Gain on Disposal of Assets", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4070", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4080", "Government Grants (AusIndustry / EMDG)", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4090", "R&D Tax Offset Income", "Revenue", "Other Income", "Credit"),
    AUGAAPAccount("4100", "Miscellaneous Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx ────────────────────────────────────────────────────────
    # Cost of sales
    AUGAAPAccount("5010", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    AUGAAPAccount("5020", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    AUGAAPAccount("5030", "Manufacturing Overhead", "Expense", "Cost of Sales", "Debit"),
    # Staff costs
    AUGAAPAccount("5100", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5101", "Superannuation — Employer Contributions", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5102", "Staff Bonuses", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5103", "Staff Benefits and Medical", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5104", "Workers Compensation Insurance", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5105", "Payroll Tax", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5106", "Staff Training and Development", "Expense", "Staff Costs", "Debit"),
    AUGAAPAccount("5107", "Fringe Benefits Tax", "Expense", "Staff Costs", "Debit"),
    # Premises
    AUGAAPAccount("5200", "Rent — Operating Lease", "Expense", "Premises Costs", "Debit"),
    AUGAAPAccount("5201", "Depreciation — Right-of-Use Asset", "Expense", "Premises Costs", "Debit"),
    AUGAAPAccount("5202", "Interest on Lease Liability", "Expense", "Finance Costs", "Debit"),
    AUGAAPAccount("5210", "Utilities — Electricity", "Expense", "Premises Costs", "Debit"),
    AUGAAPAccount("5211", "Utilities — Gas and Water", "Expense", "Premises Costs", "Debit"),
    AUGAAPAccount("5212", "Maintenance and Repairs", "Expense", "Premises Costs", "Debit"),
    # Professional fees
    AUGAAPAccount("5300", "Audit Fees", "Expense", "Professional Fees", "Debit"),
    AUGAAPAccount("5301", "Tax Agent Fees", "Expense", "Professional Fees", "Debit"),
    AUGAAPAccount("5302", "Legal Fees", "Expense", "Professional Fees", "Debit"),
    AUGAAPAccount("5303", "Company Secretary Fees", "Expense", "Professional Fees", "Debit"),
    AUGAAPAccount("5304", "Consulting Fees", "Expense", "Professional Fees", "Debit"),
    # Depreciation and amortisation
    AUGAAPAccount("5400", "Depreciation — PPE", "Expense", "Depreciation and Amortisation", "Debit"),
    AUGAAPAccount("5401", "Amortisation — Intangibles", "Expense", "Depreciation and Amortisation", "Debit"),
    AUGAAPAccount("5402", "Impairment Loss", "Expense", "Depreciation and Amortisation", "Debit"),
    # Finance costs
    AUGAAPAccount("5500", "Interest Expense — Bank Loans", "Expense", "Finance Costs", "Debit"),
    AUGAAPAccount("5501", "Bank Charges and Fees", "Expense", "Finance Costs", "Debit"),
    # Tax
    AUGAAPAccount("5600", "Corporate Income Tax Expense", "Expense", "Taxation", "Debit"),
    AUGAAPAccount("5601", "Deferred Tax Expense / (Credit)", "Expense", "Taxation", "Debit"),
    # Other operating expenses
    AUGAAPAccount("5700", "Marketing and Advertising", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5701", "Travel and Entertainment", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5702", "IT Subscriptions and SaaS", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5703", "Office Supplies and Stationery", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5704", "Insurance Premiums", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5705", "Foreign Exchange Loss", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5706", "Bad Debt Written Off", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5707", "Charitable Donations (DGR)", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5708", "Telecommunication Expenses", "Expense", "Other Operating Expenses", "Debit"),
    AUGAAPAccount("5709", "Miscellaneous Expenses", "Expense", "Other Operating Expenses", "Debit"),
]
