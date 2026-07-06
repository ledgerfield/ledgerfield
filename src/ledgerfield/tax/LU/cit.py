"""Grand Duchy of Luxembourg corporate income tax calculator.

Luxembourg levies corporate income tax (impôt sur le revenu des collectivités,
IRC) at **16%** from tax year 2025 (cut from 17%), with a reduced **14%** rate
on taxable income up to EUR 175,000 and a statutory transition band between
EUR 175,000 and EUR 200,001.

On top of the state CIT come the **7% solidarity surtax** (contribution to the
employment fund, computed on the CIT amount) and the **municipal business tax**
(impôt commercial communal, ~6.75% in Luxembourg City), giving an aggregate
effective rate of roughly **23.87%** in Luxembourg City for 2025. This module
returns only the *state* CIT; the aggregate rate is exposed in params.json as
``aggregate_effective_rate_luxembourg_city``.

VAT: 17% standard (lowest in the EU) with reduced rates of 14%, 8% and 3%.
Administered by the Administration des contributions directes (ACD).
"""
from __future__ import annotations

from dataclasses import dataclass

# 2025 IRC parameters (ACD)
REDUCED_RATE = 0.14          # taxable income <= EUR 175,000
STANDARD_RATE = 0.16         # taxable income > EUR 200,001 (2025, cut from 17%)
REDUCED_BRACKET_LIMIT = 175_000.0
TRANSITION_BAND_UPPER = 200_001.0


@dataclass
class CITResultLU:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float
    note: str


_TRANSITION_NOTE = (
    "Simplified: <= EUR 175,000 taxed at 14%; above EUR 175,000 the full 16% "
    "rate is applied. The statutory transition band (EUR 175,000 - 200,001: "
    "EUR 24,500 + 45% of income above EUR 175,000) is documented but not "
    "modelled. Result carries only the state CIT (IRC); the 7% solidarity "
    "surtax and municipal business tax (~6.75% Luxembourg City) are excluded "
    "here — see aggregate_effective_rate_luxembourg_city (0.2387) in "
    "params.json."
)


def bereken_cit_luxemburg(winst: float, jaar: int) -> CITResultLU:
    """Bereken Luxemburgse vennootschapsbelasting (IRC) voor 2025.

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultLU dataclass met alleen de staats-CIT (IRC). De solidariteits-
        opslag (7% van de CIT) en de gemeentelijke bedrijfsbelasting (~6,75%
        Luxemburg-Stad) zijn gedocumenteerd maar niet in het resultaat verwerkt.
    """
    if winst <= 0:
        return CITResultLU(
            winst=winst, jaar=jaar, cit_rate=0.0, cit_totaal=0.0,
            effectief_tarief=0.0, note=_TRANSITION_NOTE,
        )

    if winst <= REDUCED_BRACKET_LIMIT:
        cit_rate = REDUCED_RATE
    else:
        cit_rate = STANDARD_RATE

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultLU(
        winst=winst,
        jaar=jaar,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
        note=_TRANSITION_NOTE,
    )
