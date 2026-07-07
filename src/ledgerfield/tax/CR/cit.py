"""Costa Rica corporate income tax calculator.

Costa Rica levies a standard **30%** corporate income tax (Impuesto sobre las
Utilidades, Ley 7092 del Impuesto sobre la Renta), administered by the
Ministerio de Hacienda / Dirección General de Tributación.

SME regime (2025): companies whose *gross income* does not exceed
CRC 122,145,000 are taxed progressively on slices of **net** income:

    first CRC 5,761,000            →  5%
    CRC 5,761,000 – 8,643,000      → 10%
    CRC 8,643,000 – 11,524,000     → 15%
    above CRC 11,524,000           → 20%

Costa Rica applies a **territorial** system: only Costa Rican-source income
is taxed. VAT (IVA) is 13%. See params.json for the documented 2025 values.
"""
from __future__ import annotations

from dataclasses import dataclass

# Standard CIT rate (Ley 7092, art. 15).
CIT_RATE = 0.30

# SME regime eligibility: gross income ceiling for 2025 (CRC).
SME_BRUTO_GRENS_2025 = 122_145_000.0

# SME progressive slices on *net* income, 2025 published values (CRC).
# (upper bound of slice, rate); final slice unbounded at 20%.
SME_SCHIJVEN_2025: list[tuple[float, float]] = [
    (5_761_000.0, 0.05),
    (8_643_000.0, 0.10),
    (11_524_000.0, 0.15),
    (float("inf"), 0.20),
]


@dataclass
class CITResultCR:
    winst: float
    jaar: int
    sme: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_costarica(
    winst: float,
    jaar: int,
    sme: bool = False,
) -> CITResultCR:
    """Bereken Costa Ricaanse vennootschapsbelasting (Ley 7092).

    Args:
        winst: Belastbare (netto)winst in CRC.
        jaar: Belastingjaar (bijv. 2025).
        sme: True indien het SME-regime van toepassing is (bruto-inkomen
            ≤ CRC 122.145.000 in 2025) — progressieve schijven 5/10/15/20%
            over de netto-winst; anders vlak 30%.

    Returns:
        CITResultCR dataclass.
    """
    if winst <= 0:
        return CITResultCR(
            winst=winst, jaar=jaar, sme=sme,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    if sme:
        cit_totaal = 0.0
        ondergrens = 0.0
        for bovengrens, tarief in SME_SCHIJVEN_2025:
            if winst <= ondergrens:
                break
            schijf = min(winst, bovengrens) - ondergrens
            cit_totaal += schijf * tarief
            ondergrens = bovengrens
    else:
        cit_totaal = winst * CIT_RATE

    effectief_tarief = cit_totaal / winst

    return CITResultCR(
        winst=winst,
        jaar=jaar,
        sme=sme,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
