"""United Arab Emirates Corporate Tax calculator.

Federal Decree-Law No. 47 of 2022 introduced a federal Corporate Tax (CT)
effective for financial years starting on or after 1 June 2023:

    * 0% on taxable income up to AED 375,000 (Small Business threshold).
    * 9% on taxable income above AED 375,000.
    * Qualifying Free Zone Persons pay 0% on *qualifying income* and 9% on
      non-qualifying income (modelled here via ``free_zone_qualifying``).
    * A 15% Domestic Minimum Top-up Tax (DMTT) applies to large multinationals
      (consolidated revenue >= EUR 750M) for periods from 1 January 2025 —
      out of scope for this SME estimator; see params.json metadata.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultAE:
    winst: float
    jaar: int
    free_zone_qualifying: bool
    zero_band_limit: float
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_uae(
    winst: float,
    jaar: int,
    free_zone_qualifying: bool = False,
) -> CITResultAE:
    """Bereken Emiraatse vennootschapsbelasting (UAE Corporate Tax).

    Args:
        winst: Belastbare winst in AED.
        jaar: Belastingjaar (bijv. 2025).
        free_zone_qualifying: True voor een Qualifying Free Zone Person waarvan
            de winst kwalificerend inkomen is (0% tarief).

    Returns:
        CITResultAE dataclass. Het 0%-tarief geldt tot AED 375.000; daarboven 9%.
    """
    ZERO_BAND_LIMIT = 375_000.0
    STANDARD_RATE = 0.09

    if winst <= 0 or free_zone_qualifying:
        return CITResultAE(
            winst=winst, jaar=jaar, free_zone_qualifying=free_zone_qualifying,
            zero_band_limit=ZERO_BAND_LIMIT, cit_rate=0.0,
            cit_totaal=0.0, effectief_tarief=0.0,
        )

    taxable_above_band = max(0.0, winst - ZERO_BAND_LIMIT)
    cit_totaal = taxable_above_band * STANDARD_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultAE(
        winst=winst,
        jaar=jaar,
        free_zone_qualifying=free_zone_qualifying,
        zero_band_limit=ZERO_BAND_LIMIT,
        cit_rate=STANDARD_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
