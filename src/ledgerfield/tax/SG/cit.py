"""Singapore Corporate Income Tax calculator."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CITResultSG:
    winst: float
    jaar: int
    chargeable_income: float
    exemption_first: float
    exemption_second: float
    taxable_income: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_singapore(winst: float, jaar: int) -> CITResultSG:
    """Bereken Singapore Corporate Income Tax met partiële vrijstelling.

    Partial exemption scheme (normal companies):
      - First SGD 10,000 of chargeable income: 75% exempt
      - Next SGD 190,000 of chargeable income: 50% exempt
    Flat CIT rate: 17%

    Args:
        winst: Belastbare winst in SGD.
        jaar: Belastingjaar.

    Returns:
        CITResultSG dataclass met uitsplitsing.
    """
    CIT_RATE = 0.17
    FIRST_TRANCHE = 10_000.0
    FIRST_EXEMPT_PCT = 0.75
    SECOND_TRANCHE = 190_000.0
    SECOND_EXEMPT_PCT = 0.50

    if winst <= 0:
        return CITResultSG(
            winst=winst, jaar=jaar, chargeable_income=0.0,
            exemption_first=0.0, exemption_second=0.0,
            taxable_income=0.0, cit_totaal=0.0, effectief_tarief=0.0,
        )

    chargeable_income = winst

    # First tranche: first 10k, 75% exempt
    applicable_first = min(chargeable_income, FIRST_TRANCHE)
    exemption_first = applicable_first * FIRST_EXEMPT_PCT

    # Second tranche: next 190k, 50% exempt
    remaining = chargeable_income - applicable_first
    applicable_second = min(remaining, SECOND_TRANCHE)
    exemption_second = applicable_second * SECOND_EXEMPT_PCT

    total_exemption = exemption_first + exemption_second
    taxable_income = chargeable_income - total_exemption
    cit_totaal = taxable_income * CIT_RATE
    effectief_tarief = cit_totaal / winst if winst else 0.0

    return CITResultSG(
        winst=winst,
        jaar=jaar,
        chargeable_income=chargeable_income,
        exemption_first=exemption_first,
        exemption_second=exemption_second,
        taxable_income=taxable_income,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
