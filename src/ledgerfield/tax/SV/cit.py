"""Republic of El Salvador corporate income tax calculator.

El Salvador levies income tax (ISR — Impuesto sobre la Renta) under the Ley de
Impuesto sobre la Renta (LISR), administered by the Ministerio de Hacienda /
Dirección General de Impuestos Internos (DGII).

The standard corporate rate is **30%**. A reduced **25%** rate applies to
companies whose taxable income does not exceed **USD 150,000**. In Salvadoran
practice this is a whole-base (cliff) rate, not a progressive bracket: once
taxable income exceeds USD 150,000 the full base is taxed at 30%.

A 1% minimum tax on gross income was introduced in 2011/2014 but was declared
**unconstitutional** by the Constitutional Chamber (2015) and is not applied —
kept here only as a historical note. VAT (IVA) is 13%.
"""
from __future__ import annotations

from dataclasses import dataclass

REDUCED_RATE_THRESHOLD = 150_000.0


@dataclass
class CITResultSV:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_elsalvador(
    winst: float,
    jaar: int,
) -> CITResultSV:
    """Bereken Salvadoraanse vennootschapsbelasting (ISR, LISR).

    Tarief over de GEHELE grondslag (Salvadoraanse praktijk, geen schijven):
      * winst <= USD 150.000 → 25% (verlaagd tarief);
      * winst  > USD 150.000 → 30% (standaardtarief).

    Args:
        winst: Belastbare winst in USD (El Salvador is gedollariseerd).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultSV dataclass.
    """
    STANDARD_RATE = 0.30
    REDUCED_RATE = 0.25

    if winst <= 0:
        return CITResultSV(
            winst=winst, jaar=jaar,
            cit_rate=REDUCED_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_rate = REDUCED_RATE if winst <= REDUCED_RATE_THRESHOLD else STANDARD_RATE
    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultSV(
        winst=winst,
        jaar=jaar,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
