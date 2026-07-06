"""Republic of the Philippines corporate income tax calculator.

The Philippines levies a **25%** standard corporate income tax under the
CREATE Act (Republic Act No. 11534), administered by the Bureau of Internal
Revenue (BIR). Qualifying SMEs pay a reduced **20%** rate.

The CREATE MORE Act (Republic Act No. 12066) kept the 25%/20% rates and
introduced a 20% RCIT for registered business enterprises under the enhanced
deductions regime — out of scope for this SME estimator (see params.json).

A minimum corporate income tax (MCIT) of 2% of gross income applies from the
fourth taxable year of operations — noted in params.json, not modelled here.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultPH:
    winst: float
    jaar: int
    sme: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_filipijnen(
    winst: float,
    jaar: int,
    sme: bool = False,
) -> CITResultPH:
    """Bereken Filipijnse vennootschapsbelasting (CREATE Act, RA 11534).

    Args:
        winst: Belastbare winst (net taxable income) in PHP.
        jaar: Belastingjaar (bijv. 2025).
        sme: True als de vennootschap kwalificeert voor het 20% SME-tarief.
            De twee cumulatieve voorwaarden (CREATE Act, RA 11534) zijn:
            (1) net taxable income ≤ PHP 5,000,000, EN
            (2) total assets ≤ PHP 100,000,000 (exclusief de grond waarop het
            bedrijfspand/de business site staat).
            De vlag bevestigt dat de aanroeper beide voorwaarden heeft
            gecontroleerd; anders geldt het standaardtarief van 25%.

    Returns:
        CITResultPH dataclass.
    """
    STANDARD_RATE = 0.25
    SME_RATE = 0.20

    cit_rate = SME_RATE if sme else STANDARD_RATE

    if winst <= 0:
        return CITResultPH(
            winst=winst, jaar=jaar, sme=sme,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultPH(
        winst=winst,
        jaar=jaar,
        sme=sme,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
