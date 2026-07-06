"""Socialist Republic of Vietnam chart of accounts (Vietnamese Accounting Standards).

Vietnamese companies report under Vietnamese Accounting Standards (VAS,
Circular 200/2014/TT-BTC chart of accounts), converging toward IFRS. This
chart layers Vietnam-specific tax and labour accounts on top of a
VAS-inspired structure:

CIT = Corporate Income Tax (20% standard; 10% hi-tech preferential, 15 years).
VAT = Value Added Tax (10% standard; temporary 8% reduction; 5%/0% bands).
FCT = Foreign Contractor Tax (deemed CIT + VAT on foreign contractors).
PIT = Personal Income Tax (progressive 5-35%, withheld on payroll).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class VNGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


VN_GAAP: list[VNGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    VNGAAPAccount("1010", "Cash on Hand (VND)", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1020", "Vietcombank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1021", "BIDV Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1022", "VietinBank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1023", "Techcombank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    VNGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    VNGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    VNGAAPAccount("1110", "Allowance for Doubtful Debts", "Asset", "Trade and Other Receivables", "Credit"),
    VNGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    VNGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    VNGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    VNGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    VNGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    VNGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    VNGAAPAccount("1180", "Deductible VAT (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    VNGAAPAccount("1185", "VAT Refund Receivable", "Asset", "Tax Receivable", "Debit"),
    VNGAAPAccount("1190", "CIT Prepayments (Provisional Quarterly)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    VNGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    VNGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    VNGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    VNGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    VNGAAPAccount("1240", "Provision for Inventory Devaluation", "Asset", "Inventories", "Credit"),
    # Non-current assets
    VNGAAPAccount("1500", "Land Use Rights", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1510", "Buildings and Structures", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    VNGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    VNGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    VNGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    VNGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    VNGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    VNGAAPAccount("1620", "Enterprise Registration Certificate Costs", "Asset", "Intangible Assets", "Debit"),
    VNGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    VNGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    VNGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    VNGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    VNGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    VNGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    VNGAAPAccount("2100", "Output VAT Payable", "Liability", "Tax Payable", "Credit"),
    VNGAAPAccount("2110", "VAT Payable — Net Settlement", "Liability", "Tax Payable", "Credit"),
    VNGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    VNGAAPAccount("2130", "Foreign Contractor Tax (FCT) Payable", "Liability", "Tax Payable", "Credit"),
    VNGAAPAccount("2140", "Personal Income Tax Withheld Payable", "Liability", "Tax Payable", "Credit"),
    VNGAAPAccount("2150", "Business Licence Fee Payable", "Liability", "Tax Payable", "Credit"),
    VNGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    VNGAAPAccount("2210", "Social Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    VNGAAPAccount("2220", "Health Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    VNGAAPAccount("2230", "Unemployment Insurance Payable", "Liability", "Employee Benefits", "Credit"),
    VNGAAPAccount("2240", "Trade Union Fee Payable", "Liability", "Employee Benefits", "Credit"),
    VNGAAPAccount("2250", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    VNGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    VNGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    VNGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    VNGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    VNGAAPAccount("2410", "Lease Liability", "Liability", "Non-Current Liabilities", "Credit"),
    VNGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    VNGAAPAccount("3000", "Charter Capital", "Equity", "Contributed Capital", "Credit"),
    VNGAAPAccount("3010", "Capital Surplus", "Equity", "Contributed Capital", "Credit"),
    VNGAAPAccount("3100", "Investment and Development Fund", "Equity", "Reserves", "Credit"),
    VNGAAPAccount("3110", "Financial Reserve Fund", "Equity", "Reserves", "Credit"),
    VNGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    VNGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    VNGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    VNGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    VNGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    VNGAAPAccount("4020", "Revenue — Exports (0% VAT)", "Revenue", "Operating Revenue", "Credit"),
    VNGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    VNGAAPAccount("4110", "Trade Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    VNGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    VNGAAPAccount("4210", "Financial Income (Interest, FX Gain)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    VNGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    VNGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    VNGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    VNGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    VNGAAPAccount("6010", "Social Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    VNGAAPAccount("6020", "Health Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    VNGAAPAccount("6030", "Unemployment Insurance Employer Contribution", "Expense", "Staff Costs", "Debit"),
    VNGAAPAccount("6040", "Trade Union Fee Expense", "Expense", "Staff Costs", "Debit"),
    VNGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    VNGAAPAccount("6110", "Utilities (EVN Electricity, Water)", "Expense", "Occupancy Costs", "Debit"),
    VNGAAPAccount("6200", "Business Licence Fee", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6210", "Government Fees and Charges", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6230", "Telecommunications (Viettel / VNPT)", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6280", "Non-Deductible VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6290", "Foreign Contractor Tax (FCT) Expense", "Expense", "Administrative Expenses", "Debit"),
    VNGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    VNGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    VNGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
