"""Hungary chart of accounts (Hungarian Accounting Act, Act C of 2000).

Hungarian companies report under Hungarian GAAP (számviteli törvény); listed
groups use IFRS. This chart layers Hungary-specific tax and payroll accounts
on top of a standard structure:

TAO  = Corporate Income Tax (társasági adó, 9% flat — Act LXXXI of 1996).
ÁFA  = VAT (általános forgalmi adó, 27% standard / 18% / 5% reduced).
HIPA = Local Business Tax (helyi iparűzési adó, up to 2% on adjusted turnover).
SZJA = Personal Income Tax withheld (15% flat).
TB   = Social security contributions (18.5% employee) and 13% employer
       social contribution tax (szociális hozzájárulási adó, szocho).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class HUGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


HU_GAAP: list[HUGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    HUGAAPAccount("1010", "Cash on Hand (Pénztár)", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1015", "Petty Cash", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1020", "OTP Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1021", "K&H Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1022", "Erste Bank Hungary Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1023", "MBH Bank Account", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1030", "Foreign Currency Account (EUR)", "Asset", "Cash and Cash Equivalents", "Debit"),
    HUGAAPAccount("1040", "Short-Term Bank Deposits", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    HUGAAPAccount("1100", "Trade Receivables (Vevők)", "Asset", "Trade and Other Receivables", "Debit"),
    HUGAAPAccount("1110", "Allowance for Doubtful Receivables", "Asset", "Trade and Other Receivables", "Credit"),
    HUGAAPAccount("1120", "Other Receivables", "Asset", "Trade and Other Receivables", "Debit"),
    HUGAAPAccount("1130", "Advances to Suppliers", "Asset", "Trade and Other Receivables", "Debit"),
    HUGAAPAccount("1140", "Employee Advances", "Asset", "Trade and Other Receivables", "Debit"),
    HUGAAPAccount("1150", "Prepaid Expenses (Aktív időbeli elhatárolások)", "Asset", "Prepayments", "Debit"),
    HUGAAPAccount("1160", "Input VAT Receivable (Előzetesen felszámított ÁFA)", "Asset", "Tax Receivable", "Debit"),
    HUGAAPAccount("1170", "VAT Refund Receivable (ÁFA visszaigénylés)", "Asset", "Tax Receivable", "Debit"),
    HUGAAPAccount("1180", "Corporate Income Tax Prepayments (TAO előleg)", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    HUGAAPAccount("1200", "Inventory — Raw Materials (Anyagok)", "Asset", "Inventories", "Debit"),
    HUGAAPAccount("1210", "Inventory — Work in Progress", "Asset", "Inventories", "Debit"),
    HUGAAPAccount("1220", "Inventory — Finished Goods (Késztermékek)", "Asset", "Inventories", "Debit"),
    HUGAAPAccount("1230", "Goods for Resale (Áruk)", "Asset", "Inventories", "Debit"),
    HUGAAPAccount("1240", "Provision for Obsolete Inventory", "Asset", "Inventories", "Credit"),
    # Non-current assets
    HUGAAPAccount("1500", "Land (Telek)", "Asset", "Property, Plant and Equipment", "Debit"),
    HUGAAPAccount("1510", "Buildings (Épületek)", "Asset", "Property, Plant and Equipment", "Debit"),
    HUGAAPAccount("1515", "Accumulated Depreciation — Buildings", "Asset", "Property, Plant and Equipment", "Credit"),
    HUGAAPAccount("1530", "Plant and Machinery (Gépek, berendezések)", "Asset", "Property, Plant and Equipment", "Debit"),
    HUGAAPAccount("1535", "Accumulated Depreciation — Plant and Machinery", "Asset", "Property, Plant and Equipment", "Credit"),
    HUGAAPAccount("1540", "Motor Vehicles (Járművek)", "Asset", "Property, Plant and Equipment", "Debit"),
    HUGAAPAccount("1545", "Accumulated Depreciation — Motor Vehicles", "Asset", "Property, Plant and Equipment", "Credit"),
    HUGAAPAccount("1550", "Office and Computer Equipment", "Asset", "Property, Plant and Equipment", "Debit"),
    HUGAAPAccount("1600", "Goodwill (Üzleti vagy cégérték)", "Asset", "Intangible Assets", "Debit"),
    HUGAAPAccount("1610", "Software and Licences", "Asset", "Intangible Assets", "Debit"),
    HUGAAPAccount("1700", "Investment in Subsidiaries", "Asset", "Investments", "Debit"),
    HUGAAPAccount("1710", "Long-Term Deposits", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    HUGAAPAccount("2000", "Trade Payables (Szállítók)", "Liability", "Trade and Other Payables", "Credit"),
    HUGAAPAccount("2010", "Accrued Expenses (Passzív időbeli elhatárolások)", "Liability", "Trade and Other Payables", "Credit"),
    HUGAAPAccount("2020", "Other Payables", "Liability", "Trade and Other Payables", "Credit"),
    HUGAAPAccount("2030", "Advances from Customers", "Liability", "Trade and Other Payables", "Credit"),
    HUGAAPAccount("2100", "Output VAT Payable (Fizetendő ÁFA)", "Liability", "Tax Payable", "Credit"),
    HUGAAPAccount("2110", "VAT Settlement Account (ÁFA elszámolási számla)", "Liability", "Tax Payable", "Credit"),
    HUGAAPAccount("2120", "Corporate Income Tax Payable (TAO)", "Liability", "Tax Payable", "Credit"),
    HUGAAPAccount("2130", "Local Business Tax Payable (HIPA)", "Liability", "Tax Payable", "Credit"),
    HUGAAPAccount("2140", "Personal Income Tax Withheld (SZJA)", "Liability", "Tax Payable", "Credit"),
    HUGAAPAccount("2150", "Innovation Contribution Payable (Innovációs járulék)", "Liability", "Tax Payable", "Credit"),
    HUGAAPAccount("2200", "Salaries and Wages Payable (Bérek)", "Liability", "Employee Benefits", "Credit"),
    HUGAAPAccount("2210", "Social Security Contributions Payable (TB-járulék 18.5%)", "Liability", "Employee Benefits", "Credit"),
    HUGAAPAccount("2220", "Employer Social Contribution Tax Payable (Szocho 13%)", "Liability", "Employee Benefits", "Credit"),
    HUGAAPAccount("2230", "Leave Pay Provision", "Liability", "Employee Benefits", "Credit"),
    HUGAAPAccount("2300", "Bank Overdraft", "Liability", "Borrowings", "Credit"),
    HUGAAPAccount("2310", "Short-Term Loans", "Liability", "Borrowings", "Credit"),
    HUGAAPAccount("2320", "Current Portion of Long-Term Loans", "Liability", "Borrowings", "Credit"),
    HUGAAPAccount("2400", "Long-Term Loans", "Liability", "Non-Current Liabilities", "Credit"),
    HUGAAPAccount("2410", "Lease Liability", "Liability", "Non-Current Liabilities", "Credit"),
    HUGAAPAccount("2420", "Shareholder Loan (Tagi kölcsön)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    HUGAAPAccount("3000", "Share Capital (Jegyzett tőke)", "Equity", "Contributed Capital", "Credit"),
    HUGAAPAccount("3010", "Capital Reserve (Tőketartalék)", "Equity", "Contributed Capital", "Credit"),
    HUGAAPAccount("3100", "Retained Earnings (Eredménytartalék)", "Equity", "Retained Earnings", "Credit"),
    HUGAAPAccount("3110", "Tied-Up Reserve (Lekötött tartalék)", "Equity", "Reserves", "Credit"),
    HUGAAPAccount("3200", "Current Year Profit / (Loss) (Adózott eredmény)", "Equity", "Retained Earnings", "Credit"),
    HUGAAPAccount("3300", "Dividends Declared (Osztalék)", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    HUGAAPAccount("4000", "Revenue — Goods (Belföldi értékesítés)", "Revenue", "Operating Revenue", "Credit"),
    HUGAAPAccount("4010", "Revenue — Services", "Revenue", "Operating Revenue", "Credit"),
    HUGAAPAccount("4020", "Revenue — EU Intra-Community Supplies", "Revenue", "Operating Revenue", "Credit"),
    HUGAAPAccount("4030", "Revenue — Exports (Third Countries)", "Revenue", "Operating Revenue", "Credit"),
    HUGAAPAccount("4100", "Sales Returns and Allowances", "Revenue", "Operating Revenue", "Debit"),
    HUGAAPAccount("4110", "Discounts Allowed", "Revenue", "Operating Revenue", "Debit"),
    HUGAAPAccount("4200", "Other Operating Income (Egyéb bevételek)", "Revenue", "Other Income", "Credit"),
    HUGAAPAccount("4210", "Foreign Exchange Gain", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    HUGAAPAccount("5000", "Cost of Goods Sold (ELÁBÉ)", "Expense", "Cost of Sales", "Debit"),
    HUGAAPAccount("5010", "Direct Materials (Anyagköltség)", "Expense", "Cost of Sales", "Debit"),
    HUGAAPAccount("5020", "Subcontractor Costs (Közvetített szolgáltatások)", "Expense", "Cost of Sales", "Debit"),
    HUGAAPAccount("6000", "Salaries and Wages (Bérköltség)", "Expense", "Staff Costs", "Debit"),
    HUGAAPAccount("6010", "Employer Social Contribution Tax (Szocho 13%)", "Expense", "Staff Costs", "Debit"),
    HUGAAPAccount("6020", "Fringe Benefits (Cafeteria / SZÉP-kártya)", "Expense", "Staff Costs", "Debit"),
    HUGAAPAccount("6030", "Vocational Training and Other Payroll Charges", "Expense", "Staff Costs", "Debit"),
    HUGAAPAccount("6100", "Office Rent", "Expense", "Occupancy Costs", "Debit"),
    HUGAAPAccount("6110", "Utilities", "Expense", "Occupancy Costs", "Debit"),
    HUGAAPAccount("6200", "Professional and Audit Fees", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6210", "Telecommunications", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6220", "Marketing and Advertising", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6230", "Bank Charges and Financial Transaction Duty", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6240", "Depreciation Expense (Értékcsökkenési leírás)", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6250", "Repairs and Maintenance", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6260", "Non-Deductible VAT Expense (Le nem vonható ÁFA)", "Expense", "Administrative Expenses", "Debit"),
    HUGAAPAccount("6300", "Finance Costs", "Expense", "Finance Costs", "Debit"),
    HUGAAPAccount("6310", "Foreign Exchange Loss", "Expense", "Finance Costs", "Debit"),
    HUGAAPAccount("6400", "Corporate Income Tax Expense (TAO ráfordítás)", "Expense", "Tax Expense", "Debit"),
    HUGAAPAccount("6410", "Local Business Tax Expense (HIPA ráfordítás)", "Expense", "Tax Expense", "Debit"),
]
