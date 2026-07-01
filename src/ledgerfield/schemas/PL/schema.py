"""Chart of accounts — Poland (Polish GAAP / UoR).

Based on the Polish Accounting Act (Ustawa o rachunkowosci) chart of accounts.
Covers the principal account groups for sp. z o.o. and S.A. entities.
"""
from dataclasses import dataclass

__all__ = ["PLAccount", "PL_ACCOUNTS", "get_account", "accounts_by_type"]


@dataclass(frozen=True)
class PLAccount:
    code: str
    name: str
    account_type: str  # "asset", "liability", "equity", "revenue", "expense"


PL_ACCOUNTS: dict[str, PLAccount] = {
    # Aktywa / Assets
    "1010": PLAccount("1010", "Kasa / Rachunek bankowy", "asset"),
    "1020": PLAccount("1020", "Naleznosci od odbiorcow", "asset"),
    "1030": PLAccount("1030", "Zapasy / Towary", "asset"),
    "1040": PLAccount("1040", "Rozliczenia miedzyokresowe czynne", "asset"),
    "1050": PLAccount("1050", "Srodki trwale", "asset"),
    "1060": PLAccount("1060", "Wartosci niematerialne i prawne", "asset"),
    "1070": PLAccount("1070", "VAT naliczony", "asset"),
    # Pasywa — Zobowiazania / Liabilities
    "2010": PLAccount("2010", "Zobowiazania wobec dostawcow", "liability"),
    "2020": PLAccount("2020", "Podatek dochodowy od osob prawnych (CIT)", "liability"),
    "2030": PLAccount("2030", "VAT nalezny", "liability"),
    "2040": PLAccount("2040", "Zobowiazania z tytulu podatku PIT pracownikow", "liability"),
    "2050": PLAccount("2050", "Skladki ZUS", "liability"),
    "2060": PLAccount("2060", "Kredyty dlugoterminowe", "liability"),
    # Kapital wlasny / Equity
    "3010": PLAccount("3010", "Kapital zakladowy", "equity"),
    "3020": PLAccount("3020", "Zysk zatrzymany", "equity"),
    "3030": PLAccount("3030", "Wynik finansowy biezacego roku", "equity"),
    # Przychody / Revenue
    "4010": PLAccount("4010", "Przychody ze sprzedazy towarow", "revenue"),
    "4020": PLAccount("4020", "Przychody ze sprzedazy uslug", "revenue"),
    "4030": PLAccount("4030", "Pozostale przychody operacyjne", "revenue"),
    # Koszty / Expenses
    "5010": PLAccount("5010", "Koszt wlasny sprzedazy", "expense"),
    "5020": PLAccount("5020", "Wynagrodzenia", "expense"),
    "5030": PLAccount("5030", "Skladki ZUS pracodawcy", "expense"),
    "5040": PLAccount("5040", "Czynsz i media", "expense"),
    "5050": PLAccount("5050", "Uslugi zewnetrzne", "expense"),
    "5060": PLAccount("5060", "Amortyzacja", "expense"),
    "5070": PLAccount("5070", "Podatek dochodowy (CIT)", "expense"),
    "5080": PLAccount("5080", "Podatek VAT / posredni", "expense"),
}


def get_account(code: str) -> PLAccount | None:
    return PL_ACCOUNTS.get(code)


def accounts_by_type(account_type: str) -> list[PLAccount]:
    return [a for a in PL_ACCOUNTS.values() if a.account_type == account_type]
