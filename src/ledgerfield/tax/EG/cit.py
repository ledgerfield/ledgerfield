"""Arab Republic of Egypt corporate income tax calculator.

Egypt levies a standard **22.5%** corporate income tax (Income Tax Law
No. 91 of 2005, as amended), administered by the Egyptian Tax Authority
(ETA). Higher statutory rates apply to specific sectors:

- Oil & gas exploration and production companies: **40.55%**.
- Suez Canal Authority, the Egyptian General Petroleum Corporation (EGPC)
  and the Central Bank of Egypt: **40%**.

A simplified small-enterprise turnover regime exists under Law No. 6 of
2025 (annual turnover up to EGP 20 million: 0.4%–1.5% of turnover) — out
of scope for this profit-based SME estimator (see params.json). Standard
VAT is 14%.
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.225,
    "oil_gas": 0.4055,
    "state_entities": 0.40,
}


@dataclass
class CITResultEG:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_egypte(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultEG:
    """Bereken Egyptische vennootschapsbelasting (22.5% standaard, sectortarieven).

    Args:
        winst: Belastbare winst in EGP.
        jaar: Belastingjaar (bijv. 2025).
        sector: "standard" (22.5%), "oil_gas" (40.55% exploratie/productie)
            of "state_entities" (40% Suez Canal Authority / EGPC / CBE).

    Returns:
        CITResultEG dataclass.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    cit_rate = SECTOR_RATES[sector]

    if winst <= 0:
        return CITResultEG(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultEG(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
