"""Republic of Indonesia chart of accounts (PSAK / Indonesian GAAP).

Indonesian companies report under PSAK (Pernyataan Standar Akuntansi
Keuangan), which is substantially converged with IFRS. This chart layers
Indonesia-specific tax and payroll accounts on top of a PSAK/IFRS structure:

PPh Badan = Corporate Income Tax (22% standard, 19% qualifying listed).
PPN = Pajak Pertambahan Nilai (VAT, 11%; 12% luxury goods only from 2025).
PPh 21/23/26 = Withholding taxes on salaries, services, and non-residents.
BPJS = Mandatory social/health security (Ketenagakerjaan + Kesehatan).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class IDGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


ID_GAAP: list[IDGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    IDGAAPAccount("1010", "Cash on Hand", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1020", "Bank Mandiri Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1021", "Bank Central Asia (BCA) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1022", "Bank Rakyat Indonesia (BRI) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1023", "Bank Negara Indonesia (BNI) Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1030", "Foreign Currency Account (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    IDGAAPAccount("1040", "Time Deposits (Deposito Berjangka)", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    IDGAAPAccount("1100", "Trade Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    IDGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    IDGAAPAccount("1120", "Retentions Receivable", "Asset", "Trade and Other Receivables", "Debit"),
    IDGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    IDGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    IDGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    IDGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    IDGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    IDGAAPAccount("1180", "PPN Masukan (Input VAT)", "Asset", "Tax Receivable", "Debit"),
    IDGAAPAccount("1181", "Prepaid Income Tax (PPh 25 Instalments)", "Asset", "Tax Receivable", "Debit"),
    IDGAAPAccount("1182", "Withholding Tax Credits (PPh 22/23 Receivable)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    IDGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    IDGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    IDGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    IDGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    IDGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    IDGAAPAccount("1500", "Land (Hak Guna Bangunan)", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    IDGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    IDGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    IDGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1570", "Right-of-Use Asset (PSAK 73)", "Asset", "Property, Plant and Equipment", "Debit"),
    IDGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    IDGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    IDGAAPAccount("1620", "Business Licences (NIB / OSS)", "Asset", "Intangible Assets", "Debit"),
    IDGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    IDGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),
    IDGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    IDGAAPAccount("2000", "Trade Payables", "Liability", "Trade and Other Payables", "Credit"),
    IDGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    IDGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    IDGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    IDGAAPAccount("2100", "PPN Keluaran (Output VAT)", "Liability", "Tax Payable", "Credit"),
    IDGAAPAccount("2110", "PPN Payable (Net VAT Settlement)", "Liability", "Tax Payable", "Credit"),
    IDGAAPAccount("2120", "Corporate Income Tax Payable (PPh 29)", "Liability", "Tax Payable", "Credit"),
    IDGAAPAccount("2130", "Employee Income Tax Payable (PPh 21)", "Liability", "Tax Payable", "Credit"),
    IDGAAPAccount("2140", "Withholding Tax Payable (PPh 23)", "Liability", "Tax Payable", "Credit"),
    IDGAAPAccount("2150", "Non-Resident Withholding Tax Payable (PPh 26)", "Liability", "Tax Payable", "Credit"),
    IDGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    IDGAAPAccount("2210", "BPJS Ketenagakerjaan Payable", "Liability", "Employee Benefits", "Credit"),
    IDGAAPAccount("2220", "BPJS Kesehatan Payable", "Liability", "Employee Benefits", "Credit"),
    IDGAAPAccount("2230", "Religious Holiday Allowance (THR) Provision", "Liability", "Employee Benefits", "Credit"),
    IDGAAPAccount("2240", "Post-Employment Benefit Provision (PSAK 24)", "Liability", "Employee Benefits", "Credit"),
    IDGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    IDGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    IDGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    IDGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    IDGAAPAccount("2410", "Lease Liability (PSAK 73)", "Liability", "Non-Current Liabilities", "Credit"),
    IDGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),
    IDGAAPAccount("2430", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    IDGAAPAccount("3000", "Share Capital (Modal Saham)", "Equity", "Contributed Capital", "Credit"),
    IDGAAPAccount("3010", "Additional Paid-In Capital (Agio Saham)", "Equity", "Contributed Capital", "Credit"),
    IDGAAPAccount("3100", "Statutory Reserve (UU PT Art. 70)", "Equity", "Reserves", "Credit"),
    IDGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    IDGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    IDGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    IDGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    IDGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    IDGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    IDGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    IDGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    IDGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    IDGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    IDGAAPAccount("4210", "Commission Income", "Revenue", "Other Income", "Credit"),
    IDGAAPAccount("4220", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    IDGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    IDGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    IDGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    IDGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    IDGAAPAccount("6010", "Religious Holiday Allowance (THR) Expense", "Expense", "Staff Costs", "Debit"),
    IDGAAPAccount("6020", "BPJS Ketenagakerjaan Employer Contribution", "Expense", "Staff Costs", "Debit"),
    IDGAAPAccount("6030", "BPJS Kesehatan Employer Contribution", "Expense", "Staff Costs", "Debit"),
    IDGAAPAccount("6040", "Post-Employment Benefit Expense (PSAK 24)", "Expense", "Staff Costs", "Debit"),
    IDGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    IDGAAPAccount("6110", "Utilities (PLN / PDAM)", "Expense", "Occupancy Costs", "Debit"),
    IDGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    IDGAAPAccount("6200", "Business Licence and OSS Fees", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6210", "Land and Building Tax (PBB)", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6220", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6230", "Telecommunications (Telkomsel / Indosat)", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6250", "Bank Charges", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6280", "Stamp Duty (Bea Meterai)", "Expense", "Administrative Expenses", "Debit"),
    IDGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    IDGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    IDGAAPAccount("6400", "Corporate Income Tax Expense (PPh Badan)", "Expense", "Tax Expense", "Debit"),
    IDGAAPAccount("6410", "Final Tax Expense (PPh Final)", "Expense", "Tax Expense", "Debit"),
]
