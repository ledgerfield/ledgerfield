"""Chart of accounts — Finland (Finnish GAAP, FAS/IFRS)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class FIAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

FI_ACCOUNTS: dict[str, FIAccount] = {
    # Vastaavaa / Aktiva (Assets)
    "1010": FIAccount("1010", "Kassa ja Pankkitili (Cash / Bank)", "asset"),
    "1020": FIAccount("1020", "Myyntisaamiset (Accounts Receivable)", "asset"),
    "1030": FIAccount("1030", "Vaihto-omaisuus (Inventory)", "asset"),
    "1040": FIAccount("1040", "Siirtosaamiset / Ennakkomaksut (Prepaid Expenses)", "asset"),
    "1050": FIAccount("1050", "Aineelliset Käyttöomaisuudet (Fixed Assets)", "asset"),
    "1060": FIAccount("1060", "Aineettomat Hyödykkeet (Intangible Assets)", "asset"),
    "1070": FIAccount("1070", "Arvonlisäveron Palautussaatava (VAT Receivable)", "asset"),
    # Vastattavaa / Passiva (Liabilities)
    "2010": FIAccount("2010", "Ostovelat (Accounts Payable)", "liability"),
    "2020": FIAccount("2020", "Yhteisöverot Maksettavana (Corporate Tax Payable)", "liability"),
    "2030": FIAccount("2030", "Arvonlisävero Maksettavana (VAT Payable)", "liability"),
    "2040": FIAccount("2040", "Ennakonpidätys / TyEL-maksu (Payroll Tax Payable)", "liability"),
    "2050": FIAccount("2050", "Sosiaalivakuutusmaksut (Social Insurance Payable)", "liability"),
    "2060": FIAccount("2060", "Pitkäaikaiset Lainat (Long-term Loans)", "liability"),
    # Oma Pääoma (Equity)
    "3010": FIAccount("3010", "Osakepääoma (Share Capital)", "equity"),
    "3020": FIAccount("3020", "Kertyneet Voittovarat (Retained Earnings)", "equity"),
    "3030": FIAccount("3030", "Tilikauden Voitto / Tappio (Current Year Profit)", "equity"),
    # Tuotot (Revenue)
    "4010": FIAccount("4010", "Liikevaihto (Sales Revenue)", "revenue"),
    "4020": FIAccount("4020", "Palvelutulot (Service Revenue)", "revenue"),
    "4030": FIAccount("4030", "Muut Tuotot (Other Income)", "revenue"),
    # Kulut (Expenses)
    "5010": FIAccount("5010", "Myytävien Tuotteiden Hankintameno (COGS)", "expense"),
    "5020": FIAccount("5020", "Palkat ja Palkkiot (Salaries & Wages)", "expense"),
    "5030": FIAccount("5030", "Työnantajan Sosiaalivakuutus (Employer Social Insurance)", "expense"),
    "5040": FIAccount("5040", "Vuokra- ja Käyttökulut (Rent & Utilities)", "expense"),
    "5050": FIAccount("5050", "Asiantuntijapalkkiot (Professional Fees)", "expense"),
    "5060": FIAccount("5060", "Poistot (Depreciation)", "expense"),
    "5070": FIAccount("5070", "Yhteisöverokulu (Corporate Income Tax Expense)", "expense"),
    "5080": FIAccount("5080", "ALV / Välillinen Vero (VAT/Indirect Tax Expense)", "expense"),
}

get_account = FI_ACCOUNTS.get
