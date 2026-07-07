"""Senegal chart of accounts — SYSCOHADA (Système Comptable OHADA).

Senegal is an OHADA member state: companies report under the **shared
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

Country layer: Impôt sur les sociétés (IS, 30%); VAT: 18% TVA; social security: CSS / IPRES;
tax authority: DGID (https://www.dgid.sn/). Currency: XOF.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SNGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


SN_GAAP: list[SNGAAPAccount] = [
    SNGAAPAccount("101", "Capital social", "Equity", "Classe 1 — Capitaux propres", "Credit"),
    SNGAAPAccount("104", "Primes liées au capital social", "Equity", "Classe 1 — Capitaux propres", "Credit"),
    SNGAAPAccount("109", "Actionnaires, capital souscrit non appelé", "Equity", "Classe 1 — Capitaux propres", "Debit"),
    SNGAAPAccount("111", "Réserve légale", "Equity", "Classe 1 — Réserves", "Credit"),
    SNGAAPAccount("118", "Autres réserves", "Equity", "Classe 1 — Réserves", "Credit"),
    SNGAAPAccount("121", "Report à nouveau créditeur", "Equity", "Classe 1 — Report à nouveau", "Credit"),
    SNGAAPAccount("129", "Report à nouveau débiteur", "Equity", "Classe 1 — Report à nouveau", "Debit"),
    SNGAAPAccount("131", "Résultat net : bénéfice", "Equity", "Classe 1 — Résultat", "Credit"),
    SNGAAPAccount("139", "Résultat net : perte", "Equity", "Classe 1 — Résultat", "Debit"),
    SNGAAPAccount("162", "Emprunts et dettes auprès des établissements de crédit", "Liability", "Classe 1 — Dettes financières", "Credit"),
    SNGAAPAccount("168", "Autres emprunts et dettes", "Liability", "Classe 1 — Dettes financières", "Credit"),
    SNGAAPAccount("172", "Dettes de crédit-bail immobilier", "Liability", "Classe 1 — Dettes financières", "Credit"),
    SNGAAPAccount("191", "Provisions pour risques et charges", "Liability", "Classe 1 — Provisions", "Credit"),
    SNGAAPAccount("211", "Frais de développement", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    SNGAAPAccount("213", "Logiciels et sites internet", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    SNGAAPAccount("215", "Fonds commercial", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    SNGAAPAccount("221", "Terrains", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    SNGAAPAccount("231", "Bâtiments industriels et commerciaux", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    SNGAAPAccount("241", "Matériel et outillage industriel et commercial", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    SNGAAPAccount("244", "Matériel et mobilier de bureau", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    SNGAAPAccount("245", "Matériel de transport", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    SNGAAPAccount("251", "Avances et acomptes versés sur immobilisations", "Asset", "Classe 2 — Immobilisations en cours", "Debit"),
    SNGAAPAccount("261", "Titres de participation", "Asset", "Classe 2 — Immobilisations financières", "Debit"),
    SNGAAPAccount("275", "Dépôts et cautionnements versés", "Asset", "Classe 2 — Immobilisations financières", "Debit"),
    SNGAAPAccount("2831", "Amortissements des bâtiments", "Asset", "Classe 2 — Amortissements", "Credit"),
    SNGAAPAccount("2841", "Amortissements du matériel et outillage", "Asset", "Classe 2 — Amortissements", "Credit"),
    SNGAAPAccount("2845", "Amortissements du matériel de transport", "Asset", "Classe 2 — Amortissements", "Credit"),
    SNGAAPAccount("311", "Marchandises", "Asset", "Classe 3 — Stocks", "Debit"),
    SNGAAPAccount("321", "Matières premières", "Asset", "Classe 3 — Stocks", "Debit"),
    SNGAAPAccount("331", "Autres approvisionnements", "Asset", "Classe 3 — Stocks", "Debit"),
    SNGAAPAccount("361", "Produits finis", "Asset", "Classe 3 — Stocks", "Debit"),
    SNGAAPAccount("391", "Dépréciations des stocks de marchandises", "Asset", "Classe 3 — Dépréciations", "Credit"),
    SNGAAPAccount("401", "Fournisseurs, dettes en compte", "Liability", "Classe 4 — Fournisseurs", "Credit"),
    SNGAAPAccount("409", "Fournisseurs débiteurs : avances et acomptes versés", "Asset", "Classe 4 — Fournisseurs", "Debit"),
    SNGAAPAccount("411", "Clients", "Asset", "Classe 4 — Clients", "Debit"),
    SNGAAPAccount("416", "Créances clients litigieuses ou douteuses", "Asset", "Classe 4 — Clients", "Debit"),
    SNGAAPAccount("419", "Clients créditeurs : avances et acomptes reçus", "Liability", "Classe 4 — Clients", "Credit"),
    SNGAAPAccount("421", "Personnel, avances et acomptes", "Asset", "Classe 4 — Personnel", "Debit"),
    SNGAAPAccount("422", "Personnel, rémunérations dues", "Liability", "Classe 4 — Personnel", "Credit"),
    SNGAAPAccount("431", "Sécurité sociale (CSS / IPRES)", "Liability", "Classe 4 — Organismes sociaux", "Credit"),
    SNGAAPAccount("441", "État, impôt sur les bénéfices (IS 30%)", "Liability", "Classe 4 — État", "Credit"),
    SNGAAPAccount("442", "État, autres impôts et taxes", "Liability", "Classe 4 — État", "Credit"),
    SNGAAPAccount("443", "État, TVA facturée", "Liability", "Classe 4 — État", "Credit"),
    SNGAAPAccount("445", "État, TVA récupérable", "Asset", "Classe 4 — État", "Debit"),
    SNGAAPAccount("447", "État, impôts retenus à la source", "Liability", "Classe 4 — État", "Credit"),
    SNGAAPAccount("449", "État, créances et dettes diverses (crédit de TVA)", "Asset", "Classe 4 — État", "Debit"),
    SNGAAPAccount("455", "Associés, comptes courants", "Liability", "Classe 4 — Associés", "Credit"),
    SNGAAPAccount("476", "Charges constatées d'avance", "Asset", "Classe 4 — Régularisations", "Debit"),
    SNGAAPAccount("477", "Produits constatés d'avance", "Liability", "Classe 4 — Régularisations", "Credit"),
    SNGAAPAccount("5211", "Banque — CBAO Groupe Attijariwafa", "Asset", "Classe 5 — Banques", "Debit"),
    SNGAAPAccount("5212", "Banque — SGBS (Société Générale Sénégal)", "Asset", "Classe 5 — Banques", "Debit"),
    SNGAAPAccount("531", "Chèques postaux", "Asset", "Classe 5 — Trésorerie", "Debit"),
    SNGAAPAccount("561", "Banques, crédits de trésorerie (découverts)", "Liability", "Classe 5 — Trésorerie", "Credit"),
    SNGAAPAccount("571", "Caisse", "Asset", "Classe 5 — Trésorerie", "Debit"),
    SNGAAPAccount("585", "Virements de fonds", "Asset", "Classe 5 — Trésorerie", "Debit"),
    SNGAAPAccount("601", "Achats de marchandises", "Expense", "Classe 6 — Achats", "Debit"),
    SNGAAPAccount("602", "Achats de matières premières et fournitures liées", "Expense", "Classe 6 — Achats", "Debit"),
    SNGAAPAccount("604", "Achats stockés de matières et fournitures consommables", "Expense", "Classe 6 — Achats", "Debit"),
    SNGAAPAccount("605", "Autres achats (eau, électricité, fournitures)", "Expense", "Classe 6 — Achats", "Debit"),
    SNGAAPAccount("611", "Transports sur achats", "Expense", "Classe 6 — Transports", "Debit"),
    SNGAAPAccount("612", "Transports sur ventes", "Expense", "Classe 6 — Transports", "Debit"),
    SNGAAPAccount("622", "Locations et charges locatives", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("624", "Entretien, réparations et maintenance", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("625", "Primes d'assurance", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("627", "Publicité, publications, relations publiques", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("628", "Frais de télécommunications", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("631", "Frais bancaires", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("632", "Rémunérations d'intermédiaires et de conseils", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    SNGAAPAccount("641", "Impôts et taxes directs (patente, taxes locales)", "Expense", "Classe 6 — Impôts et taxes", "Debit"),
    SNGAAPAccount("646", "Droits d'enregistrement", "Expense", "Classe 6 — Impôts et taxes", "Debit"),
    SNGAAPAccount("661", "Rémunérations directes versées au personnel national", "Expense", "Classe 6 — Charges de personnel", "Debit"),
    SNGAAPAccount("664", "Charges sociales (CSS / IPRES)", "Expense", "Classe 6 — Charges de personnel", "Debit"),
    SNGAAPAccount("671", "Intérêts des emprunts", "Expense", "Classe 6 — Frais financiers", "Debit"),
    SNGAAPAccount("676", "Pertes de change", "Expense", "Classe 6 — Frais financiers", "Debit"),
    SNGAAPAccount("681", "Dotations aux amortissements d'exploitation", "Expense", "Classe 6 — Dotations", "Debit"),
    SNGAAPAccount("691", "Dotations aux provisions d'exploitation", "Expense", "Classe 6 — Dotations", "Debit"),
    SNGAAPAccount("701", "Ventes de marchandises", "Revenue", "Classe 7 — Ventes", "Credit"),
    SNGAAPAccount("702", "Ventes de produits finis", "Revenue", "Classe 7 — Ventes", "Credit"),
    SNGAAPAccount("706", "Services vendus", "Revenue", "Classe 7 — Ventes", "Credit"),
    SNGAAPAccount("707", "Produits accessoires", "Revenue", "Classe 7 — Ventes", "Credit"),
    SNGAAPAccount("718", "Autres subventions d'exploitation", "Revenue", "Classe 7 — Subventions", "Credit"),
    SNGAAPAccount("758", "Produits divers", "Revenue", "Classe 7 — Autres produits", "Credit"),
    SNGAAPAccount("771", "Intérêts de prêts et créances", "Revenue", "Classe 7 — Revenus financiers", "Credit"),
    SNGAAPAccount("776", "Gains de change", "Revenue", "Classe 7 — Revenus financiers", "Credit"),
    SNGAAPAccount("812", "Valeurs comptables des cessions d'immobilisations", "Expense", "Classe 8 — HAO", "Debit"),
    SNGAAPAccount("822", "Produits des cessions d'immobilisations", "Revenue", "Classe 8 — HAO", "Credit"),
    SNGAAPAccount("891", "Impôts sur les bénéfices de l'exercice (IS 30%)", "Expense", "Classe 8 — Impôt sur le résultat", "Debit"),
]
