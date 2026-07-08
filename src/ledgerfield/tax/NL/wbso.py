"""WBSO — Speur & Ontwikkeling (S&O) afdrachtvermindering, NL.

Implements the WBSO rules as they actually work since the 2016 RDA-integration:

    S&O-grondslag = S&O-loonkosten + (forfait  OR  werkelijke kosten en uitgaven)

The afdrachtvermindering is a percentage of that grondslag, in two brackets,
with a higher starter rate on the first bracket. It can only be settled against
the loonheffing that is actually due — it can never push a period's afdracht
below zero (the *afdrachtruimte* cap), and any surplus not used within the
calendar year lapses.

Public rules/rates only; no taxpayer-specific data lives here.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

__all__ = [
    "WBSOResult", "SOGrondslag",
    "forfait", "bereken_wbso", "verrekenbaar",
    "SO_ACCOUNTS", "boek_kosten", "boek_uitgave", "boek_afdrachtvermindering",
]

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


def _wbso_params(jaar: int) -> dict | None:
    years = json.load(open(PARAMS_PATH))["years"]
    y = years.get(str(jaar))
    return (y or {}).get("WBSO")


# ── grondslag ────────────────────────────────────────────────────────────

def forfait(so_uren: float, jaar: int = 2025) -> float:
    """Kosten-en-uitgaven-forfait: a fixed allowance per S&O-hour, tiered.

    (€10/uur for the first 1.800 uur, €4/uur above.) Automatic, no invoices —
    the alternative to declaring *werkelijke kosten en uitgaven*.
    """
    w = _wbso_params(jaar) or {}
    lo = w.get("forfait_tarief_laag", 10.0)
    hi = w.get("forfait_tarief_hoog", 4.0)
    grens = w.get("forfait_urengrens", 1800)
    if so_uren <= 0:
        return 0.0
    return min(so_uren, grens) * lo + max(0.0, so_uren - grens) * hi


@dataclass
class SOGrondslag:
    """The full S&O base for one WBSO-verklaring in one boekjaar."""

    jaar: int
    so_loon: float                       # S&O-uren × vastgesteld S&O-uurloon
    so_uren: float = 0.0
    regime: str = "forfait"              # "forfait" | "werkelijk"
    kosten: float = 0.0                  # werkelijke kosten (materialen, chemicaliën, analyses)
    uitgaven: float = 0.0                # werkelijke uitgaven (bedrijfsmiddelen, S&O-deel)
    starter: bool = False

    def kosten_uitgaven_deel(self) -> float:
        if self.regime == "werkelijk":
            return round(self.kosten + self.uitgaven, 2)
        return round(forfait(self.so_uren, self.jaar), 2)

    def grondslag(self) -> float:
        return round(self.so_loon + self.kosten_uitgaven_deel(), 2)


# ── afdrachtvermindering ──────────────────────────────────────────────────

@dataclass
class WBSOResult:
    jaar: int
    grondslag: float
    so_loon: float
    kosten_uitgaven: float
    regime: str
    starter: bool
    tarief_schijf_1: float
    tarief_schijf_2: float
    schijf_1_grens: float
    voordeel_schijf_1: float
    voordeel_schijf_2: float
    totaal_voordeel: float               # totale afdrachtvermindering (jaar)

    @property
    def maandbedrag(self) -> float:
        return round(self.totaal_voordeel / 12, 2)


def bereken_wbso(basis, jaar: int = 2025) -> WBSOResult:
    """Afdrachtvermindering for a grondslag.

    ``basis`` is an :class:`SOGrondslag`, or a float for the legacy loon-only
    call ``bereken_wbso(loonkosten_so, jaar)`` (treated as loon = grondslag).
    """
    if not isinstance(basis, SOGrondslag):
        basis = SOGrondslag(jaar=jaar, so_loon=float(basis), regime="werkelijk")
    else:
        jaar = basis.jaar

    w = _wbso_params(jaar)
    if w is None:                        # geen regeling dat jaar / buiten scope
        return WBSOResult(jaar, basis.so_loon, basis.so_loon, 0.0, basis.regime,
                          basis.starter, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    t1 = w["tarief_starter"] if (basis.starter and "tarief_starter" in w) else w["tarief_schijf_1"]
    t2 = w.get("tarief_schijf_2", 0.0)
    grens = w["schijf_1_grens"]
    g = basis.grondslag()
    v1 = round(min(g, grens) * t1, 2)
    v2 = round(max(0.0, g - grens) * t2, 2)
    return WBSOResult(jaar, g, basis.so_loon, basis.kosten_uitgaven_deel(),
                      basis.regime, basis.starter, t1, t2, grens, v1, v2,
                      round(v1 + v2, 2))


def verrekenbaar(voordeel: float, loonheffing_afdracht: float) -> tuple[float, float]:
    """Split a WBSO-voordeel into (verrekend, onbenut) against available afdracht.

    WBSO can never bring the loonheffing-afdracht below zero. Applied per
    boekjaar: any surplus above the year's total afdracht lapses. Returns the
    settleable amount and the amount that cannot be used.
    """
    room = max(0.0, loonheffing_afdracht)
    verrekend = round(min(voordeel, room), 2)
    return verrekend, round(voordeel - verrekend, 2)


# ── ledger posting ─────────────────────────────────────────────────────────
# Minimal S&O chart-of-accounts additions (code, name, type). Codes follow an
# RGS-like grouping; swap for your own schema codes when integrating.

SO_ACCOUNTS = {
    "so_kosten":              ("WKosSOK", "S&O kosten (materialen, chemicaliën, analyses)", "expense"),
    "so_apparatuur":          ("BMvaSOA", "S&O bedrijfsmiddelen (uitgaven)",                "asset"),
    "loonheffing_te_betalen": ("SchLhTb", "Af te dragen loonheffing",                       "liability"),
    "wbso_bate":              ("WOmzWBS", "WBSO-afdrachtvermindering (bate)",               "revenue"),
    "crediteuren":            ("SchCre",  "Crediteuren / te betalen",                       "liability"),
}


def boek_kosten(ledger, amount: float, periode: str, *, debit="WKosSOK",
                credit="SchCre", document_ref="", entry_id=None):
    """S&O kosten (verbruik): expense ↑, crediteuren ↑."""
    return _post(ledger, "S&O kosten", debit, credit, amount, periode, document_ref, entry_id)


def boek_uitgave(ledger, amount: float, periode: str, *, debit="BMvaSOA",
                 credit="SchCre", document_ref="", entry_id=None):
    """S&O uitgave (bedrijfsmiddel): asset ↑, crediteuren ↑."""
    return _post(ledger, "S&O uitgave (bedrijfsmiddel)", debit, credit, amount, periode, document_ref, entry_id)


def boek_afdrachtvermindering(ledger, amount: float, periode: str, *,
                              debit="SchLhTb", credit="WOmzWBS", document_ref="", entry_id=None):
    """WBSO-verrekening: af te dragen loonheffing ↓, WBSO-bate ↑.

    Pass only the *verrekenbare* amount (see :func:`verrekenbaar`).
    """
    return _post(ledger, "WBSO-afdrachtvermindering", debit, credit, amount, periode, document_ref, entry_id)


def _post(ledger, description, debit, credit, amount, periode, document_ref, entry_id):
    from ...ledger import JournalEntry
    eid = entry_id or f"{description}:{periode}:{debit}->{credit}:{amount}"
    return ledger.post(JournalEntry(
        id=eid, timestamp=0.0, description=description,
        debit_account=debit, credit_account=credit, amount=round(amount, 2),
        period=periode, category="wbso", document_ref=document_ref))
