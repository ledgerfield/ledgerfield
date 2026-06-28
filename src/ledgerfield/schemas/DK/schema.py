"""Chart of accounts — Denmark (Danish GAAP, ÅRL/IFRS)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class DKAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

DK_ACCOUNTS: dict[str, DKAccount] = {
    # Aktiver (Assets)
    "1010": DKAccount("1010", "Likvide Midler / Bank (Cash / Bank)", "asset"),
    "1020": DKAccount("1020", "Tilgodehavender fra Salg (Accounts Receivable)", "asset"),
    "1030": DKAccount("1030", "Varebeholdninger (Inventory)", "asset"),
    "1040": DKAccount("1040", "Forudbetalte Udgifter (Prepaid Expenses)", "asset"),
    "1050": DKAccount("1050", "Materielle Anlægsaktiver (Fixed Assets)", "asset"),
    "1060": DKAccount("1060", "Immaterielle Anlægsaktiver (Intangible Assets)", "asset"),
    "1070": DKAccount("1070", "Indgående Moms (VAT Receivable)", "asset"),
    # Passiver / Gæld (Liabilities)
    "2010": DKAccount("2010", "Leverandørgæld (Accounts Payable)", "liability"),
    "2020": DKAccount("2020", "Skyldig Selskabsskat (Corporate Tax Payable)", "liability"),
    "2030": DKAccount("2030", "Udgående Moms (VAT Payable)", "liability"),
    "2040": DKAccount("2040", "A-skat / AM-bidrag (Payroll Tax Payable)", "liability"),
    "2050": DKAccount("2050", "ATP / Socialsikring (Social Insurance Payable)", "liability"),
    "2060": DKAccount("2060", "Langfristet Gæld (Long-term Loans)", "liability"),
    # Egenkapital (Equity)
    "3010": DKAccount("3010", "Aktiekapital (Share Capital)", "equity"),
    "3020": DKAccount("3020", "Overført Overskud (Retained Earnings)", "equity"),
    "3030": DKAccount("3030", "Årets Resultat (Current Year Profit)", "equity"),
    # Omsætning (Revenue)
    "4010": DKAccount("4010", "Nettoomsætning (Sales Revenue)", "revenue"),
    "4020": DKAccount("4020", "Serviceindtægter (Service Revenue)", "revenue"),
    "4030": DKAccount("4030", "Andre Indtægter (Other Income)", "revenue"),
    # Omkostninger (Expenses)
    "5010": DKAccount("5010", "Vareforbruget (Cost of Goods Sold)", "expense"),
    "5020": DKAccount("5020", "Lønninger og Gager (Salaries & Wages)", "expense"),
    "5030": DKAccount("5030", "Arbejdsgiverbidrag (Employer Social Insurance)", "expense"),
    "5040": DKAccount("5040", "Husleje og Forsyninger (Rent & Utilities)", "expense"),
    "5050": DKAccount("5050", "Rådgivningshonorar (Professional Fees)", "expense"),
    "5060": DKAccount("5060", "Afskrivninger (Depreciation)", "expense"),
    "5070": DKAccount("5070", "Selskabsskat Omkostning (Corporate Income Tax Expense)", "expense"),
    "5080": DKAccount("5080", "Moms / Indirekte Skat (VAT/Indirect Tax Expense)", "expense"),
}

get_account = DK_ACCOUNTS.get
