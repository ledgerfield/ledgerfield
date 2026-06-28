"""SKR03 — Standardkontenrahmen 03, German chart of accounts for service/consulting.

~80 accounts covering Kontenklassen 0–4 and 8, as used by German GmbH/service companies.
"""
from __future__ import annotations
from dataclasses import dataclass

__all__ = ["SKR03Account", "SKR03_DE", "get_account", "accounts_by_class"]


@dataclass(frozen=True)
class SKR03Account:
    code: str          # 4-digit Kontonummer
    name: str          # German account name
    klasse: int        # Kontenklasse (0-9)
    statement: str     # "Bilanz" or "GuV"
    category: str      # e.g. "Anlagevermögen", "Umlaufvermögen", "Eigenkapital", ...
    vat_relevant: bool = False   # whether VAT applies in typical bookings

    @property
    def is_asset(self) -> bool:
        return self.statement == "Bilanz" and self.category in (
            "Anlagevermögen", "Umlaufvermögen"
        )

    @property
    def is_liability(self) -> bool:
        return self.statement == "Bilanz" and self.category in (
            "Eigenkapital", "Verbindlichkeiten", "Rückstellungen"
        )

    @property
    def is_revenue(self) -> bool:
        return self.statement == "GuV" and self.category == "Umsatzerlöse"

    @property
    def is_expense(self) -> bool:
        return self.statement == "GuV" and self.category in (
            "Personalaufwand", "Betrieblicher Aufwand", "Abschreibungen",
            "Finanzaufwand", "Steueraufwand"
        )


