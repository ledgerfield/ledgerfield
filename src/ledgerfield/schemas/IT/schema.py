"""Italian OIC (Organismo Italiano di Contabilità) chart of accounts.

Based on the standard Italian piano dei conti (chart of accounts) as defined by
OIC (Organismo Italiano di Contabilità) principles. Used by Italian S.p.A., S.r.l.,
and other entities subject to Italian Civil Code art. 2423–2435-ter.

CIT = IRES 24% + IRAP 3.9% (regional production tax).
VAT (IVA) = 22% standard rate (also 10%, 5%, 4% reduced rates).
"""
from __future__ import annotations
from dataclasses import dataclass


__all__ = ["OICAccount", "OIC_IT", "get_account", "accounts_by_category"]


@dataclass(frozen=True)
class OICAccount:
    code: str          # Italian account code (e.g. "1.1.10")
    name: str          # Italian/English account name
    category: str      # Attivo | Passivo | Patrimonio netto | Ricavi | Costi
    subcategory: str   # e.g. "Immobilizzazioni", "Disponibilità liquide", ...
    normal_balance: str  # Dare (Debit) | Avere (Credit)
    iva_relevant: bool = False  # whether IVA (VAT) applies in typical bookings

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
    # ── ATTIVO — IMMOBILIZZAZIONI (Fixed Assets) ──────────────────────────────
    OICAccount("B.I.1",   "Costi di impianto e ampliamento",               "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.2",   "Costi di sviluppo",                             "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.3",   "Diritti di brevetto e opere dell'ingegno",      "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.4",   "Concessioni, licenze, marchi",                  "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.5",   "Avviamento",                                    "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.I.6",   "Immobilizzazioni in corso e acconti (immat.)",  "Attivo", "Immobilizzazioni immateriali", "Dare"),
    OICAccount("B.II.1",  "Terreni e fabbricati",                          "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.2",  "Impianti e macchinari",                         "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.3",  "Attrezzature industriali e commerciali",        "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.4",  "Altri beni materiali",                          "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.II.5",  "Immobilizzazioni in corso e acconti (mat.)",    "Attivo", "Immobilizzazioni materiali",   "Dare"),
    OICAccount("B.III.1", "Partecipazioni in imprese controllate",         "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.2", "Partecipazioni in imprese collegate",           "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.3", "Partecipazioni in imprese controllanti",        "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.4", "Crediti finanziari a lungo termine",            "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    OICAccount("B.III.5", "Titoli immobilizzati",                          "Attivo", "Immobilizzazioni finanziarie", "Dare"),
    # ── ATTIVO — ATTIVO CIRCOLANTE (Current Assets) ───────────────────────────
    OICAccount("C.I.1",   "Materie prime, sussidiarie e di consumo",       "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.2",   "Prodotti in lavorazione e semilavorati",        "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.3",   "Lavori in corso su ordinazione",                "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.4",   "Prodotti finiti e merci",                       "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.I.5",   "Acconti su acquisti",                           "Attivo", "Rimanenze",                    "Dare"),
    OICAccount("C.II.1",  "Crediti verso clienti",                         "Attivo", "Crediti",                      "Dare", True),
    OICAccount("C.II.2",  "Crediti verso imprese controllate",             "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.3",  "Crediti verso imprese collegate",               "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.4",  "Crediti verso controllanti",                    "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.5",  "Crediti tributari",                             "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.6",  "Imposte anticipate (IRES/IRAP)",                "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.II.7",  "Crediti verso altri",                           "Attivo", "Crediti",                      "Dare"),
    OICAccount("C.III.1", "Partecipazioni in imprese controllate (circ.)", "Attivo", "Attività finanziarie",         "Dare"),
    OICAccount("C.III.2", "Altre partecipazioni (circ.)",                  "Attivo", "Attività finanziarie",         "Dare"),
    OICAccount("C.III.3", "Altri titoli",                                  "Attivo", "Attività finanziarie",         "Dare"),
    OICAccount("C.III.4", "Azioni proprie (treasury shares)",              "Attivo", "Attività finanziarie",         "Dare"),
    OICAccount("C.IV.1",  "Depositi bancari e postali",                    "Attivo", "Disponibilità liquide",        "Dare"),
    OICAccount("C.IV.2",  "Assegni",                                       "Attivo", "Disponibilità liquide",        "Dare"),
    OICAccount("C.IV.3",  "Denaro e valori in cassa",                      "Attivo", "Disponibilità liquide",        "Dare"),
    # ── ATTIVO — RATEI E RISCONTI ─────────────────────────────────────────────
    OICAccount("D.1",     "Ratei attivi",                                  "Attivo", "Ratei e risconti attivi",      "Dare"),
    OICAccount("D.2",     "Risconti attivi",                               "Attivo", "Ratei e risconti attivi",      "Dare"),
    # ── PASSIVO — PATRIMONIO NETTO (Equity) ───────────────────────────────────
    OICAccount("A.I",     "Capitale sociale",                              "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.II",    "Riserva da sovrapprezzo azioni",                "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.III",   "Riserva di rivalutazione",                      "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.IV",    "Riserva legale",                                "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.V",     "Riserve statutarie",                            "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.VI",    "Altre riserve",                                 "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.VII",   "Riserva per operazioni di copertura",           "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.VIII",  "Utili (perdite) portati a nuovo",               "Patrimonio netto", "Patrimonio netto",   "Avere"),
    OICAccount("A.IX",    "Utile (perdita) dell'esercizio",                "Patrimonio netto", "Patrimonio netto",   "Avere"),
    # ── PASSIVO — FONDI (Provisions) ─────────────────────────────────────────
    OICAccount("B.1",     "Fondi per rischi e oneri futuri (pensioni)",    "Passivo", "Fondi per rischi e oneri",    "Avere"),
    OICAccount("B.2",     "Fondi per imposte",                             "Passivo", "Fondi per rischi e oneri",    "Avere"),
    OICAccount("B.3",     "Strumenti finanziari derivati passivi",         "Passivo", "Fondi per rischi e oneri",    "Avere"),
    OICAccount("B.4",     "Altri fondi",                                   "Passivo", "Fondi per rischi e oneri",    "Avere"),
    # ── PASSIVO — TFR ─────────────────────────────────────────────────────────
    OICAccount("C.1",     "Trattamento di fine rapporto (TFR)",            "Passivo", "TFR",                         "Avere"),
    # ── PASSIVO — DEBITI (Liabilities) ───────────────────────────────────────
    OICAccount("D.1",     "Obbligazioni",                                  "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.2",     "Obbligazioni convertibili",                     "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.3",     "Debiti verso soci per finanziamenti",           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.4",     "Debiti verso banche",                           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.5",     "Debiti verso altri finanziatori",               "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.6",     "Acconti da clienti",                            "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.7",     "Debiti verso fornitori",                        "Passivo", "Debiti",                      "Avere", True),
    OICAccount("D.8",     "Debiti verso imprese controllate",              "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.9",     "Debiti verso imprese collegate",                "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.10",    "Debiti verso controllanti",                     "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.11",    "Debiti tributari (IRES, IRAP, IVA)",           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.12",    "Debiti verso istituti di previdenza",           "Passivo", "Debiti",                      "Avere"),
    OICAccount("D.13",    "Altri debiti",                                  "Passivo", "Debiti",                      "Avere"),
    # ── PASSIVO — RATEI E RISCONTI ────────────────────────────────────────────
    OICAccount("E.1",     "Ratei passivi",                                 "Passivo", "Ratei e risconti passivi",    "Avere"),
    OICAccount("E.2",     "Risconti passivi",                              "Passivo", "Ratei e risconti passivi",    "Avere"),
    # ── CONTO ECONOMICO — RICAVI (Revenue) ───────────────────────────────────
    OICAccount("A.1",     "Ricavi delle vendite e delle prestazioni",      "Ricavi",  "Valore della produzione",     "Avere", True),
    OICAccount("A.2",     "Variazione delle rimanenze prodotti",           "Ricavi",  "Valore della produzione",     "Avere"),
    OICAccount("A.3",     "Variazione dei lavori in corso su ordinazione", "Ricavi",  "Valore della produzione",     "Avere"),
    OICAccount("A.4",     "Incrementi di immobilizzazioni per lavori int.","Ricavi",  "Valore della produzione",     "Avere"),
    OICAccount("A.5",     "Altri ricavi e proventi",                       "Ricavi",  "Valore della produzione",     "Avere"),
    # ── CONTO ECONOMICO — COSTI (Costs) ──────────────────────────────────────
    OICAccount("B.6",     "Materie prime, sussidiarie, di consumo e merci","Costi",   "Costi della produzione",      "Dare",  True),
    OICAccount("B.7",     "Servizi",                                       "Costi",   "Costi della produzione",      "Dare",  True),
    OICAccount("B.8",     "Godimento di beni di terzi",                    "Costi",   "Costi della produzione",      "Dare",  True),
    OICAccount("B.9a",    "Salari e stipendi",                             "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.9b",    "Oneri sociali",                                 "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.9c",    "Trattamento di fine rapporto (costo)",          "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.9d",    "Trattamento di quiescenza",                     "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.9e",    "Altri costi del personale",                     "Costi",   "Costi del personale",         "Dare"),
    OICAccount("B.10a",   "Ammortamento immobilizzazioni immateriali",     "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.10b",   "Ammortamento immobilizzazioni materiali",       "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.10c",   "Altre svalutazioni delle immobilizzazioni",     "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.10d",   "Svalutazione dei crediti circolanti",           "Costi",   "Ammortamenti e svalutazioni", "Dare"),
    OICAccount("B.11",    "Variazione delle rimanenze mat. prime",         "Costi",   "Costi della produzione",      "Dare"),
    OICAccount("B.12",    "Accantonamento per rischi",                     "Costi",   "Accantonamenti",              "Dare"),
    OICAccount("B.13",    "Altri accantonamenti",                          "Costi",   "Accantonamenti",              "Dare"),
    OICAccount("B.14",    "Oneri diversi di gestione",                     "Costi",   "Costi della produzione",      "Dare"),
    # ── CONTO ECONOMICO — GESTIONE FINANZIARIA ───────────────────────────────
    OICAccount("C.15",    "Proventi da partecipazioni",                    "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.16a",   "Proventi da crediti finanziari imm.",           "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.16b",   "Proventi da titoli immobilizzati",              "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.16c",   "Proventi da titoli circolanti",                 "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.16d",   "Proventi diversi dai precedenti",               "Ricavi",  "Proventi e oneri finanziari", "Avere"),
    OICAccount("C.17",    "Interessi e altri oneri finanziari",            "Costi",   "Proventi e oneri finanziari", "Dare"),
    OICAccount("C.17bis", "Utili e perdite su cambi",                      "Costi",   "Proventi e oneri finanziari", "Dare"),
    # ── CONTO ECONOMICO — IMPOSTE ─────────────────────────────────────────────
    OICAccount("22",      "Imposte sul reddito — IRES corrente",           "Costi",   "Imposte",                     "Dare"),
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
