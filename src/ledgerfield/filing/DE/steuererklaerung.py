"""Steuererklärung-Helfer für deutsche Rechtsträger (KStG / GewStG)."""
from __future__ import annotations
from dataclasses import dataclass
import json
import datetime

__all__ = [
    "Koerperschaftsteuererklaerung",
    "Gewerbesteuererklaerung",
    "erzeuge_koerperschaftsteuer",
    "erzeuge_gewerbesteuer",
]

# ---------------------------------------------------------------------------
# Körperschaftsteuer 2025 (KStG §23)
# Steuersatz: 15 % pauschal auf das zu versteuernde Einkommen
# Solidaritätszuschlag: 5,5 % der festgesetzten Körperschaftsteuer (SolzG)
#   → effektiver Bundessatz 15 % * 1,055 = 15,825 %
# ---------------------------------------------------------------------------
_KST_SATZ = 0.15
_SOLI_SATZ = 0.055

# ---------------------------------------------------------------------------
# Gewerbesteuer 2025 (GewStG)
# Steuermesszahl: 3,5 % auf den Gewerbeertrag → Steuermessbetrag
# Gewerbesteuer = Steuermessbetrag × Hebesatz der Gemeinde
#   (durchschnittlicher Hebesatz ~400 % → effektiv ~14 %)
# Freibetrag: 24.500 € für Einzelunternehmen/Personengesellschaften
#   (NICHT für Kapitalgesellschaften — daher standardmäßig 0).
# ---------------------------------------------------------------------------
_GEWST_MESSZAHL = 0.035
_GEWST_STANDARD_HEBESATZ = 4.00          # 400 %
_GEWST_FREIBETRAG_PERSONEN = 24_500.0


