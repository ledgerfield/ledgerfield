"""Jamaica corporate income tax calculator.

Jamaica levies corporate income tax under the Income Tax Act, administered
by Tax Administration Jamaica (TAJ):

* **25%** for unregulated companies (the general rate), and
* **33⅓%** for regulated companies (banks, insurers, securities dealers and
  other entities regulated by the Bank of Jamaica / Financial Services
  Commission).

The regulated rate is one third exactly; this module uses Python's ``1 / 3``
(an IEEE-754 double, ~0.3333333333333333) rather than a truncated literal so
the computed tax on e.g. JMD 1,000,000 is 333,333.33… General Consumption
Tax (GCT) applies at 15%; the Minimum Business Tax (MBT) was abolished
(from year of assessment 2019).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultJM:
    winst: float
    jaar: int
    regulated: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_jamaica(
    winst: float,
    jaar: int,
    regulated: bool = False,
) -> CITResultJM:
    """Bereken Jamaicaanse vennootschapsbelasting (25% / 33⅓%).

    Args:
        winst: Belastbare winst in JMD.
        jaar: Belastingjaar (bijv. 2025).
        regulated: True voor gereguleerde ondernemingen (banken,
            verzekeraars, effectenhandelaars) → 33⅓%; anders 25%.

    Returns:
        CITResultJM dataclass.
    """
    # 33⅓% is exactly one third; use 1/3 (IEEE-754 double) — not 0.3333 — so
    # rounding error stays at float precision (~1e-16 relative).
    cit_rate = (1 / 3) if regulated else 0.25

    if winst <= 0:
        return CITResultJM(
            winst=winst, jaar=jaar, regulated=regulated,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultJM(
        winst=winst,
        jaar=jaar,
        regulated=regulated,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
