"""Chart of accounts — Sweden (Swedish GAAP, BAS/K-regulations)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class SEAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

SE_ACCOUNTS: dict[str, SEAccount] = {
    # Tillgångar (Assets)
    "1010": SEAccount("1010", "Kassa och Bank (Cash / Bank)", "asset"),
    "1020": SEAccount("1020", "Kundfordringar (Accounts Receivable)", "asset"),
    "1030": SEAccount("1030", "Varulager (Inventory)", "asset"),
    "1040": SEAccount("1040", "Förutbetalda Kostnader (Prepaid Expenses)", "asset"),
    "1050": SEAccount("1050", "Materiella Anläggningstillgångar (Fixed Assets)", "asset"),
    "1060": SEAccount("1060", "Immateriella Anläggningstillgångar (Intangible Assets)", "asset"),
    "1070": SEAccount("1070", "Ingående Moms (VAT Receivable)", "asset"),
    # Skulder (Liabilities)
    "2010": SEAccount("2010", "Leverantörsskulder (Accounts Payable)", "liability"),
    "2020": SEAccount("2020", "Aktuell Bolagsskatt (Corporate Tax Payable)", "liability"),
    "2030": SEAccount("2030", "Utgående Moms (VAT Payable)", "liability"),
    "2040": SEAccount("2040", "Källskatt / Arbetsgivaravgift (Payroll Tax Payable)", "liability"),
    "2050": SEAccount("2050", "Sociala Avgifter (Social Insurance Payable)", "liability"),
    "2060": SEAccount("2060", "Långfristiga Lån (Long-term Loans)", "liability"),
    # Eget Kapital (Equity)
    "3010": SEAccount("3010", "Aktiekapital (Share Capital)", "equity"),
    "3020": SEAccount("3020", "Balanserade Vinstmedel (Retained Earnings)", "equity"),
    "3030": SEAccount("3030", "Årets Resultat (Current Year Profit)", "equity"),
    # Intäkter (Revenue)
    "4010": SEAccount("4010", "Nettoomsättning (Sales Revenue)", "revenue"),
    "4020": SEAccount("4020", "Tjänsteintäkter (Service Revenue)", "revenue"),
    "4030": SEAccount("4030", "Övriga Intäkter (Other Income)", "revenue"),
    # Kostnader (Expenses)
    "5010": SEAccount("5010", "Kostnad Sålda Varor (Cost of Goods Sold)", "expense"),
    "5020": SEAccount("5020", "Löner och Arvoden (Salaries & Wages)", "expense"),
    "5030": SEAccount("5030", "Arbetsgivaravgifter (Employer Social Insurance)", "expense"),
    "5040": SEAccount("5040", "Hyra och Driftskostnader (Rent & Utilities)", "expense"),
    "5050": SEAccount("5050", "Konsultarvoden (Professional Fees)", "expense"),
    "5060": SEAccount("5060", "Avskrivningar (Depreciation)", "expense"),
    "5070": SEAccount("5070", "Bolagsskattekostnad (Corporate Income Tax Expense)", "expense"),
    "5080": SEAccount("5080", "Moms / Indirekt Skatt (VAT/Indirect Tax Expense)", "expense"),
}

get_account = SE_ACCOUNTS.get