SKR03_DE: list[SKR03Account] = [
    # ── Klasse 0: Anlagevermögen ─────────────────────────────────────────────
    SKR03Account("0100", "Immaterielle Vermögensgegenstände",           0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0120", "Konzessionen, Lizenzen, ähnliche Rechte",     0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0140", "Selbst erstellte Software",                   0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0190", "Geschäftswert (Firmenwert)",                  0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0200", "Grundstücke und Gebäude",                     0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0210", "Grundstücke ohne Gebäude",                    0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0400", "Technische Anlagen und Maschinen",            0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0410", "Betriebs- und Geschäftsausstattung",          0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0420", "Büromaschinen, EDV-Anlagen",                  0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0490", "Geringwertige Wirtschaftsgüter (GWG)",        0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0500", "Finanzanlagen",                               0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0510", "Anteile an verbundenen Unternehmen",          0, "Bilanz", "Anlagevermögen"),
    SKR03Account("0560", "Wertpapiere des Anlagevermögens",             0, "Bilanz", "Anlagevermögen"),

    # ── Klasse 1: Umlaufvermögen ─────────────────────────────────────────────
    SKR03Account("1000", "Kasse",                                       1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1200", "Forderungen aus Lieferungen und Leistungen",  1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1210", "Forderungen gegen verbundene Unternehmen",    1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1400", "Sonstige Vermögensgegenstände",               1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1410", "Forderungen Finanzamt (USt-Guthaben)",        1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1460", "Geleistete Anzahlungen",                      1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1600", "Vorräte / Waren",                             1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1800", "Bank",                                        1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1810", "Kasse (Handkasse)",                           1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1820", "Geldtransit",                                 1, "Bilanz", "Umlaufvermögen"),
    SKR03Account("1900", "Aktive Rechnungsabgrenzung (ARAP)",           1, "Bilanz", "Umlaufvermögen"),

    # ── Klasse 2: Eigenkapital / Rücklagen ───────────────────────────────────
    SKR03Account("2000", "Eigenkapital",                                2, "Bilanz", "Eigenkapital"),
    SKR03Account("2010", "Gezeichnetes Kapital (Stammkapital)",         2, "Bilanz", "Eigenkapital"),
    SKR03Account("2030", "Ausstehende Einlagen",                        2, "Bilanz", "Eigenkapital"),
    SKR03Account("2100", "Kapitalrücklage",                             2, "Bilanz", "Eigenkapital"),
    SKR03Account("2110", "Gesetzliche Rücklage",                        2, "Bilanz", "Eigenkapital"),
    SKR03Account("2120", "Andere Gewinnrücklagen",                      2, "Bilanz", "Eigenkapital"),
    SKR03Account("2700", "Jahresüberschuss / Jahresfehlbetrag",         2, "Bilanz", "Eigenkapital"),
    SKR03Account("2900", "Passive Rechnungsabgrenzung (PRAP)",          2, "Bilanz", "Eigenkapital"),

    # ── Klasse 3: Verbindlichkeiten / Rückstellungen ─────────────────────────
    SKR03Account("3000", "Rückstellungen",                              3, "Bilanz", "Rückstellungen"),
    SKR03Account("3010", "Rückstellungen für Pensionen",                3, "Bilanz", "Rückstellungen"),
    SKR03Account("3040", "Steuerrückstellungen",                        3, "Bilanz", "Rückstellungen"),
    SKR03Account("3050", "Sonstige Rückstellungen",                     3, "Bilanz", "Rückstellungen"),
    SKR03Account("3200", "Verbindlichkeiten gegenüber Kreditinstituten",3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3300", "Erhaltene Anzahlungen",                       3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3400", "Verbindlichkeiten aus Lieferungen und Leistungen", 3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3500", "Verbindlichkeiten gegenüber Finanzamt (USt)", 3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3510", "Umsatzsteuer (laufendes Jahr)",               3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3520", "Körperschaftsteuer-Verbindlichkeit",          3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3540", "Lohnsteuer-Verbindlichkeit",                  3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3550", "Sozialversicherungsbeiträge (AN-Anteil)",     3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3600", "Verbindlichkeiten gegenüber Gesellschaftern", 3, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("3720", "Sonstige Verbindlichkeiten",                  3, "Bilanz", "Verbindlichkeiten"),

    # ── Klasse 4: Betriebliche Aufwendungen (GuV) ────────────────────────────
    # Personalaufwand
    SKR03Account("4100", "Löhne und Gehälter",                          4, "GuV", "Personalaufwand"),
    SKR03Account("4110", "Gehälter",                                    4, "GuV", "Personalaufwand"),
    SKR03Account("4120", "Löhne",                                       4, "GuV", "Personalaufwand"),
    SKR03Account("4130", "Gesetzliche soziale Aufwendungen (AG-Anteil)",4, "GuV", "Personalaufwand"),
    SKR03Account("4140", "Freiwillige soziale Aufwendungen",            4, "GuV", "Personalaufwand"),
    SKR03Account("4150", "Aushilfslöhne",                               4, "GuV", "Personalaufwand"),

    # Raumkosten
    SKR03Account("4200", "Raumkosten",                                  4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4210", "Miete / Pacht",                               4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4230", "Heizung / Strom / Wasser",                    4, "GuV", "Betrieblicher Aufwand"),

    # Fahrzeugkosten
    SKR03Account("4300", "Kfz-Kosten (ohne Steuer/Versicherung)",       4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4360", "Kfz-Leasing",                                 4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4380", "Kfz-Steuer und Kfz-Versicherung",             4, "GuV", "Betrieblicher Aufwand"),

    # Marketing / Vertrieb
    SKR03Account("4400", "Werbekosten",                                 4, "GuV", "Betrieblicher Aufwand", True),
    SKR03Account("4410", "Messen und Ausstellungen",                    4, "GuV", "Betrieblicher Aufwand", True),

    # Reise / Bewirtung
    SKR03Account("4530", "Reisekosten",                                 4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4540", "Bewirtungskosten (70 % abzugsfähig)",         4, "GuV", "Betrieblicher Aufwand"),

    # Verwaltung
    SKR03Account("4570", "Buchführungskosten / Steuerberatung",         4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4580", "Bürobedarf",                                  4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4590", "Zeitschriften, Fachliteratur",                4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4630", "Telefon, Telefax, Internet",                  4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4660", "Beiträge und Abgaben",                        4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4700", "Versicherungen",                              4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4730", "Aufwendungen für Rechts- und Beratungskosten",4, "GuV", "Betrieblicher Aufwand"),

    # Abschreibungen (in SKR03 under Klasse 4)
    SKR03Account("4810", "Abschreibungen auf immaterielle Anlagegüter", 4, "GuV", "Abschreibungen"),
    SKR03Account("4820", "Abschreibungen auf Sachanlagen",              4, "GuV", "Abschreibungen"),
    SKR03Account("4830", "Abschreibungen auf GWG",                      4, "GuV", "Abschreibungen"),

    # Finanz- und Steueraufwand (Klasse 4)
    SKR03Account("4900", "Sonstige betriebliche Aufwendungen",          4, "GuV", "Betrieblicher Aufwand"),
    SKR03Account("4930", "Zinsaufwendungen",                            4, "GuV", "Finanzaufwand"),
    SKR03Account("4960", "Körperschaftsteuer",                          4, "GuV", "Steueraufwand"),
    SKR03Account("4964", "Solidaritätszuschlag",                        4, "GuV", "Steueraufwand"),
    SKR03Account("4970", "Gewerbesteuer",                               4, "GuV", "Steueraufwand"),

    # ── Klasse 8: Erlöse / Umsatzerlöse (GuV) ───────────────────────────────
    SKR03Account("8000", "Umsatzerlöse 19 % (Inland)",                  8, "GuV", "Umsatzerlöse", True),
    SKR03Account("8010", "Umsatzerlöse 7 % (Inland, ermäßigt)",         8, "GuV", "Umsatzerlöse", True),
    SKR03Account("8100", "Umsatzerlöse EU (innergemeinschaftlich)",      8, "GuV", "Umsatzerlöse", True),
    SKR03Account("8120", "Umsatzerlöse EU (ohne USt, § 4 Nr. 1b UStG)", 8, "GuV", "Umsatzerlöse"),
    SKR03Account("8200", "Umsatzerlöse Drittland (Export)",             8, "GuV", "Umsatzerlöse"),
    SKR03Account("8300", "Provisionserlöse",                            8, "GuV", "Umsatzerlöse", True),
    SKR03Account("8400", "Sonstige betriebliche Erträge",               8, "GuV", "Umsatzerlöse"),
    SKR03Account("8510", "Zinserträge",                                  8, "GuV", "Umsatzerlöse"),
    SKR03Account("8600", "Erträge aus Anlagenabgängen",                  8, "GuV", "Umsatzerlöse"),

    # ── Klasse 9: Kapitalkonten / Verrechnungskonten ─────────────────────────
    SKR03Account("9000", "Saldenvortragskonten",                         9, "Bilanz", "Eigenkapital"),
    SKR03Account("9800", "Umsatzsteuer-Voranmeldung (Verrechnung)",      9, "Bilanz", "Verbindlichkeiten"),
    SKR03Account("9810", "Vorsteuer (Verrechnung)",                      9, "Bilanz", "Umlaufvermögen"),
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def get_account(code: str) -> SKR03Account | None:
    """Return account by 4-digit Kontonummer, or None."""
    for acc in SKR03_DE:
        if acc.code == code:
            return acc
    return None


def accounts_by_class(klasse: int) -> list[SKR03Account]:
    """Return all accounts for the given Kontenklasse (0-9)."""
    return [a for a in SKR03_DE if a.klasse == klasse]
