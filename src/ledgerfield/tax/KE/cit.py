"""Republic of Kenya corporate income tax calculator.

Kenya levies a **30%** corporate income tax on resident companies (Income Tax
Act, Cap 470), administered by the Kenya Revenue Authority (KRA). Non-resident
companies operating through a branch (permanent establishment) are taxed at
**37.5%**.

Export Processing Zone (EPZ) enterprises enjoy a 0% rate for the first ten
years and 25% for the following ten years — out of scope for this SME
estimator (see params.json). Kenya's VAT standard rate is 16%. The Significant
Economic Presence (SEP) tax of 3% replaced the Digital Service Tax (Finance
Act 2024), and a minimum top-up tax (Pillar Two QDMTT) applies from 2025 to
in-scope multinational groups.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultKE:
    winst: float
    jaar: int
    non_resident_branch: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_kenia(
    winst: float,
    jaar: int,
    non_resident_branch: bool = False,
) -> CITResultKE:
    """Bereken Keniaanse vennootschapsbelasting (30% resident / 37.5% branch).

    Args:
        winst: Belastbare winst in KES.
        jaar: Belastingjaar (bijv. 2025).
        non_resident_branch: True voor een filiaal (vaste inrichting) van een
            niet-ingezeten vennootschap (37.5%), anders 30% resident-tarief.

    Returns:
        CITResultKE dataclass.
    """
    RESIDENT_RATE = 0.30
    NON_RESIDENT_BRANCH_RATE = 0.375

    cit_rate = NON_RESIDENT_BRANCH_RATE if non_resident_branch else RESIDENT_RATE

    if winst <= 0:
        return CITResultKE(
            winst=winst, jaar=jaar, non_resident_branch=non_resident_branch,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultKE(
        winst=winst,
        jaar=jaar,
        non_resident_branch=non_resident_branch,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
