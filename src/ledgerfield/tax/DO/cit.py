"""Dominican Republic corporate income tax calculator.

The Dominican Republic levies a flat **27%** Impuesto Sobre la Renta (ISR)
on corporate profits (Código Tributario, Ley 11-92 as amended), administered
by the Dirección General de Impuestos Internos (DGII).

A 1% tax on assets (Impuesto sobre Activos) operates as an alternative
minimum tax: companies pay the higher of 27% ISR on profit or 1% of taxable
assets — the asset-based minimum is out of scope for this SME estimator
(see params.json). VAT (ITBIS) applies at 18% standard / 16% reduced; free
zones (zonas francas) enjoy a 0% CIT regime.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultDO:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_dominicaanse(winst: float, jaar: int) -> CITResultDO:
    """Bereken Dominicaanse vennootschapsbelasting (ISR, 27% flat).

    Args:
        winst: Belastbare winst in DOP.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultDO dataclass.

    Let op: het 1%-activabelasting-alternatief (alternative minimum) en het
    0%-vrijezoneregime worden hier niet doorgerekend (zie params.json).
    """
    CIT_RATE = 0.27

    if winst <= 0:
        return CITResultDO(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultDO(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
