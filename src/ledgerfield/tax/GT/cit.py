"""Republic of Guatemala corporate income tax calculator.

Guatemala's Ley de Actualización Tributaria (Decreto 10-2012) offers two
income-tax regimes for lucrative activities:

1. **Profits regime** (Régimen Sobre las Utilidades de Actividades
   Lucrativas): flat **25%** on net taxable income. Companies in this regime
   are additionally subject to the ISO solidarity tax (Impuesto de
   Solidaridad), a ~1% minimum tax on the higher of net assets or gross
   revenue, creditable against CIT (see params.json note).
2. **Simplified optional regime** (Régimen Opcional Simplificado Sobre
   Ingresos de Actividades Lucrativas): levied **on gross revenue**, not net
   profit — 5% on monthly gross revenue up to GTQ 30,000 and 7% on the
   excess.

This calculator only implements the profits regime: its input ``winst`` is
net taxable profit, while the simplified regime uses a *different tax base*
(monthly gross revenue). Computing the simplified regime from an annual net
profit figure would be meaningless, so ``regime="simplified"`` raises
``ValueError`` instead of returning a wrong number.

Administered by SAT (Superintendencia de Administración Tributaria).
VAT (IVA) is 12%.
"""
from __future__ import annotations

import os
from dataclasses import dataclass

PARAMS_PATH = os.path.join(os.path.dirname(__file__), "params.json")


@dataclass
class CITResultGT:
    winst: float
    jaar: int
    regime: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_guatemala(
    winst: float,
    jaar: int,
    regime: str = "profits",
) -> CITResultGT:
    """Bereken Guatemalteekse vennootschapsbelasting (profits regime, 25%).

    Args:
        winst: Belastbare nettowinst in GTQ.
        jaar: Belastingjaar (bijv. 2025).
        regime: Alleen ``"profits"`` wordt ondersteund. Het optionele
            vereenvoudigde regime (``"simplified"``) wordt geheven over de
            *bruto maandomzet* (5% tot GTQ 30.000/maand, 7% daarboven) — een
            andere grondslag dan nettowinst — en kan dus niet uit ``winst``
            worden berekend; deze functie raise-t dan een ValueError.

    Returns:
        CITResultGT dataclass.
    """
    if regime != "profits":
        raise ValueError(
            "Only the 'profits' regime is supported: the simplified optional "
            "regime is levied on gross revenue (5% up to GTQ 30,000/month, "
            "7% above), a different tax base than net profit (winst), so it "
            "cannot be computed from this input."
        )

    CIT_RATE = 0.25

    if winst <= 0:
        return CITResultGT(
            winst=winst, jaar=jaar, regime=regime,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultGT(
        winst=winst,
        jaar=jaar,
        regime=regime,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
