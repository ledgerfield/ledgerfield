"""Sultanate of Oman chart of accounts (IFRS as applied in Oman).

Omani companies report under IFRS. This chart layers Oman-specific tax and
labour accounts on top of an IFRS structure:

CIT = Corporate Income Tax (15% standard; 3% qualifying SME rate).
WHT = Withholding Tax (10% on certain non-resident payments).
VAT = Value Added Tax (5% since April 2021, Royal Decree No. 121/2020).
EOSB = End-of-Service Benefits (Oman Labour Law).
PASI = Public Authority for Social Insurance / Social Protection Fund
(Omani nationals only).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class OMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


OM_GAAP: list[OMGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    OMGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1020", "Bank Muscat Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1021", "National Bank of Oman Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1022", "Sohar International Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1023", "Bank Dhofar Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1024", "Bank Nizwa (Islamic) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    OMGAAPAccount("1040", "Wakala Term Deposit", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    OMGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    OMGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    OMGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    OMGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    OMGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    OMGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    OMGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    OMGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    OMGAAPAccount("1180", "Withholding Tax Receivable", "Asset", "Tax Receivable", "Debit"),
    OMGAAPAccount("1190", "VAT Input (Recoverable)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    OMGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    OMGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    OMGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    OMGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    OMGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    OMGAAPAccount("1500", "Land", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    OMGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    OMGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    OMGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    OMGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    OMGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    OMGAAPAccount("1620", "Commercial Registration and Licences", "Asset", "Intangible Assets", "Debit"),
    OMGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    OMGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    OMGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    OMGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    OMGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    OMGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    OMGAAPAccount("2040", "Retentions Payable", "Liability", "Trade and Other Payables", "Credit"),
    OMGAAPAccount("2100", "VAT Output Payable", "Liability", "Tax Payable", "Credit"),
    OMGAAPAccount("2110", "VAT Settlement Account (Net)", "Liability", "Tax Payable", "Credit"),
    OMGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    OMGAAPAccount("2130", "Withholding Tax Payable", "Liability", "Tax Payable", "Credit"),
    OMGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    OMGAAPAccount("2210", "WPS Payroll Clearing", "Liability", "Employee Benefits", "Credit"),
    OMGAAPAccount("2220", "End-of-Service Benefits Provision", "Liability", "Employee Benefits", "Credit"),
    OMGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    OMGAAPAccount("2240", "Social Insurance Payable (PASI — Omani Nationals)", "Liability", "Employee Benefits", "Credit"),
    OMGAAPAccount("2250", "Job Security Fund Payable", "Liability", "Employee Benefits", "Credit"),
    OMGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    OMGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    OMGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    OMGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    OMGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    OMGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    OMGAAPAccount("3000", "Share Capital", "Equity", "Contributed Capital", "Credit"),
    OMGAAPAccount("3010", "Partners' Current Account", "Equity", "Contributed Capital", "Credit"),
    OMGAAPAccount("3100", "Legal Reserve", "Equity", "Reserves", "Credit"),
    OMGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    OMGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    OMGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    OMGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    OMGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    OMGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    OMGAAPAccount("4020", "Revenue — Exports (Zero-Rated)", "Revenue", "Operating Revenue", "Credit"),
    OMGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    OMGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    OMGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    OMGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    OMGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    OMGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    OMGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    OMGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    OMGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    OMGAAPAccount("6010", "End-of-Service Benefits Expense", "Expense", "Staff Costs", "Debit"),
    OMGAAPAccount("6020", "Social Insurance Employer Contribution (PASI)", "Expense", "Staff Costs", "Debit"),
    OMGAAPAccount("6025", "Job Security Fund Contribution", "Expense", "Staff Costs", "Debit"),
    OMGAAPAccount("6030", "Employee Medical Insurance", "Expense", "Staff Costs", "Debit"),
    OMGAAPAccount("6040", "Residence Permit and Visa Fees", "Expense", "Staff Costs", "Debit"),
    OMGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    OMGAAPAccount("6110", "Utilities (Electricity and Water)", "Expense", "Occupancy Costs", "Debit"),
    OMGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    OMGAAPAccount("6200", "Commercial Registration Renewal", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6210", "Government and Municipality Fees", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6230", "Telecommunications (Omantel / Ooredoo)", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6280", "Irrecoverable VAT Expense", "Expense", "Administrative Expenses", "Debit"),
    OMGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    OMGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    OMGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
