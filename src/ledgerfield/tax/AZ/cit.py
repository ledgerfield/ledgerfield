"""Republic of Azerbaijan corporate profit tax calculator.

Azerbaijan levies a flat **20%** corporate profit tax (Tax Code of the Republic
of Azerbaijan), administered by the State Tax Service under the Ministry of
Economy. The standard rate applies to the taxable profit of resident legal
entities and to the Azerbaijan-sourced profit of permanent establishments.

Value added tax (VAT) is charged at **18%**. Small businesses below the VAT
registration threshold may instead opt into a simplified turnover-based regime
(a percentage of gross receipts in lieu of profit tax and VAT) — out of scope
for this SME profit-tax estimator (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultAZ:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_azerbeidzjan(winst: float, jaar: int) -> CITResultAZ:
    """Bereken Azerbeidzjaanse vennootschapsbelasting (vlak 20%).

    Args:
        winst: Belastbare winst in AZN.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultAZ dataclass. Niet-positieve winst levert 0 belasting op.
    """
    CIT_RATE = 0.20

    if winst <= 0:
        return CITResultAZ(
            winst=winst,
            jaar=jaar,
            cit_rate=CIT_RATE,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultAZ(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
