"""Cameroon chart of accounts — SYSCOHADA (Système Comptable OHADA).

Cameroon is an OHADA member state: companies report under the **shared
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

Country layer: Impôt sur les sociétés (IS, 33% incl. CAC); VAT: 19.25% TVA (17.5% + 10% CAC); social security: CNPS;
tax authority: DGI (https://www.impots.cm/). Currency: XAF.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CMGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


CM_GAAP: list[CMGAAPAccount] = [
    CMGAAPAccount("101", "Capital social", "Equity", "Classe 1 — Capitaux propres", "Credit"),
    CMGAAPAccount("104", "Primes liées au capital social", "Equity", "Classe 1 — Capitaux propres", "Credit"),
    CMGAAPAccount("109", "Actionnaires, capital souscrit non appelé", "Equity", "Classe 1 — Capitaux propres", "Debit"),
    CMGAAPAccount("111", "Réserve légale", "Equity", "Classe 1 — Réserves", "Credit"),
    CMGAAPAccount("118", "Autres réserves", "Equity", "Classe 1 — Réserves", "Credit"),
    CMGAAPAccount("121", "Report à nouveau créditeur", "Equity", "Classe 1 — Report à nouveau", "Credit"),
    CMGAAPAccount("129", "Report à nouveau débiteur", "Equity", "Classe 1 — Report à nouveau", "Debit"),
    CMGAAPAccount("131", "Résultat net : bénéfice", "Equity", "Classe 1 — Résultat", "Credit"),
    CMGAAPAccount("139", "Résultat net : perte", "Equity", "Classe 1 — Résultat", "Debit"),
    CMGAAPAccount("162", "Emprunts et dettes auprès des établissements de crédit", "Liability", "Classe 1 — Dettes financières", "Credit"),
    CMGAAPAccount("168", "Autres emprunts et dettes", "Liability", "Classe 1 — Dettes financières", "Credit"),
    CMGAAPAccount("172", "Dettes de crédit-bail immobilier", "Liability", "Classe 1 — Dettes financières", "Credit"),
    CMGAAPAccount("191", "Provisions pour risques et charges", "Liability", "Classe 1 — Provisions", "Credit"),
    CMGAAPAccount("211", "Frais de développement", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    CMGAAPAccount("213", "Logiciels et sites internet", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    CMGAAPAccount("215", "Fonds commercial", "Asset", "Classe 2 — Immobilisations incorporelles", "Debit"),
    CMGAAPAccount("221", "Terrains", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CMGAAPAccount("231", "Bâtiments industriels et commerciaux", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CMGAAPAccount("241", "Matériel et outillage industriel et commercial", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CMGAAPAccount("244", "Matériel et mobilier de bureau", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CMGAAPAccount("245", "Matériel de transport", "Asset", "Classe 2 — Immobilisations corporelles", "Debit"),
    CMGAAPAccount("251", "Avances et acomptes versés sur immobilisations", "Asset", "Classe 2 — Immobilisations en cours", "Debit"),
    CMGAAPAccount("261", "Titres de participation", "Asset", "Classe 2 — Immobilisations financières", "Debit"),
    CMGAAPAccount("275", "Dépôts et cautionnements versés", "Asset", "Classe 2 — Immobilisations financières", "Debit"),
    CMGAAPAccount("2831", "Amortissements des bâtiments", "Asset", "Classe 2 — Amortissements", "Credit"),
    CMGAAPAccount("2841", "Amortissements du matériel et outillage", "Asset", "Classe 2 — Amortissements", "Credit"),
    CMGAAPAccount("2845", "Amortissements du matériel de transport", "Asset", "Classe 2 — Amortissements", "Credit"),
    CMGAAPAccount("311", "Marchandises", "Asset", "Classe 3 — Stocks", "Debit"),
    CMGAAPAccount("321", "Matières premières", "Asset", "Classe 3 — Stocks", "Debit"),
    CMGAAPAccount("331", "Autres approvisionnements", "Asset", "Classe 3 — Stocks", "Debit"),
    CMGAAPAccount("361", "Produits finis", "Asset", "Classe 3 — Stocks", "Debit"),
    CMGAAPAccount("391", "Dépréciations des stocks de marchandises", "Asset", "Classe 3 — Dépréciations", "Credit"),
    CMGAAPAccount("401", "Fournisseurs, dettes en compte", "Liability", "Classe 4 — Fournisseurs", "Credit"),
    CMGAAPAccount("409", "Fournisseurs débiteurs : avances et acomptes versés", "Asset", "Classe 4 — Fournisseurs", "Debit"),
    CMGAAPAccount("411", "Clients", "Asset", "Classe 4 — Clients", "Debit"),
    CMGAAPAccount("416", "Créances clients litigieuses ou douteuses", "Asset", "Classe 4 — Clients", "Debit"),
    CMGAAPAccount("419", "Clients créditeurs : avances et acomptes reçus", "Liability", "Classe 4 — Clients", "Credit"),
    CMGAAPAccount("421", "Personnel, avances et acomptes", "Asset", "Classe 4 — Personnel", "Debit"),
    CMGAAPAccount("422", "Personnel, rémunérations dues", "Liability", "Classe 4 — Personnel", "Credit"),
    CMGAAPAccount("431", "Sécurité sociale (CNPS)", "Liability", "Classe 4 — Organismes sociaux", "Credit"),
    CMGAAPAccount("441", "État, impôt sur les bénéfices (IS 33% incl. CAC)", "Liability", "Classe 4 — État", "Credit"),
    CMGAAPAccount("442", "État, autres impôts et taxes", "Liability", "Classe 4 — État", "Credit"),
    CMGAAPAccount("443", "État, TVA facturée", "Liability", "Classe 4 — État", "Credit"),
    CMGAAPAccount("445", "État, TVA récupérable", "Asset", "Classe 4 — État", "Debit"),
    CMGAAPAccount("447", "État, impôts retenus à la source", "Liability", "Classe 4 — État", "Credit"),
    CMGAAPAccount("449", "État, créances et dettes diverses (crédit de TVA)", "Asset", "Classe 4 — État", "Debit"),
    CMGAAPAccount("455", "Associés, comptes courants", "Liability", "Classe 4 — Associés", "Credit"),
    CMGAAPAccount("476", "Charges constatées d'avance", "Asset", "Classe 4 — Régularisations", "Debit"),
    CMGAAPAccount("477", "Produits constatés d'avance", "Liability", "Classe 4 — Régularisations", "Credit"),
    CMGAAPAccount("5211", "Banque — Afriland First Bank", "Asset", "Classe 5 — Banques", "Debit"),
    CMGAAPAccount("5212", "Banque — BICEC", "Asset", "Classe 5 — Banques", "Debit"),
    CMGAAPAccount("531", "Chèques postaux", "Asset", "Classe 5 — Trésorerie", "Debit"),
    CMGAAPAccount("561", "Banques, crédits de trésorerie (découverts)", "Liability", "Classe 5 — Trésorerie", "Credit"),
    CMGAAPAccount("571", "Caisse", "Asset", "Classe 5 — Trésorerie", "Debit"),
    CMGAAPAccount("585", "Virements de fonds", "Asset", "Classe 5 — Trésorerie", "Debit"),
    CMGAAPAccount("601", "Achats de marchandises", "Expense", "Classe 6 — Achats", "Debit"),
    CMGAAPAccount("602", "Achats de matières premières et fournitures liées", "Expense", "Classe 6 — Achats", "Debit"),
    CMGAAPAccount("604", "Achats stockés de matières et fournitures consommables", "Expense", "Classe 6 — Achats", "Debit"),
    CMGAAPAccount("605", "Autres achats (eau, électricité, fournitures)", "Expense", "Classe 6 — Achats", "Debit"),
    CMGAAPAccount("611", "Transports sur achats", "Expense", "Classe 6 — Transports", "Debit"),
    CMGAAPAccount("612", "Transports sur ventes", "Expense", "Classe 6 — Transports", "Debit"),
    CMGAAPAccount("622", "Locations et charges locatives", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("624", "Entretien, réparations et maintenance", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("625", "Primes d'assurance", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("627", "Publicité, publications, relations publiques", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("628", "Frais de télécommunications", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("631", "Frais bancaires", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("632", "Rémunérations d'intermédiaires et de conseils", "Expense", "Classe 6 — Services extérieurs", "Debit"),
    CMGAAPAccount("641", "Impôts et taxes directs (patente, taxes locales)", "Expense", "Classe 6 — Impôts et taxes", "Debit"),
    CMGAAPAccount("646", "Droits d'enregistrement", "Expense", "Classe 6 — Impôts et taxes", "Debit"),
    CMGAAPAccount("661", "Rémunérations directes versées au personnel national", "Expense", "Classe 6 — Charges de personnel", "Debit"),
    CMGAAPAccount("664", "Charges sociales (CNPS)", "Expense", "Classe 6 — Charges de personnel", "Debit"),
    CMGAAPAccount("671", "Intérêts des emprunts", "Expense", "Classe 6 — Frais financiers", "Debit"),
    CMGAAPAccount("676", "Pertes de change", "Expense", "Classe 6 — Frais financiers", "Debit"),
    CMGAAPAccount("681", "Dotations aux amortissements d'exploitation", "Expense", "Classe 6 — Dotations", "Debit"),
    CMGAAPAccount("691", "Dotations aux provisions d'exploitation", "Expense", "Classe 6 — Dotations", "Debit"),
    CMGAAPAccount("701", "Ventes de marchandises", "Revenue", "Classe 7 — Ventes", "Credit"),
    CMGAAPAccount("702", "Ventes de produits finis", "Revenue", "Classe 7 — Ventes", "Credit"),
    CMGAAPAccount("706", "Services vendus", "Revenue", "Classe 7 — Ventes", "Credit"),
    CMGAAPAccount("707", "Produits accessoires", "Revenue", "Classe 7 — Ventes", "Credit"),
    CMGAAPAccount("718", "Autres subventions d'exploitation", "Revenue", "Classe 7 — Subventions", "Credit"),
    CMGAAPAccount("758", "Produits divers", "Revenue", "Classe 7 — Autres produits", "Credit"),
    CMGAAPAccount("771", "Intérêts de prêts et créances", "Revenue", "Classe 7 — Revenus financiers", "Credit"),
    CMGAAPAccount("776", "Gains de change", "Revenue", "Classe 7 — Revenus financiers", "Credit"),
    CMGAAPAccount("812", "Valeurs comptables des cessions d'immobilisations", "Expense", "Classe 8 — HAO", "Debit"),
    CMGAAPAccount("822", "Produits des cessions d'immobilisations", "Revenue", "Classe 8 — HAO", "Credit"),
    CMGAAPAccount("891", "Impôts sur les bénéfices de l'exercice (IS 33% incl. CAC)", "Expense", "Classe 8 — Impôt sur le résultat", "Debit"),
]
