"""RGS NEN4400 — Referentie Grootboekschema voor Nederlandse BV/MKB.

Niveau 1-3 rekeningschema conform NEN4400 en Belastingdienst-eisen.
107 rekeningen, ingedeeld in: Balans (Activa/Passiva) en W&V (Opbrengsten/Kosten).
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

__all__ = ["AccountCategory", "RGSAccount", "RGS_NL", "get_account", "accounts_by_category"]


class AccountCategory(Enum):
    BALANS_ACTIVA = "Balans/Activa"
    BALANS_PASSIVA = "Balans/Passiva"
    WV_OPBRENGSTEN = "W&V/Opbrengsten"
    WV_PERSONEELSKOSTEN = "W&V/Personeelskosten"
    WV_KOSTEN = "W&V/Kosten"
    WV_AFSCHRIJVINGEN = "W&V/Afschrijvingen"
    WV_FINANCIEEL = "W&V/Financieel"
    WV_BELASTINGEN = "W&V/Belastingen"


@dataclass(frozen=True)
class RGSAccount:
    code: str
    name: str
    statement: str   # "Balans" or "W&V"
    category: str    # "Activa", "Passiva", "Opbrengsten", "Personeelskosten", etc.

    @property
    def is_asset(self) -> bool:
        return self.statement == "Balans" and self.category == "Activa"

    @property
    def is_liability(self) -> bool:
        return self.statement == "Balans" and self.category == "Passiva"

    @property
    def is_revenue(self) -> bool:
        return self.statement == "W&V" and self.category == "Opbrengsten"

    @property
    def is_expense(self) -> bool:
        return self.statement == "W&V" and self.category != "Opbrengsten"


# Full RGS dict: code → RGSAccount (ported from rgs_source.py RGS_SCHEMA)
RGS_NL: dict[str, RGSAccount] = {
    # ─── 0: VASTE ACTIVA ─────────────────────────────────────
    '0100': RGSAccount('0100', 'Immateriële vaste activa', 'Balans', 'Activa'),
    '0110': RGSAccount('0110', 'Kosten van ontwikkeling', 'Balans', 'Activa'),
    '0120': RGSAccount('0120', 'Concessies, vergunningen, IP', 'Balans', 'Activa'),
    '0130': RGSAccount('0130', 'Goodwill', 'Balans', 'Activa'),
    '0140': RGSAccount('0140', 'Software', 'Balans', 'Activa'),
    '0200': RGSAccount('0200', 'Materiële vaste activa', 'Balans', 'Activa'),
    '0210': RGSAccount('0210', 'Bedrijfsgebouwen', 'Balans', 'Activa'),
    '0220': RGSAccount('0220', 'Machines en installaties', 'Balans', 'Activa'),
    '0230': RGSAccount('0230', 'Inventaris en inrichting', 'Balans', 'Activa'),
    '0240': RGSAccount('0240', 'Vervoermiddelen', 'Balans', 'Activa'),
    '0250': RGSAccount('0250', 'Hardware / ICT', 'Balans', 'Activa'),
    '0300': RGSAccount('0300', 'Financiële vaste activa', 'Balans', 'Activa'),
    '0310': RGSAccount('0310', 'Deelnemingen', 'Balans', 'Activa'),
    '0320': RGSAccount('0320', 'Leningen u/g', 'Balans', 'Activa'),
    '0330': RGSAccount('0330', 'Deelneming EHMAC BV', 'Balans', 'Activa'),
    '0340': RGSAccount('0340', 'Deelneming SLAG BV (25%)', 'Balans', 'Activa'),

    # ─── INTERCOMPANY RC ─────────────────────────────────────
    '0350': RGSAccount('0350', 'RC vordering op EHMAC BV', 'Balans', 'Activa'),
    '0360': RGSAccount('0360', 'RC vordering op DGA privé', 'Balans', 'Activa'),

    # ─── 1: VLOTTENDE ACTIVA ─────────────────────────────────
    '1000': RGSAccount('1000', 'Voorraden', 'Balans', 'Activa'),
    '1100': RGSAccount('1100', 'Onderhanden werk', 'Balans', 'Activa'),
    '1200': RGSAccount('1200', 'Debiteuren', 'Balans', 'Activa'),
    '1210': RGSAccount('1210', 'Debiteuren binnenland', 'Balans', 'Activa'),
    '1220': RGSAccount('1220', 'Debiteuren buitenland', 'Balans', 'Activa'),
    '1300': RGSAccount('1300', 'Overige vorderingen', 'Balans', 'Activa'),
    '1310': RGSAccount('1310', 'Te ontvangen BTW', 'Balans', 'Activa'),
    '1320': RGSAccount('1320', 'Vooruitbetaalde bedragen', 'Balans', 'Activa'),
    '1330': RGSAccount('1330', 'RC vordering DGA', 'Balans', 'Activa'),
    '1400': RGSAccount('1400', 'Liquide middelen', 'Balans', 'Activa'),
    '1410': RGSAccount('1410', 'Kas', 'Balans', 'Activa'),
    '1420': RGSAccount('1420', 'Bank zakelijke rekening', 'Balans', 'Activa'),
    '1430': RGSAccount('1430', 'Bank G-rekening', 'Balans', 'Activa'),
    '1440': RGSAccount('1440', 'Spaarrekening', 'Balans', 'Activa'),
    '1500': RGSAccount('1500', 'Overlopende activa', 'Balans', 'Activa'),
    '1510': RGSAccount('1510', 'Nog te ontvangen bedragen', 'Balans', 'Activa'),
    '1520': RGSAccount('1520', 'Vooruitbetaalde bedragen (overlopend)', 'Balans', 'Activa'),

    # ─── 2: EIGEN VERMOGEN & VOORZIENINGEN ───────────────────
    '2000': RGSAccount('2000', 'Eigen vermogen', 'Balans', 'Passiva'),
    '2010': RGSAccount('2010', 'Aandelenkapitaal', 'Balans', 'Passiva'),
    '2020': RGSAccount('2020', 'Agioreserve', 'Balans', 'Passiva'),
    '2030': RGSAccount('2030', 'Overige reserves', 'Balans', 'Passiva'),
    '2040': RGSAccount('2040', 'Onverdeelde winst', 'Balans', 'Passiva'),
    '2050': RGSAccount('2050', 'Resultaat boekjaar', 'Balans', 'Passiva'),
    '2100': RGSAccount('2100', 'Voorzieningen', 'Balans', 'Passiva'),

    # ─── 3: LANGLOPENDE SCHULDEN ─────────────────────────────
    '3000': RGSAccount('3000', 'Langlopende schulden', 'Balans', 'Passiva'),
    '3010': RGSAccount('3010', 'Hypothecaire leningen', 'Balans', 'Passiva'),
    '3020': RGSAccount('3020', 'Leningen o/g', 'Balans', 'Passiva'),
    '3030': RGSAccount('3030', 'RC schuld aan holding', 'Balans', 'Passiva'),

    # ─── 4: KORTLOPENDE SCHULDEN ─────────────────────────────
    '4000': RGSAccount('4000', 'Kortlopende schulden', 'Balans', 'Passiva'),
    '4010': RGSAccount('4010', 'Crediteuren', 'Balans', 'Passiva'),
    '4020': RGSAccount('4020', 'Af te dragen BTW', 'Balans', 'Passiva'),
    '4030': RGSAccount('4030', 'Af te dragen loonheffing', 'Balans', 'Passiva'),
    '4040': RGSAccount('4040', 'Te betalen VPB', 'Balans', 'Passiva'),
    '4050': RGSAccount('4050', 'Overige schulden', 'Balans', 'Passiva'),
    '4060': RGSAccount('4060', 'Geblokkeerde rekening (G-rekening)', 'Balans', 'Passiva'),
    '4070': RGSAccount('4070', 'Overlopende passiva', 'Balans', 'Passiva'),
    '4080': RGSAccount('4080', 'Nog te betalen bedragen', 'Balans', 'Passiva'),

    # ─── 8: OPBRENGSTEN ──────────────────────────────────────
    '8000': RGSAccount('8000', 'Netto-omzet', 'W&V', 'Opbrengsten'),
    '8010': RGSAccount('8010', 'Omzet dienstverlening binnenland', 'W&V', 'Opbrengsten'),
    '8020': RGSAccount('8020', 'Omzet dienstverlening buitenland', 'W&V', 'Opbrengsten'),
    '8030': RGSAccount('8030', 'Omzet producten', 'W&V', 'Opbrengsten'),
    '8100': RGSAccount('8100', 'Overige bedrijfsopbrengsten', 'W&V', 'Opbrengsten'),
    '8110': RGSAccount('8110', 'Subsidies (WBSO)', 'W&V', 'Opbrengsten'),

    # ─── PERSONEELSKOSTEN ────────────────────────────────────
    '4100': RGSAccount('4100', 'Lonen en salarissen', 'W&V', 'Personeelskosten'),
    '4110': RGSAccount('4110', 'DGA-salaris', 'W&V', 'Personeelskosten'),
    '4120': RGSAccount('4120', 'Lonen werknemers', 'W&V', 'Personeelskosten'),
    '4130': RGSAccount('4130', 'Sociale lasten', 'W&V', 'Personeelskosten'),
    '4140': RGSAccount('4140', 'Pensioenlasten', 'W&V', 'Personeelskosten'),
    '4150': RGSAccount('4150', 'Inhuur personeel (uitzendkrachten)', 'W&V', 'Personeelskosten'),
    '4160': RGSAccount('4160', 'Reiskostenvergoeding', 'W&V', 'Personeelskosten'),

    # ─── HUISVESTING ─────────────────────────────────────────
    '4200': RGSAccount('4200', 'Huisvestingskosten', 'W&V', 'Bedrijfskosten'),
    '4210': RGSAccount('4210', 'Huur bedrijfspand', 'W&V', 'Bedrijfskosten'),
    '4220': RGSAccount('4220', 'Energie en water', 'W&V', 'Bedrijfskosten'),
    '4230': RGSAccount('4230', 'Onderhoud bedrijfspand', 'W&V', 'Bedrijfskosten'),
    '4240': RGSAccount('4240', 'Verzekeringen pand', 'W&V', 'Bedrijfskosten'),

    # ─── VERVOER ─────────────────────────────────────────────
    '4300': RGSAccount('4300', 'Vervoerskosten', 'W&V', 'Bedrijfskosten'),
    '4310': RGSAccount('4310', 'Brandstof / laden', 'W&V', 'Bedrijfskosten'),
    '4320': RGSAccount('4320', 'Lease auto', 'W&V', 'Bedrijfskosten'),
    '4330': RGSAccount('4330', 'Onderhoud vervoermiddelen', 'W&V', 'Bedrijfskosten'),
    '4340': RGSAccount('4340', 'Parkeerkosten', 'W&V', 'Bedrijfskosten'),

    # ─── KANTOOR ─────────────────────────────────────────────
    '4400': RGSAccount('4400', 'Kantoorkosten', 'W&V', 'Bedrijfskosten'),
    '4410': RGSAccount('4410', 'Kantoorbenodigdheden', 'W&V', 'Bedrijfskosten'),
    '4420': RGSAccount('4420', 'Telefoon en internet', 'W&V', 'Bedrijfskosten'),
    '4430': RGSAccount('4430', 'Porti en verzendkosten', 'W&V', 'Bedrijfskosten'),
    '4440': RGSAccount('4440', 'Software en licenties', 'W&V', 'Bedrijfskosten'),

    # ─── VERKOOP ─────────────────────────────────────────────
    '4500': RGSAccount('4500', 'Verkoopkosten', 'W&V', 'Bedrijfskosten'),
    '4510': RGSAccount('4510', 'Reclame en marketing', 'W&V', 'Bedrijfskosten'),
    '4520': RGSAccount('4520', 'Representatiekosten', 'W&V', 'Bedrijfskosten'),
    '4530': RGSAccount('4530', 'Relatiegeschenken', 'W&V', 'Bedrijfskosten'),

    # ─── ALGEMENE KOSTEN ─────────────────────────────────────
    '4600': RGSAccount('4600', 'Algemene kosten', 'W&V', 'Bedrijfskosten'),
    '4610': RGSAccount('4610', 'Accountant en administratie', 'W&V', 'Bedrijfskosten'),
    '4620': RGSAccount('4620', 'Juridische kosten', 'W&V', 'Bedrijfskosten'),
    '4630': RGSAccount('4630', 'Verzekeringen bedrijf', 'W&V', 'Bedrijfskosten'),
    '4640': RGSAccount('4640', 'Contributies en abonnementen', 'W&V', 'Bedrijfskosten'),
    '4650': RGSAccount('4650', 'Bankkosten', 'W&V', 'Bedrijfskosten'),
    '4660': RGSAccount('4660', 'Overige algemene kosten', 'W&V', 'Bedrijfskosten'),

    # ─── AFSCHRIJVINGEN ──────────────────────────────────────
    '4700': RGSAccount('4700', 'Afschrijvingen', 'W&V', 'Afschrijvingen'),
    '4710': RGSAccount('4710', 'Afschrijving immateriële activa', 'W&V', 'Afschrijvingen'),
    '4720': RGSAccount('4720', 'Afschrijving materiële activa', 'W&V', 'Afschrijvingen'),

    # ─── FINANCIEEL ──────────────────────────────────────────
    '4800': RGSAccount('4800', 'Financiële baten en lasten', 'W&V', 'Financieel'),
    '4810': RGSAccount('4810', 'Rentebaten', 'W&V', 'Financieel'),
    '4820': RGSAccount('4820', 'Rentelasten', 'W&V', 'Financieel'),
    '4830': RGSAccount('4830', 'Bankkosten', 'W&V', 'Financieel'),

    # ─── BELASTINGEN ─────────────────────────────────────────
    '4900': RGSAccount('4900', 'Belastingen', 'W&V', 'Belastingen'),
    '4910': RGSAccount('4910', 'Vennootschapsbelasting', 'W&V', 'Belastingen'),
}


def get_account(code: str) -> RGSAccount | None:
    return RGS_NL.get(code)


def accounts_by_category(category: str) -> list[RGSAccount]:
    return [a for a in RGS_NL.values() if a.category == category]
