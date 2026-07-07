"""Côte d'Ivoire chart of accounts — SYSCOHADA (Système Comptable OHADA).

Côte d'Ivoire is an OHADA member state: companies report under the **shared
SYSCOHADA chart of accounts** (Système Comptable OHADA, revised AUDCIF
uniform act), common to all 17 OHADA member states. This chart follows the
SYSCOHADA classe 1-7 structure (plus classe 8 for HAO items and income tax):

* Classe 1 — Comptes de ressources durables (equity, financial debt)
* Classe 2 — Comptes d'actif immobilisé (fixed assets)
* Classe 3 — Comptes de stocks (inventories)
* Classe 4 — Comptes de tiers (receivables/payables, État/TVA)
* Classe 5 — Comptes de trésorerie (cash and banks)
* Classe 6 — Comptes de charges (expenses)
* Classe 7 — Comptes de produits (revenue)

Country layer: Impôt sur les bénéfices (BIC, 25%); VAT: 18% TVA; social security: CNPS;
tax authority: DGI (https://www.dgi.gouv.ci/). Currency: XOF.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CIGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CI_GAAP: list[CIGAAPAccount] = [
    CIGAAPAccount("101", "Capital social", "Equity", "Classe 1 — Capitaux propres", "Credit"),
    CIGAAPAccount("104", "Primes liées au capital social", "Equity", "Classe 1 — Capitaux propres", "Credit"),
    CIGAAPAccount("109", "Actionnaires, capital souscrit non appelé", "Equity", "Classe 1 — Capitaux propres", "Debit"),
    CIGAAPAccount("111", "Réserve légale", "Equity", "Classe 1 — Réserves", "Credit"),
    CIGAAPAccount("118", "Autres réserves", "Equity", "Classe 1 — Réserves", "Credit"),
    CIGAAPAccount("121", "Report à nouveau créditeur", "Equity", "Classe 1 — Report à nouveau", "Credit"),
    CIGAAPAccount("129", "Report à nouveau débiteur", "Equity", "Classe 1 — Report à nouveau", "Debit"),
    CIGAAPAccount("131", "Résultat net : bénéfice", "Equity", "Classe 1 — Résultat", "Credit"),
    CIGAAPAccount("139", "Résultat net : perte", "Equity", "Classe 1 — Résultat", "Debit"),
    CIGAAPAccount("162", "Emprunts et dettes auprès des établissements de crédit", "Liability", "Classe 1 — Dettes financières", "Credit"),
    CIGAAPAccount("168", "Autres emprunts et dettes", "Liability", "Classe 1 — Dettes financières", "Credit"),
    CIGAAPAccount("172", "Dettes de crédit-bail immobilier", "Liability", "Classe 1 — Dettes financières", "Credit"),
    CIGAAPAccount("191", "Provisions pour risques et charges", "Liability", "Classe 1 — Provisions", "Credit"),
    CIGAAPAccount("211", "Frais de développement", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    CIGAAPAccount("213", "Logiciels et sites internet", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    CIGAAPAccount("215", "Fonds commercial", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    CIGAAPAccount("221", "Terrains", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CIGAAPAccount("231", "Bâtiments industriels et commerciaux", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CIGAAPAccount("241", "Matériel et outillage industriel et commercial", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CIGAAPAccount("244", "Matériel et mobilier de bureau", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CIGAAPAccount("245", "Matériel de transport", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CIGAAPAccount("251", "Avances et acomptes versés sur immobilisations", "Asset", "Classe 2 — Immobilisations en cours", "Debit"),
    CIGAAPAccount("261", "Titres de participation", "Asset", "Classe 2 — Immobilisations financières", "Debit"),
    CIGAAPAccount("275", "Dépôts et cautionnements versés", "Asset", "Classe 2 — Immobilisations financières", "Debit"),
    CIGAAPAccount("2831", "Amortissements des bâtiments", "Asset", "Classe 2 — Amortissements", "Credit"),
    CIGAAPAccount("2841", "Amortissements du matériel et outillage", "Asset", "Classe 2 — Amortissements", "Credit"),
    CIGAAPAccount("2845", "Amortissements du matériel de transport", "Asset", "Classe 2 — Amortissements", "Credit"),
    CIGAAPAccount("311", "Marchandises", "Asset", "Classe 3 — Stocks", "Debit"),
    CIGAAPAccount("321", "Matières premières", "Asset", "Classe 3 — Stocks", "Debit"),
    CIGAAPAccount("331", "Autres approvisionnements", "Asset", "Classe 3 — Stocks", "Debit"),
    CIGAAPAccount("361", "Produits finis", "Asset", "Classe 3 — Stocks", "Debit"),
    CIGAAPAccount("391", "Dépréciations des stocks de marchandises", "Asset", "Classe 3 — Dépréciations", "Credit"),
    CIGAAPAccount("401", "Fournisseurs, dettes en compte", "Liability", "Classe 4 — Fournisseurs", "Credit"),
    CIGAAPAccount("409", "Fournisseurs débiteurs : avances et acomptes versés", "Asset", "Classe 4 — Fournisseurs", "Debit"),
    CIGAAPAccount("411", "Clients", "Asset", "Classe 4 — Clients", "Debit"),
    CIGAAPAccount("416", "Créances clients litigieuses ou douteuses", "Asset", "Classe 4 — Clients", "Debit"),
    CIGAAPAccount("419", "Clients créditeurs : avances et acomptes reçus", "Liability", "Classe 4 — Clients", "Credit"),
    CIGAAPAccount("421", "Personnel, avances et acomptes", "Asset", "Classe 4 — Personnel", "Debit"),
    CIGAAPAccount("422", "Personnel, rémunérations dues", "Liability", "Classe 4 — Personnel", "Credit"),
    CIGAAPAccount("431", "Sécurité sociale (CNPS)", "Liability", "Classe 4 — Organismes sociaux", "Credit"),
    CIGAAPAccount("441", "État, impôt sur les bénéfices (BIC 25%)", "Liability", "Classe 4 — État", "Credit"),
    CIGAAPAccount("442", "État, autres impôts et taxes", "Liability", "Classe 4 — État", "Credit"),
    CIGAAPAccount("443", "État, TVA facturée", "Liability", "Classe 4 — État", "Credit"),
    CIGAAPAccount("445", "État, TVA récupérable", "Asset", "Classe 4 — État", "Debit"),
    CIGAAPAccount("447", "État, impôts retenus à la source", "Liability", "Classe 4 — État", "Credit"),
    CIGAAPAccount("449", "État, créances et dettes diverses (crédit de TVA)", "Asset", "Classe 4 — État", "Debit"),
    CIGAAPAccount("455", "Associés, comptes courants", "Liability", "Classe 4 — Associés", "Credit"),
    CIGAAPAccount("476", "Charges constatées d'avance", "Asset", "Classe 4 — Régularisations", "Debit"),
    CIGAAPAccount("477", "Produits constatés d'avance", "Liability", "Classe 4 — Régularisations", "Credit"),
    CIGAAPAccount("5211", "Banque — SGCI (Société Générale Côte d'Ivoire)", "Asset", "Classe 5 — Banques", "Debit"),
    CIGAAPAccount("5212", "Banque — BICICI", "Asset", "Classe 5 — Banques", "Debit"),
    CIGAAPAccount("531", "Chèques postaux", "Asset", "Classe 5 — Trésorerie", "Debit"),
    CIGAAPAccount("561", "Banques, crédits de trésorerie (découverts)", "Liability", "Classe 5 — Trésorerie", "Credit"),
    CIGAAPAccount("571", "Caisse", "Asset", "Classe 5 — Trésorerie", "Debit"),
    CIGAAPAccount("585", "Virements de fonds", "Asset", "Classe 5 — Trésorerie", "Debit"),
    CIGAAPAccount("601", "Achats de marchandises", "Expense", "Classe 6 — Achats", "Debit"),
    CIGAAPAccount("602", "Achats de matières premières et fournitures liées", "Expense", "Classe 6 — Achats", "Debit"),
    CIGAAPAccount("604", "Achats stockés de matières et fournitures consommables", "Expense", "Classe 6 — Achats", "Debit"),
    CIGAAPAccount("605", "Autres achats (eau, électricité, fournitures)", "Expense", "Classe 6 — Achats", "Debit"),
    CIGAAPAccount("611", "Transports sur achats", "Expense", "Classe 6 — Transports", "Debit"),
    CIGAAPAccount("612", "Transports sur ventes", "Expense", "Classe 6 — Transports", "Debit"),
    CIGAAPAccount("622", "Locations et charges locatives", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("624", "Entretien, réparations et maintenance", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("625", "Primes d'assurance", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("627", "Publicité, publications, relations publiques", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("628", "Frais de télécommunications", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("631", "Frais bancaires", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("632", "Rémunérations d'intermédiaires et de conseils", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CIGAAPAccount("641", "Impôts et taxes directs (patente, taxes locales)", "Expense", "Classe 6 — Impôts et taxes", "Debit"),
    CIGAAPAccount("646", "Droits d'enregistrement", "Expense", "Classe 6 — Impôts et taxes", "Debit"),
    CIGAAPAccount("661", "Rémunérations directes versées au personnel national", "Expense", "Classe 6 — Charges de personnel", "Debit"),
    CIGAAPAccount("664", "Charges sociales (CNPS)", "Expense", "Classe 6 — Charges de personnel", "Debit"),
    CIGAAPAccount("671", "Intérêts des emprunts", "Expense", "Classe 6 — Frais financiers", "Debit"),
    CIGAAPAccount("676", "Pertes de change", "Expense", "Classe 6 — Frais financiers", "Debit"),
    CIGAAPAccount("681", "Dotations aux amortissements d'exploitation", "Expense", "Classe 6 — Dotations", "Debit"),
    CIGAAPAccount("691", "Dotations aux provisions d'exploitation", "Expense", "Classe 6 — Dotations", "Debit"),
    CIGAAPAccount("701", "Ventes de marchandises", "Revenue", "Classe 7 — Ventes", "Credit"),
    CIGAAPAccount("702", "Ventes de produits finis", "Revenue", "Classe 7 — Ventes", "Credit"),
    CIGAAPAccount("706", "Services vendus", "Revenue", "Classe 7 — Ventes", "Credit"),
    CIGAAPAccount("707", "Produits accessoires", "Revenue", "Classe 7 — Ventes", "Credit"),
    CIGAAPAccount("718", "Autres subventions d'exploitation", "Revenue", "Classe 7 — Subventions", "Credit"),
    CIGAAPAccount("758", "Produits divers", "Revenue", "Classe 7 — Autres produits", "Credit"),
    CIGAAPAccount("771", "Intérêts de prêts et créances", "Revenue", "Classe 7 — Revenus financiers", "Credit"),
    CIGAAPAccount("776", "Gains de change", "Revenue", "Classe 7 — Revenus financiers", "Credit"),
    CIGAAPAccount("812", "Valeurs comptables des cessions d'immobilisations", "Expense", "Classe 8 — HAO", "Debit"),
    CIGAAPAccount("822", "Produits des cessions d'immobilisations", "Revenue", "Classe 8 — HAO", "Credit"),
    CIGAAPAccount("891", "Impôts sur les bénéfices de l'exercice (BIC 25%)", "Expense", "Classe 8 — Impôt sur le résultat", "Debit"),
]
