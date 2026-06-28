"""VPB en IB aangifte helpers voor Nederlandse entiteiten."""
from __future__ import annotations
from dataclasses import dataclass, field
import json
import datetime

__all__ = ["VPBAangifte", "IBAangifte", "genereer_vpb_aangifte", "genereer_ib_aangifte"]

# ---------------------------------------------------------------------------
# VPB tarieven 2024/2025 (Wet VPB 1969, art. 22)
# Schijf 1: t/m €200.000 → 19%
# Schijf 2: boven €200.000 → 25,8%
# ---------------------------------------------------------------------------
_VPB_SCHIJF1_GRENS = 200_000.0
_VPB_SCHIJF1_TARIEF = 0.19
_VPB_SCHIJF2_TARIEF = 0.258

# ---------------------------------------------------------------------------
# IB tarieven 2025
# Box 1 (schijf 1: t/m €38.441 → 35,82%; schijf 2: daarboven → 49,50%)
# Box 2: 24,5% t/m €67.000; 33% daarboven (ab-houders)
# Box 3: heffing over fictief rendement; 2025 rate ≈ 36% over grondslag
#         Vrijstelling: €57.684 per persoon (2025)
# ---------------------------------------------------------------------------
_IB_BOX1_SCHIJF1_GRENS = 38_441.0
_IB_BOX1_SCHIJF1_TARIEF = 0.3582
_IB_BOX1_SCHIJF2_TARIEF = 0.4950

_IB_BOX2_SCHIJF1_GRENS = 67_000.0
_IB_BOX2_SCHIJF1_TARIEF = 0.245
_IB_BOX2_SCHIJF2_TARIEF = 0.33

_IB_BOX3_FICTIEF_RENDEMENT = 0.036   # fictief rendement 2025 (spaargeld/beleggingen gemiddeld)
_IB_BOX3_TARIEF = 0.36
_IB_BOX3_VRIJSTELLING = 57_684.0

# Heffingskortingen 2025 (vereenvoudigd, maximale bedragen)
_ALGEMENE_HEFFINGSKORTING_MAX = 3_362.0
_ARBEIDSKORTING_MAX = 5_158.0


