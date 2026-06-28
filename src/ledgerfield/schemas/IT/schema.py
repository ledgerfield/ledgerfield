"""Italian OIC (Organismo Italiano di Contabilità) chart of accounts.

Based on the standard Italian piano dei conti as defined by OIC principles.
Used by S.p.A., S.r.l. and other entities subject to Italian Civil Code art. 2423-2435-ter.

CIT = IRES 24% + IRAP 3.9%. VAT (IVA) = 22% standard rate.
"""
from __future__ import annotations
from dataclasses import dataclass

__all__ = ["OICAccount", "OIC_IT", "get_account", "accounts_by_category"]


@dataclass(frozen=True)
class OICAccount:
    code: str
    name: str
    category: str      # Attivo | Passivo | Patrimonio netto | Ricavi | Costi
    subcategory: str
    normal_balance: str  # Dare | Avere
    iva_relevant: bool = False

    @property
    def is_asset(self) -> bool:
        return self.category == "Attivo"

    @property
    def is_liability(self) -> bool:
        return self.category in ("Passivo", "Patrimonio netto")

    @property
    def is_revenue(self) -> bool:
        return self.category == "Ricavi"

    @property
    def is_cost(self) -> bool:
        return self.category == "Costi"


OIC_IT: list[OICAccount] = [
    # Immobilizzazioni immateriali
    OICAccount("B.I.1",   "Costi di impianto e ampliamento",               "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.2",   "Costi di sviluppo",                             "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.3",   "Diritti di brevetto e opere dell ingegno",      "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.4",   "Concessioni, licenze, marchi",                  "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.5",   "Avviamento",                                    "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.6",   "Immobilizzazioni in corso (immat.)",            "Attivo", "Immobilizzazioni immateriali", "Dare"),
    # Immobilizzazioni materiali
    OICAccount("B.II.1",  "Terreni e fabbricati",                          "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.2",  "Impianti e macchinari",                         "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.3",  "Attrezzature industriali e commerciali",        "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.4",  "Altri beni materiali",                          "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.5",  "Immobilizzazioni in corso (mat.)",              "Attivo", "Immobilizzazioni materiali",   "Dare"),
    # Immobilizzazioni finanziarie
    OICAccount("B.III.1", "Partecipazioni in imprese controllate",         "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.2", "Partecipazioni in imprese collegate",           "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.3", "Partecipazioni in imprese controllanti",        "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.4", "Crediti finanziari a lungo termine",            "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.5", "Titoli immobilizzati",                          "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    # Rimanenze
    OICAccount("C.I.1",   "Materie prime, sussidiarie e di consumo",       "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.2",   "Prodotti in lavorazione e semilavorati",        "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.3",   "Lavori in corso su ordinazione",                "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.4",   "Prodotti finiti e merci",                       "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.5",   "Acconti su acquisti",                           "Attivo", "Rimanenze",                    "Dare"),
    # Crediti
    OICAccount("C.II.1",  "Crediti verso clienti",                         "Attivo", "Crediti",                      "Dare", True),
    OICAccount("C.II.2",  "Crediti verso imprese controllate",             "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.3",  "Crediti verso imprese collegate",               "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.4",  "Crediti verso controllanti",                    "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.5",  "Crediti tributari",                             "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.6",  "Imposte anticipate (IRES/IRAP)",               "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.7",  "Crediti verso altri",                           "Attivo", "Crediti",                      "Dare"),
    # Attivita finanziarie
    OICAccount("C.III.1", "Partecipazioni circolanti controllate",         "Attivo", "Attivita finanziarie",         "Dare"),
    OICAccount("C.III.2", "Altre partecipazioni circolanti",               "Attivo", "Attivita finanziarie",         "Dare"),
    OICAccount("C.III.3", "Altri titoli",                                  "Attivo", "Attivita finanziarie",         "Dare"),
    OICAccount("C.III.4", "Azioni proprie (treasury shares)",              "Attivo", "Attivita finanziarie",         "Dare"),
    # Disponibilita liquide
    OICAccount("C.IV.1",  "Depositi bancari e postali",                    "Attivo", "Disponibilita liquide",        "Dare"),
    OICAccount("C.IV.2",  "Assegni",                                       "Attivo", "Disponibilita liquide",        "Dare"),
    OICAccount("C.IV.3",  "Denaro e valori in cassa",                      "Attivo", "Disponibilita liquide",        "Dare"),
    # Ratei e risconti attivi
    OICAccount("D.att.1", "Ratei attivi",                                  "Attivo", "Ratei e risconti attivi",      "Dare"),
    OICAccount("D.att.2", "Risconti attivi",                               "Attivo", "Ratei e risconti attivi",      "Dare"),
    # Patrimonio netto
    OICAccount("A.I",     "Capitale sociale",                              "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.II",    "Riserva da sovrapprezzo azioni",                "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.III",   "Riserva di rivalutazione",                      "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.IV",    "Riserva legale",                                "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.V",     "Riserve statutarie",                            "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.VI",    "Altre riserve",                                 "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.VII",   "Riserva per operazioni di copertura",           "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.VIII",  "Utili (perdite) portati a nuovo",               "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.IX",    "Utile (perdita) dell esercizio",                "Patrimonio netto", "Patrimonio netto",   "Avere"),
    # Fondi per rischi e oneri
    OICAccount("B.fon.1", "Fondi per rischi e oneri futuri (pensioni)",   "Passivo", "Fondi per rischi e oneri",    "Avere"),
    OICAccount("B.fon.2", "Fondi per imposte",                             "Passivo", "Fondi per rischi e oneri",    "Avere"),
    OICAccount("B.fon.3", "Strumenti finanziari derivati passivi",         "Passivo", "Fondi per rischi e oneri",    "Avere"),
    OICAccount("B.fon.4", "Altri fondi",                                   "Passivo", "Fondi per rischi e oneri",    "Avere"),
    # TFR
    OICAccount("C.tfr",   "Trattamento di fine rapporto (TFR)",            "Passivo", "TFR",                         "Avere"),
    # Debiti
    OICAccount("D.pas.1", "Obbligazioni",                                  "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.2", "Obbligazioni convertibili",                     "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.3", "Debiti verso soci per finanziamenti",           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.4", "Debiti verso banche",                           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.5", "Debiti verso altri finanziatori",               "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.6", "Acconti da clienti",                            "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.7", "Debiti verso fornitori",                        "Passivo", "Debiti",                      "Avere", True),
    OICAccount("D.pas.8", "Debiti verso imprese controllate",              "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.9", "Debiti verso imprese collegate",                "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.10","Debiti verso controllanti",                     "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.11","Debiti tributari (IRES, IRAP, IVA)",           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.12","Debiti verso istituti di previdenza",           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.pas.13","Altri debiti",                                  "Passivo", "Debiti",                      "Avere"),
    # Ratei e risconti passivi
    OICAccount("E.1",     "Ratei passivi",                                 "Passivo", "Ratei e risconti passivi",    "Avere"),
    OICAccount("E.2",     "Risconti passivi",                              "Passivo", "Ratei e risconti passivi",    "Avere"),
    # Ricavi
    OICAccount("A.CE.1",  "Ricavi delle vendite e delle prestazioni",      "Ricavi",  "Valore della produzione",     "Avere", True),
    OICAccount("A.CE.2",  "Variazione delle rimanenze prodotti",           "Ricavi",  "Valore della produzione",     "Avere"),
    OICAccount("A.CE.3",  "Variazione dei lavori in corso su ordinazione", "Ricavi",  "Valore della produzione",     "Avere"),
    OICAccount("A.CE.4",  "Incrementi di immobilizzazioni per lavori int.","Ricavi",  "Valore della produzione",     "Avere"),
    OICAccount("A.CE.5",  "Altri ricavi e proventi",                       "Ricavi",  "Valore della produzione",     "Avere"),
    # Costi della produzione
    OICAccount("B.CE.6",  "Materie prime, sussidiarie, consumo e merci",   "Costi",   "Costi della produzione",      "Dare",  True),
    OICAccount("B.CE.7",  "Servizi",                                       "Costi",   "Costi della produzione",      "Dare",  True),
    OICAccount("B.CE.8",  "Godimento di beni di terzi",                    "Costi",   "Costi della produzione",      "Dare",  True),
    OICAccount("B.CE.9a", "Salari e stipendi",                             "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.CE.9b", "Oneri sociali",                                 "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.CE.9c", "Trattamento di fine rapporto (costo)",          "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.CE.9d", "Trattamento di quiescenza",                     "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.CE.9e", "Altri costi del personale",                     "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.CE.10a","Ammortamento immobilizzazioni immateriali",     "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.CE.10b","Ammortamento immobilizzazioni materiali",       "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.CE.10c","Altre svalutazioni delle immobilizzazioni",     "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.CE.10d","Svalutazione dei crediti circolanti",           "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.CE.11", "Variazione delle rimanenze mat. prime",         "Costi",   "Costi della produzione",      "Dare"),
    OICAccount("B.CE.12", "Accantonamento per rischi",                     "Costi",   "Accantonamenti",              "Dare"),
    OICAccount("B.CE.13", "Altri accantonamenti",                          "Costi",   "Accantonamenti",              "Dare"),
    OICAccount("B.CE.14", "Oneri diversi di gestione",                     "Costi",   "Costi della produzione",      "Dare"),
    # Gestione finanziaria
    OICAccount("C.CE.15", "Proventi da partecipazioni",                    "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.CE.16a","Proventi da crediti finanziari imm.",           "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.CE.16b","Proventi da titoli immobilizzati",              "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.CE.16c","Proventi da titoli circolanti",                 "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.CE.16d","Proventi diversi dai precedenti",               "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.CE.17", "Interessi e altri oneri finanziari",            "Costi",   "Proventi e oneri finanziari", "Dare"),
    OICAccount("C.CE.17b","Utili e perdite su cambi",                      "Costi",   "Proventi e oneri finanziari", "Dare"),
    # Imposte
    OICAccount("22",      "Imposte sul reddito IRES corrente",             "Costi",   "Imposte",                     "Dare"),
    OICAccount("23",      "IRAP corrente",                                 "Costi",   "Imposte",                     "Dare"),
    OICAccount("24",      "Imposte anticipate/differite (IRES)",           "Costi",   "Imposte",                     "Dare"),
]


def get_account(code: str) -> OICAccount | None:
    """Return OICAccount by code, or None if not found."""
    for acc in OIC_IT:
        if acc.code == code:
            return acc
    return None


def accounts_by_category(category: str) -> list[OICAccount]:
    """Return all accounts matching category."""
    return [a for a in OIC_IT if a.category == category]
