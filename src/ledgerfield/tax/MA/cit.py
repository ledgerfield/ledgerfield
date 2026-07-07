"""Kingdom of Morocco corporate income tax (Impôt sur les Sociétés, IS) calculator.

Finance Law 2023 launched a **four-year convergence** (2023-2026) of Morocco's
former progressive IS scale towards a two-rate target system, fully effective
from 2026 (2025 is year 3 of the glide path):

* **20%** for companies with net taxable profit **below MAD 100,000,000**;
* **35%** for companies with net taxable profit **of MAD 100,000,000 or more**;
* **40%** for credit institutions and insurance/reinsurance companies.

This SME estimator applies the **2026 target rates** as the simplest defensible
model; the exact 2025 transitional rates differ slightly per bracket (see
params.json). Per Moroccan practice the applicable rate is applied to the
**whole** taxable profit once a threshold is crossed (not marginally per slice).

A minimum contribution (*cotisation minimale*, generally 0.25% of turnover) is
due even in loss years — noted in params.json, out of scope for this estimator.
Administered by the Direction Générale des Impôts (DGI, https://www.tax.gov.ma/).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultMA:
    winst: float
    jaar: int
    financial_institution: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_marokko(
    winst: float,
    jaar: int,
    financial_institution: bool = False,
) -> CITResultMA:
    """Bereken Marokkaanse vennootschapsbelasting (IS, 2026-doeltarieven).

    Args:
        winst: Belastbare nettowinst in MAD.
        jaar: Belastingjaar (bijv. 2025).
        financial_institution: True voor kredietinstellingen en
            (her)verzekeraars — die convergeren naar 40%.

    Returns:
        CITResultMA dataclass.

    Note:
        Het toepasselijke tarief geldt op de GEHELE winst zodra de drempel
        van MAD 100.000.000 is overschreden (Marokkaanse praktijk; geen
        schijvensysteem in het doelstelsel).
    """
    HIGH_RATE_THRESHOLD = 100_000_000.0
    STANDARD_RATE = 0.20
    HIGH_RATE = 0.35
    FINANCIAL_RATE = 0.40

    if financial_institution:
        cit_rate = FINANCIAL_RATE
    elif winst >= HIGH_RATE_THRESHOLD:
        cit_rate = HIGH_RATE
    else:
        cit_rate = STANDARD_RATE

    if winst <= 0:
        return CITResultMA(
            winst=winst, jaar=jaar, financial_institution=financial_institution,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultMA(
        winst=winst,
        jaar=jaar,
        financial_institution=financial_institution,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
