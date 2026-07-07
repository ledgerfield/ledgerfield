"""Independent State of Papua New Guinea corporate income tax calculator.

Papua New Guinea levies corporate income tax administered by the Internal
Revenue Commission (IRC). For the 2025 target period the headline rates are:

* **30%** — resident companies.
* **48%** — non-resident companies.

Mining and petroleum operations are subject to specific resource-sector regimes
(different rates, additional profits tax, and levies) that are out of scope for
this simplified CIT estimator (see params.json). A Goods and Services Tax (GST)
of **10%** applies to most goods and services.

NOTE: Rates are AI-estimated and require verification against official IRC
guidance before any filing or production use.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultPG:
    winst: float
    jaar: int
    non_resident: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_png(
    winst: float,
    jaar: int,
    non_resident: bool = False,
) -> CITResultPG:
    """Bereken Papoea-Nieuw-Guinese vennootschapsbelasting.

    Args:
        winst: Belastbare winst in PGK.
        jaar: Belastingjaar (bijv. 2025).
        non_resident: True voor niet-ingezeten vennootschappen (48%);
            False voor ingezeten vennootschappen (30%).

    Returns:
        CITResultPG dataclass.
    """
    cit_rate = 0.48 if non_resident else 0.30

    if winst <= 0:
        return CITResultPG(
            winst=winst,
            jaar=jaar,
            non_resident=non_resident,
            cit_rate=cit_rate,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultPG(
        winst=winst,
        jaar=jaar,
        non_resident=non_resident,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
