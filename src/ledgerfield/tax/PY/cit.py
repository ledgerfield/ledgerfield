"""Republic of Paraguay corporate income tax calculator.

Paraguay levies a flat **10%** corporate income tax — the IRE (Impuesto a la
Renta Empresarial), Ley 6380/2019 — administered by the DNIT (Dirección
Nacional de Ingresos Tributarios). At 10% flat, Paraguay has the **lowest
corporate income tax rate in South America**.

Dividend distributions are subject to the IDU (Impuesto a los Dividendos y a
las Utilidades): 8% for resident shareholders, 15% for non-residents — out of
scope for this SME estimator (see params.json). Small taxpayers may opt into
the SIMPLE / RESIMPLE simplified regimes instead of the general IRE.

VAT (IVA) is 10% standard with a 5% reduced rate — also the lowest standard
VAT rate in South America.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultPY:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_paraguay(winst: float, jaar: int) -> CITResultPY:
    """Bereken Paraguayaanse vennootschapsbelasting (IRE, 10% flat).

    Paraguay heft een vlak IRE-tarief van 10% (Ley 6380/2019) — het laagste
    vennootschapsbelastingtarief van Zuid-Amerika.

    Args:
        winst: Belastbare winst in PYG.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultPY dataclass.
    """
    CIT_RATE = 0.10

    if winst <= 0:
        return CITResultPY(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultPY(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
