"""Republic of Mozambique corporate income tax calculator.

Mozambique levies **IRPC** (Imposto sobre o Rendimento das Pessoas
Colectivas) at a standard rate of **32%** (Código do IRPC). Agriculture and
aquaculture benefit from a reduced **10%** rate under an extended incentive.

Mining and petroleum operations fall under specific fiscal regimes (production
taxes and dedicated IRPC rules) — out of scope for this SME estimator (see
params.json). Administered by the Autoridade Tributária de Moçambique.
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES_MZ: dict[str, float] = {
    "standard": 0.32,
    "agriculture": 0.10,
}


@dataclass
class CITResultMZ:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_mozambique(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultMZ:
    """Bereken Mozambikaanse vennootschapsbelasting (IRPC).

    Args:
        winst: Belastbare winst in MZN.
        jaar: Belastingjaar (bijv. 2025).
        sector: "standard" (32%) of "agriculture" (10% — landbouw en
            aquacultuur, verlengde stimuleringsregeling).

    Returns:
        CITResultMZ dataclass.

    Raises:
        ValueError: Bij een onbekende sector.
    """
    if sector not in CIT_RATES_MZ:
        raise ValueError(
            f"Unknown sector {sector!r}; expected one of {sorted(CIT_RATES_MZ)}"
        )

    cit_rate = CIT_RATES_MZ[sector]

    if winst <= 0:
        return CITResultMZ(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultMZ(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
