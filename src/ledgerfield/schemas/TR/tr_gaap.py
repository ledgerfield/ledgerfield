"""Republic of Türkiye chart of accounts (IFRS layer, Turkish uniform chart style).

Turkish companies keep statutory books under the Uniform Chart of Accounts
(Tekdüzen Hesap Planı); listed/large entities report under TFRS (IFRS as
adopted in Türkiye). This chart layers Türkiye-specific tax and labour
accounts on top of an IFRS structure:

CIT = Corporate Income Tax (25% standard; 30% financial institutions,
      Law No. 5520).
KDV = Value Added Tax (VAT), standard 20% with reduced 10% / 1% rates.
SGK = Social Security Institution (Sosyal Güvenlik Kurumu) contributions.
Inflation adjustment: mandatory restatement under Tax Procedure Law
Art. 298 mükerrer (re-activated FY2024+) — reflected in equity restatement
difference accounts and monetary gain/loss accounts.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TRGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


TR_GAAP: list[TRGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    TRGAAPAccount("1010", "Cash on Hand (Kasa)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1020", "Ziraat Bankası Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1021", "İş Bankası Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1022", "Garanti BBVA Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1023", "Akbank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1024", "Yapı Kredi Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1030", "Foreign Currency Account (EUR/USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1040", "Time Deposit (Vadeli Mevduat)", "Asset", "Cash and Cash Equivalents", "Debit"),
    TRGAAPAccount("1050", "Cheques Received", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    TRGAAPAccount("1100", "Trade Receivables (Alıcılar)", "Asset", "Trade and Other Receivables", "Debit"),
    TRGAAPAccount("1105", "Notes Receivable (Alacak Senetleri)", "Asset", "Trade and Other Receivables", "Debit"),
    TRGAAPAccount("1110", "Allowance for Expected Credit Losses", "Asset", "Trade and Other Receivables", "Credit"),
    TRGAAPAccount("1130", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    TRGAAPAccount("1140", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    TRGAAPAccount("1150", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    TRGAAPAccount("1160", "Prepaid Expenses", "Asset", "Prepayments", "Debit"),
    TRGAAPAccount("1170", "Prepaid Rent", "Asset", "Prepayments", "Debit"),
    TRGAAPAccount("1180", "Deductible VAT (İndirilecek KDV)", "Asset", "Tax Receivable", "Debit"),
    TRGAAPAccount("1185", "VAT Carried Forward (Devreden KDV)", "Asset", "Tax Receivable", "Debit"),
    TRGAAPAccount("1190", "Prepaid Taxes and Withholdings (Peşin Vergiler)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    TRGAAPAccount("1200", "Inventory — Raw Materials", "Asset", "Inventories", "Debit"),
    TRGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    TRGAAPAccount("1220", "Inventory — Finished Goods", "Asset", "Inventories", "Debit"),
    TRGAAPAccount("1230", "Goods in Transit", "Asset", "Inventories", "Debit"),
    TRGAAPAccount("1240", "Provision for Slow-Moving Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    TRGAAPAccount("1500", "Land (Arazi ve Arsalar)", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1510", "Buildings", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    TRGAAPAccount("1520", "Leasehold Improvements", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1530", "Plant and Machinery", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    TRGAAPAccount("1540", "Motor Vehicles", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    TRGAAPAccount("1550", "Furniture and Fixtures", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1560", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1570", "Right-of-Use Asset (IFRS 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    TRGAAPAccount("1600", "Goodwill", "Asset", "Intangible Assets", "Debit"),
    TRGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    TRGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    TRGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),
    TRGAAPAccount("1800", "Deferred Tax Asset", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    TRGAAPAccount("2000", "Trade Payables (Satıcılar)", "Liability", "Trade and Other Payables", "Credit"),
    TRGAAPAccount("2005", "Notes Payable (Borç Senetleri)", "Liability", "Trade and Other Payables", "Credit"),
    TRGAAPAccount("2010", "Accrued Expenses", "Liability", "Trade and Other Payables", "Credit"),
    TRGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    TRGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    TRGAAPAccount("2100", "Output VAT Payable (Hesaplanan KDV)", "Liability", "Tax Payable", "Credit"),
    TRGAAPAccount("2110", "VAT Settlement Payable (Ödenecek KDV)", "Liability", "Tax Payable", "Credit"),
    TRGAAPAccount("2120", "Corporate Income Tax Payable", "Liability", "Tax Payable", "Credit"),
    TRGAAPAccount("2130", "Withholding Tax Payable (Stopaj)", "Liability", "Tax Payable", "Credit"),
    TRGAAPAccount("2140", "Stamp Duty Payable (Damga Vergisi)", "Liability", "Tax Payable", "Credit"),
    TRGAAPAccount("2200", "Salaries and Wages Payable", "Liability", "Employee Benefits", "Credit"),
    TRGAAPAccount("2210", "SGK Premiums Payable", "Liability", "Employee Benefits", "Credit"),
    TRGAAPAccount("2215", "Unemployment Insurance Payable (İşsizlik Sigortası)", "Liability", "Employee Benefits", "Credit"),
    TRGAAPAccount("2220", "Severance Pay Provision (Kıdem Tazminatı)", "Liability", "Employee Benefits", "Credit"),
    TRGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    TRGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    TRGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    TRGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    TRGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    TRGAAPAccount("2410", "Lease Liability (IFRS 16)", "Liability", "Non-Current Liabilities", "Credit"),
    TRGAAPAccount("2420", "Shareholder Loan", "Liability", "Non-Current Liabilities", "Credit"),
    TRGAAPAccount("2430", "Deferred Tax Liability", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    TRGAAPAccount("3000", "Share Capital (Sermaye)", "Equity", "Contributed Capital", "Credit"),
    TRGAAPAccount("3010", "Share Premium", "Equity", "Contributed Capital", "Credit"),
    TRGAAPAccount("3100", "Legal Reserve (Yasal Yedekler)", "Equity", "Reserves", "Credit"),
    TRGAAPAccount("3110", "General Reserve", "Equity", "Reserves", "Credit"),
    TRGAAPAccount("3120", "Inflation Restatement Difference — Capital (Sermaye Düzeltmesi Olumlu Farkları)", "Equity", "Reserves", "Credit"),
    TRGAAPAccount("3200", "Retained Earnings", "Equity", "Retained Earnings", "Credit"),
    TRGAAPAccount("3210", "Current Year Profit / (Loss)", "Equity", "Retained Earnings", "Credit"),
    TRGAAPAccount("3300", "Dividends Declared", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    TRGAAPAccount("4000", "Revenue — Goods", "Revenue", "Operating Revenue", "Credit"),
    TRGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    TRGAAPAccount("4020", "Revenue — Exports", "Revenue", "Operating Revenue", "Credit"),
    TRGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    TRGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    TRGAAPAccount("4200", "Other Operating Income", "Revenue", "Other Income", "Credit"),
    TRGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),
    TRGAAPAccount("4220", "Net Monetary Position Gain (Inflation Adjustment)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    TRGAAPAccount("5000", "Cost of Goods Sold", "Expense", "Cost of Sales", "Debit"),
    TRGAAPAccount("5010", "Direct Labour", "Expense", "Cost of Sales", "Debit"),
    TRGAAPAccount("5020", "Subcontractor Costs", "Expense", "Cost of Sales", "Debit"),
    TRGAAPAccount("6000", "Salaries and Wages", "Expense", "Staff Costs", "Debit"),
    TRGAAPAccount("6010", "SGK Employer Contribution (20.75%)", "Expense", "Staff Costs", "Debit"),
    TRGAAPAccount("6015", "Unemployment Insurance Employer Contribution (2%)", "Expense", "Staff Costs", "Debit"),
    TRGAAPAccount("6020", "Severance Pay Expense (Kıdem Tazminatı)", "Expense", "Staff Costs", "Debit"),
    TRGAAPAccount("6030", "Employee Meal and Transport Allowances", "Expense", "Staff Costs", "Debit"),
    TRGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    TRGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    TRGAAPAccount("6120", "Depreciation of Right-of-Use Asset", "Expense", "Occupancy Costs", "Debit"),
    TRGAAPAccount("6200", "Trade Registry and Chamber Fees", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6210", "Stamp Duty Expense (Damga Vergisi)", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6220", "Professional and Audit Fees (YMM/SMMM)", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6230", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6240", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6250", "Bank Charges and BSMV", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6260", "Depreciation Expense", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6270", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    TRGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    TRGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    TRGAAPAccount("6320", "Net Monetary Position Loss (Inflation Adjustment)", "Expense", "Finance Costs", "Debit"),
    TRGAAPAccount("6400", "Corporate Income Tax Expense", "Expense", "Tax Expense", "Debit"),
]
