"""South Africa SA GAAP (IFRS) chart of accounts.

SA GAAP is fully converged with IFRS. Currency: ZAR (South African Rand).
CIT = 27% (reduced from 28% effective 1 April 2022).
VAT = 15% (standard rate); some supplies zero-rated or exempt.
Dividends Tax = 20% (withheld at source by company paying dividend).
SDL = Skills Development Levy (1% of leviable amount, SARS administered).
UIF = Unemployment Insurance Fund (1% employer + 1% employee).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ZAGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


ZA_GAAP: list[ZAGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    # Cash and bank
    ZAGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZAGAAPAccount("1020", "Standard Bank — Business Current Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZAGAAPAccount("1021", "ABSA Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZAGAAPAccount("1022", "FNB Business Cheque Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZAGAAPAccount("1023", "Nedbank Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZAGAAPAccount("1024", "Capitec Business Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    ZAGAAPAccount("1030", "Petty Cash Float", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Fixed deposits
    ZAGAAPAccount("1040", "Fixed Deposits — Current (<=12 months)", "Asset", "Short-term Investments", "Debit"),
    ZAGAAPAccount("1041", "Fixed Deposits — Non-current (>12 months)", "Asset", "Long-term Investments", "Debit"),
    # Trade receivables
    ZAGAAPAccount("1100", "Accounts Receivable — Trade", "Asset", "Trade Receivables", "Debit"),
    ZAGAAPAccount("1101", "Allowance for Credit Losses (IFRS 9 ECL)", "Asset", "Trade Receivables", "Credit"),
    ZAGAAPAccount("1102", "Accounts Receivable — Related Parties", "Asset", "Trade Receivables", "Debit"),
    # VAT
    ZAGAAPAccount("1110", "VAT Input (Receivable from SARS)", "Asset", "Tax Receivables", "Debit"),
    ZAGAAPAccount("1111", "VAT Input — Capital Goods", "Asset", "Tax Receivables", "Debit"),
    # Inventory
    ZAGAAPAccount("1200", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    ZAGAAPAccount("1201", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    ZAGAAPAccount("1202", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    ZAGAAPAccount("1203", "Inventory Write-down Provision", "Asset", "Inventories", "Credit"),
    # Prepayments and other current assets
    ZAGAAPAccount("1300", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    ZAGAAPAccount("1301", "Prepaid Insurance", "Asset", "Prepayments", "Debit"),
    ZAGAAPAccount("1302", "Prepaid Subscriptions / Licences", "Asset", "Prepayments", "Debit"),
    ZAGAAPAccount("1310", "Other Current Assets", "Asset", "Other Current Assets", "Debit"),
    ZAGAAPAccount("1320", "Loans to Directors / Shareholders", "Asset", "Other Receivables", "Debit"),
    ZAGAAPAccount("1330", "Staff Advances", "Asset", "Other Receivables", "Debit"),
    ZAGAAPAccount("1340", "SIC (Section 12J / R&D) Tax Credit Receivable", "Asset", "Tax Receivables", "Debit"),
    # Property, Plant and Equipment
    ZAGAAPAccount("1500", "Land and Buildings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    ZAGAAPAccount("1501", "Land and Buildings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    ZAGAAPAccount("1510", "Leasehold Improvements — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    ZAGAAPAccount("1511", "Leasehold Improvements — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    ZAGAAPAccount("1520", "Machinery and Equipment — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    ZAGAAPAccount("1521", "Machinery and Equipment — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    ZAGAAPAccount("1530", "Furniture and Fittings — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    ZAGAAPAccount("1531", "Furniture and Fittings — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    ZAGAAPAccount("1540", "Computer Hardware — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    ZAGAAPAccount("1541", "Computer Hardware — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    ZAGAAPAccount("1550", "Motor Vehicles — Cost", "Asset", "Property Plant and Equipment", "Debit"),
    ZAGAAPAccount("1551", "Motor Vehicles — Accumulated Depreciation", "Asset", "Property Plant and Equipment", "Credit"),
    ZAGAAPAccount("1560", "Right-of-Use Assets (IFRS 16) — Cost", "Asset", "Right-of-Use Assets", "Debit"),
    ZAGAAPAccount("1561", "Right-of-Use Assets — Accumulated Depreciation", "Asset", "Right-of-Use Assets", "Credit"),
    # Intangibles
    ZAGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    ZAGAAPAccount("1601", "Computer Software — Cost", "Asset", "Intangible Assets", "Debit"),
    ZAGAAPAccount("1602", "Computer Software — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    ZAGAAPAccount("1603", "Trademarks and Patents — Cost", "Asset", "Intangible Assets", "Debit"),
    ZAGAAPAccount("1604", "Trademarks and Patents — Accumulated Amortisation", "Asset", "Intangible Assets", "Credit"),
    # Investments
    ZAGAAPAccount("1700", "Investments — Equity Securities (FVTPL)", "Asset", "Financial Assets", "Debit"),
    ZAGAAPAccount("1701", "Investments — Equity Securities (FVTOCI)", "Asset", "Financial Assets", "Debit"),
    ZAGAAPAccount("1702", "Investments — Debt Instruments (Amortised Cost)", "Asset", "Financial Assets", "Debit"),
    ZAGAAPAccount("1710", "Investment in Subsidiaries", "Asset", "Financial Assets", "Debit"),
    ZAGAAPAccount("1720", "Investment in Associates", "Asset", "Financial Assets", "Debit"),
    # Deferred tax
    ZAGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    # Trade payables
    ZAGAAPAccount("2010", "Accounts Payable — Trade", "Liability", "Trade Payables", "Credit"),
    ZAGAAPAccount("2011", "Accounts Payable — Related Parties", "Liability", "Trade Payables", "Credit"),
    # Tax payables
    ZAGAAPAccount("2100", "VAT Output (Payable to SARS)", "Liability", "Tax Payables", "Credit"),
    ZAGAAPAccount("2110", "Corporate Income Tax (CIT) Payable", "Liability", "Tax Payables", "Credit"),
    ZAGAAPAccount("2111", "PAYE Withholding Payable", "Liability", "Tax Payables", "Credit"),
    ZAGAAPAccount("2112", "Dividends Tax Payable (20%)", "Liability", "Tax Payables", "Credit"),
    ZAGAAPAccount("2113", "Provisional Tax (IRP6) Payable", "Liability", "Tax Payables", "Credit"),
    # Payroll
    ZAGAAPAccount("2120", "UIF Payable — Employer Contribution (1%)", "Liability", "Payroll Payables", "Credit"),
    ZAGAAPAccount("2121", "UIF Payable — Employee Contribution (1%)", "Liability", "Payroll Payables", "Credit"),
    ZAGAAPAccount("2122", "SDL Payable — Skills Development Levy (1%)", "Liability", "Payroll Payables", "Credit"),
    ZAGAAPAccount("2123", "Salaries and Wages Payable", "Liability", "Payroll Payables", "Credit"),
    ZAGAAPAccount("2124", "Annual Leave Accrual", "Liability", "Employee Entitlements", "Credit"),
    # Accruals and other
    ZAGAAPAccount("2200", "Accrued Expenses", "Liability", "Accruals", "Credit"),
    ZAGAAPAccount("2201", "Accrued Audit Fees", "Liability", "Accruals", "Credit"),
    ZAGAAPAccount("2202", "Accrued Bonuses", "Liability", "Accruals", "Credit"),
    ZAGAAPAccount("2210", "Deferred Revenue", "Liability", "Deferred Income", "Credit"),
    ZAGAAPAccount("2220", "Customer Deposits Received", "Liability", "Other Payables", "Credit"),
    ZAGAAPAccount("2230", "Dividends Payable", "Liability", "Other Payables", "Credit"),
    # Loans and lease
    ZAGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    ZAGAAPAccount("2310", "Bank Loan — Current Portion", "Liability", "Borrowings", "Credit"),
    ZAGAAPAccount("2311", "Bank Loan — Non-current Portion", "Liability", "Borrowings", "Credit"),
    ZAGAAPAccount("2320", "Director Loan", "Liability", "Borrowings", "Credit"),
    ZAGAAPAccount("2330", "Lease Liability — Current (IFRS 16)", "Liability", "Lease Liabilities", "Credit"),
    ZAGAAPAccount("2331", "Lease Liability — Non-current (IFRS 16)", "Liability", "Lease Liabilities", "Credit"),
    # Deferred tax
    ZAGAAPAccount("2400", "Deferred Tax Liability", "Liability", "Deferred Tax", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ZAGAAPAccount("3010", "Share Capital — Ordinary Shares", "Equity", "Issued Capital", "Credit"),
    ZAGAAPAccount("3020", "Share Premium", "Equity", "Issued Capital", "Credit"),
    ZAGAAPAccount("3030", "Retained Earnings — Brought Forward", "Equity", "Retained Earnings", "Credit"),
    ZAGAAPAccount("3040", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    ZAGAAPAccount("3050", "Other Comprehensive Income Reserve", "Equity", "Reserves", "Credit"),
    ZAGAAPAccount("3060", "Asset Revaluation Surplus (IFRS)", "Equity", "Reserves", "Credit"),
    ZAGAAPAccount("3070", "Dividends Declared", "Equity", "Retained Earnings", "Debit"),
    ZAGAAPAccount("3080", "Foreign Currency Translation Reserve", "Equity", "Reserves", "Credit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ZAGAAPAccount("4010", "Sales of Goods", "Revenue", "Operating Revenue", "Credit"),
    ZAGAAPAccount("4011", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    ZAGAAPAccount("4020", "Service Revenue", "Revenue", "Operating Revenue", "Credit"),
    ZAGAAPAccount("4030", "Rental Income", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4040", "Interest Income", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4050", "Dividend Income (received)", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4060", "Gain on Disposal of Assets", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4070", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4080", "Government Grants (DTI / SEDA / IDC)", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4090", "R&D Tax Incentive Income (s11D)", "Revenue", "Other Income", "Credit"),
    ZAGAAPAccount("4100", "Miscellaneous Income", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx ────────────────────────────────────────────────────────
    # Cost of sales
    ZAGAAPAccount("5010", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    ZAGAAPAccount("5020", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    ZAGAAPAccount("5030", "Manufacturing Overhead", "Expense", "Cost of Sales", "Debit"),
    # Staff costs
    ZAGAAPAccount("5100", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    ZAGAAPAccount("5101", "UIF — Employer Contribution (1%)", "Expense", "Staff Costs", "Debit"),
    ZAGAAPAccount("5102", "SDL — Skills Development Levy (1%)", "Expense", "Staff Costs", "Debit"),
    ZAGAAPAccount("5103", "Staff Bonuses", "Expense", "Staff Costs", "Debit"),
    ZAGAAPAccount("5104", "Staff Benefits and Medical Aid", "Expense", "Staff Costs", "Debit"),
    ZAGAAPAccount("5105", "Staff Training (Section 12H)", "Expense", "Staff Costs", "Debit"),
    ZAGAAPAccount("5106", "Fringe Benefits Tax (deemed FBT)", "Expense", "Staff Costs", "Debit"),
    # Premises
    ZAGAAPAccount("5200", "Rent — Operating Lease", "Expense", "Premises Costs", "Debit"),
    ZAGAAPAccount("5201", "Depreciation — Right-of-Use Asset (IFRS 16)", "Expense", "Premises Costs", "Debit"),
    ZAGAAPAccount("5202", "Interest on Lease Liability", "Expense", "Finance Costs", "Debit"),
    ZAGAAPAccount("5210", "Utilities — Electricity (Eskom)", "Expense", "Premises Costs", "Debit"),
    ZAGAAPAccount("5211", "Utilities — Water and Sanitation", "Expense", "Premises Costs", "Debit"),
    ZAGAAPAccount("5212", "Maintenance and Repairs", "Expense", "Premises Costs", "Debit"),
    # Professional fees
    ZAGAAPAccount("5300", "Audit Fees", "Expense", "Professional Fees", "Debit"),
    ZAGAAPAccount("5301", "Tax Practitioner Fees", "Expense", "Professional Fees", "Debit"),
    ZAGAAPAccount("5302", "Legal Fees", "Expense", "Professional Fees", "Debit"),
    ZAGAAPAccount("5303", "CIPC / Company Secretarial Fees", "Expense", "Professional Fees", "Debit"),
    ZAGAAPAccount("5304", "Consulting Fees", "Expense", "Professional Fees", "Debit"),
    # Depreciation and amortisation
    ZAGAAPAccount("5400", "Depreciation — PPE", "Expense", "Depreciation and Amortisation", "Debit"),
    ZAGAAPAccount("5401", "Amortisation — Intangibles", "Expense", "Depreciation and Amortisation", "Debit"),
    ZAGAAPAccount("5402", "Impairment Loss", "Expense", "Depreciation and Amortisation", "Debit"),
    # Finance costs
    ZAGAAPAccount("5500", "Interest Expense — Bank Loans", "Expense", "Finance Costs", "Debit"),
    ZAGAAPAccount("5501", "Bank Charges and Fees", "Expense", "Finance Costs", "Debit"),
    # Tax
    ZAGAAPAccount("5600", "Corporate Income Tax Expense (27%)", "Expense", "Taxation", "Debit"),
    ZAGAAPAccount("5601", "Deferred Tax Expense / (Credit)", "Expense", "Taxation", "Debit"),
    ZAGAAPAccount("5602", "Dividends Tax Expense (20%)", "Expense", "Taxation", "Debit"),
    # Other operating expenses
    ZAGAAPAccount("5700", "Marketing and Advertising", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5701", "Travel and Entertainment", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5702", "IT Subscriptions and SaaS", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5703", "Office Supplies and Stationery", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5704", "Insurance Premiums", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5705", "Foreign Exchange Loss", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5706", "Bad Debt Written Off", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5707", "Charitable Donations (s18A)", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5708", "Telecommunication Expenses", "Expense", "Other Operating Expenses", "Debit"),
    ZAGAAPAccount("5709", "Miscellaneous Expenses", "Expense", "Other Operating Expenses", "Debit"),
]
