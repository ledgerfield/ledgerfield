"""Republic of Colombia corporate income tax calculator.

Colombia levies a **35%** corporate income tax (impuesto sobre la renta,
Estatuto Tributario Art. 240), administered by the DIAN (Dirección de
Impuestos y Aduanas Nacionales).

Financial institutions pay a **+5 percentage-point surtax** (sobretasa)
through 2027, for a combined **40%** rate.

Colombia also applies a Pillar-Two-style domestic minimum effective tax
rate (Tasa de Tributación Depurada, TTD) of 15% — note only, not modelled.
VAT (IVA) applies at 19%; municipalities levy the ICA turnover tax.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultCO:
    winst: float
    jaar: int
    financial_institution: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_colombia(
    winst: float,
    jaar: int,
    financial_institution: bool = False,
) -> CITResultCO:
    """Bereken Colombiaanse vennootschapsbelasting (impuesto sobre la renta).

    Args:
        winst: Belastbare winst in COP.
        jaar: Belastingjaar (bijv. 2025).
        financial_institution: True voor financiële instellingen
            (35% + 5pp sobretasa = 40%, geldig t/m 2027); False voor het
            algemene 35%-tarief (Estatuto Tributario Art. 240).

    Returns:
        CITResultCO dataclass.
    """
    cit_rate = 0.40 if financial_institution else 0.35

    if winst <= 0:
        return CITResultCO(
            winst=winst, jaar=jaar, financial_institution=financial_institution,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultCO(
        winst=winst,
        jaar=jaar,
        financial_institution=financial_institution,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
