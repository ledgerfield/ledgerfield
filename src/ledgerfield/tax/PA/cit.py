"""Panama corporate income tax calculator.

Panama levies a **25%** corporate income tax (Impuesto sobre la Renta,
Código Fiscal), administered by the Dirección General de Ingresos (DGI) of
the Ministerio de Economía y Finanzas.

CAIR (Cálculo Alterno del Impuesto sobre la Renta): companies with taxable
gross income above **USD 1,500,000** pay the *greater* of

    25% of net taxable income   vs.   4.67% of gross taxable income
    (4.67% = 25% applied to a deemed 18.67% presumptive net-income base)

Panama applies a **territorial** system (only Panama-source income is taxed)
and operates free zones (e.g. Zona Libre de Colón) with special regimes.
VAT (ITBMS) is 7%. See params.json for the documented 2025 values.
"""
from __future__ import annotations

from dataclasses import dataclass

# Standard CIT rate (Código Fiscal, art. 699).
CIT_RATE = 0.25

# CAIR alternative-minimum rate on gross taxable income.
CAIR_RATE = 0.0467

# CAIR applies only above this gross taxable income threshold (USD/PAB).
CAIR_BRUTO_GRENS = 1_500_000.0


@dataclass
class CITResultPA:
    winst: float
    jaar: int
    bruto_inkomen: float | None
    cit_rate: float
    cair_toegepast: bool
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_panama(
    winst: float,
    jaar: int,
    bruto_inkomen: float | None = None,
) -> CITResultPA:
    """Bereken Panamese vennootschapsbelasting (25% flat, met CAIR-minimum).

    Args:
        winst: Belastbare nettowinst in USD/PAB.
        jaar: Belastingjaar (bijv. 2025).
        bruto_inkomen: Belastbaar bruto-inkomen in USD/PAB. Indien opgegeven
            en boven USD 1.500.000, geldt het CAIR-alternatief:
            max(25% van netto, 4,67% van bruto).

    Returns:
        CITResultPA dataclass (met cair_toegepast-vlag).
    """
    if winst <= 0:
        return CITResultPA(
            winst=winst, jaar=jaar, bruto_inkomen=bruto_inkomen,
            cit_rate=CIT_RATE, cair_toegepast=False,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    regulier = winst * CIT_RATE
    cair_toegepast = False
    cit_totaal = regulier

    if bruto_inkomen is not None and bruto_inkomen > CAIR_BRUTO_GRENS:
        cair = bruto_inkomen * CAIR_RATE
        if cair > regulier:
            cit_totaal = cair
            cair_toegepast = True

    effectief_tarief = cit_totaal / winst

    return CITResultPA(
        winst=winst,
        jaar=jaar,
        bruto_inkomen=bruto_inkomen,
        cit_rate=CIT_RATE,
        cair_toegepast=cair_toegepast,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
