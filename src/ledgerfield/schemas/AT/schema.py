"""Chart of accounts — Austria (Austrian GAAP, UGB/IFRS)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ATAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

AT_ACCOUNTS: dict[str, ATAccount] = {
    # Aktiva (Assets)
    "1010": ATAccount("1010", "Kasse und Bank (Cash / Bank)", "asset"),
    "1020": ATAccount("1020", "Forderungen aus Lieferungen (Accounts Receivable)", "asset"),
    "1030": ATAccount("1030", "Vorräte (Inventory)", "asset"),
    "1040": ATAccount("1040", "Aktive Rechnungsabgrenzung (Prepaid Expenses)", "asset"),
    "1050": ATAccount("1050", "Sachanlagen (Fixed Assets)", "asset"),
    "1060": ATAccount("1060", "Immaterielle Vermögensgegenstände (Intangible Assets)", "asset"),
    "1070": ATAccount("1070", "Vorsteuer (VAT Receivable)", "asset"),
    # Passiva (Liabilities)
    "2010": ATAccount("2010", "Verbindlichkeiten aus Lieferungen (Accounts Payable)", "liability"),
    "2020": ATAccount("2020", "Körperschaftsteuer Passiva (Corporate Tax Payable)", "liability"),
    "2030": ATAccount("2030", "Umsatzsteuer Schulden (VAT Payable)", "liability"),
    "2040": ATAccount("2040", "Lohnsteuer / DB / DZ (Payroll Tax Payable)", "liability"),
    "2050": ATAccount("2050", "Sozialversicherung Beiträge (Social Insurance Payable)", "liability"),
    "2060": ATAccount("2060", "Langfristige Verbindlichkeiten (Long-term Loans)", "liability"),
    # Eigenkapital (Equity)
    "3010": ATAccount("3010", "Stamm-/Grundkapital (Share Capital)", "equity"),
    "3020": ATAccount("3020", "Gewinnrücklagen (Retained Earnings)", "equity"),
    "3030": ATAccount("3030", "Jahresgewinn / -verlust (Current Year Profit)", "equity"),
    # Erträge (Revenue)
    "4010": ATAccount("4010", "Umsatzerlöse (Sales Revenue)", "revenue"),
    "4020": ATAccount("4020", "Dienstleistungserlöse (Service Revenue)", "revenue"),
    "4030": ATAccount("4030", "Sonstige betriebliche Erträge (Other Income)", "revenue"),
    # Aufwendungen (Expenses)
    "5010": ATAccount("5010", "Materialaufwand / Wareneinsatz (COGS)", "expense"),
    "5020": ATAccount("5020", "Personalaufwand / Löhne (Salaries & Wages)", "expense"),
    "5030": ATAccount("5030", "Dienstgeberanteil SV (Employer Social Insurance)", "expense"),
    "5040": ATAccount("5040", "Miete und Betriebskosten (Rent & Utilities)", "expense"),
    "5050": ATAccount("5050", "Beratungs- und Prüfungskosten (Professional Fees)", "expense"),
    "5060": ATAccount("5060", "Abschreibungen (Depreciation)", "expense"),
    "5070": ATAccount("5070", "Körperschaftsteuer Aufwand (Corporate Income Tax Expense)", "expense"),
    "5080": ATAccount("5080", "Umsatzsteuer / Indirekte Steuer (VAT/Indirect Tax Expense)", "expense"),
}

get_account = AT_ACCOUNTS.get
