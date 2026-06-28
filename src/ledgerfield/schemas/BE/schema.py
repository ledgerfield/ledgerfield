"""Chart of accounts — Belgium (Belgian GAAP, BE-GAAP)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class BEAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

BE_ACCOUNTS: dict[str, BEAccount] = {
    # Activa / Actief (Assets)
    "1010": BEAccount("1010", "Liquide Middelen / Bank (Cash / Bank)", "asset"),
    "1020": BEAccount("1020", "Handelsvorderingen (Accounts Receivable)", "asset"),
    "1030": BEAccount("1030", "Voorraden (Inventory)", "asset"),
    "1040": BEAccount("1040", "Over te Dragen Kosten (Prepaid Expenses)", "asset"),
    "1050": BEAccount("1050", "Materiële Vaste Activa (Fixed Assets)", "asset"),
    "1060": BEAccount("1060", "Immateriële Vaste Activa (Intangible Assets)", "asset"),
    "1070": BEAccount("1070", "Te Ontvangen BTW (VAT Receivable)", "asset"),
    # Passiva (Liabilities)
    "2010": BEAccount("2010", "Handelsschulden (Accounts Payable)", "liability"),
    "2020": BEAccount("2020", "Vennootschapsbelasting te Betalen (CIT Payable)", "liability"),
    "2030": BEAccount("2030", "Te Betalen BTW (VAT Payable)", "liability"),
    "2040": BEAccount("2040", "Bedrijfsvoorheffing (Withholding Tax Payable)", "liability"),
    "2050": BEAccount("2050", "RSZ-bijdragen (Social Security Payable)", "liability"),
    "2060": BEAccount("2060", "Langlopende Leningen (Long-term Loans)", "liability"),
    # Eigen Vermogen (Equity)
    "3010": BEAccount("3010", "Maatschappelijk Kapitaal (Share Capital)", "equity"),
    "3020": BEAccount("3020", "Overgedragen Winst (Retained Earnings)", "equity"),
    "3030": BEAccount("3030", "Winst / Verlies van het Boekjaar (Current Year Profit)", "equity"),
    # Opbrengsten (Revenue)
    "4010": BEAccount("4010", "Omzet uit Verkopen (Sales Revenue)", "revenue"),
    "4020": BEAccount("4020", "Dienstverleningsomzet (Service Revenue)", "revenue"),
    "4030": BEAccount("4030", "Andere Bedrijfsopbrengsten (Other Income)", "revenue"),
    # Kosten (Expenses)
    "5010": BEAccount("5010", "Kostprijs Verkochte Goederen (COGS)", "expense"),
    "5020": BEAccount("5020", "Bezoldigingen en Lonen (Salaries & Wages)", "expense"),
    "5030": BEAccount("5030", "Werkgeversbijdragen RSZ (Employer Social Insurance)", "expense"),
    "5040": BEAccount("5040", "Huur en Kosten (Rent & Utilities)", "expense"),
    "5050": BEAccount("5050", "Professionele Erelonen (Professional Fees)", "expense"),
    "5060": BEAccount("5060", "Afschrijvingen (Depreciation)", "expense"),
    "5070": BEAccount("5070", "Vennootschapsbelasting Kost (Corporate Income Tax Expense)", "expense"),
    "5080": BEAccount("5080", "BTW / Indirecte Belasting (VAT/Indirect Tax Expense)", "expense"),
}

get_account = BE_ACCOUNTS.get
