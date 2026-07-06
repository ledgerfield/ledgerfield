"""Republic of Indonesia corporate income tax (PPh Badan) calculator.

Indonesia levies a standard **22%** corporate income tax (UU HPP —
Law No. 7 of 2021 on Harmonisation of Tax Regulations), administered by the
Direktorat Jenderal Pajak (DJP). Publicly listed companies that meet the
40%-free-float conditions (minimum public ownership, spread over at least
300 parties, each holding <5%, for at least 183 days) qualify for a
3-percentage-point reduction → **19%**.

Out of scope for this SME estimator (see params.json):
- 0.5% FINAL tax on TURNOVER for small businesses with annual gross turnover
  ≤ IDR 4.8bn (PP 55/2022) — a different tax base entirely.
- Art. 31E: 50% rate discount on the first IDR 4.8bn taxable-income slice for
  companies with turnover ≤ IDR 50bn.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultID:
    winst: float
    jaar: int
    public_listed: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_indonesie(
    winst: float,
    jaar: int,
    public_listed: bool = False,
) -> CITResultID:
    """Bereken Indonesische vennootschapsbelasting (PPh Badan, 22% standaard).

    Args:
        winst: Belastbare winst in IDR.
        jaar: Belastingjaar (bijv. 2025).
        public_listed: True als de vennootschap beursgenoteerd is en voldoet
            aan de 40%-free-float-voorwaarden (3 procentpunt korting → 19%).

    Returns:
        CITResultID dataclass.
    """
    STANDARD_RATE = 0.22
    LISTED_REDUCTION = 0.03

    cit_rate = STANDARD_RATE - LISTED_REDUCTION if public_listed else STANDARD_RATE

    if winst <= 0:
        return CITResultID(
            winst=winst, jaar=jaar, public_listed=public_listed,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultID(
        winst=winst,
        jaar=jaar,
        public_listed=public_listed,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
