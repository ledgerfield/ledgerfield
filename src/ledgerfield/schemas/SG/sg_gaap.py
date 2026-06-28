"""Singapore Financial Reporting Standards (SFRS) chart of accounts.

SFRS is aligned with IFRS as issued by the IASB.
CPF = Central Provident Fund (mandatory social security, employer ~17%).
GST = Goods and Services Tax (currently 9%).
CIT = Corporate Income Tax.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SGGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


SG_GAAP: list[SGGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    # Cash and bank
    SGGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    SGGAAPAccount("1020", "OCBC Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SGGAAPAccount("1021", "DBS Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SGGAAPAccount("1022", "UOB Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    SGGAAPAccount("1030", "PayNow / PayLah Float", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Fixed deposits
    SGGAAPAccount("1040", "Fixed Deposits — Current (≤12 months)", "Asset", "Short-term Investments", "Debit"),
    SGGAAPAccount("1041", "Fixed Deposits — Non-current (>12 months)", "Asset", "Long-term Investments", "Debit"),
    # Trade receivables
    SGGAAPAccount("1100", "Accounts Receivable — Trade", "Asset", "Trade Receivables", "Debit"),
    SGGAAPAccount("1101", "Allowance for Doubtful Debts", "Asset", "Trade Receivables", "Credit"),
    SGGAAPAccount("1102", "Accounts Receivable — Related Parties", "Asset", "Trade Receivables", "Debit"),
    # GST
    SGGAAPAccount("1110", "GST Receivable (Input Tax)", "Asset", "Tax Receivables", "Debit"),
    SGGAAPAccount("1111", "GST Claimable — Capital Goods", "Asset", "Tax Receivables", "Debit"),
    # Inventory
    SGGAAPAccount("1200", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    SGGAAPAccount("1201", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    SGGAAPAccount("1202", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    SGGAAPAccount("1203", "Inventory Write-down Allowance", "Asset", "Inventories", "Credit"),
    # Prepayments and other current assets
    SGGAAPAccount("1300", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    SGGAAPAccount("1301", "Prepaid Insurance", "Asset", "Prepayments", "Debit"),
    SGGAAPAccount("1302", "Prepaid Subscriptions / Licences", "Asset", "Prepayments", "Debit"),
    SGGAAPAccount("1310", "Other Current Assets", "Asset", "Other Current Assets", "Debit"),
    SGGAAPAccount("1320", "Loans to Directors / Shareholders", "Asset", "Other Receivables", "Debit"),
    SGGAAPAccount("1330", "Staff Advances", "Asset", "Other Receivables", "Debit"),
    # Property, Plant and Equipment
    SGGAAPAccount("1500", "Land and Buildings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    SGGAAPAccount("1501", "Land and Buildings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    SGGAAPAccount("1510", "Leasehold Improvements — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    SGGAAPAccount("1511", "Leasehold Improvements — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    SGGAAPAccount("1520", "Machinery and Equipment — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    SGGAAPAccount("1521", "Machinery and Equipment — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    SGGAAPAccount("1530", "Furniture and Fittings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    SGGAAPAccount("1531", "Furniture and Fittings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    SGGAAPAccount("1540", "Computer Hardware — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    SGGAAPAccount("1541", "Computer Hardware — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    SGGAAPAccount("1550", "Motor Vehicles — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    SGGAAPAccount("1551", "Motor Vehicles — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    SGGAAPAccount("1560", "Right-of-Use Assets (SFRS(I) 16) — Cost", "Asset", "Right-of-Use Assets", "Debit"),
    SGGAAPAccount("1561", "Right-of-Use Assets — Accumulated Depreciation", "Asset", "Right-of-Use Assets", "Credit"),
    # Intangibles
    SGGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    SGGAAPAccount("1601", "Computer Software — Cost", "Asset", "Intangible Assets", "Debit"),
    SGGAAPAccount("1602", "Computer Software — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    SGGAAPAccount("1603", "Trademarks and Patents — Cost", "Asset", "Intangible Assets", "Debit"),
    SGGAAPAccount("1604", "Trademarks and Patents — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    # Investments
    SGGAAPAccount("1700", "Investments — Equity Securities (FVTPL)", "Asset", "Financial Assets", "Debit"),
    SGGAAPAccount("1701", "Investments — Equity Securities (FVTOCI)", "Asset", "Financial Assets", "Debit"),
    SGGAAPAccount("1702", "Investments — Debt Instruments (Amortised Cost)", "Asset", "Financial Assets", "Debit"),
    SGGAAPAccount("1710", "Investment in Subsidiaries", "Asset", "Financial Assets", "Debit"),
    SGGAAPAccount("1720", "Investment in Associates", "Asset", "Financial Assets", "Debit"),
    # Deferred tax
    SGGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    # Trade payables
    SGGAAPAccount("2010", "Accounts Payable — Trade", "Liability", "Trade Payables", "Credit"),
    SGGAAPAccount("2011", "Accounts Payable — Related Parties", "Liability", "Trade Payables", "Credit"),
    # Tax payables
    SGGAAPAccount("2100", "GST Payable (Output Tax)", "Liability", "Tax Payables", "Credit"),
    SGGAAPAccount("2101", "GST Payable — Imported Services", "Liability", "Tax Payables", "Credit"),
    SGGAAPAccount("2110", "Corporate Income Tax (CIT) Payable", "Liability", "Tax Payables", "Credit"),
    SGGAAPAccount("2111", "Withholding Tax Payable", "Liability", "Tax Payables", "Credit"),
    # CPF and employee
    SGGAAPAccount("2120", "CPF Payable — Employer Contribution", "Liability", "Payroll Payables", "Credit"),
    SGGAAPAccount("2121", "CPF Payable — Employee Contribution", "Liability", "Payroll Payables", "Credit"),
    SGGAAPAccount("2122", "Salaries Payable", "Liability", "Payroll Payables", "Credit"),
    SGGAAPAccount("2123", "SDL Payable (Skills Development Levy)", "Liability", "Payroll Payables", "Credit"),
    # Accruals and other
    SGGAAPAccount("2200", "Accrued Expenses", "Liability", "Accruals", "Credit"),
    SGGAAPAccount("2201", "Accrued Audit Fees", "Liability", "Accruals", "Credit"),
    SGGAAPAccount("2202", "Accrued Bonuses", "Liability", "Accruals", "Credit"),
    SGGAAPAccount("2210", "Deferred Revenue", "Liability", "Deferred Income", "Credit"),
    SGGAAPAccount("2220", "Customer Deposits Received", "Liability", "Other Payables", "Credit"),
    SGGAAPAccount("2230", "Dividends Payable", "Liability", "Other Payables", "Credit"),
    # Loans and lease
    SGGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    SGGAAPAccount("2310", "Bank Loan — Current Portion", "Liability", "Borrowings", "Credit"),
    SGGAAPAccount("2311", "Bank Loan — Non-current Portion", "Liability", "Borrowings", "Credit"),
    SGGAAPAccount("2320", "Director Loan", "Liability", "Borrowings", "Credit"),
    SGGAAPAccount("2330", "Lease Liability — Current (SFRS(I) 16)", "Liability", "Lease Liabilities", "Credit"),
    SGGAAPAccount("2331", "Lease Liability — Non-current (SFRS(I) 16)", "Liability", "Lease Liabilities", "Credit"),
    # Deferred tax
    SGGAAPAccount("2400", "Deferred Tax Liability", "Liability", "Deferred Tax", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    SGGAAPAccount("3010", "Share Capital — Ordinary Shares", "Equity", "Issued Capital", "Credit"),
    SGGAAPAccount("3020", "Share Premium", "Equity", "Issued Capital", "Credit"),
    SGGAAPAccount("3030", "Retained Earnings — Brought Forward", "Equity", "Retained Earnings", "Credit"),
    SGGAAPAccount("3040", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    SGGAAPAccount("3050", "Other Comprehensive Income Reserve", "Equity", "Reserves", "Credit"),
    SGGAAPAccount("3060", "Statutory Reserve", "Equity", "Reserves", "Credit"),
    SGGAAPAccount("3070", "Dividends Declared", "Equity", "Retained Earnings", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    SGGAAPAccount("4010", "Sales of Goods", "Revenue", "Operating Revenue", "Credit"),
    SGGAAPAccount("4011", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    SGGAAPAccount("4020", "Service Revenue", "Revenue", "Operating Revenue", "Credit"),
    SGGAAPAccount("4030", "Rental Income", "Revenue", "Other Income", "Credit"),
    SGGAAPAccount("4040", "Interest Income", "Revenue", "Other Income", "Credit"),
    SGGAAPAccount("4050", "Dividend Income", "Revenue", "Other Income", "Credit"),
    SGGAAPAccount("4060", "Gain on Disposal of Assets", "Revenue", "Other Income", "Credit"),
    SGGAAPAccount("4070", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    SGGAAPAccount("4080", "Government Grants (EDB / ESG / PSG)", "Revenue", "Other Income", "Credit"),
    SGGAAPAccount("4090", "Miscellaneous Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx ────────────────────────────────────────────────────────
    # Cost of sales
    SGGAAPAccount("5010", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    SGGAAPAccount("5020", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    SGGAAPAccount("5030", "Manufacturing Overhead", "Expense", "Cost of Sales", "Debit"),
    # Staff costs
    SGGAAPAccount("5100", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    SGGAAPAccount("5101", "CPF — Employer Contribution", "Expense", "Staff Costs", "Debit"),
    SGGAAPAccount("5102", "Staff Bonuses and AWS", "Expense", "Staff Costs", "Debit"),
    SGGAAPAccount("5103", "Staff Benefits and Medical", "Expense", "Staff Costs", "Debit"),
    SGGAAPAccount("5104", "SDL (Skills Development Levy)", "Expense", "Staff Costs", "Debit"),
    SGGAAPAccount("5105", "Work Permit / EP Fees", "Expense", "Staff Costs", "Debit"),
    SGGAAPAccount("5106", "Staff Training and Development", "Expense", "Staff Costs", "Debit"),
    # Premises
    SGGAAPAccount("5200", "Rent — Operating Lease", "Expense", "Premises Costs", "Debit"),
    SGGAAPAccount("5201", "Depreciation — Right-of-Use Asset", "Expense", "Premises Costs", "Debit"),
    SGGAAPAccount("5202", "Interest on Lease Liability", "Expense", "Finance Costs", "Debit"),
    SGGAAPAccount("5210", "Utilities — Electricity", "Expense", "Premises Costs", "Debit"),
    SGGAAPAccount("5211", "Utilities — Water", "Expense", "Premises Costs", "Debit"),
    SGGAAPAccount("5212", "Maintenance and Repairs", "Expense", "Premises Costs", "Debit"),
    # Professional fees
    SGGAAPAccount("5300", "Audit Fees", "Expense", "Professional Fees", "Debit"),
    SGGAAPAccount("5301", "Tax Agent Fees", "Expense", "Professional Fees", "Debit"),
    SGGAAPAccount("5302", "Legal Fees", "Expense", "Professional Fees", "Debit"),
    SGGAAPAccount("5303", "Company Secretary Fees", "Expense", "Professional Fees", "Debit"),
    SGGAAPAccount("5304", "Consulting Fees", "Expense", "Professional Fees", "Debit"),
    # Depreciation and amortisation
    SGGAAPAccount("5400", "Depreciation — PPE", "Expense", "Depreciation and Amortisation", "Debit"),
    SGGAAPAccount("5401", "Amortisation — Intangibles", "Expense", "Depreciation and Amortisation", "Debit"),
    SGGAAPAccount("5402", "Impairment Loss", "Expense", "Depreciation and Amortisation", "Debit"),
    # Finance costs
    SGGAAPAccount("5500", "Interest Expense — Bank Loans", "Expense", "Finance Costs", "Debit"),
    SGGAAPAccount("5501", "Bank Charges and Fees", "Expense", "Finance Costs", "Debit"),
    # Tax
    SGGAAPAccount("5600", "Corporate Income Tax Expense", "Expense", "Taxation", "Debit"),
    SGGAAPAccount("5601", "Deferred Tax Expense / (Credit)", "Expense", "Taxation", "Debit"),
    # Other operating expenses
    SGGAAPAccount("5700", "Marketing and Advertising", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5701", "Travel and Entertainment", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5702", "IT Subscriptions and SaaS", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5703", "Office Supplies and Stationery", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5704", "Insurance Premiums", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5705", "Foreign Exchange Loss", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5706", "Bad Debt Written Off", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5707", "Charitable Donations (IRAS-approved IPC)", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5708", "Telecommunication Expenses", "Expense", "Other Operating Expenses", "Debit"),
    SGGAAPAccount("5709", "Miscellaneous Expenses", "Expense", "Other Operating Expenses", "Debit"),
]