@dataclass
class VPBAangifte:
    """Vennootschapsbelasting aangifte (vereenvoudigd)."""
    entiteit_id: str
    kvk: str
    jaar: int
    # Winst & Verliesrekening (vereenvoudigd)
    omzet: float = 0.0
    kostprijs_omzet: float = 0.0
    brutowinst: float = 0.0
    personeelskosten: float = 0.0
    huisvestingskosten: float = 0.0
    afschrijvingen: float = 0.0
    overige_bedrijfskosten: float = 0.0
    bedrijfsresultaat: float = 0.0
    financiele_baten_lasten: float = 0.0
    resultaat_voor_belasting: float = 0.0
    # Fiscale correcties
    wbso_aftrek: float = 0.0
    innovatiebox_winst: float = 0.0
    niet_aftrekbare_kosten: float = 0.0
    belastbare_winst: float = 0.0
    # VPB berekening
    vpb_schijf_1: float = 0.0
    vpb_schijf_2: float = 0.0
    vpb_totaal: float = 0.0
    # Aangiftedeadline
    deadline: str = ""

    def bereken(self) -> "VPBAangifte":
        """Herbereken alle afleide velden."""
        # W&V
        self.brutowinst = self.omzet - self.kostprijs_omzet
        totaal_opex = (
            self.personeelskosten
            + self.huisvestingskosten
            + self.afschrijvingen
            + self.overige_bedrijfskosten
        )
        self.bedrijfsresultaat = self.brutowinst - totaal_opex
        self.resultaat_voor_belasting = self.bedrijfsresultaat + self.financiele_baten_lasten

        # Fiscale winst
        # Innovatiebox: gekwalificeerde winst belast tegen effectief 9% i.p.v. normaal tarief.
        # Hier verminderen we de grondslag met het innovatiebox-gedeelte (correctie apart gehouden).
        self.belastbare_winst = max(
            0.0,
            self.resultaat_voor_belasting
            - self.wbso_aftrek
            - self.innovatiebox_winst
            + self.niet_aftrekbare_kosten,
        )

        # VPB berekening (art. 22 Wet VPB)
        if self.belastbare_winst <= _VPB_SCHIJF1_GRENS:
            self.vpb_schijf_1 = self.belastbare_winst * _VPB_SCHIJF1_TARIEF
            self.vpb_schijf_2 = 0.0
        else:
            self.vpb_schijf_1 = _VPB_SCHIJF1_GRENS * _VPB_SCHIJF1_TARIEF
            self.vpb_schijf_2 = (self.belastbare_winst - _VPB_SCHIJF1_GRENS) * _VPB_SCHIJF2_TARIEF

        # Innovatiebox-voordeel: over innovatiebox_winst geldt 9% i.p.v. normaal tarief
        innovatiebox_vpb = self.innovatiebox_winst * 0.09

        self.vpb_totaal = self.vpb_schijf_1 + self.vpb_schijf_2 + innovatiebox_vpb

        # Aangiftedeadline: standaard 1 juni volgend jaar (of uitstelregeling accountant: 1 mei jaar+1)
        self.deadline = f"{self.jaar + 1}-06-01"

        return self

    def to_dict(self) -> dict:
        return {
            "entiteit_id": self.entiteit_id,
            "kvk": self.kvk,
            "jaar": self.jaar,
            "omzet": self.omzet,
            "kostprijs_omzet": self.kostprijs_omzet,
            "brutowinst": self.brutowinst,
            "personeelskosten": self.personeelskosten,
            "huisvestingskosten": self.huisvestingskosten,
            "afschrijvingen": self.afschrijvingen,
            "overige_bedrijfskosten": self.overige_bedrijfskosten,
            "bedrijfsresultaat": self.bedrijfsresultaat,
            "financiele_baten_lasten": self.financiele_baten_lasten,
            "resultaat_voor_belasting": self.resultaat_voor_belasting,
            "wbso_aftrek": self.wbso_aftrek,
            "innovatiebox_winst": self.innovatiebox_winst,
            "niet_aftrekbare_kosten": self.niet_aftrekbare_kosten,
            "belastbare_winst": self.belastbare_winst,
            "vpb_schijf_1": self.vpb_schijf_1,
            "vpb_schijf_2": self.vpb_schijf_2,
            "vpb_totaal": self.vpb_totaal,
            "deadline": self.deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T NL, vereenvoudigd)."""
        d = self.to_dict()
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:NL">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.kvk}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.jaar}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <Omzet>{self.omzet:.2f}</Omzet>\n'
            f'    <KostprijsOmzet>{self.kostprijs_omzet:.2f}</KostprijsOmzet>\n'
            f'    <Brutowinst>{self.brutowinst:.2f}</Brutowinst>\n'
            f'    <Personeelskosten>{self.personeelskosten:.2f}</Personeelskosten>\n'
            f'    <Huisvestingskosten>{self.huisvestingskosten:.2f}</Huisvestingskosten>\n'
            f'    <Afschrijvingen>{self.afschrijvingen:.2f}</Afschrijvingen>\n'
            f'    <OverigeBedrijfskosten>{self.overige_bedrijfskosten:.2f}</OverigeBedrijfskosten>\n'
            f'    <Bedrijfsresultaat>{self.bedrijfsresultaat:.2f}</Bedrijfsresultaat>\n'
            f'    <FinancieleBatenLasten>{self.financiele_baten_lasten:.2f}</FinancieleBatenLasten>\n'
            f'    <ResultaatVoorBelasting>{self.resultaat_voor_belasting:.2f}</ResultaatVoorBelasting>\n'
            "  </GeneralLedger>\n"
            "  <TaxReturn type=\"VPB\">\n"
            f'    <WBSOAftrek>{self.wbso_aftrek:.2f}</WBSOAftrek>\n'
            f'    <InnovatieboxWinst>{self.innovatiebox_winst:.2f}</InnovatieboxWinst>\n'
            f'    <NietAftrekbareKosten>{self.niet_aftrekbare_kosten:.2f}</NietAftrekbareKosten>\n'
            f'    <BelastbareWinst>{self.belastbare_winst:.2f}</BelastbareWinst>\n'
            f'    <VPBSchijf1>{self.vpb_schijf_1:.2f}</VPBSchijf1>\n'
            f'    <VPBSchijf2>{self.vpb_schijf_2:.2f}</VPBSchijf2>\n'
            f'    <VPBTotaal>{self.vpb_totaal:.2f}</VPBTotaal>\n'
            f'    <Deadline>{self.deadline}</Deadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class IBAangifte:
    """Inkomstenbelasting aangifte (DGA, ZZP, particulier)."""
    persoon_id: str
    bsn_versleuteld: str    # vault-encrypted BSN
    jaar: int
    # Box 1: Werk en woning
    salaris_dga: float = 0.0
    overig_inkomen: float = 0.0
    eigenwoningforfait: float = 0.0
    hypotheekrente_aftrek: float = 0.0
    lijfrente_aftrek: float = 0.0
    box1_inkomen: float = 0.0
    # Box 2: Aanmerkelijk belang
    dividend_ontvangen: float = 0.0
    box2_inkomen: float = 0.0
    # Box 3: Sparen en beleggen
    spaargeld: float = 0.0
    beleggingen: float = 0.0
    heffingsvrij_vermogen: float = 0.0
    box3_grondslag: float = 0.0
    # Heffingskortingen
    algemene_heffingskorting: float = 0.0
    arbeidskorting: float = 0.0
    # Belasting
    ib_box1: float = 0.0
    ib_box2: float = 0.0
    ib_box3: float = 0.0
    ib_totaal: float = 0.0
    reeds_ingehouden_loonheffing: float = 0.0
    te_betalen: float = 0.0

    def bereken(self) -> "IBAangifte":
        """Herbereken alle afleide velden."""
        # --- Box 1 ---
        bruto_box1 = (
            self.salaris_dga
            + self.overig_inkomen
            + self.eigenwoningforfait
            - self.hypotheekrente_aftrek
            - self.lijfrente_aftrek
        )
        self.box1_inkomen = max(0.0, bruto_box1)

        if self.box1_inkomen <= _IB_BOX1_SCHIJF1_GRENS:
            self.ib_box1 = self.box1_inkomen * _IB_BOX1_SCHIJF1_TARIEF
        else:
            self.ib_box1 = (
                _IB_BOX1_SCHIJF1_GRENS * _IB_BOX1_SCHIJF1_TARIEF
                + (self.box1_inkomen - _IB_BOX1_SCHIJF1_GRENS) * _IB_BOX1_SCHIJF2_TARIEF
            )

        # --- Box 2 ---
        self.box2_inkomen = self.dividend_ontvangen
        if self.box2_inkomen <= _IB_BOX2_SCHIJF1_GRENS:
            self.ib_box2 = self.box2_inkomen * _IB_BOX2_SCHIJF1_TARIEF
        else:
            self.ib_box2 = (
                _IB_BOX2_SCHIJF1_GRENS * _IB_BOX2_SCHIJF1_TARIEF
                + (self.box2_inkomen - _IB_BOX2_SCHIJF1_GRENS) * _IB_BOX2_SCHIJF2_TARIEF
            )

        # --- Box 3 ---
        if self.heffingsvrij_vermogen == 0.0:
            self.heffingsvrij_vermogen = _IB_BOX3_VRIJSTELLING
        totaal_vermogen = self.spaargeld + self.beleggingen
        self.box3_grondslag = max(0.0, totaal_vermogen - self.heffingsvrij_vermogen)
        fictief_rendement = self.box3_grondslag * _IB_BOX3_FICTIEF_RENDEMENT
        self.ib_box3 = fictief_rendement * _IB_BOX3_TARIEF

        # --- Heffingskortingen (vereenvoudigd: maximale kortingen, afbouw niet gemodelleerd) ---
        if self.algemene_heffingskorting == 0.0:
            self.algemene_heffingskorting = _ALGEMENE_HEFFINGSKORTING_MAX
        if self.arbeidskorting == 0.0 and (self.salaris_dga + self.overig_inkomen) > 0:
            self.arbeidskorting = _ARBEIDSKORTING_MAX

        totale_kortingen = self.algemene_heffingskorting + self.arbeidskorting

        # --- Totaal IB ---
        self.ib_totaal = max(0.0, self.ib_box1 + self.ib_box2 + self.ib_box3 - totale_kortingen)
        self.te_betalen = self.ib_totaal - self.reeds_ingehouden_loonheffing

        return self

    def to_dict(self) -> dict:
        return {
            "persoon_id": self.persoon_id,
            "bsn_versleuteld": self.bsn_versleuteld,
            "jaar": self.jaar,
            "salaris_dga": self.salaris_dga,
            "overig_inkomen": self.overig_inkomen,
            "eigenwoningforfait": self.eigenwoningforfait,
            "hypotheekrente_aftrek": self.hypotheekrente_aftrek,
            "lijfrente_aftrek": self.lijfrente_aftrek,
            "box1_inkomen": self.box1_inkomen,
            "dividend_ontvangen": self.dividend_ontvangen,
            "box2_inkomen": self.box2_inkomen,
            "spaargeld": self.spaargeld,
            "beleggingen": self.beleggingen,
            "heffingsvrij_vermogen": self.heffingsvrij_vermogen,
            "box3_grondslag": self.box3_grondslag,
            "algemene_heffingskorting": self.algemene_heffingskorting,
            "arbeidskorting": self.arbeidskorting,
            "ib_box1": self.ib_box1,
            "ib_box2": self.ib_box2,
            "ib_box3": self.ib_box3,
            "ib_totaal": self.ib_totaal,
            "reeds_ingehouden_loonheffing": self.reeds_ingehouden_loonheffing,
            "te_betalen": self.te_betalen,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


def genereer_vpb_aangifte(
    entiteit_id: str,
    kvk: str,
    jaar: int,
    ledger_data: dict,
) -> VPBAangifte:
    """Genereer VPB aangifte vanuit P&L data uit de ledger.

    ledger_data sleutels (allemaal optioneel):
      omzet, kosten, kostprijs_omzet, personeelskosten,
      huisvestingskosten, afschrijvingen, overige_bedrijfskosten,
      financiele_baten_lasten, wbso_aftrek, innovatiebox_winst,
      niet_aftrekbare_kosten
    """
    omzet = float(ledger_data.get("omzet", 0.0))

    # 'kosten' is een shorthand voor totale operationele kosten minus kostprijs.
    # Als 'kosten' opgegeven is zonder specificatie, verdelen we het als overige_bedrijfskosten.
    kosten_totaal = float(ledger_data.get("kosten", 0.0))

    kostprijs_omzet = float(ledger_data.get("kostprijs_omzet", 0.0))
    personeelskosten = float(ledger_data.get("personeelskosten", 0.0))
    huisvestingskosten = float(ledger_data.get("huisvestingskosten", 0.0))
    afschrijvingen = float(ledger_data.get("afschrijvingen", 0.0))
    overige_bedrijfskosten = float(ledger_data.get("overige_bedrijfskosten", 0.0))

    # Als 'kosten' opgegeven maar geen gespecificeerde kostencategorieën:
    if kosten_totaal > 0 and not any(
        ledger_data.get(k) for k in (
            "kostprijs_omzet", "personeelskosten",
            "huisvestingskosten", "afschrijvingen", "overige_bedrijfskosten"
        )
    ):
        overige_bedrijfskosten = kosten_totaal

    aangifte = VPBAangifte(
        entiteit_id=entiteit_id,
        kvk=kvk,
        jaar=jaar,
        omzet=omzet,
        kostprijs_omzet=kostprijs_omzet,
        personeelskosten=personeelskosten,
        huisvestingskosten=huisvestingskosten,
        afschrijvingen=afschrijvingen,
        overige_bedrijfskosten=overige_bedrijfskosten,
        financiele_baten_lasten=float(ledger_data.get("financiele_baten_lasten", 0.0)),
        wbso_aftrek=float(ledger_data.get("wbso_aftrek", 0.0)),
        innovatiebox_winst=float(ledger_data.get("innovatiebox_winst", 0.0)),
        niet_aftrekbare_kosten=float(ledger_data.get("niet_aftrekbare_kosten", 0.0)),
    )
    return aangifte.bereken()


def genereer_ib_aangifte(
    persoon_id: str,
    bsn_versleuteld: str,
    jaar: int,
    inkomen_data: dict,
) -> IBAangifte:
    """Genereer IB aangifte voor particulier/DGA.

    inkomen_data sleutels (allemaal optioneel):
      salaris_dga, overig_inkomen, eigenwoningforfait,
      hypotheekrente_aftrek, lijfrente_aftrek,
      dividend_ontvangen, spaargeld, beleggingen,
      heffingsvrij_vermogen (default: wettelijk vrijgesteld bedrag),
      algemene_heffingskorting, arbeidskorting,
      reeds_ingehouden_loonheffing
    """
    aangifte = IBAangifte(
        persoon_id=persoon_id,
        bsn_versleuteld=bsn_versleuteld,
        jaar=jaar,
        salaris_dga=float(inkomen_data.get("salaris_dga", 0.0)),
        overig_inkomen=float(inkomen_data.get("overig_inkomen", 0.0)),
        eigenwoningforfait=float(inkomen_data.get("eigenwoningforfait", 0.0)),
        hypotheekrente_aftrek=float(inkomen_data.get("hypotheekrente_aftrek", 0.0)),
        lijfrente_aftrek=float(inkomen_data.get("lijfrente_aftrek", 0.0)),
        dividend_ontvangen=float(inkomen_data.get("dividend_ontvangen", 0.0)),
        spaargeld=float(inkomen_data.get("spaargeld", 0.0)),
        beleggingen=float(inkomen_data.get("beleggingen", 0.0)),
        heffingsvrij_vermogen=float(inkomen_data.get("heffingsvrij_vermogen", 0.0)),
        algemene_heffingskorting=float(inkomen_data.get("algemene_heffingskorting", 0.0)),
        arbeidskorting=float(inkomen_data.get("arbeidskorting", 0.0)),
        reeds_ingehouden_loonheffing=float(inkomen_data.get("reeds_ingehouden_loonheffing", 0.0)),
    )
    return aangifte.bereken()