@dataclass
class Koerperschaftsteuererklaerung:
    """Körperschaftsteuererklärung (vereinfacht, KStG §23)."""
    unternehmen_id: str
    steuernummer: str
    jahr: int
    # Gewinn- und Verlustrechnung (vereinfacht)
    umsatz: float = 0.0
    umsatzkosten: float = 0.0
    bruttoergebnis: float = 0.0
    betriebsausgaben: float = 0.0
    betriebsergebnis: float = 0.0
    # Steuerliche Korrekturen
    nicht_abzugsfaehige_aufwendungen: float = 0.0
    steuerfreie_ertraege: float = 0.0
    zu_versteuerndes_einkommen: float = 0.0
    # Steuerberechnung
    koerperschaftsteuer: float = 0.0
    solidaritaetszuschlag: float = 0.0
    summe_koerperschaftsteuer: float = 0.0
    # Abgabefrist
    abgabefrist: str = ""

    def berechne(self) -> "Koerperschaftsteuererklaerung":
        """Alle abgeleiteten Felder neu berechnen."""
        # G+V
        self.bruttoergebnis = self.umsatz - self.umsatzkosten
        self.betriebsergebnis = self.bruttoergebnis - self.betriebsausgaben

        # Zu versteuerndes Einkommen (KStG §8)
        self.zu_versteuerndes_einkommen = max(
            0.0,
            self.betriebsergebnis
            + self.nicht_abzugsfaehige_aufwendungen
            - self.steuerfreie_ertraege,
        )

        # Körperschaftsteuer 15 % (KStG §23)
        self.koerperschaftsteuer = self.zu_versteuerndes_einkommen * _KST_SATZ
        # Solidaritätszuschlag 5,5 % der Körperschaftsteuer (SolzG)
        self.solidaritaetszuschlag = self.koerperschaftsteuer * _SOLI_SATZ
        self.summe_koerperschaftsteuer = (
            self.koerperschaftsteuer + self.solidaritaetszuschlag
        )

        # Abgabefrist: 31. Juli des Folgejahres (später mit Steuerberater)
        self.abgabefrist = f"{self.jahr + 1}-07-31"

        return self

    def to_dict(self) -> dict:
        return {
            "unternehmen_id": self.unternehmen_id,
            "steuernummer": self.steuernummer,
            "jahr": self.jahr,
            "umsatz": self.umsatz,
            "umsatzkosten": self.umsatzkosten,
            "bruttoergebnis": self.bruttoergebnis,
            "betriebsausgaben": self.betriebsausgaben,
            "betriebsergebnis": self.betriebsergebnis,
            "nicht_abzugsfaehige_aufwendungen": self.nicht_abzugsfaehige_aufwendungen,
            "steuerfreie_ertraege": self.steuerfreie_ertraege,
            "zu_versteuerndes_einkommen": self.zu_versteuerndes_einkommen,
            "koerperschaftsteuer": self.koerperschaftsteuer,
            "solidaritaetszuschlag": self.solidaritaetszuschlag,
            "summe_koerperschaftsteuer": self.summe_koerperschaftsteuer,
            "abgabefrist": self.abgabefrist,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML-Gerüst (OECD SAF-T DE, vereinfacht)."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:DE">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.steuernummer}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.jahr}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <Umsatz>{self.umsatz:.2f}</Umsatz>\n'
            f'    <Umsatzkosten>{self.umsatzkosten:.2f}</Umsatzkosten>\n'
            f'    <Bruttoergebnis>{self.bruttoergebnis:.2f}</Bruttoergebnis>\n'
            f'    <Betriebsausgaben>{self.betriebsausgaben:.2f}</Betriebsausgaben>\n'
            f'    <Betriebsergebnis>{self.betriebsergebnis:.2f}</Betriebsergebnis>\n'
            "  </GeneralLedger>\n"
            '  <TaxReturn type="KSt">\n'
            f'    <NichtAbzugsfaehigeAufwendungen>{self.nicht_abzugsfaehige_aufwendungen:.2f}</NichtAbzugsfaehigeAufwendungen>\n'
            f'    <SteuerfreieErtraege>{self.steuerfreie_ertraege:.2f}</SteuerfreieErtraege>\n'
            f'    <ZuVersteuerndesEinkommen>{self.zu_versteuerndes_einkommen:.2f}</ZuVersteuerndesEinkommen>\n'
            f'    <Koerperschaftsteuer>{self.koerperschaftsteuer:.2f}</Koerperschaftsteuer>\n'
            f'    <Solidaritaetszuschlag>{self.solidaritaetszuschlag:.2f}</Solidaritaetszuschlag>\n'
            f'    <SummeKoerperschaftsteuer>{self.summe_koerperschaftsteuer:.2f}</SummeKoerperschaftsteuer>\n'
            f'    <Abgabefrist>{self.abgabefrist}</Abgabefrist>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class Gewerbesteuererklaerung:
    """Gewerbesteuererklärung (vereinfacht, GewStG)."""
    unternehmen_id: str
    steuernummer: str
    jahr: int
    # Ausgangsgröße
    gewerbeertrag: float = 0.0
    # Kapitalgesellschaften haben KEINEN Freibetrag; Personenunternehmen 24.500 €.
    ist_personenunternehmen: bool = False
    freibetrag: float = 0.0
    hebesatz: float = _GEWST_STANDARD_HEBESATZ   # 4.00 = 400 %
    # Berechnung
    bereinigter_gewerbeertrag: float = 0.0
    messbetrag: float = 0.0
    gewerbesteuer: float = 0.0
    # Abgabefrist
    abgabefrist: str = ""

    def berechne(self) -> "Gewerbesteuererklaerung":
        """Alle abgeleiteten Felder neu berechnen."""
        # Freibetrag nur für Personenunternehmen (GewStG §11 Abs. 1)
        if self.ist_personenunternehmen and self.freibetrag == 0.0:
            self.freibetrag = _GEWST_FREIBETRAG_PERSONEN

        self.bereinigter_gewerbeertrag = max(
            0.0, self.gewerbeertrag - self.freibetrag
        )

        # Steuermessbetrag = bereinigter Gewerbeertrag × 3,5 %
        self.messbetrag = self.bereinigter_gewerbeertrag * _GEWST_MESSZAHL
        # Gewerbesteuer = Messbetrag × Hebesatz
        self.gewerbesteuer = self.messbetrag * self.hebesatz

        # Abgabefrist: 31. Juli des Folgejahres
        self.abgabefrist = f"{self.jahr + 1}-07-31"

        return self

    def to_dict(self) -> dict:
        return {
            "unternehmen_id": self.unternehmen_id,
            "steuernummer": self.steuernummer,
            "jahr": self.jahr,
            "gewerbeertrag": self.gewerbeertrag,
            "ist_personenunternehmen": self.ist_personenunternehmen,
            "freibetrag": self.freibetrag,
            "hebesatz": self.hebesatz,
            "bereinigter_gewerbeertrag": self.bereinigter_gewerbeertrag,
            "messbetrag": self.messbetrag,
            "gewerbesteuer": self.gewerbesteuer,
            "abgabefrist": self.abgabefrist,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML-Gerüst (OECD SAF-T DE, vereinfacht)."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:DE">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.steuernummer}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.jahr}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            '  <TaxReturn type="GewSt">\n'
            f'    <Gewerbeertrag>{self.gewerbeertrag:.2f}</Gewerbeertrag>\n'
            f'    <Freibetrag>{self.freibetrag:.2f}</Freibetrag>\n'
            f'    <BereinigterGewerbeertrag>{self.bereinigter_gewerbeertrag:.2f}</BereinigterGewerbeertrag>\n'
            f'    <Messbetrag>{self.messbetrag:.2f}</Messbetrag>\n'
            f'    <Hebesatz>{self.hebesatz:.2f}</Hebesatz>\n'
            f'    <Gewerbesteuer>{self.gewerbesteuer:.2f}</Gewerbesteuer>\n'
            f'    <Abgabefrist>{self.abgabefrist}</Abgabefrist>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


