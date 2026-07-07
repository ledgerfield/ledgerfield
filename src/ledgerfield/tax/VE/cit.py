"""Bolivarian Republic of Venezuela corporate income tax calculator.

Venezuela levies corporate income tax (ISLR, Ley de Impuesto sobre la Renta)
under **Tarifa 2**, a progressive schedule denominated in Tax Units
(Unidades Tributarias, UT):

* 15% on taxable income up to 2,000 UT;
* 22% on the portion between 2,000 and 3,000 UT;
* 34% on the portion above 3,000 UT.

Because the bolívar value of the UT shifts with hyperinflation and is
re-fixed administratively by SENIAT, the UT brackets cover only a trivially
small slice of profit for any real company. This SME estimator therefore
models the **top band** as a flat rate:

* standard companies: 34%;
* banking and insurance: 40% (Tarifa proportional rate);
* hydrocarbons and related activities: 50% (Tarifa 3).

Venezuela also applies a fiscal inflation adjustment (Ajuste por Inflación /
Reajuste Regular por Inflación, API/RPA) revaluing non-monetary assets — out
of scope here (see params.json). VAT (IVA) standard rate is 16%.
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.34,
    "banking_insurance": 0.40,
    "hydrocarbons": 0.50,
}


@dataclass
class CITResultVE:
    winst: float
    jaar: int
    sector: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_venezuela(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultVE:
    """Bereken Venezolaanse vennootschapsbelasting (ISLR, top-band model).

    Args:
        winst: Belastbare winst in VES (bolívares).
        jaar: Belastingjaar (bijv. 2025).
        sector: "standard" (34%), "banking_insurance" (40%) of
            "hydrocarbons" (50%).

    Returns:
        CITResultVE dataclass.

    Raises:
        ValueError: Bij een onbekende sector.

    Note:
        De wettelijke Tarifa 2 is progressief in Tax Units (UT):
        15% tot 2.000 UT, 22% van 2.000–3.000 UT, 34% daarboven. Omdat de
        UT-waarde door hyperinflatie verschuift, modelleert deze schatter
        de topschijf als vlak tarief.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    cit_rate = SECTOR_RATES[sector]

    if winst <= 0:
        return CITResultVE(
            winst=winst, jaar=jaar, sector=sector,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultVE(
        winst=winst,
        jaar=jaar,
        sector=sector,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
