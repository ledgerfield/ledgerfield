"""Tests für das deutsche Steuererklärungs-Modul (KStG / GewStG)."""
import json

from ledgerfield.filing.DE.steuererklaerung import (
    Koerperschaftsteuererklaerung,
    Gewerbesteuererklaerung,
    erzeuge_koerperschaftsteuer,
    erzeuge_gewerbesteuer,
)


def _kst(zve: float, jahr: int = 2025) -> Koerperschaftsteuererklaerung:
    return erzeuge_koerperschaftsteuer(
        "DE-GmbH-1", "151/815/08155", jahr, {"umsatz": zve}
    )


def _gewst(ertrag: float, hebesatz: float = 4.00, jahr: int = 2025):
    return erzeuge_gewerbesteuer(
        "DE-GmbH-1", "151/815/08155", jahr,
        {"gewerbeertrag": ertrag, "hebesatz": hebesatz},
    )


# --- Körperschaftsteuer ----------------------------------------------------

def test_kst_bei_1mio():
    k = _kst(1_000_000.0)
    assert k.koerperschaftsteuer == 150_000.0
    assert k.solidaritaetszuschlag == 8_250.0
    assert k.summe_koerperschaftsteuer == 158_250.0


def test_soli_ist_genau_5_5_prozent_der_kst():
    k = _kst(742_318.0)
    assert abs(k.solidaritaetszuschlag - k.koerperschaftsteuer * 0.055) < 1e-9


def test_kst_zve_berechnung():
    e = erzeuge_koerperschaftsteuer(
        "X", "1", 2025,
        {"umsatz": 500_000.0, "umsatzkosten": 200_000.0, "betriebsausgaben": 100_000.0},
    )
    assert e.bruttoergebnis == 300_000.0
    assert e.betriebsergebnis == 200_000.0
    assert e.zu_versteuerndes_einkommen == 200_000.0
    assert e.koerperschaftsteuer == 30_000.0


def test_kst_negativ_ist_null():
    e = erzeuge_koerperschaftsteuer(
        "X", "1", 2025, {"umsatz": 100_000.0, "betriebsausgaben": 300_000.0}
    )
    assert e.zu_versteuerndes_einkommen == 0.0
    assert e.koerperschaftsteuer == 0.0
    assert e.solidaritaetszuschlag == 0.0
    assert e.summe_koerperschaftsteuer == 0.0


def test_kst_effektiver_bundessatz():
    # 15 % * 1,055 = 15,825 %
    k = _kst(1_000_000.0)
    assert abs(k.summe_koerperschaftsteuer / 1_000_000.0 - 0.15825) < 1e-9


# --- Gewerbesteuer ---------------------------------------------------------

def test_gewst_bei_1mio_hebesatz_400():
    g = _gewst(1_000_000.0, 4.00)
    assert g.messbetrag == 35_000.0
    assert g.gewerbesteuer == 140_000.0


def test_gewst_muenchen_hebesatz_490():
    g = _gewst(1_000_000.0, 4.90)
    assert g.messbetrag == 35_000.0
    assert g.gewerbesteuer == 171_500.0


def test_gewst_negativ_ist_null():
    g = _gewst(-50_000.0)
    assert g.bereinigter_gewerbeertrag == 0.0
    assert g.messbetrag == 0.0
    assert g.gewerbesteuer == 0.0


def test_gewst_freibetrag_nur_personenunternehmen():
    g = erzeuge_gewerbesteuer(
        "EU-1", "1", 2025,
        {"gewerbeertrag": 100_000.0, "hebesatz": 4.00, "ist_personenunternehmen": True},
    )
    assert g.freibetrag == 24_500.0
    assert g.bereinigter_gewerbeertrag == 75_500.0
    # Kapitalgesellschaft: kein Freibetrag
    k = _gewst(100_000.0)
    assert k.freibetrag == 0.0
    assert k.bereinigter_gewerbeertrag == 100_000.0


def test_gewst_standard_hebesatz_ist_400():
    g = erzeuge_gewerbesteuer("X", "1", 2025, {"gewerbeertrag": 100_000.0})
    assert g.hebesatz == 4.00


# --- Kombinierte Belastung -------------------------------------------------

def test_kombinierte_koerperschaft_last_rund_29_8_prozent():
    zve = 1_000_000.0
    k = _kst(zve)
    g = _gewst(zve, 4.00)
    gesamt = (k.summe_koerperschaftsteuer + g.gewerbesteuer) / zve
    assert 0.29 < gesamt < 0.30  # ~29,8 %


# --- Serialisierung --------------------------------------------------------

def test_kst_to_json_round_trip():
    k = _kst(1_000_000.0)
    d = json.loads(k.to_json())
    assert d["summe_koerperschaftsteuer"] == 158_250.0
    assert d == k.to_dict()


def test_gewst_to_json_round_trip():
    g = _gewst(1_000_000.0, 4.90)
    d = json.loads(g.to_json())
    assert d["gewerbesteuer"] == 171_500.0
    assert d == g.to_dict()


def test_xml_saf_t_vorhanden():
    k = _kst(1_000_000.0)
    g = _gewst(1_000_000.0)
    kx = k.to_xml_saf_t()
    gx = g.to_xml_saf_t()
    assert kx.startswith("<?xml")
    assert "<SummeKoerperschaftsteuer>158250.00</SummeKoerperschaftsteuer>" in kx
    assert "urn:StandardAuditFile-Taxation:DE" in kx
    assert gx.startswith("<?xml")
    assert "<Gewerbesteuer>140000.00</Gewerbesteuer>" in gx


# --- Abgabefristen ---------------------------------------------------------

def test_abgabefristen_korrekt():
    k = _kst(1_000_000.0, jahr=2025)
    g = _gewst(1_000_000.0, jahr=2025)
    assert k.abgabefrist == "2026-07-31"
    assert g.abgabefrist == "2026-07-31"
