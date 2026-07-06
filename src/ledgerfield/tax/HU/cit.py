"""Hungary corporate income tax calculator.

Hungary levies a flat **9%** corporate income tax (társasági adó, Act LXXXI of
1996) — the lowest headline CIT rate in the European Union. It is administered
by the National Tax and Customs Administration (NAV).

On top of CIT, municipalities may levy a local business tax (HIPA, helyi
iparűzési adó) of up to 2% on *adjusted turnover* — a different base than
profit, so it is documented in params.json rather than computed here. Small
businesses may opt into the alternative KIVA regime (10% on a payroll-plus
base) instead of CIT. Hungary implements a Pillar Two QDMTT despite its 9%
headline rate; sector surtaxes (banks, retail, energy) also apply — see
params.json notes.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultHU:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_hongarije(winst: float, jaar: int) -> CITResultHU:
    """Bereken Hongaarse vennootschapsbelasting (9% flat, Act LXXXI/1996).

    Args:
        winst: Belastbare winst in HUF.
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultHU dataclass.
    """
    CIT_RATE = 0.09

    if winst <= 0:
        return CITResultHU(
            winst=winst, jaar=jaar,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    return CITResultHU(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
