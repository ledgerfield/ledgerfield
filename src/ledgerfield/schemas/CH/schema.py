"""Chart of accounts — Switzerland (Swiss Code of Obligations / OR)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class CHAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

CH_ACCOUNTS: dict[str, CHAccount] = {
    # Aktiven / Actif (Assets)
    "1010": CHAccount("1010", "Kasse / Bank (Cash / Bank)", "asset"),
    "1020": CHAccount("1020", "Forderungen aus Lieferungen (Accounts Receivable)", "asset"),
    "1030": CHAccount("1030", "Warenvorräte (Inventory)", "asset"),
    "1040": CHAccount("1040", "Aktive Rechnungsabgrenzung (Prepaid Expenses)", "asset"),
    "1050": CHAccount("1050", "Sachanlagen (Fixed Assets)", "asset"),
    "1060": CHAccount("1060", "Immaterielle Anlagen (Intangible Assets)", "asset"),
    "1070": CHAccount("1070", "MWST-Guthaben (VAT Receivable)", "asset"),
    # Passiven / Passif (Liabilities)
    "2010": CHAccount("2010", "Verbindlichkeiten aus Lieferungen (Accounts Payable)", "liability"),
    "2020": CHAccount("2020", "Gewinnsteuer Passiva (Corporate Tax Payable)", "liability"),
    "2030": CHAccount("2030", "MWST-Schulden (VAT Payable)", "liability"),
    "2040": CHAccount("2040", "Quellensteuer / Lohnsteuer (Withholding / Payroll Tax)", "liability"),
    "2050": CHAccount("2050", "AHV / IV / ALV Schulden (Social Insurance Payable)", "liability"),
    "2060": CHAccount("2060", "Langfristige Darlehen (Long-term Loans)", "liability"),
    # Eigenkapital / Fonds propres (Equity)
    "3010": CHAccount("3010", "Aktienkapital (Share Capital)", "equity"),
    "3020": CHAccount("3020", "Gewinnreserven (Retained Earnings)", "equity"),
    "3030": CHAccount("3030", "Jahresgewinn / -verlust (Current Year Profit)", "equity"),
    # Ertrag / Produits (Revenue)
    "4010": CHAccount("4010", "Warenertrag (Sales Revenue)", "revenue"),
    "4020": CHAccount("4020", "Dienstleistungsertrag (Service Revenue)", "revenue"),
    "4030": CHAccount("4030", "Übriger Ertrag (Other Income)", "revenue"),
    # Aufwand / Charges (Expenses)
    "5010": CHAccount("5010", "Warenaufwand (Cost of Goods Sold)", "expense"),
    "5020": CHAccount("5020", "Lohnaufwand (Salaries & Wages)", "expense"),
    "5030": CHAccount("5030", "AHV / IV / ALV Arbeitgeber (Social Insurance Employer)", "expense"),
    "5040": CHAccount("5040", "Miet- und Nebenkosten (Rent & Utilities)", "expense"),
    "5050": CHAccount("5050", "Beratungskosten (Professional Fees)", "expense"),
    "5060": CHAccount("5060", "Abschreibungen (Depreciation)", "expense"),
    "5070": CHAccount("5070", "Gewinnsteuer Aufwand (Corporate Income Tax Expense)", "expense"),
    "5080": CHAccount("5080", "MWST-Aufwand (VAT/Indirect Tax Expense)", "expense"),
}

get_account = CH_ACCOUNTS.get
