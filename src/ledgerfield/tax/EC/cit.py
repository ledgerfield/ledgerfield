"""Ecuador corporate income tax (Impuesto a la Renta de Sociedades) calculator.

Ecuador levies a standard **25%** corporate income tax on companies under the
Ley de Régimen Tributario Interno (LRTI), administered by the SRI (Servicio
de Rentas Internas).

The rate rises by **3 percentage points to 28%** when shareholders resident
in tax havens or low-tax jurisdictions hold (or the entity fails to disclose)
50% or more of the ownership chain. When the tax-haven/undisclosed share is
below 50%, the surcharge applies proportionally — this simplified estimator
models the all-or-nothing ≥50% case via a boolean flag.

VAT (IVA) is 15% since April 2024 (raised from 12% by the Ley Orgánica para
Enfrentar el Conflicto Armado Interno — "Ley de Solidaridad"). The ISD
currency-exit tax (5%) and SME/microenterprise regimes are documented in
params.json.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultEC:
    winst: float
    jaar: int
    tax_haven_shareholders: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


# 2025 rates (LRTI): standard 25%, +3pp when tax-haven/undisclosed
# shareholders reach the 50% threshold.
CIT_RATE_STANDARD = 0.25
CIT_RATE_TAX_HAVEN = 0.28


def bereken_cit_ecuador(
    winst: float,
    jaar: int,
    tax_haven_shareholders: bool = False,
) -> CITResultEC:
    """Bereken Ecuadoraanse vennootschapsbelasting (Impuesto a la Renta).

    Args:
        winst: Belastbare winst in USD.
        jaar: Belastingjaar (bijv. 2025).
        tax_haven_shareholders: True wanneer aandeelhouders in belasting-
            paradijzen (of niet-gerapporteerde aandeelhouders) ≥50% van de
            eigendomsketen vormen — tarief stijgt dan met 3pp naar 28%.
            False (default): standaardtarief 25%.

    Returns:
        CITResultEC dataclass.
    """
    cit_rate = CIT_RATE_TAX_HAVEN if tax_haven_shareholders else CIT_RATE_STANDARD

    if winst <= 0:
        return CITResultEC(
            winst=winst, jaar=jaar, tax_haven_shareholders=tax_haven_shareholders,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultEC(
        winst=winst,
        jaar=jaar,
        tax_haven_shareholders=tax_haven_shareholders,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
