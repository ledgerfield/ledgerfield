"""Chart of accounts — Norway (Norwegian GAAP, NRS/IFRS)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class NOAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

NO_ACCOUNTS: dict[str, NOAccount] = {
    # Eiendeler (Assets)
    "1010": NOAccount("1010", "Kontanter og Bank (Cash / Bank)", "asset"),
    "1020": NOAccount("1020", "Kundefordringer (Accounts Receivable)", "asset"),
    "1030": NOAccount("1030", "Varelager (Inventory)", "asset"),
    "1040": NOAccount("1040", "Forskuddsbetalte Kostnader (Prepaid Expenses)", "asset"),
    "1050": NOAccount("1050", "Varige Driftsmidler (Fixed Assets)", "asset"),
    "1060": NOAccount("1060", "Immaterielle Eiendeler (Intangible Assets)", "asset"),
    "1070": NOAccount("1070", "Inngående MVA (VAT Receivable)", "asset"),
    # Gjeld (Liabilities)
    "2010": NOAccount("2010", "Leverandørgjeld (Accounts Payable)", "liability"),
    "2020": NOAccount("2020", "Betalbar Selskapsskatt (Corporate Tax Payable)", "liability"),
    "2030": NOAccount("2030", "Utgående MVA (VAT Payable)", "liability"),
    "2040": NOAccount("2040", "Skattetrekk / Arbeidsgiveravgift (Payroll Tax Payable)", "liability"),
    "2050": NOAccount("2050", "Trygdeavgift / NAV-bidrag (Social Insurance Payable)", "liability"),
    "2060": NOAccount("2060", "Langsiktig Gjeld (Long-term Loans)", "liability"),
    # Egenkapital (Equity)
    "3010": NOAccount("3010", "Aksjekapital (Share Capital)", "equity"),
    "3020": NOAccount("3020", "Opptjent Egenkapital (Retained Earnings)", "equity"),
    "3030": NOAccount("3030", "Årets Resultat (Current Year Profit)", "equity"),
    # Inntekter (Revenue)
    "4010": NOAccount("4010", "Salgsinntekter (Sales Revenue)", "revenue"),
    "4020": NOAccount("4020", "Tjenesteinntekter (Service Revenue)", "revenue"),
    "4030": NOAccount("4030", "Andre Inntekter (Other Income)", "revenue"),
    # Kostnader (Expenses)
    "5010": NOAccount("5010", "Varekostnad (Cost of Goods Sold)", "expense"),
    "5020": NOAccount("5020", "Lønn og Honorarer (Salaries & Wages)", "expense"),
    "5030": NOAccount("5030", "Arbeidsgiveravgift (Employer Social Insurance)", "expense"),
    "5040": NOAccount("5040", "Leie og Driftskostnader (Rent & Utilities)", "expense"),
    "5050": NOAccount("5050", "Konsulenthonorarer (Professional Fees)", "expense"),
    "5060": NOAccount("5060", "Avskrivninger (Depreciation)", "expense"),
    "5070": NOAccount("5070", "Selskapsskatt Kostnad (Corporate Income Tax Expense)", "expense"),
    "5080": NOAccount("5080", "MVA / Indirekte Skatt (VAT/Indirect Tax Expense)", "expense"),
}

get_account = NO_ACCOUNTS.get
