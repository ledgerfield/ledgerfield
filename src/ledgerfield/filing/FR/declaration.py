"""Aides à la déclaration fiscale pour les entités françaises (IS 2065 / IR 2042)."""
from __future__ import annotations
from dataclasses import dataclass
import json
import datetime

__all__ = [
    "LiasseFiscale2065",
    "DeclarationIR2042",
    "generer_liasse_2065",
    "generer_ir_2042",
]

# ---------------------------------------------------------------------------
# Impôt sur les sociétés (IS) 2025 — CGI art. 219
# Taux normal : 25%
# Taux réduit PME : 15% sur les premiers 42 500 € de bénéfice
#   (chiffre d'affaires < 10 M€ ET ≥ 75% détenu par des personnes physiques)
# ---------------------------------------------------------------------------
_IS_TAUX_NORMAL = 0.25
_IS_TAUX_REDUIT_PME = 0.15
_IS_SEUIL_TAUX_REDUIT = 42_500.0
_IS_PLAFOND_CA_PME = 10_000_000.0

# ---------------------------------------------------------------------------
# Impôt sur le revenu (IR) 2042 — barème progressif 2025 (revenus 2024)
# 0%    jusqu'à 11 497 €
# 11%   de 11 497 € à 29 315 €
# 30%   de 29 315 € à 83 823 €
# 41%   de 83 823 € à 180 294 €
# 45%   au-delà de 180 294 €
# Tranches modélisées par part (une part par défaut ; quotient familial en note).
# ---------------------------------------------------------------------------
_IR_BAREME = [
    (11_497.0, 0.00),
    (29_315.0, 0.11),
    (83_823.0, 0.30),
    (180_294.0, 0.41),
    (float("inf"), 0.45),
]


