"""Plurinational State of Bolivia corporate income tax calculator.

Bolivia levies the **IUE** (Impuesto sobre las Utilidades de las Empresas,
Ley 843) at a flat **25%** on annual net taxable profits, administered by
the Servicio de Impuestos Nacionales (SIN).

Sector surtaxes — out of scope for this SME estimator (see params.json):

* Financial sector: additional AA-IUE of 25% on profits when return on
  equity (ROE) exceeds 6% (banks and insurance excess-profitability surtax).
* Mining: additional IUE surtax of 12.5% (and up to 25% combined additional
  burden under price-linked rules); hydrocarbons carry their own additional
  regime.

VAT (IVA) is 13% charged *inside* the price (tax-inclusive base), an
effective 14.94% on the net price. A 3% transactions tax (IT, Impuesto a
las Transacciones) applies on gross receipts, creditable against IUE paid.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultBO:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_bolivia(
    winst: float,
    jaar: int,
) -> CITResultBO:
    """Bereken Boliviaanse vennootschapsbelasting (IUE, 25% vlak).

    Args:
        winst: Belastbare winst in BOB (bolivianos).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultBO dataclass.

    Note:
        Sectorspecifieke toeslagen (AA-IUE 25% voor de financiele sector bij
        ROE > 6%; mijnbouw/koolwaterstoffen 12,5%-25%) en de 3% IT
        (transactiebelasting, verrekenbaar met betaalde IUE) vallen buiten
        deze schatter.
    """
    IUE_RATE = 0.25

    if winst <= 0:
        return CITResultBO(
            winst=winst, jaar=jaar,
            cit_rate=IUE_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * IUE_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultBO(
        winst=winst,
        jaar=jaar,
        cit_rate=IUE_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
