"""Plan Comptable Général (PCG) — French mandatory chart of accounts.

Classes 1-7 per the PCG as defined by the Autorité des normes comptables (ANC).
Mandatory for all French companies (Code de commerce L123-12).
"""
from __future__ import annotations
from dataclasses import dataclass

__all__ = ["PCGAccount", "PCG_FR", "get_account", "accounts_by_classe"]


@dataclass(frozen=True)
class PCGAccount:
    code: str
    name: str
    classe: int          # 1-7
    nature: str          # "actif", "passif", "charge", "produit"
    debit_normal: bool   # True = normally debited (assets, expenses); False = normally credited

    @property
    def is_asset(self) -> bool:
        return self.nature == "actif"

    @property
    def is_liability(self) -> bool:
        return self.nature == "passif"

    @property
    def is_expense(self) -> bool:
        return self.nature == "charge"

    @property
    def is_revenue(self) -> bool:
        return self.nature == "produit"


PCG_FR: list[PCGAccount] = [
    # ── Classe 1 : Comptes de capitaux ──────────────────────────────────────
    PCGAccount("101",   "Capital social ou individuel",                         1, "passif", False),
    PCGAccount("1011",  "Capital souscrit — non appelé",                        1, "passif", False),
    PCGAccount("1012",  "Capital souscrit — appelé, non versé",                 1, "passif", False),
    PCGAccount("1013",  "Capital souscrit — appelé, versé",                     1, "passif", False),
    PCGAccount("106",   "Réserves",                                             1, "passif", False),
    PCGAccount("1061",  "Réserve légale",                                       1, "passif", False),
    PCGAccount("1063",  "Réserves statutaires ou contractuelles",               1, "passif", False),
    PCGAccount("1068",  "Autres réserves",                                      1, "passif", False),
    PCGAccount("110",   "Report à nouveau (solde créditeur)",                   1, "passif", False),
    PCGAccount("119",   "Report à nouveau (solde débiteur)",                    1, "actif",  True),
    PCGAccount("120",   "Résultat de l'exercice (bénéfice)",                    1, "passif", False),
    PCGAccount("129",   "Résultat de l'exercice (perte)",                       1, "actif",  True),
    PCGAccount("131",   "Subventions d'équipement",                             1, "passif", False),
    PCGAccount("145",   "Provisions réglementées",                              1, "passif", False),
    PCGAccount("151",   "Provisions pour risques",                              1, "passif", False),
    PCGAccount("155",   "Provisions pour impôts",                               1, "passif", False),
    PCGAccount("164",   "Emprunts auprès des établissements de crédit",         1, "passif", False),
    PCGAccount("165",   "Dépôts et cautionnements reçus",                       1, "passif", False),
    PCGAccount("168",   "Autres emprunts et dettes assimilées",                 1, "passif", False),

    # ── Classe 2 : Comptes d'immobilisations ────────────────────────────────
    PCGAccount("201",   "Frais d'établissement",                                2, "actif",  True),
    PCGAccount("203",   "Frais de recherche et développement",                  2, "actif",  True),
    PCGAccount("205",   "Concessions, brevets, licences, logiciels",            2, "actif",  True),
    PCGAccount("207",   "Fonds commercial",                                     2, "actif",  True),
    PCGAccount("211",   "Terrains",                                             2, "actif",  True),
    PCGAccount("212",   "Agencements et aménagements de terrains",              2, "actif",  True),
    PCGAccount("213",   "Constructions",                                        2, "actif",  True),
    PCGAccount("215",   "Installations techniques, matériel et outillage",      2, "actif",  True),
    PCGAccount("218",   "Autres immobilisations corporelles",                   2, "actif",  True),
    PCGAccount("2182",  "Matériel de transport",                                2, "actif",  True),
    PCGAccount("2183",  "Matériel de bureau et matériel informatique",          2, "actif",  True),
    PCGAccount("261",   "Titres de participation",                              2, "actif",  True),
    PCGAccount("271",   "Titres immobilisés (droit de propriété)",              2, "actif",  True),
    PCGAccount("274",   "Prêts",                                                2, "actif",  True),
    PCGAccount("280",   "Amortissements des immobilisations incorporelles",     2, "passif", False),
    PCGAccount("281",   "Amortissements des immobilisations corporelles",       2, "passif", False),
    PCGAccount("291",   "Dépréciations des immobilisations incorporelles",      2, "passif", False),

    # ── Classe 3 : Comptes de stocks et en-cours ────────────────────────────
    PCGAccount("31",    "Matières premières et fournitures",                    3, "actif",  True),
    PCGAccount("32",    "Autres approvisionnements",                            3, "actif",  True),
    PCGAccount("33",    "En-cours de production de biens",                     3, "actif",  True),
    PCGAccount("34",    "En-cours de production de services",                  3, "actif",  True),
    PCGAccount("35",    "Stocks de produits",                                   3, "actif",  True),
    PCGAccount("37",    "Stocks de marchandises",                               3, "actif",  True),

    # ── Classe 4 : Comptes de tiers ─────────────────────────────────────────
    PCGAccount("401",   "Fournisseurs",                                         4, "passif", False),
    PCGAccount("403",   "Fournisseurs — Effets à payer",                        4, "passif", False),
    PCGAccount("408",   "Fournisseurs — Factures non parvenues",                4, "passif", False),
    PCGAccount("411",   "Clients",                                              4, "actif",  True),
    PCGAccount("413",   "Clients — Effets à recevoir",                         4, "actif",  True),
    PCGAccount("416",   "Clients douteux ou litigieux",                         4, "actif",  True),
    PCGAccount("418",   "Clients — Produits non encore facturés",               4, "actif",  True),
    PCGAccount("419",   "Clients créditeurs",                                   4, "passif", False),
    PCGAccount("421",   "Personnel — Rémunérations dues",                       4, "passif", False),
    PCGAccount("425",   "Personnel — Avances et acomptes",                      4, "actif",  True),
    PCGAccount("431",   "Sécurité sociale",                                     4, "passif", False),
    PCGAccount("437",   "Autres organismes sociaux",                            4, "passif", False),
    PCGAccount("444",   "État — Impôts sur les bénéfices",                      4, "passif", False),
    PCGAccount("445",   "État — Taxes sur le chiffre d'affaires (TVA)",         4, "passif", False),
    PCGAccount("44566", "TVA déductible sur autres biens et services",          4, "actif",  True),
    PCGAccount("44571", "TVA collectée",                                        4, "passif", False),
    PCGAccount("447",   "Autres impôts, taxes et versements assimilés",         4, "passif", False),
    PCGAccount("455",   "Associés — Comptes courants",                          4, "passif", False),
    PCGAccount("467",   "Autres comptes débiteurs ou créditeurs",               4, "actif",  True),

    # ── Classe 5 : Comptes financiers ───────────────────────────────────────
    PCGAccount("512",   "Banque",                                               5, "actif",  True),
    PCGAccount("513",   "Chèques postaux",                                      5, "actif",  True),
    PCGAccount("514",   "Chèques à encaisser",                                  5, "actif",  True),
    PCGAccount("530",   "Caisse",                                               5, "actif",  True),
    PCGAccount("580",   "Virements internes",                                   5, "actif",  True),

    # ── Classe 6 : Comptes de charges ───────────────────────────────────────
    PCGAccount("601",   "Achats stockés — Matières premières",                  6, "charge", True),
    PCGAccount("602",   "Achats stockés — Autres approvisionnements",           6, "charge", True),
    PCGAccount("604",   "Achats d'études et prestations de services",           6, "charge", True),
    PCGAccount("606",   "Achats non stockés de matières et fournitures",        6, "charge", True),
    PCGAccount("607",   "Achats de marchandises",                               6, "charge", True),
    PCGAccount("611",   "Sous-traitance générale",                              6, "charge", True),
    PCGAccount("613",   "Locations",                                            6, "charge", True),
    PCGAccount("615",   "Entretien et réparations",                             6, "charge", True),
    PCGAccount("616",   "Primes d'assurance",                                   6, "charge", True),
    PCGAccount("618",   "Divers",                                               6, "charge", True),
    PCGAccount("621",   "Personnel extérieur à l'entreprise",                   6, "charge", True),
    PCGAccount("622",   "Rémunérations d'intermédiaires et honoraires",         6, "charge", True),
    PCGAccount("623",   "Publicité, publications, relations publiques",         6, "charge", True),
    PCGAccount("624",   "Transports de biens et transports collectifs",         6, "charge", True),
    PCGAccount("625",   "Déplacements, missions et réceptions",                 6, "charge", True),
    PCGAccount("626",   "Frais postaux et de télécommunications",               6, "charge", True),
    PCGAccount("627",   "Services bancaires et assimilés",                      6, "charge", True),
    PCGAccount("628",   "Divers (cotisations, documentation…)",                 6, "charge", True),
    PCGAccount("635",   "Autres impôts, taxes et versements assimilés",         6, "charge", True),
    PCGAccount("641",   "Rémunérations du personnel",                           6, "charge", True),
    PCGAccount("644",   "Rémunération du travail de l'exploitant",              6, "charge", True),
    PCGAccount("645",   "Charges de sécurité sociale et de prévoyance",        6, "charge", True),
    PCGAccount("647",   "Autres charges sociales",                              6, "charge", True),
    PCGAccount("651",   "Redevances pour concessions, brevets, licences",       6, "charge", True),
    PCGAccount("661",   "Charges d'intérêts",                                   6, "charge", True),
    PCGAccount("671",   "Charges exceptionnelles sur opérations de gestion",    6, "charge", True),
    PCGAccount("681",   "Dotations aux amortissements — immobilisations",       6, "charge", True),
    PCGAccount("686",   "Dotations aux dépréciations financières",              6, "charge", True),
    PCGAccount("695",   "Impôts sur les bénéfices",                             6, "charge", True),

    # ── Classe 7 : Comptes de produits ──────────────────────────────────────
    PCGAccount("701",   "Ventes de produits finis",                             7, "produit", False),
    PCGAccount("706",   "Prestations de services",                              7, "produit", False),
    PCGAccount("707",   "Ventes de marchandises",                               7, "produit", False),
    PCGAccount("708",   "Produits des activités annexes",                       7, "produit", False),
    PCGAccount("709",   "Rabais, remises et ristournes accordés",               7, "produit", True),
    PCGAccount("721",   "Production immobilisée — immobilisations incorporelles",7,"produit", False),
    PCGAccount("731",   "Variations des stocks de produits en cours",           7, "produit", False),
    PCGAccount("740",   "Subventions d'exploitation",                           7, "produit", False),
    PCGAccount("751",   "Redevances pour concessions, brevets, licences reçues",7, "produit", False),
    PCGAccount("761",   "Produits de participations",                           7, "produit", False),
    PCGAccount("764",   "Revenus de valeurs mobilières de placement",           7, "produit", False),
    PCGAccount("771",   "Produits exceptionnels sur opérations de gestion",     7, "produit", False),
    PCGAccount("781",   "Reprises sur amortissements et dépréciations",         7, "produit", False),
]


def get_account(code: str) -> PCGAccount | None:
    """Return account by exact code, or None."""
    for acc in PCG_FR:
        if acc.code == code:
            return acc
    return None


def accounts_by_classe(classe: int) -> list[PCGAccount]:
    """Return all accounts belonging to the given PCG class (1-7)."""
    return [acc for acc in PCG_FR if acc.classe == classe]
