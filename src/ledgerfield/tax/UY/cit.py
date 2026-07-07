"""Oriental Republic of Uruguay corporate income tax calculator.

Uruguay levies a flat **25%** corporate income tax — the IRAE (Impuesto a las
Rentas de las Actividades Económicas), Título 4 — administered by the DGI
(Dirección General Impositiva).

Free-trade-zone (zona franca) companies and qualifying software/IT services
enjoy broad IRAE exemptions; agricultural producers may opt for the IMEBA
(Impuesto a la Enajenación de Bienes Agropecuarios) turnover tax instead of
IRAE — out of scope for this SME estimator (see params.json).

VAT (IVA) is 22% standard with a 10% reduced (mínimo) rate. A 1.5% net-wealth
tax (Impuesto al Patrimonio, IP) applies to corporate net worth.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultUY:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_uruguay(winst: float, jaar: int) -> CITResultUY:
    """Bereken Uruguayaanse vennootschapsbelasting (IRAE, 25% flat).

    Uruguay heft een vlak IRAE-tarief van 25% (Título 4). Zona-franca- en
    kwalificerende softwarebedrijven kunnen vrijgesteld zijn; agrarische
    producenten kunnen kiezen voor IMEBA — beide buiten scope.

    Args:
        winst: Belastbare winst in UYU.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultUY dataclass.
    """
    CIT_RATE = 0.25

    if winst <= 0:
        return CITResultUY(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultUY(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
