"""Romania corporate income tax calculator.

Romania levies a flat **16%** corporate income tax ("impozit pe profit",
Fiscal Code — Law 227/2015), administered by ANAF (Agentia Nationala de
Administrare Fiscala).

Special regimes documented in params.json but out of scope for this
profit-based estimator:

* Micro-enterprise regime: 1% (or 3%) of *turnover* for companies with
  revenue up to EUR 250,000 (2025 threshold; drops to EUR 100,000 in 2026).
  Different tax base (turnover, not profit) → not computed here.
* Minimum turnover tax (IMCA): 1% of turnover for large companies with
  turnover above EUR 50 million.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultRO:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_roemenie(winst: float, jaar: int) -> CITResultRO:
    """Bereken Roemeense vennootschapsbelasting (16% flat, Wet 227/2015).

    Args:
        winst: Belastbare winst in RON.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultRO dataclass.

    Note:
        Het micro-ondernemingsregime (1%/3% van de *omzet* tot EUR 250.000)
        en de minimum-omzetbelasting IMCA (1% bij omzet > EUR 50 mln) hebben
        een andere grondslag (omzet i.p.v. winst) en vallen buiten deze
        winst-gebaseerde estimator; zie params.json.
    """
    CIT_RATE = 0.16

    if winst <= 0:
        return CITResultRO(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultRO(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
