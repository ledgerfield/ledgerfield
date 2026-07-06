"""Hellenic Republic (Greece) corporate income tax calculator.

Greece levies a flat **22%** corporate income tax (Law 4172/2013, as
amended), administered by the Independent Authority for Public Revenue
(AADE). Credit institutions that have opted into the deferred-tax-asset
framework remain taxed at **29%**.

Other notes (informational, out of scope for this SME estimator):

- VAT (ΦΠΑ) standard rate 24%, reduced rates 13% and 6%, with reduced
  rates on certain Aegean islands.
- The business tax (τέλος επιτηδεύματος / telos epitidevmatos) is
  abolished for individuals/professionals as of 2025 and phased out.
- Pillar Two (15% minimum tax) applies to in-scope groups
  (Law 5100/2024, transposing Council Directive (EU) 2022/2523).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultGR:
    winst: float
    jaar: int
    credit_institution: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_griekenland(
    winst: float,
    jaar: int,
    credit_institution: bool = False,
) -> CITResultGR:
    """Bereken Griekse vennootschapsbelasting (22% vlak; banken 29%).

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).
        credit_institution: True voor kredietinstellingen onder het
            deferred-tax-asset regime (29% i.p.v. 22%).

    Returns:
        CITResultGR dataclass.
    """
    cit_rate = 0.29 if credit_institution else 0.22

    if winst <= 0:
        return CITResultGR(
            winst=winst, jaar=jaar, credit_institution=credit_institution,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultGR(
        winst=winst,
        jaar=jaar,
        credit_institution=credit_institution,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
