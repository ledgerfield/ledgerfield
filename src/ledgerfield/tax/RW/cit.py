"""Republic of Rwanda corporate income tax calculator.

Rwanda levies a flat **28%** corporate income tax, reduced from 30% by the
2023 Income Tax Law (Law No 027/2022), administered by the Rwanda Revenue
Authority (RRA). The government's Medium-Term Revenue Strategy roadmap
foresees a further reduction to **26%**.

Small businesses can opt for flat-rate / lump-sum regimes below the
real-regime turnover thresholds, and newly listed companies enjoy reduced
25% / 20% rates depending on the share of equity floated — both are noted in
params.json but out of scope for this SME estimator. VAT is 18%.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultRW:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_rwanda(
    winst: float,
    jaar: int,
) -> CITResultRW:
    """Bereken Rwandese vennootschapsbelasting (28% flat).

    Args:
        winst: Belastbare winst in RWF.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultRW dataclass.
    """
    CIT_RATE = 0.28

    if winst <= 0:
        return CITResultRW(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultRW(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
