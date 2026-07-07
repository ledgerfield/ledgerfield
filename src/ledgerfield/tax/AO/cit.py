"""Republic of Angola corporate income tax calculator.

Angola levies **Imposto Industrial** (Industrial Tax) at a standard rate of
**25%** (Law 26/20 — Industrial Tax Code, as amended). Sector rates:

* banking, insurance and telecommunications — **35%**;
* agriculture, forestry and livestock — **10%**.

Oil and gas operations fall under a separate petroleum income tax regime
(Imposto sobre o Rendimento do Petróleo) — out of scope for this SME
estimator (see params.json). Administered by the Administração Geral
Tributária (AGT).
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES_AO: dict[str, float] = {
    "standard": 0.25,
    "banking_insurance_telecom": 0.35,
    "agriculture": 0.10,
}


@dataclass
class CITResultAO:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_angola(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultAO:
    """Bereken Angolese vennootschapsbelasting (Imposto Industrial).

    Args:
        winst: Belastbare winst in AOA.
        jaar: Belastingjaar (bijv. 2025).
        sector: "standard" (25%), "banking_insurance_telecom" (35%) of
            "agriculture" (10% — landbouw, bosbouw, veeteelt).

    Returns:
        CITResultAO dataclass.

    Raises:
        ValueError: Bij een onbekende sector.
    """
    if sector not in CIT_RATES_AO:
        raise ValueError(
            f"Unknown sector {sector!r}; expected one of {sorted(CIT_RATES_AO)}"
        )

    cit_rate = CIT_RATES_AO[sector]

    if winst <= 0:
        return CITResultAO(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultAO(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
