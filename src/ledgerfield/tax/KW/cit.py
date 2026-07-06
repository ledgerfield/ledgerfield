"""State of Kuwait corporate income tax calculator.

Kuwait levies a flat **15%** corporate income tax (Decree No. 3 of 1955 as
amended by Law No. 2 of 2008), administered by the Ministry of Finance. The
tax applies to the profit share attributable to *foreign (non-GCC)* corporate
ownership; wholly Kuwaiti / GCC-owned entities are exempt from CIT.

Listed Kuwaiti companies are instead subject to Zakat (1%) and the National
Labour Support Tax (2.5%) — out of scope for this SME estimator (see
params.json). Kuwait has not implemented VAT as of the target period.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultKW:
    winst: float
    jaar: int
    foreign_ownership_share: float
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_koeweit(
    winst: float,
    jaar: int,
    foreign_ownership_share: float = 1.0,
) -> CITResultKW:
    """Bereken Koeweitse vennootschapsbelasting (15% flat op buitenlands aandeel).

    Args:
        winst: Belastbare winst in KWD.
        jaar: Belastingjaar (bijv. 2025).
        foreign_ownership_share: Aandeel niet-GCC (buitenlandse) eigenaren,
            tussen 0.0 (volledig Koeweits/GCC, vrijgesteld) en 1.0.

    Returns:
        CITResultKW dataclass.
    """
    if not 0.0 <= foreign_ownership_share <= 1.0:
        raise ValueError("foreign_ownership_share must be between 0.0 and 1.0")

    CIT_RATE = 0.15

    if winst <= 0:
        return CITResultKW(
            winst=winst, jaar=jaar, foreign_ownership_share=foreign_ownership_share,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * foreign_ownership_share * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultKW(
        winst=winst,
        jaar=jaar,
        foreign_ownership_share=foreign_ownership_share,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
