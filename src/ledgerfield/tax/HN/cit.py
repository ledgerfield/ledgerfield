"""Republic of Honduras corporate income tax calculator.

Honduras levies a **25%** corporate income tax (Impuesto Sobre la Renta,
Ley del ISR) on net taxable income, administered by SAR (Servicio de
Administración de Rentas). On top of the CIT, a **5% solidarity
contribution** (aportación solidaria) applies to the portion of net taxable
income *exceeding HNL 1,000,000*.

An alternative minimum tax of 1.5% on gross income can apply to companies
with gross revenue above HNL 1 billion (out of scope for this SME
estimator — see params.json). Honduras taxes on a territorial basis:
foreign-source income is generally outside the Honduran tax net. Sales tax
(ISV, Impuesto Sobre Ventas) is 15% (18% for alcohol and tobacco).
"""
from __future__ import annotations

import os
from dataclasses import dataclass

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


@dataclass
class CITResultHN:
    winst: float
    jaar: int
    cit_rate: float
    cit_bedrag: float
    solidariteit_rate: float
    solidariteit_bedrag: float
    totaal_bedrag: float
    effectief_tarief: float


def bereken_cit_honduras(
    winst: float,
    jaar: int,
) -> CITResultHN:
    """Bereken Hondurese vennootschapsbelasting (25% ISR + 5% aportación solidaria).

    De aportación solidaria (solidariteitsbijdrage) van 5% wordt geheven over
    het deel van de belastbare nettowinst *boven* HNL 1.000.000; onder die
    drempel is alleen de 25% ISR verschuldigd.

    Args:
        winst: Belastbare nettowinst in HNL.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultHN dataclass met cit_bedrag (25% van winst),
        solidariteit_bedrag (5% van max(0, winst − 1.000.000)) en
        totaal_bedrag.
    """
    CIT_RATE = 0.25
    SOLIDARITEIT_RATE = 0.05
    SOLIDARITEIT_DREMPEL = 1_000_000.0

    if winst <= 0:
        return CITResultHN(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_bedrag=0.0,
            solidariteit_rate=SOLIDARITEIT_RATE, solidariteit_bedrag=0.0,
            totaal_bedrag=0.0, effectief_tarief=0.0,
        )

    cit_bedrag = winst * CIT_RATE
    solidariteit_bedrag = SOLIDARITEIT_RATE * max(0.0, winst - SOLIDARITEIT_DREMPEL)
    totaal_bedrag = cit_bedrag + solidariteit_bedrag
    effectief_tarief = totaal_bedrag / winst

    return CITResultHN(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_bedrag=cit_bedrag,
        solidariteit_rate=SOLIDARITEIT_RATE,
        solidariteit_bedrag=solidariteit_bedrag,
        totaal_bedrag=totaal_bedrag,
        effectief_tarief=effectief_tarief,
    )
