"""Slovak Republic corporate income tax calculator.

Slovakia's 2025 consolidation package (novela zákona č. 595/2003 Z. z. o dani
z príjmov) introduces a three-band CIT structure from 1 January 2025:

* **10%** reduced rate for taxpayers with taxable revenue up to
  **EUR 100,000** per tax period (``company_size="small"``).
* **21%** standard rate (``company_size="standard"``).
* **24%** increased rate on a tax base exceeding **EUR 5,000,000**
  (``company_size="large"``).

Administered by the Financial Administration of the Slovak Republic
(Finančná správa, https://www.financnasprava.sk/). The 2025 package also
introduces a financial transaction tax and Slovakia applies the EU Pillar Two
minimum tax rules (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATES_SK = {
    "small": 0.10,     # taxable revenue <= EUR 100,000
    "standard": 0.21,  # default rate
    "large": 0.24,     # tax base > EUR 5,000,000
}


@dataclass
class CITResultSK:
    winst: float
    jaar: int
    company_size: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_slowakije(
    winst: float,
    jaar: int,
    company_size: str = "standard",
) -> CITResultSK:
    """Bereken Slowaakse vennootschapsbelasting (2025 consolidatiepakket).

    Tariefbanden 2025:
        * ``"small"``    → 10% — verlaagd tarief voor belastbare omzet
          tot en met EUR 100.000 per belastingtijdvak.
        * ``"standard"`` → 21% — standaardtarief.
        * ``"large"``    → 24% — verhoogd tarief voor een belastinggrondslag
          boven EUR 5.000.000.

    Args:
        winst: Belastbare winst (belastinggrondslag) in EUR.
        jaar: Belastingjaar (bijv. 2025).
        company_size: Tariefband: "small", "standard" of "large".

    Returns:
        CITResultSK dataclass.

    Raises:
        ValueError: Bij een onbekende ``company_size``.
    """
    if company_size not in CIT_RATES_SK:
        raise ValueError(
            f"Unknown company_size {company_size!r}; "
            f"expected one of {sorted(CIT_RATES_SK)}"
        )

    cit_rate = CIT_RATES_SK[company_size]

    if winst <= 0:
        return CITResultSK(
            winst=winst, jaar=jaar, company_size=company_size,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultSK(
        winst=winst,
        jaar=jaar,
        company_size=company_size,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
