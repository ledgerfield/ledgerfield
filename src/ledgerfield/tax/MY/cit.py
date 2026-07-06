"""Malaysia corporate income tax calculator.

Malaysia levies corporate income tax under the Income Tax Act 1967,
administered by the Inland Revenue Board of Malaysia (Lembaga Hasil Dalam
Negeri, LHDN). The standard rate is a flat **24%**.

Resident SMEs/MSMEs (paid-up capital <= RM2.5 million, gross income
<= RM50 million, not part of a large group) enjoy a tiered preferential
regime: the first RM150,000 of chargeable income at **15%**, the band
RM150,001–RM600,000 at **17%**, and the excess above RM600,000 at **24%**.

Malaysia has no VAT/GST (GST was repealed in 2018); instead it applies the
two-tier Sales and Service Tax (SST) — see params.json.
"""
from __future__ import annotations

from dataclasses import dataclass

# SME/MSME bracket structure (Income Tax Act 1967, YA 2025).
SME_BRACKET_1_LIMIT = 150_000.0   # first RM150,000
SME_BRACKET_1_RATE = 0.15
SME_BRACKET_2_LIMIT = 600_000.0   # RM150,001 – RM600,000
SME_BRACKET_2_RATE = 0.17
STANDARD_RATE = 0.24              # flat rate / SME excess above RM600,000


@dataclass
class CITResultMY:
    winst: float
    jaar: int
    sme: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_maleisie(
    winst: float,
    jaar: int,
    sme: bool = False,
) -> CITResultMY:
    """Bereken Maleisische vennootschapsbelasting (Income Tax Act 1967).

    Args:
        winst: Belastbare winst (chargeable income) in MYR (RM).
        jaar: Belastingjaar / year of assessment (bijv. 2025).
        sme: True voor het SME/MSME-regime (resident, gestort kapitaal
            <= RM2,5 mln, bruto-inkomen <= RM50 mln, geen deel van een grote
            groep): eerste RM150.000 tegen 15%, RM150.001–600.000 tegen 17%,
            daarboven 24%. False geeft het vlakke 24%-tarief.

    Returns:
        CITResultMY dataclass.
    """
    if winst <= 0:
        return CITResultMY(
            winst=winst, jaar=jaar, sme=sme,
            cit_rate=STANDARD_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    if sme:
        bracket_1 = min(winst, SME_BRACKET_1_LIMIT) * SME_BRACKET_1_RATE
        bracket_2 = (
            max(0.0, min(winst, SME_BRACKET_2_LIMIT) - SME_BRACKET_1_LIMIT)
            * SME_BRACKET_2_RATE
        )
        bracket_3 = max(0.0, winst - SME_BRACKET_2_LIMIT) * STANDARD_RATE
        cit_totaal = bracket_1 + bracket_2 + bracket_3
    else:
        cit_totaal = winst * STANDARD_RATE

    effectief_tarief = cit_totaal / winst

    return CITResultMY(
        winst=winst,
        jaar=jaar,
        sme=sme,
        cit_rate=STANDARD_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
