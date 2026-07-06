"""Kingdom of Bahrain corporate income tax calculator.

Bahrain levies **no general corporate income tax** (0%): the zero-CIT path is
the core model for this jurisdiction. The only long-standing exception is the
oil and gas exploration/production sector, taxed at **46%** under Legislative
Decree No. 22 of 1979.

From 1 January 2025 Bahrain also applies a 15% Domestic Minimum Top-up Tax
(DMTT, Decree-Law No. 11 of 2024) to large MNEs (≥ EUR 750m consolidated
revenue) — the first GCC state to do so. That regime targets large
multinationals and is out of scope for this SME estimator (see params.json).
Bahrain levies 10% VAT (raised from 5% on 1 January 2022).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultBH:
    winst: float
    jaar: int
    oil_and_gas: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_bahrein(
    winst: float,
    jaar: int,
    oil_and_gas: bool = False,
) -> CITResultBH:
    """Bereken Bahreinse vennootschapsbelasting (0% algemeen; 46% olie & gas).

    Args:
        winst: Belastbare winst in BHD.
        jaar: Belastingjaar (bijv. 2025).
        oil_and_gas: True voor olie- en gasexploratie/-productie
            (46%, Legislative Decree No. 22 of 1979); anders 0% (zero-CIT).

    Returns:
        CITResultBH dataclass.
    """
    CIT_RATE = 0.46 if oil_and_gas else 0.0

    if winst <= 0:
        return CITResultBH(
            winst=winst, jaar=jaar, oil_and_gas=oil_and_gas,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultBH(
        winst=winst,
        jaar=jaar,
        oil_and_gas=oil_and_gas,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
