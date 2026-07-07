"""Georgia corporate income tax calculator — Estonian (distributed-profit) model.

Since 2017 Georgia applies the **Estonian model** of corporate income tax:
CIT is levied at **15%** only on *distributed* profit (e.g. dividends and
certain deemed distributions). Retained / reinvested profit is taxed at
**0%** — no CIT is due until profit leaves the company.

Administered by the Revenue Service (Georgia). Georgia applies a standard
**18%** VAT.

Note: for some distributions Georgia grosses up the base (dividing the net
distribution by 0.85, i.e. 15% of the 100/85 gross-up). This estimator keeps
it simple and applies 15% directly to the distribution amount; see params.json.

WARNING: Rates in this pack are AI-estimated and MUST be verified against the
Revenue Service (rs.ge) before any production filing (see params.json).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultGE:
    distributie: float
    jaar: int
    ingehouden: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_georgie(
    distributie: float,
    jaar: int,
    ingehouden: bool = False,
) -> CITResultGE:
    """Bereken Georgische winstbelasting (Estisch model: 15% op uitgekeerde winst).

    Args:
        distributie: Uitgekeerde winst in GEL (bijv. dividend). Bij ingehouden
            winst is dit het bedrag dat wordt ingehouden/geherinvesteerd.
        jaar: Belastingjaar (bijv. 2025).
        ingehouden: True als de winst wordt ingehouden/geherinvesteerd
            (Estisch model → 0% CIT). False (standaard) → 15% op de distributie.

    Returns:
        CITResultGE dataclass. Ingehouden of niet-positieve winst levert nul
        belasting (kern van het Estische model).
    """
    CIT_RATE = 0.15

    # Estonian model: retained/reinvested profit is not taxed.
    if ingehouden or distributie <= 0:
        return CITResultGE(
            distributie=distributie, jaar=jaar, ingehouden=ingehouden,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = distributie * CIT_RATE
    effectief_tarief = cit_totaal / distributie

    return CITResultGE(
        distributie=distributie,
        jaar=jaar,
        ingehouden=ingehouden,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
