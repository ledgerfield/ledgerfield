"""Kingdom of Cambodia Tax on Income (ToI) calculator.

Cambodia levies a flat **20%** Tax on Income (ToI) on medium and large
taxpayers under the Law on Taxation (2023), administered by the General
Department of Taxation (GDT). Oil and gas operations and the exploitation of
certain mineral resources are taxed at **30%**.

Insurance companies pay a 5% tax on gross premiums for their insurance
activities (out of scope for this SME estimator — see params.json).
Qualified Investment Projects (QIPs) approved by the CDC enjoy ToI exemption
periods of 3 to 9 years — modelled as a note only.

Small taxpayers are taxed under progressive brackets of 0-20% on annual
profit (KHR-denominated: 0% up to KHR 16M ... 20% above KHR 102M). This SME
estimator keeps a flat-rate model; the brackets are documented in
params.json as a note.

A minimum tax of 1% of annual turnover applies unless the taxpayer maintains
proper accounting records, and a 1% monthly prepayment of ToI on turnover is
creditable against the annual ToI liability — both noted in params.json.
"""
from __future__ import annotations

from dataclasses import dataclass

SECTOR_RATES: dict[str, float] = {
    "standard": 0.20,
    "oil_gas_minerals": 0.30,
}


@dataclass
class CITResultKH:
    winst: float
    jaar: int
    sector: str
    toi_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_toi_cambodja(
    winst: float,
    jaar: int,
    sector: str = "standard",
) -> CITResultKH:
    """Bereken Cambodjaanse Tax on Income (20% standaard / 30% olie-gas-mineralen).

    Args:
        winst: Belastbare winst in KHR (of USD-equivalent voor deze schatter).
        jaar: Belastingjaar (bijv. 2025).
        sector: "standard" (20%) of "oil_gas_minerals" (30%).

    Returns:
        CITResultKH dataclass.

    Raises:
        ValueError: bij een onbekende sector.
    """
    if sector not in SECTOR_RATES:
        raise ValueError(
            f"Unknown sector {sector!r}; expected one of {sorted(SECTOR_RATES)}"
        )

    toi_rate = SECTOR_RATES[sector]

    if winst <= 0:
        return CITResultKH(
            winst=winst, jaar=jaar, sector=sector,
            toi_rate=toi_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * toi_rate
    effectief_tarief = cit_totaal / winst

    return CITResultKH(
        winst=winst,
        jaar=jaar,
        sector=sector,
        toi_rate=toi_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
