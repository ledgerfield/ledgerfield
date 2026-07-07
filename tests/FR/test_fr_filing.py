"""Tests pour le module de déclaration fiscale française (IS 2065 / IR 2042)."""
import json

from ledgerfield.filing.FR.declaration import (
    LiasseFiscale2065,
    DeclarationIR2042,
    generer_liasse_2065,
    generer_ir_2042,
)


# --------------------------------------------------------------------------
# Impôt sur les sociétés (IS / 2065)
# --------------------------------------------------------------------------
def test_is_non_pme_taux_normal():
    """Non-PME 1 000 000 € → 25% = 250 000 €."""
    liasse = generer_liasse_2065(
        "ent-1", "123456789", 2024,
        {"chiffre_affaires": 2_000_000, "cout_des_ventes": 1_000_000, "pme": False},
    )
    assert liasse.resultat_fiscal == 1_000_000
    assert liasse.impot_societes == 250_000
    assert liasse.impot_net == 250_000


def test_is_pme_taux_reduit_15():
    """PME 40 000 € (≤ 42 500) → 15% = 6 000 €."""
    liasse = generer_liasse_2065(
        "ent-2", "123456789", 2024,
        {"chiffre_affaires": 40_000, "pme": True},
    )
    assert liasse.resultat_fiscal == 40_000
    assert liasse.impot_societes == 6_000
    assert liasse.impot_taux_normal == 0.0


def test_is_pme_mixte_taux():
    """PME 100 000 € → 15%*42 500 + 25%*57 500 = 6 375 + 14 375 = 20 750 €."""
    liasse = LiasseFiscale2065(
        "ent-3", "123456789", 2024,
        chiffre_affaires=100_000, pme=True,
    ).calculer()
    assert liasse.impot_taux_reduit == 6_375
    assert liasse.impot_taux_normal == 14_375
    assert liasse.impot_societes == 20_750


def test_is_credit_impot():
    """Le crédit d'impôt réduit l'impôt net."""
    liasse = generer_liasse_2065(
        "ent-4", "123456789", 2024,
        {"chiffre_affaires": 1_000_000, "pme": False, "credit_impot": 50_000},
    )
    assert liasse.impot_societes == 250_000
    assert liasse.impot_net == 200_000


def test_is_resultat_negatif_zero():
    """Résultat fiscal négatif → aucun impôt."""
    liasse = generer_liasse_2065(
        "ent-5", "123456789", 2024,
        {"chiffre_affaires": 100_000, "cout_des_ventes": 150_000, "pme": True},
    )
    assert liasse.resultat_fiscal == -50_000
    assert liasse.impot_societes == 0.0
    assert liasse.impot_net == 0.0


def test_is_pme_seuil_ca_depasse():
    """PME cochée mais CA ≥ 10 M€ → taux normal sur tout le bénéfice."""
    liasse = LiasseFiscale2065(
        "ent-6", "123456789", 2024,
        chiffre_affaires=12_000_000, cout_des_ventes=11_960_000, pme=True,
    ).calculer()
    assert liasse.resultat_fiscal == 40_000
    # CA >= 10 M€ : le taux réduit ne s'applique pas
    assert liasse.impot_societes == 40_000 * 0.25


def test_is_date_limite():
    liasse = generer_liasse_2065("ent-7", "123456789", 2024, {"chiffre_affaires": 1000})
    assert liasse.date_limite == "2025-05-15"


def test_is_to_json_round_trip():
    liasse = generer_liasse_2065(
        "ent-8", "123456789", 2024,
        {"chiffre_affaires": 500_000, "cout_des_ventes": 200_000, "pme": True},
    )
    data = json.loads(liasse.to_json())
    assert data["impot_societes"] == liasse.impot_societes
    assert data["siren"] == "123456789"
    assert data["date_limite"] == "2025-05-15"


def test_is_to_xml_saf_t_present():
    liasse = generer_liasse_2065("ent-9", "123456789", 2024, {"chiffre_affaires": 1000})
    xml = liasse.to_xml_saf_t()
    assert "<?xml" in xml
    assert 'type="IS"' in xml
    assert "<ImpotSocietes>" in xml
    assert "urn:StandardAuditFile-Taxation:FR" in xml


# --------------------------------------------------------------------------
# Impôt sur le revenu (IR / 2042)
# --------------------------------------------------------------------------
def test_ir_bareme_progressif():
    """Revenu imposable 50 000 € (1 part) →
    11%*(29315-11497) + 30%*(50000-29315) = 1959.98 + 6205.5 = 8165.48 €."""
    decl = generer_ir_2042(
        "per-1", "9999", 2025,
        {"traitements_salaires": 50_000},
    )
    assert decl.revenu_imposable == 50_000
    assert round(decl.impot_brut, 2) == 8_165.48
    assert round(decl.impot_net, 2) == 8_165.48


def test_ir_tranche_zero():
    """Revenu sous 11 497 € → 0% → aucun impôt."""
    decl = generer_ir_2042(
        "per-2", "9999", 2025,
        {"traitements_salaires": 10_000},
    )
    assert decl.revenu_imposable == 10_000
    assert decl.impot_brut == 0.0
    assert decl.impot_net == 0.0


def test_ir_revenu_negatif_zero():
    """Charges supérieures aux revenus → base 0, impôt 0."""
    decl = generer_ir_2042(
        "per-3", "9999", 2025,
        {"traitements_salaires": 20_000, "charges_deductibles": 30_000},
    )
    assert decl.revenu_imposable == 0.0
    assert decl.impot_net == 0.0


def test_ir_prelevement_a_la_source():
    """Le prélèvement à la source est déduit du solde à payer."""
    decl = generer_ir_2042(
        "per-4", "9999", 2025,
        {"traitements_salaires": 50_000, "prelevement_a_la_source": 5_000},
    )
    assert round(decl.solde_a_payer, 2) == round(decl.impot_net - 5_000, 2)


def test_ir_quotient_familial_parts():
    """2 parts : impôt calculé par part puis multiplié → allègement."""
    une_part = generer_ir_2042("per-5a", "9999", 2025, {"traitements_salaires": 60_000})
    deux_parts = generer_ir_2042(
        "per-5b", "9999", 2025,
        {"traitements_salaires": 60_000, "nombre_parts": 2},
    )
    assert deux_parts.impot_brut < une_part.impot_brut


def test_ir_date_limite():
    decl = generer_ir_2042("per-6", "9999", 2025, {"traitements_salaires": 30_000})
    assert decl.date_limite == "2025-05-22"


def test_ir_to_json_round_trip():
    decl = generer_ir_2042("per-7", "9999", 2025, {"traitements_salaires": 45_000})
    data = json.loads(decl.to_json())
    assert data["impot_net"] == decl.impot_net
    assert data["annee"] == 2025


def test_ir_to_xml_saf_t_present():
    decl = generer_ir_2042("per-8", "9999", 2025, {"traitements_salaires": 45_000})
    xml = decl.to_xml_saf_t()
    assert "<?xml" in xml
    assert 'type="IR"' in xml
    assert "<ImpotNet>" in xml
    assert "urn:StandardAuditFile-Taxation:FR" in xml
