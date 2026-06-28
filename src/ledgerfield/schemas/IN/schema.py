"""Chart of accounts — India (Ind AS, IFRS-aligned)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class INAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

IN_ACCOUNTS: dict[str, INAccount] = {
    # Assets
    "1010": INAccount("1010", "Nakit / Banka (Cash / Bank)", "asset"),
    "1020": INAccount("1020", "Debitors / Trade Receivables", "asset"),
    "1030": INAccount("1030", "Stock-in-Trade (Inventory)", "asset"),
    "1040": INAccount("1040", "Prepaid Expenses", "asset"),
    "1050": INAccount("1050", "Property, Plant & Equipment", "asset"),
    "1060": INAccount("1060", "Intangible Assets", "asset"),
    "1070": INAccount("1070", "GST Input Tax Credit Receivable", "asset"),
    # Liabilities
    "2010": INAccount("2010", "Creditors / Trade Payables", "liability"),
    "2020": INAccount("2020", "Corporate Tax Payable (Income Tax)", "liability"),
    "2030": INAccount("2030", "GST Payable (Output Tax)", "liability"),
    "2040": INAccount("2040", "TDS / TCS Payable", "liability"),
    "2050": INAccount("2050", "PF / ESI Payable", "liability"),
    "2060": INAccount("2060", "Long-term Borrowings", "liability"),
    # Equity
    "3010": INAccount("3010", "Share Capital", "equity"),
    "3020": INAccount("3020", "Reserves & Surplus (Retained Earnings)", "equity"),
    "3030": INAccount("3030", "Profit & Loss (Current Year)", "equity"),
    # Revenue
    "4010": INAccount("4010", "Revenue from Operations (Sales)", "revenue"),
    "4020": INAccount("4020", "Service Revenue", "revenue"),
    "4030": INAccount("4030", "Other Income", "revenue"),
    # Expenses
    "5010": INAccount("5010", "Cost of Materials / COGS", "expense"),
    "5020": INAccount("5020", "Employee Benefits Expense (Salaries)", "expense"),
    "5030": INAccount("5030", "PF / ESI (Employer Contribution)", "expense"),
    "5040": INAccount("5040", "Rent & Utilities", "expense"),
    "5050": INAccount("5050", "Professional & Legal Fees", "expense"),
    "5060": INAccount("5060", "Depreciation & Amortisation", "expense"),
    "5070": INAccount("5070", "Current Tax Expense (CIT)", "expense"),
    "5080": INAccount("5080", "GST / Indirect Tax Expense", "expense"),
}

get_account = IN_ACCOUNTS.get