def erzeuge_koerperschaftsteuer(
    unternehmen_id: str,
    steuernummer: str,
    jahr: int,
    hauptbuch_daten: dict,
) -> Koerperschaftsteuererklaerung:
    """Körperschaftsteuererklärung aus G+V-Daten des Hauptbuchs erzeugen.

    hauptbuch_daten-Schlüssel (alle optional):
      umsatz, umsatzkosten, betriebsausgaben,
      nicht_abzugsfaehige_aufwendungen, steuerfreie_ertraege
    """
    erklaerung = Koerperschaftsteuererklaerung(
        unternehmen_id=unternehmen_id,
        steuernummer=steuernummer,
        jahr=jahr,
        umsatz=float(hauptbuch_daten.get("umsatz", 0.0)),
        umsatzkosten=float(hauptbuch_daten.get("umsatzkosten", 0.0)),
        betriebsausgaben=float(hauptbuch_daten.get("betriebsausgaben", 0.0)),
        nicht_abzugsfaehige_aufwendungen=float(
            hauptbuch_daten.get("nicht_abzugsfaehige_aufwendungen", 0.0)
        ),
        steuerfreie_ertraege=float(hauptbuch_daten.get("steuerfreie_ertraege", 0.0)),
    )
    return erklaerung.berechne()


def erzeuge_gewerbesteuer(
    unternehmen_id: str,
    steuernummer: str,
    jahr: int,
    hauptbuch_daten: dict,
) -> Gewerbesteuererklaerung:
    """Gewerbesteuererklärung aus Ertragsdaten des Hauptbuchs erzeugen.

    hauptbuch_daten-Schlüssel (alle optional):
      gewerbeertrag, hebesatz (Standard 4.00 = 400 %),
      ist_personenunternehmen (bool), freibetrag
    """
    erklaerung = Gewerbesteuererklaerung(
        unternehmen_id=unternehmen_id,
        steuernummer=steuernummer,
        jahr=jahr,
        gewerbeertrag=float(hauptbuch_daten.get("gewerbeertrag", 0.0)),
        ist_personenunternehmen=bool(
            hauptbuch_daten.get("ist_personenunternehmen", False)
        ),
        freibetrag=float(hauptbuch_daten.get("freibetrag", 0.0)),
        hebesatz=float(hauptbuch_daten.get("hebesatz", _GEWST_STANDARD_HEBESATZ)),
    )
    return erklaerung.berechne()
