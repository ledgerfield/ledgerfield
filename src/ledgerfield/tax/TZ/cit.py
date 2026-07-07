"""United Republic of Tanzania corporate income tax calculator.

Tanzania levies a standard **30%** corporate income tax (Income Tax Act 2004),
administered by the Tanzania Revenue Authority (TRA). Reduced rates apply to:

- Companies newly listed on the Dar es Salaam Stock Exchange (DSE) with at
  least 30% of shares issued to the public: **25%** for three consecutive
  years from listing.
- New manufacturers of pharmaceuticals or leather products (with a
  performance agreement with the Government): **20%**.
- New assemblers of vehicles, tractors and fishing boats: **10%** for the
  first five years from commencement.

Companies with perpetual unrelieved losses for three consecutive years are
subject to an alternative minimum tax of 0.5% of turnover — out of scope for
this SME estimator (see params.json). VAT is 18% on the mainland (Zanzibar
applies 15%).
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES_TZ: dict[str, float] = {
    "standard": 0.30,
    "newly_listed": 0.25,
    "new_manufacturer": 0.20,
    "assembler": 0.10,
}


@dataclass
class CITResultTZ:
    winst: float
    jaar: int
    regime: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_tanzania(
    winst: float,
    jaar: int,
    regime: str = "standard",
) -> CITResultTZ:
    """Bereken Tanzaniaanse vennootschapsbelasting (Income Tax Act 2004).

    Args:
        winst: Belastbare winst in TZS.
        jaar: Belastingjaar (bijv. 2025).
        regime: Een van "standard" (30%), "newly_listed" (25%, DSE-notering
            met >=30% publiek aandeel, 3 jaar), "new_manufacturer" (20%,
            farmaceutica/leer) of "assembler" (10%, voertuig-/tractor-
            assemblage).

    Returns:
        CITResultTZ dataclass.
    """
    if regime not in CIT_RATES_TZ:
        raise ValueError(
            f"unknown regime {regime!r}; expected one of {sorted(CIT_RATES_TZ)}"
        )

    cit_rate = CIT_RATES_TZ[regime]

    if winst <= 0:
        return CITResultTZ(
            winst=winst, jaar=jaar, regime=regime,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultTZ(
        winst=winst,
        jaar=jaar,
        regime=regime,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
