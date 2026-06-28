"""Loonstrook generator — Nederland 2022-2025."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

__all__ = [
    "Werknemer", "LoonstrookRegel", "Loonstrook", "genereer_loonstrook",
    "GebruikelijkLoonCheck", "controleer_gebruikelijk_loon",
]

# ---------------------------------------------------------------------------
# Tax params loader
# ---------------------------------------------------------------------------

_PARAMS_PATH = Path(__file__).parents[2] / "tax" / "NL" / "params.json"

# Fallback hardcoded 2025 values (used when params.json is absent)
_HARDCODED_PARAMS: dict[str, dict] = {
    "2025": {
        "IB": {
            "schijf_1_grens": 76817,
            "tarief_schijf_1": 0.3550,
            "tarief_schijf_2": 0.495,
            "max_algemene_heffingskorting": 3068,
            "max_arbeidskorting": 5599,
            "aow_franchise": 18475,
        },
        "ZVW": {"bijdrage_pct": 0.0557, "max_bijdragegrondslag": 75864},
        "LH": {"dga_min_salaris": 56000, "reiskostenvergoeding_per_km": 0.23},
        "Thuiswerk": {"vergoeding_per_dag": 2.40},
        "WKR": {"vrije_ruimte_pct_tot_400k": 0.02},
    }
}


def _load_params(jaar: int) -> dict:
    """Laad belastingparameters uit params.json; fallback naar hardcoded 2025."""
    try:
        data = json.loads(_PARAMS_PATH.read_text())
        year_data = data["years"].get(str(jaar))
        if year_data:
            return year_data
    except Exception:
        pass
    return _HARDCODED_PARAMS.get(str(jaar), _HARDCODED_PARAMS["2025"])


# ---------------------------------------------------------------------------
# Enums en dataclasses
# ---------------------------------------------------------------------------

class RegelSoort(Enum):
    BRUTO_SALARIS = "Bruto salaris"
    VAKANTIEGELD = "Vakantiegeld (8%)"
    ONKOSTENVERGOEDING = "Onkostenvergoeding"
    REISKOSTENVERGOEDING = "Reiskosten"
    THUISWERK_VERGOEDING = "Thuiswerkvergoeding"
    LOONHEFFING = "Loonheffing"
    ZVW_BIJDRAGE = "ZVW bijdrage werkgever"
    PENSIOEN_WERKNEMER = "Pensioeninhoud werknemer"
    PENSIOEN_WERKGEVER = "Pensioen werkgever"
    WERKGEVERSLASTEN = "Werkgeverslasten"
    WKR_EINDHEFFING = "WKR eindheffing"
    NETTO_LOON = "Netto loon"


@dataclass
class Werknemer:
    id: str
    naam: str
    bsn: str = ""                    # encrypted in vault — never logged
    jaarsalaris: float = 0.0
    pensioen_pct: float = 0.04       # 4% werknemersbijdrage
    reisafstand_km: float = 0.0      # enkele reisafstand
    thuiswerk_dagen_pw: float = 0.0
    is_dga: bool = False
    vast_contract: bool = True


@dataclass
class LoonstrookRegel:
    soort: RegelSoort
    omschrijving: str
    bedrag: float                    # positief = inkomen/last, negatief = inhoud


@dataclass
class Loonstrook:
    werknemer_id: str
    periode: str                     # YYYY-MM
    werkgever_id: str = ""
    regels: list[LoonstrookRegel] = field(default_factory=list)
    jaar: int = 2025

    def bruto(self) -> float:
        """Bruto arbeidsinkomen (werknemer-zijde, excl. werkgeverslasten)."""
        return sum(r.bedrag for r in self.regels if r.soort in {
            RegelSoort.BRUTO_SALARIS, RegelSoort.VAKANTIEGELD,
            RegelSoort.ONKOSTENVERGOEDING, RegelSoort.REISKOSTENVERGOEDING,
            RegelSoort.THUISWERK_VERGOEDING})

    def netto(self) -> float:
        """Som van alle regels (netto uitbetaling aan werknemer + werkgeverslasten)."""
        return sum(r.bedrag for r in self.regels)

    def werkgeverslasten_totaal(self) -> float:
        """Totale werkgeverslasten bovenop bruto loon."""
        return sum(r.bedrag for r in self.regels if r.soort in {
            RegelSoort.WERKGEVERSLASTEN, RegelSoort.PENSIOEN_WERKGEVER,
            RegelSoort.ZVW_BIJDRAGE})

    def to_dict(self) -> dict:
        return {
            "werknemer_id": self.werknemer_id,
            "periode": self.periode,
            "werkgever_id": self.werkgever_id,
            "jaar": self.jaar,
            "bruto": round(self.bruto(), 2),
            "netto": round(self.netto(), 2),
            "werkgeverslasten_totaal": round(self.werkgeverslasten_totaal(), 2),
            "regels": [
                {
                    "soort": r.soort.value,
                    "omschrijving": r.omschrijving,
                    "bedrag": round(r.bedrag, 2),
                }
                for r in self.regels
            ],
        }


# ---------------------------------------------------------------------------
# Heffingskorting berekeningen
# ---------------------------------------------------------------------------

# Grenzen voor afbouw AHK: (laag, hoog) per jaar
_AHK_GRENZEN: dict[int, tuple[float, float]] = {
    2022: (20658.0, 69398.0),
    2023: (22660.0, 73031.0),
    2024: (24812.0, 75518.0),
    2025: (24812.0, 76817.0),
}

# Arbeidskorting afbouw: (max_bereikt_bij, afbouw_einde) per jaar
_AK_AFBOUW: dict[int, tuple[float, float]] = {
    2022: (36587.0, 102110.0),
    2023: (37691.0, 115295.0),
    2024: (39958.0, 124935.0),
    2025: (43071.0, 124935.0),
}


def _bereken_algemene_heffingskorting(jaarloon: float, ib: dict, jaar: int) -> float:
    """Algemene heffingskorting: lineaire afbouw tussen laag en hoog grens."""
    max_ahk = float(ib["max_algemene_heffingskorting"])
    g_laag, g_hoog = _AHK_GRENZEN.get(jaar, (24812.0, float(ib["schijf_1_grens"])))

    if jaarloon <= g_laag:
        return max_ahk
    if jaarloon >= g_hoog:
        return 0.0
    afbouw_pct = max_ahk / (g_hoog - g_laag)
    return max(0.0, max_ahk - (jaarloon - g_laag) * afbouw_pct)


def _bereken_arbeidskorting(arbeidsinkomen: float, ib: dict, jaar: int) -> float:
    """Arbeidskorting: lineaire opbouw tot max, daarna lineaire afbouw.

    Vereenvoudigd model: opbouw 0 → max tot afbouw_start, dan afbouw tot 0.
    """
    max_ak = float(ib["max_arbeidskorting"])
    afbouw_start, afbouw_einde = _AK_AFBOUW.get(jaar, (43071.0, 124935.0))

    if arbeidsinkomen <= afbouw_start:
        # Lineaire opbouw van 0 naar max_ak
        return min(max_ak, (arbeidsinkomen / afbouw_start) * max_ak)
    if arbeidsinkomen <= afbouw_einde:
        afbouw_pct = max_ak / (afbouw_einde - afbouw_start)
        return max(0.0, max_ak - (arbeidsinkomen - afbouw_start) * afbouw_pct)
    return 0.0


# ---------------------------------------------------------------------------
# Loonheffing (withholding tax)
# ---------------------------------------------------------------------------

def _bereken_loonheffing_jaar(jaarloon: float, params: dict, jaar: int) -> float:
    """Jaarlijkse loonheffing na aftrek heffingskortingen."""
    ib = params["IB"]
    grens = float(ib["schijf_1_grens"])
    t1 = float(ib["tarief_schijf_1"])
    t2 = float(ib["tarief_schijf_2"])

    if jaarloon <= grens:
        belasting = jaarloon * t1
    else:
        belasting = grens * t1 + (jaarloon - grens) * t2

    ahk = _bereken_algemene_heffingskorting(jaarloon, ib, jaar)
    ak = _bereken_arbeidskorting(jaarloon, ib, jaar)
    return max(0.0, belasting - ahk - ak)


# ---------------------------------------------------------------------------
# Constanten
# ---------------------------------------------------------------------------

_WERKDAGEN_PER_MAAND = 260.0 / 12.0   # ≈ 21.67
_WEKEN_PER_MAAND = 52.0 / 12.0        # ≈ 4.33

# WW-premie 2025 (awf laag/hoog) en WIA gemiddeld
_WW_VAST = 0.0274
_WW_FLEX = 0.0774
_WIA_PCT = 0.0086


# ---------------------------------------------------------------------------
# Hoofdfunctie
# ---------------------------------------------------------------------------

def genereer_loonstrook(werknemer: Werknemer, periode: str, jaar: int = 2025) -> Loonstrook:
    """Genereer een maandloonstrook met alle NL inhoudingen.

    Berekeningen:
    - Maandbruto = jaarsalaris / 12
    - Vakantiegeld = maandbruto * 0.08 (gereserveerd, uitbetaling juni)
    - Reiskosten = reisafstand_km * 2 * werkdagen_per_maand * 0.23 (belastingvrij)
    - Thuiswerk = thuiswerk_dagen_pw * 4.33 weken * 2.40 per dag (belastingvrij)
    - Loonheffing: berekend op jaarinkomen → maand (schijven + heffingskortingen)
    - ZVW werkgeversbijdrage: 5.57% over jaarinkomen, max €75.864
    - Pensioen werknemer: maandbruto * pensioen_pct (inhoud)
    - Pensioen werkgever: gelijk aan werknemersbijdrage
    - WW/WIA: 2.74% (vast) of 7.74% (flex) + 0.86% WIA over maandbruto
    """
    params = _load_params(jaar)
    lh_params = params.get("LH", {})
    zvw_params = params.get("ZVW", {})
    thuiswerk_params = params.get("Thuiswerk", {})

    # --- Bruto salaris ---
    maandbruto = werknemer.jaarsalaris / 12.0

    # --- Vakantiegeld (8% opbouw, uitbetaling in juni) ---
    vakantiegeld_maand = maandbruto * 0.08

    # --- Reiskosten (belastingvrij tot wettelijk maximum) ---
    km_vrij = float(lh_params.get("reiskostenvergoeding_per_km", 0.23))
    reiskosten = werknemer.reisafstand_km * 2.0 * _WERKDAGEN_PER_MAAND * km_vrij

    # --- Thuiswerkvergoeding (belastingvrij via WKR) ---
    tw_dag = float(thuiswerk_params.get("vergoeding_per_dag", 2.40))
    thuiswerk = werknemer.thuiswerk_dagen_pw * _WEKEN_PER_MAAND * tw_dag

    # --- Loonheffing ---
    # Fiscaal jaarinkomen = jaarsalaris (reiskosten/thuiswerk zijn vrij;
    # vakantiegeld wordt apart afgerekend bij uitbetaling in juni)
    fiscaal_jaarloon = werknemer.jaarsalaris
    loonheffing_jaar = _bereken_loonheffing_jaar(fiscaal_jaarloon, params, jaar)
    maand_loonheffing = loonheffing_jaar / 12.0

    # --- Pensioen werknemer (inhoud op netto) ---
    pensioen_wn = maandbruto * werknemer.pensioen_pct

    # --- Pensioen werkgever (zelfde percentage, werkgeverskosten) ---
    pensioen_wg = maandbruto * werknemer.pensioen_pct

    # --- ZVW werkgeversbijdrage ---
    zvw_pct = float(zvw_params.get("bijdrage_pct", 0.0557))
    zvw_max = float(zvw_params.get("max_bijdragegrondslag", 75864))
    zvw_grondslag = min(werknemer.jaarsalaris, zvw_max)
    zvw_maand = (zvw_grondslag * zvw_pct) / 12.0

    # --- WW + WIA werkgeverslast ---
    ww_pct = _WW_VAST if werknemer.vast_contract else _WW_FLEX
    werkgeverslasten_maand = maandbruto * (ww_pct + _WIA_PCT)

    # --- WKR eindheffing (0 tenzij vrije ruimte overschreden) ---
    wkr_eindheffing = 0.0

    # --- Bouw regels op ---
    regels: list[LoonstrookRegel] = []

    bruto_label = "Bruto maandsalaris DGA" if werknemer.is_dga else "Bruto maandsalaris"
    regels.append(LoonstrookRegel(
        RegelSoort.BRUTO_SALARIS,
        bruto_label,
        maandbruto,
    ))
    regels.append(LoonstrookRegel(
        RegelSoort.VAKANTIEGELD,
        "Vakantiegeld opbouw (8%)",
        vakantiegeld_maand,
    ))

    if reiskosten > 0.0:
        regels.append(LoonstrookRegel(
            RegelSoort.REISKOSTENVERGOEDING,
            f"Reiskosten {werknemer.reisafstand_km:.0f} km (enkele reis, belastingvrij)",
            reiskosten,
        ))

    if thuiswerk > 0.0:
        regels.append(LoonstrookRegel(
            RegelSoort.THUISWERK_VERGOEDING,
            f"Thuiswerkvergoeding {werknemer.thuiswerk_dagen_pw:.1f} dag/wk",
            thuiswerk,
        ))

    # Inhoudingen (negatief)
    regels.append(LoonstrookRegel(
        RegelSoort.LOONHEFFING,
        "Loonheffing (witte tabel)",
        -maand_loonheffing,
    ))
    regels.append(LoonstrookRegel(
        RegelSoort.PENSIOEN_WERKNEMER,
        f"Pensioeninhoud werknemer ({werknemer.pensioen_pct * 100:.1f}%)",
        -pensioen_wn,
    ))

    # Werkgeverslasten (positief — werkgever betaalt deze bovenop netto)
    regels.append(LoonstrookRegel(
        RegelSoort.ZVW_BIJDRAGE,
        f"ZVW werkgeversbijdrage ({zvw_pct * 100:.2f}%)",
        zvw_maand,
    ))
    regels.append(LoonstrookRegel(
        RegelSoort.PENSIOEN_WERKGEVER,
        f"Pensioen werkgever ({werknemer.pensioen_pct * 100:.1f}%)",
        pensioen_wg,
    ))
    regels.append(LoonstrookRegel(
        RegelSoort.WERKGEVERSLASTEN,
        f"WW/WIA werkgeverslast ({'vast' if werknemer.vast_contract else 'flex'})",
        werkgeverslasten_maand,
    ))

    if wkr_eindheffing > 0.0:
        regels.append(LoonstrookRegel(
            RegelSoort.WKR_EINDHEFFING,
            "WKR eindheffing (80% over overschrijding)",
            wkr_eindheffing,
        ))

    return Loonstrook(
        werknemer_id=werknemer.id,
        periode=periode,
        jaar=jaar,
        regels=regels,
    )


# ---------------------------------------------------------------------------
# DGA: Gebruikelijk loon check (art. 12a Wet LB 1964)
# ---------------------------------------------------------------------------

@dataclass
class GebruikelijkLoonCheck:
    """Resultaat van de gebruikelijk-loon toets voor een DGA."""
    jaar: int
    jaarsalaris: float
    norm: float                  # wettelijk minimum gebruikelijk loon
    voldoet: bool
    tekort: float                # 0 indien voldoet, anders (norm - jaarsalaris)
    waarschuwing: str

    def to_dict(self) -> dict:
        return {
            "jaar": self.jaar,
            "jaarsalaris": self.jaarsalaris,
            "norm": self.norm,
            "voldoet": self.voldoet,
            "tekort": self.tekort,
            "waarschuwing": self.waarschuwing,
        }


def controleer_gebruikelijk_loon(
    werknemer: Werknemer,
    jaar: int = 2025,
) -> GebruikelijkLoonCheck:
    """Toets DGA-salaris aan de gebruikelijk-loon norm (art. 12a Wet LB 1964).

    De Belastingdienst hanteert als minimum het hoogste van:
    - Het wettelijk vastgestelde normbedrag (€56.000 in 2024/2025)
    - 75% van het loon uit de meest vergelijkbare dienstbetrekking
    - Het loon van de meestverdienende werknemer in de BV

    Hier wordt alleen het wettelijke normbedrag gecontroleerd.
    """
    params = _load_params(jaar)
    norm = float(params.get("LH", {}).get("dga_min_salaris", 56000))

    voldoet = werknemer.jaarsalaris >= norm
    tekort = max(0.0, norm - werknemer.jaarsalaris)

    if voldoet:
        waarschuwing = ""
    else:
        waarschuwing = (
            f"DGA-salaris €{werknemer.jaarsalaris:,.0f} ligt onder de gebruikelijk-loon norm "
            f"€{norm:,.0f} voor {jaar}. Tekort: €{tekort:,.0f}. "
            f"Risico: correctie + heffingsrente Belastingdienst (art. 12a Wet LB 1964)."
        )

    return GebruikelijkLoonCheck(
        jaar=jaar,
        jaarsalaris=werknemer.jaarsalaris,
        norm=norm,
        voldoet=voldoet,
        tekort=tekort,
        waarschuwing=waarschuwing,
    )
