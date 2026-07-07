"""WBSO S&O-afdrachtvermindering — rules + ledger posting.

Generic example figures only; no taxpayer-specific data.
"""
import pytest

from ledgerfield.ledger import Account, AccountType, Ledger
from ledgerfield.tax.NL.wbso import (
    SOGrondslag, WBSOResult, bereken_wbso, forfait, verrekenbaar,
    SO_ACCOUNTS, boek_kosten, boek_uitgave, boek_afdrachtvermindering,
)


# 1 — forfait is tiered: €10/uur ≤ 1.800, €4/uur daarboven
def test_forfait_tiered():
    assert forfait(1000, 2025) == 1000 * 10
    assert forfait(1800, 2025) == 1800 * 10
    assert forfait(2000, 2025) == 1800 * 10 + 200 * 4
    assert forfait(0, 2025) == 0.0


# 2 — grondslag = S&O-loon + kosten + uitgaven (werkelijk regime)
def test_grondslag_werkelijk():
    g = SOGrondslag(jaar=2026, so_loon=120_000, kosten=18_000, uitgaven=22_000, regime="werkelijk")
    assert g.kosten_uitgaven_deel() == 40_000
    assert g.grondslag() == 160_000


# 3 — grondslag met forfait i.p.v. werkelijke kosten
def test_grondslag_forfait():
    g = SOGrondslag(jaar=2026, so_loon=120_000, so_uren=1500, regime="forfait")
    assert g.kosten_uitgaven_deel() == 1500 * 10          # 15.000
    assert g.grondslag() == 135_000


# 4 — starter 50% beats standaard 36% on schijf 1
def test_starter_vs_standaard():
    g = SOGrondslag(jaar=2026, so_loon=100_000, kosten=0, uitgaven=0, regime="werkelijk")
    std = bereken_wbso(SOGrondslag(jaar=2026, so_loon=100_000, regime="werkelijk", starter=False))
    start = bereken_wbso(SOGrondslag(jaar=2026, so_loon=100_000, regime="werkelijk", starter=True))
    assert std.tarief_schijf_1 == 0.36 and std.totaal_voordeel == 36_000
    assert start.tarief_schijf_1 == 0.50 and start.totaal_voordeel == 50_000


# 5 — kosten & uitgaven lift the afdrachtvermindering (the whole point)
def test_kosten_uitgaven_verhogen_voordeel():
    loon_only = bereken_wbso(SOGrondslag(jaar=2026, so_loon=100_000, regime="werkelijk", starter=True))
    met_ku = bereken_wbso(SOGrondslag(jaar=2026, so_loon=100_000, kosten=20_000,
                                      uitgaven=40_000, regime="werkelijk", starter=True))
    assert loon_only.totaal_voordeel == 50_000
    assert met_ku.grondslag == 160_000
    assert met_ku.totaal_voordeel == 80_000                # 50% × 160.000
    assert round(met_ku.totaal_voordeel - loon_only.totaal_voordeel, 2) == 30_000


# 6 — second bracket (16%) applies above the €380k grens
def test_schijf_2():
    g = SOGrondslag(jaar=2026, so_loon=500_000, regime="werkelijk", starter=False)
    r = bereken_wbso(g)
    assert r.voordeel_schijf_1 == 380_000 * 0.36
    assert r.voordeel_schijf_2 == 120_000 * 0.16
    assert r.totaal_voordeel == round(380_000 * 0.36 + 120_000 * 0.16, 2)


# 7 — afdrachtruimte cap: WBSO can't exceed the loonheffing actually due
def test_verrekenbaar_cap():
    verrekend, onbenut = verrekenbaar(50_000, 19_000)      # low DGA payroll
    assert verrekend == 19_000 and onbenut == 31_000
    verrekend, onbenut = verrekenbaar(50_000, 80_000)      # ample payroll
    assert verrekend == 50_000 and onbenut == 0.0
    assert verrekenbaar(1000, -5)[0] == 0.0                # never below zero


# 8 — legacy loon-only float call still works
def test_backward_compatible_float():
    r = bereken_wbso(100_000, 2025)
    assert isinstance(r, WBSOResult) and r.grondslag == 100_000
    assert r.totaal_voordeel == 36_000                     # standaard 36%


# 9 — no WBSO block that year → zero, no crash
def test_no_regeling():
    r = bereken_wbso(SOGrondslag(jaar=2022, so_loon=50_000))
    assert r.totaal_voordeel == 0.0


# 10 — ledger postings balance (double-entry) and settle correctly
def test_ledger_postings_balance():
    led = Ledger(entity_id="example-bv", jurisdiction="NL")
    for key, (code, name, typ) in SO_ACCOUNTS.items():
        led.add_account(Account(code=code, name=name, account_type=AccountType[typ.upper()]))
    # a period with S&O kosten, an uitgave, and the WBSO settlement
    boek_kosten(led, 5_000, "2026-03", document_ref="INV-chem-01")
    boek_uitgave(led, 8_000, "2026-03", document_ref="INV-edge-01")
    # afdrachtvermindering, only the settleable part
    voordeel_maand = 80_000 / 12
    afdracht_maand = 1_600.0
    verrekend, onbenut = verrekenbaar(voordeel_maand, afdracht_maand)
    boek_afdrachtvermindering(led, verrekend, "2026-03", document_ref="LH-2026-03")
    tb = led.trial_balance()
    # double-entry invariant (natural-balance sign convention):
    # sum(asset + expense) == sum(liability + equity + revenue)
    typ_by_code = {code: typ for _, (code, _n, typ) in SO_ACCOUNTS.items()}
    debit_side = sum(b for c, b in tb.items() if typ_by_code[c] in ("asset", "expense"))
    credit_side = sum(b for c, b in tb.items() if typ_by_code[c] in ("liability", "equity", "revenue"))
    assert round(debit_side, 2) == round(credit_side, 2) == 13_000.0
    assert tb["WKosSOK"] == 5_000            # expense up
    assert tb["BMvaSOA"] == 8_000            # asset up
    assert tb["SchLhTb"] == -verrekend       # loonheffing-schuld down by verrekend
    assert tb["WOmzWBS"] == verrekend        # WBSO-bate up
    assert verrekend == round(afdracht_maand, 2)   # capped by the month's afdracht
