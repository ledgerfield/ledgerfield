"""Republic of Türkiye corporate income tax calculator.

Türkiye levies a **25%** standard corporate income tax (Corporate Tax Law
No. 5520, as amended). Banks and other financial institutions (financial
leasing, factoring, financing and savings-finance companies, electronic
payment institutions, asset management companies, capital-market
institutions, insurance/reinsurance and pension companies) are taxed at
**30%**. Administered by the Revenue Administration (Gelir İdaresi
Başkanlığı).

High-inflation adjustment (issue #31): under Tax Procedure Law (VUK)
Art. 298 repeating (mükerrer), inflation adjustment of financial statements
is mandatory when cumulative PPI conditions are met; it was re-activated
for FY2024+. This estimator does **not** recompute the restatement — the
``inflation_adjusted`` flag simply records that the supplied ``winst`` is
already an inflation-restated figure, and is surfaced in the result.

A domestic minimum CIT of 10% of adjusted profit before certain exemptions
applies from 2025 (Law No. 7524) — see params.json note; out of scope for
this SME estimator.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultTR:
    winst: float
    jaar: int
    financial_institution: bool
    inflation_adjusted: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_turkije(
    winst: float,
    jaar: int,
    financial_institution: bool = False,
    inflation_adjusted: bool = False,
) -> CITResultTR:
    """Bereken Turkse vennootschapsbelasting (25% standaard; 30% financieel).

    Args:
        winst: Belastbare winst in TRY. Als ``inflation_adjusted`` True is,
            wordt aangenomen dat dit bedrag reeds is herrekend volgens de
            verplichte inflatiecorrectie (VUK Art. 298 mükerrer).
        jaar: Belastingjaar (bijv. 2025).
        financial_institution: True voor banken en financiële instellingen
            (30%-tarief onder Wet nr. 5520 zoals gewijzigd).
        inflation_adjusted: Registreert dat de aangeleverde winst al een
            inflatie-gecorrigeerd (herrekend) bedrag is. Deze vlag rekent
            zelf NIETS om; hij wordt alleen doorgegeven in het resultaat.

    Returns:
        CITResultTR dataclass.
    """
    cit_rate = 0.30 if financial_institution else 0.25

    if winst <= 0:
        return CITResultTR(
            winst=winst,
            jaar=jaar,
            financial_institution=financial_institution,
            inflation_adjusted=inflation_adjusted,
            cit_rate=cit_rate,
            cit_totaal=0.0,
            effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultTR(
        winst=winst,
        jaar=jaar,
        financial_institution=financial_institution,
        inflation_adjusted=inflation_adjusted,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
