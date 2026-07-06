"""Republic of Slovenia corporate income tax calculator.

Slovenia levies corporate income tax (davek od dohodkov pravnih oseb, DDPO)
under the ZDDPO-2 Act. The rate is **22%** for the years **2024–2028**: the
standard 19% rate was temporarily raised by 3 percentage points as a
post-flood reconstruction levy (Act on Reconstruction, Development and
Provision of Financial Resources — ZORZFS). It is scheduled to revert to 19%
from 2029.

Slovenia also applies minimum tax base rules: relief and loss deductions may
not reduce the tax base below **63%** of the pre-relief tax base (a floor not
modelled by this SME estimator — see params.json). Administered by the
Financial Administration of the Republic of Slovenia (FURS,
https://www.fu.gov.si/). Slovenia applies the EU Pillar Two minimum tax rules.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultSI:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_slovenie(winst: float, jaar: int) -> CITResultSI:
    """Bereken Sloveense vennootschapsbelasting (vlak 22%, 2024-2028).

    Het tarief is voor 2024-2028 tijdelijk verhoogd van 19% naar 22%
    (wederopbouwheffing na de overstromingen van 2023, ZORZFS); vanaf 2029
    is terugkeer naar 19% voorzien.

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultSI dataclass.
    """
    CIT_RATE = 0.22  # 2024-2028 temporary rate (standard 19% + 3pp levy)

    if winst <= 0:
        return CITResultSI(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultSI(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
