"""Tests for ledgerfield.payroll.NL.loonstrook — loonstrook generator."""
import pytest
from ledgerfield.payroll.NL.loonstrook import (
    Werknemer, genereer_loonstrook, RegelSoort,
    GebruikelijkLoonCheck, controleer_gebruikelijk_loon,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def werknemer_standaard():
    """Standaard werknemer zonder toeslagen, 60k jaarsalaris."""
    return Werknemer(
        id="w001",
        naam="Jan de Vries",
        jaarsalaris=60_000.0,
        pensioen_pct=0.04,
        reisafstand_km=0.0,
        thuiswerk_dagen_pw=0.0,
    )


@pytest.fixture
def loonstrook_standaard(werknemer_standaard):
    return genereer_loonstrook(werknemer_standaard, "2025-06")


# ---------------------------------------------------------------------------
# Test 1: Bruto = jaarsalaris / 12, geen toeslagen
# ---------------------------------------------------------------------------

def test_bruto_equals_jaarsalaris_div_12_no_allowances(loonstrook_standaard, werknemer_standaard):
    """Bruto maandsalaris-regel bedrag == jaarsalaris / 12."""
    bruto_regels = [
        r for r in loonstrook_standaard.regels if r.soort == RegelSoort.BRUTO_SALARIS
    ]
    assert len(bruto_regels) == 1
    assert bruto_regels[0].bedrag == pytest.approx(werknemer_standaard.jaarsalaris / 12.0)


# ---------------------------------------------------------------------------
# Test 2: Netto < Bruto (moderate salary, 60k)
# ---------------------------------------------------------------------------

def test_netto_kleiner_dan_bruto(loonstrook_standaard):
    """Netto (alle regels) < bruto voor redelijk salaris (60k)."""
    assert loonstrook_standaard.netto() < loonstrook_standaard.bruto()


# ---------------------------------------------------------------------------
# Test 3: Loonheffing regel aanwezig en negatief
# ---------------------------------------------------------------------------

def test_loonheffing_regel_aanwezig_en_negatief(loonstrook_standaard):
    lh_regels = [r for r in loonstrook_standaard.regels if r.soort == RegelSoort.LOONHEFFING]
    assert len(lh_regels) == 1
    assert lh_regels[0].bedrag < 0


# ---------------------------------------------------------------------------
# Test 4: ZVW bijdrage aanwezig
# ---------------------------------------------------------------------------

def test_zvw_bijdrage_aanwezig(loonstrook_standaard):
    zvw_regels = [r for r in loonstrook_standaard.regels if r.soort == RegelSoort.ZVW_BIJDRAGE]
    assert len(zvw_regels) == 1


# ---------------------------------------------------------------------------
# Test 5: Pensioen aanwezig wanneer pensioen_pct > 0
# ---------------------------------------------------------------------------

def test_pensioen_aanwezig_wanneer_pct_positief():
    w = Werknemer(id="p01", naam="Pensioen Test", jaarsalaris=50_000.0, pensioen_pct=0.05)
    ls = genereer_loonstrook(w, "2025-06")
    pensioen_regels = [r for r in ls.regels if r.soort == RegelSoort.PENSIOEN_WERKNEMER]
    assert len(pensioen_regels) == 1
    # inhoud is negatief
    assert pensioen_regels[0].bedrag < 0


# ---------------------------------------------------------------------------
# Test 6: Reiskosten aanwezig wanneer reisafstand_km > 0
# ---------------------------------------------------------------------------

def test_reiskosten_aanwezig_wanneer_afstand_positief():
    w = Werknemer(
        id="r01", naam="Reiziger", jaarsalaris=50_000.0, reisafstand_km=30.0
    )
    ls = genereer_loonstrook(w, "2025-06")
    reis_regels = [r for r in ls.regels if r.soort == RegelSoort.REISKOSTENVERGOEDING]
    assert len(reis_regels) == 1
    assert reis_regels[0].bedrag > 0


# ---------------------------------------------------------------------------
# Test 7: Thuiswerkvergoeding aanwezig wanneer thuiswerk_dagen_pw > 0
# ---------------------------------------------------------------------------

def test_thuiswerk_aanwezig_wanneer_dagen_positief():
    w = Werknemer(
        id="t01", naam="Thuiswerker", jaarsalaris=50_000.0, thuiswerk_dagen_pw=3.0
    )
    ls = genereer_loonstrook(w, "2025-06")
    tw_regels = [r for r in ls.regels if r.soort == RegelSoort.THUISWERK_VERGOEDING]
    assert len(tw_regels) == 1
    assert tw_regels[0].bedrag > 0


# ---------------------------------------------------------------------------
# Test 8: Netto = sum van alle regels
# ---------------------------------------------------------------------------

def test_netto_equals_sum_alle_regels(loonstrook_standaard):
    expected = sum(r.bedrag for r in loonstrook_standaard.regels)
    assert loonstrook_standaard.netto() == pytest.approx(expected)


# ---------------------------------------------------------------------------
# Test 9: DGA: is_dga=True → speciaal label in omschrijving
# ---------------------------------------------------------------------------

def test_dga_speciaal_label():
    """Loonstrook voor DGA moet een 'DGA'-markering tonen in minimaal één regel."""
    w = Werknemer(
        id="dga01",
        naam="Edwin Hauwert",
        jaarsalaris=60_000.0,
        is_dga=True,
        pensioen_pct=0.04,
    )
    ls = genereer_loonstrook(w, "2025-06")
    assert any(
        "DGA" in r.omschrijving or "dga" in r.omschrijving.lower()
        for r in ls.regels
    ), "Verwacht minstens één regel met 'DGA' in de omschrijving voor een DGA-werknemer"


# ---------------------------------------------------------------------------
# Test 10: Hoog salaris → hoger % loonheffing dan laag salaris
# ---------------------------------------------------------------------------

def test_hoog_salaris_hoger_pct_loonheffing():
    w_hoog = Werknemer(id="h01", naam="Hoog", jaarsalaris=200_000.0, pensioen_pct=0.0)
    w_laag = Werknemer(id="l01", naam="Laag", jaarsalaris=30_000.0, pensioen_pct=0.0)

    ls_hoog = genereer_loonstrook(w_hoog, "2025-06")
    ls_laag = genereer_loonstrook(w_laag, "2025-06")

    def lh_pct(ls, w):
        lh = next(r for r in ls.regels if r.soort == RegelSoort.LOONHEFFING)
        maandbruto = w.jaarsalaris / 12.0
        return abs(lh.bedrag) / maandbruto

    assert lh_pct(ls_hoog, w_hoog) > lh_pct(ls_laag, w_laag)


# ---------------------------------------------------------------------------
# Test 11: Reiskosten NIET aanwezig wanneer reisafstand = 0
# ---------------------------------------------------------------------------

def test_reiskosten_afwezig_wanneer_afstand_nul(loonstrook_standaard):
    reis_regels = [r for r in loonstrook_standaard.regels if r.soort == RegelSoort.REISKOSTENVERGOEDING]
    assert len(reis_regels) == 0


# ---------------------------------------------------------------------------
# Test 12: Thuiswerk NIET aanwezig wanneer thuiswerk_dagen_pw = 0
# ---------------------------------------------------------------------------

def test_thuiswerk_afwezig_wanneer_geen_thuiswerk(loonstrook_standaard):
    tw_regels = [r for r in loonstrook_standaard.regels if r.soort == RegelSoort.THUISWERK_VERGOEDING]
    assert len(tw_regels) == 0


# ---------------------------------------------------------------------------
# Tests 13-18: GebruikelijkLoonCheck (art. 12a Wet LB 1964)
# ---------------------------------------------------------------------------

def test_gebruikelijk_loon_voldoet_aan_norm():
    """DGA met salaris >= €56.000 voldoet aan de norm."""
    w = Werknemer(id="d1", naam="DGA OK", jaarsalaris=60_000.0, is_dga=True)
    check = controleer_gebruikelijk_loon(w, 2025)
    assert check.voldoet is True
    assert check.tekort == 0.0
    assert check.waarschuwing == ""


def test_gebruikelijk_loon_onder_norm_geeft_waarschuwing():
    """DGA met salaris < €56.000 krijgt waarschuwing + tekortbedrag."""
    w = Werknemer(id="d2", naam="DGA Te Laag", jaarsalaris=40_000.0, is_dga=True)
    check = controleer_gebruikelijk_loon(w, 2025)
    assert check.voldoet is False
    assert check.tekort == pytest.approx(16_000.0)
    assert "art. 12a" in check.waarschuwing
    assert "16.000" in check.waarschuwing or "16000" in check.waarschuwing.replace(",", "")


def test_gebruikelijk_loon_norm_2025():
    """Norm 2025 is €56.000."""
    w = Werknemer(id="d3", naam="DGA", jaarsalaris=56_000.0, is_dga=True)
    check = controleer_gebruikelijk_loon(w, 2025)
    assert check.norm == 56_000.0
    assert check.voldoet is True


def test_gebruikelijk_loon_norm_2024():
    """Norm 2024 is ook €56.000."""
    w = Werknemer(id="d4", naam="DGA", jaarsalaris=55_000.0, is_dga=True)
    check = controleer_gebruikelijk_loon(w, 2024)
    assert check.norm == 56_000.0
    assert check.voldoet is False


def test_gebruikelijk_loon_to_dict():
    """to_dict bevat alle verwachte sleutels."""
    w = Werknemer(id="d5", naam="DGA", jaarsalaris=60_000.0, is_dga=True)
    d = controleer_gebruikelijk_loon(w, 2025).to_dict()
    assert set(d.keys()) >= {"jaar", "jaarsalaris", "norm", "voldoet", "tekort", "waarschuwing"}


def test_gebruikelijk_loon_precies_op_grens():
    """Precies op de norm: voldoet, tekort=0."""
    w = Werknemer(id="d6", naam="DGA Grens", jaarsalaris=56_000.0, is_dga=True)
    check = controleer_gebruikelijk_loon(w, 2025)
    assert check.voldoet is True
    assert check.tekort == pytest.approx(0.0)
