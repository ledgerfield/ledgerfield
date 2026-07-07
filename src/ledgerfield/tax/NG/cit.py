"""Federal Republic of Nigeria corporate income tax calculator.

Nigeria levies Companies Income Tax (CIT) under the Companies Income Tax Act
(CITA), as amended by the Finance Acts. For 2025 the CIT rate depends on
**company size**, which is determined by gross **turnover** (not profit):

* small  — turnover ≤ ₦25 million:            0% CIT
* medium — turnover > ₦25m and ≤ ₦100 million: 20% CIT
* large  — turnover > ₦100 million:            30% CIT

This estimator takes ``company_size`` as a string; classification is
turnover-based and must be asserted by the caller — the ``winst`` (profit)
argument is *not* used to classify size.

In addition, medium and large companies pay **Tertiary Education Tax (TET)**
at 3% of assessable profit (Tertiary Education Trust Fund Act, as amended by
the Finance Act 2021 raising the rate from 2% to 2.5% and the Finance Act
2023 to 3%). Small companies are exempt from TET. The TET amount is exposed
as ``tet_bedrag`` and included in ``totaal_bedrag``.

VAT is 7.5% (Finance Act 2019, effective February 2020).

2025 Tax Reform Acts note: the Nigeria Tax Act 2025 (signed June 2025,
consolidating CITA and related acts) takes effect in 2026 — it raises the
small-company turnover threshold to ₦100 million and replaces TET with a 4%
Development Levy. Note only; this module models the 2025 ruleset.

Administered by the Federal Inland Revenue Service (FIRS),
https://www.firs.gov.ng/ (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES: dict[str, float] = {
    "small": 0.0,
    "medium": 0.20,
    "large": 0.30,
}

TET_RATE = 0.03


@dataclass
class CITResultNG:
    winst: float
    jaar: int
    company_size: str
    cit_rate: float
    cit_bedrag: float
    tet_rate: float
    tet_bedrag: float
    totaal_bedrag: float
    effectief_tarief: float


def bereken_cit_nigeria(
    winst: float,
    jaar: int,
    company_size: str = "large",
) -> CITResultNG:
    """Bereken Nigeriaanse vennootschapsbelasting (CIT + Tertiary Education Tax).

    Args:
        winst: Belastbare (assessable) winst in NGN.
        jaar: Belastingjaar (bijv. 2025).
        company_size: "small" (omzet ≤ ₦25m, 0%), "medium" (₦25m–₦100m, 20%)
            of "large" (> ₦100m, 30%). De classificatie is gebaseerd op
            OMZET (turnover), niet op winst — de aanroeper is verantwoordelijk
            voor de juiste classificatie.

    Returns:
        CITResultNG dataclass. ``tet_bedrag`` is 3% van de assessable winst
        voor medium/large (0 voor small) en is opgenomen in ``totaal_bedrag``.
        ``effectief_tarief`` is berekend over ``totaal_bedrag``.
    """
    if company_size not in CIT_RATES:
        raise ValueError(
            f"company_size must be one of {sorted(CIT_RATES)}, got {company_size!r}"
        )

    cit_rate = CIT_RATES[company_size]
    tet_rate = TET_RATE if company_size in ("medium", "large") else 0.0

    if winst <= 0:
        return CITResultNG(
            winst=winst, jaar=jaar, company_size=company_size,
            cit_rate=cit_rate, cit_bedrag=0.0,
            tet_rate=tet_rate, tet_bedrag=0.0,
            totaal_bedrag=0.0, effectief_tarief=0.0,
        )

    cit_bedrag = winst * cit_rate
    tet_bedrag = winst * tet_rate
    totaal_bedrag = cit_bedrag + tet_bedrag
    effectief_tarief = totaal_bedrag / winst

    return CITResultNG(
        winst=winst,
        jaar=jaar,
        company_size=company_size,
        cit_rate=cit_rate,
        cit_bedrag=cit_bedrag,
        tet_rate=tet_rate,
        tet_bedrag=tet_bedrag,
        totaal_bedrag=totaal_bedrag,
        effectief_tarief=effectief_tarief,
    )