@dataclass
class LiasseFiscale2065:
    """Liasse fiscale — impôt sur les sociétés (formulaire 2065, simplifié)."""
    entite_id: str
    siren: str
    exercice: int
    # Compte de résultat (simplifié)
    chiffre_affaires: float = 0.0
    cout_des_ventes: float = 0.0
    marge_brute: float = 0.0
    charges_exploitation: float = 0.0
    resultat_exploitation: float = 0.0
    resultat_financier: float = 0.0
    resultat_fiscal: float = 0.0
    # Régime PME (taux réduit)
    pme: bool = False
    # Calcul de l'IS
    impot_taux_reduit: float = 0.0
    impot_taux_normal: float = 0.0
    impot_societes: float = 0.0
    credit_impot: float = 0.0
    impot_net: float = 0.0
    # Date limite de dépôt
    date_limite: str = ""

    def calculer(self) -> "LiasseFiscale2065":
        """Recalcule tous les champs dérivés."""
        # Compte de résultat
        self.marge_brute = self.chiffre_affaires - self.cout_des_ventes
        self.resultat_exploitation = self.marge_brute - self.charges_exploitation
        self.resultat_fiscal = self.resultat_exploitation + self.resultat_financier

        # Régime PME : CA < 10 M€ (la détention par personnes physiques est
        # supposée remplie lorsque pme=True).
        eligible_pme = self.pme and self.chiffre_affaires < _IS_PLAFOND_CA_PME

        benefice = max(0.0, self.resultat_fiscal)

        # Calcul de l'IS (CGI art. 219)
        if benefice <= 0.0:
            self.impot_taux_reduit = 0.0
            self.impot_taux_normal = 0.0
        elif eligible_pme:
            if benefice <= _IS_SEUIL_TAUX_REDUIT:
                self.impot_taux_reduit = benefice * _IS_TAUX_REDUIT_PME
                self.impot_taux_normal = 0.0
            else:
                self.impot_taux_reduit = _IS_SEUIL_TAUX_REDUIT * _IS_TAUX_REDUIT_PME
                self.impot_taux_normal = (benefice - _IS_SEUIL_TAUX_REDUIT) * _IS_TAUX_NORMAL
        else:
            self.impot_taux_reduit = 0.0
            self.impot_taux_normal = benefice * _IS_TAUX_NORMAL

        self.impot_societes = self.impot_taux_reduit + self.impot_taux_normal
        self.impot_net = max(0.0, self.impot_societes - self.credit_impot)

        # Date limite : 2e jour ouvré suivant le 1er mai (exercice civil).
        self.date_limite = "2025-05-15"

        return self

    def to_dict(self) -> dict:
        return {
            "entite_id": self.entite_id,
            "siren": self.siren,
            "exercice": self.exercice,
            "chiffre_affaires": self.chiffre_affaires,
            "cout_des_ventes": self.cout_des_ventes,
            "marge_brute": self.marge_brute,
            "charges_exploitation": self.charges_exploitation,
            "resultat_exploitation": self.resultat_exploitation,
            "resultat_financier": self.resultat_financier,
            "resultat_fiscal": self.resultat_fiscal,
            "pme": self.pme,
            "impot_taux_reduit": self.impot_taux_reduit,
            "impot_taux_normal": self.impot_taux_normal,
            "impot_societes": self.impot_societes,
            "credit_impot": self.credit_impot,
            "impot_net": self.impot_net,
            "date_limite": self.date_limite,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """Squelette XML SAF-T (OCDE SAF-T FR, simplifié)."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:FR">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.siren}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.exercice}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <ChiffreAffaires>{self.chiffre_affaires:.2f}</ChiffreAffaires>\n'
            f'    <CoutDesVentes>{self.cout_des_ventes:.2f}</CoutDesVentes>\n'
            f'    <MargeBrute>{self.marge_brute:.2f}</MargeBrute>\n'
            f'    <ChargesExploitation>{self.charges_exploitation:.2f}</ChargesExploitation>\n'
            f'    <ResultatExploitation>{self.resultat_exploitation:.2f}</ResultatExploitation>\n'
            f'    <ResultatFinancier>{self.resultat_financier:.2f}</ResultatFinancier>\n'
            f'    <ResultatFiscal>{self.resultat_fiscal:.2f}</ResultatFiscal>\n'
            "  </GeneralLedger>\n"
            '  <TaxReturn type="IS" formulaire="2065">\n'
            f'    <ImpotTauxReduit>{self.impot_taux_reduit:.2f}</ImpotTauxReduit>\n'
            f'    <ImpotTauxNormal>{self.impot_taux_normal:.2f}</ImpotTauxNormal>\n'
            f'    <ImpotSocietes>{self.impot_societes:.2f}</ImpotSocietes>\n'
            f'    <CreditImpot>{self.credit_impot:.2f}</CreditImpot>\n'
            f'    <ImpotNet>{self.impot_net:.2f}</ImpotNet>\n'
            f'    <DateLimite>{self.date_limite}</DateLimite>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class DeclarationIR2042:
    """Déclaration d'impôt sur le revenu (formulaire 2042, simplifié)."""
    personne_id: str
    numero_fiscal_chiffre: str    # numéro fiscal chiffré (vault)
    annee: int
    # Revenus
    traitements_salaires: float = 0.0
    revenus_capitaux_mobiliers: float = 0.0
    revenus_fonciers: float = 0.0
    autres_revenus: float = 0.0
    # Charges déductibles
    charges_deductibles: float = 0.0
    abattement: float = 0.0
    # Quotient familial (nombre de parts ; 1 part par défaut)
    nombre_parts: float = 1.0
    # Base imposable
    revenu_brut_global: float = 0.0
    revenu_imposable: float = 0.0
    # Calcul de l'IR
    impot_brut: float = 0.0
    reduction_impot: float = 0.0
    credit_impot: float = 0.0
    impot_net: float = 0.0
    prelevement_a_la_source: float = 0.0
    solde_a_payer: float = 0.0
    # Date limite de dépôt (variable selon le département)
    date_limite: str = ""

    def _bareme(self, revenu: float) -> float:
        """Applique le barème progressif par tranches sur un revenu (par part)."""
        impot = 0.0
        borne_inf = 0.0
        for borne_sup, taux in _IR_BAREME:
            if revenu > borne_inf:
                tranche = min(revenu, borne_sup) - borne_inf
                impot += tranche * taux
                borne_inf = borne_sup
            else:
                break
        return impot

    def calculer(self) -> "DeclarationIR2042":
        """Recalcule tous les champs dérivés."""
        self.revenu_brut_global = (
            self.traitements_salaires
            + self.revenus_capitaux_mobiliers
            + self.revenus_fonciers
            + self.autres_revenus
        )
        self.revenu_imposable = max(
            0.0,
            self.revenu_brut_global - self.charges_deductibles - self.abattement,
        )

        # Quotient familial : impôt par part, multiplié par le nombre de parts.
        parts = self.nombre_parts if self.nombre_parts > 0 else 1.0
        revenu_par_part = self.revenu_imposable / parts
        self.impot_brut = self._bareme(revenu_par_part) * parts

        self.impot_net = max(
            0.0, self.impot_brut - self.reduction_impot - self.credit_impot
        )
        self.solde_a_payer = self.impot_net - self.prelevement_a_la_source

        # Date limite : variable selon le département (mai–juin).
        self.date_limite = "2025-05-22"

        return self

    def to_dict(self) -> dict:
        return {
            "personne_id": self.personne_id,
            "numero_fiscal_chiffre": self.numero_fiscal_chiffre,
            "annee": self.annee,
            "traitements_salaires": self.traitements_salaires,
            "revenus_capitaux_mobiliers": self.revenus_capitaux_mobiliers,
            "revenus_fonciers": self.revenus_fonciers,
            "autres_revenus": self.autres_revenus,
            "charges_deductibles": self.charges_deductibles,
            "abattement": self.abattement,
            "nombre_parts": self.nombre_parts,
            "revenu_brut_global": self.revenu_brut_global,
            "revenu_imposable": self.revenu_imposable,
            "impot_brut": self.impot_brut,
            "reduction_impot": self.reduction_impot,
            "credit_impot": self.credit_impot,
            "impot_net": self.impot_net,
            "prelevement_a_la_source": self.prelevement_a_la_source,
            "solde_a_payer": self.solde_a_payer,
            "date_limite": self.date_limite,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """Squelette XML SAF-T (OCDE SAF-T FR, simplifié)."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:FR">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.numero_fiscal_chiffre}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.annee}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            '  <TaxReturn type="IR" formulaire="2042">\n'
            f'    <TraitementsSalaires>{self.traitements_salaires:.2f}</TraitementsSalaires>\n'
            f'    <RevenusCapitauxMobiliers>{self.revenus_capitaux_mobiliers:.2f}</RevenusCapitauxMobiliers>\n'
            f'    <RevenusFonciers>{self.revenus_fonciers:.2f}</RevenusFonciers>\n'
            f'    <AutresRevenus>{self.autres_revenus:.2f}</AutresRevenus>\n'
            f'    <RevenuBrutGlobal>{self.revenu_brut_global:.2f}</RevenuBrutGlobal>\n'
            f'    <RevenuImposable>{self.revenu_imposable:.2f}</RevenuImposable>\n'
            f'    <NombreParts>{self.nombre_parts:.2f}</NombreParts>\n'
            f'    <ImpotBrut>{self.impot_brut:.2f}</ImpotBrut>\n'
            f'    <ImpotNet>{self.impot_net:.2f}</ImpotNet>\n'
            f'    <PrelevementALaSource>{self.prelevement_a_la_source:.2f}</PrelevementALaSource>\n'
            f'    <SoldeAPayer>{self.solde_a_payer:.2f}</SoldeAPayer>\n'
            f'    <DateLimite>{self.date_limite}</DateLimite>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


def generer_liasse_2065(
    entite_id: str,
    siren: str,
    exercice: int,
    donnees_comptables: dict,
) -> LiasseFiscale2065:
    """Génère la liasse fiscale IS (2065) à partir des données du grand livre.

    Clés de donnees_comptables (toutes optionnelles) :
      chiffre_affaires, cout_des_ventes, charges_exploitation,
      resultat_financier, pme, credit_impot
    """
    liasse = LiasseFiscale2065(
        entite_id=entite_id,
        siren=siren,
        exercice=exercice,
        chiffre_affaires=float(donnees_comptables.get("chiffre_affaires", 0.0)),
        cout_des_ventes=float(donnees_comptables.get("cout_des_ventes", 0.0)),
        charges_exploitation=float(donnees_comptables.get("charges_exploitation", 0.0)),
        resultat_financier=float(donnees_comptables.get("resultat_financier", 0.0)),
        pme=bool(donnees_comptables.get("pme", False)),
        credit_impot=float(donnees_comptables.get("credit_impot", 0.0)),
    )
    return liasse.calculer()


def generer_ir_2042(
    personne_id: str,
    numero_fiscal_chiffre: str,
    annee: int,
    donnees_revenus: dict,
) -> DeclarationIR2042:
    """Génère la déclaration IR (2042) pour un particulier.

    Clés de donnees_revenus (toutes optionnelles) :
      traitements_salaires, revenus_capitaux_mobiliers, revenus_fonciers,
      autres_revenus, charges_deductibles, abattement, nombre_parts,
      reduction_impot, credit_impot, prelevement_a_la_source
    """
    declaration = DeclarationIR2042(
        personne_id=personne_id,
        numero_fiscal_chiffre=numero_fiscal_chiffre,
        annee=annee,
        traitements_salaires=float(donnees_revenus.get("traitements_salaires", 0.0)),
        revenus_capitaux_mobiliers=float(donnees_revenus.get("revenus_capitaux_mobiliers", 0.0)),
        revenus_fonciers=float(donnees_revenus.get("revenus_fonciers", 0.0)),
        autres_revenus=float(donnees_revenus.get("autres_revenus", 0.0)),
        charges_deductibles=float(donnees_revenus.get("charges_deductibles", 0.0)),
        abattement=float(donnees_revenus.get("abattement", 0.0)),
        nombre_parts=float(donnees_revenus.get("nombre_parts", 1.0)),
        reduction_impot=float(donnees_revenus.get("reduction_impot", 0.0)),
        credit_impot=float(donnees_revenus.get("credit_impot", 0.0)),
        prelevement_a_la_source=float(donnees_revenus.get("prelevement_a_la_source", 0.0)),
    )
    return declaration.calculer()
