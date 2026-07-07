"""Republic of Chile corporate income tax calculator.

Chile levies a **27%** First Category Tax (Impuesto de Primera Categoría)
under the semi-integrated regime (Art. 14A, Ley sobre Impuesto a la Renta),
administered by the Servicio de Impuestos Internos (SII).

SMEs qualifying for the **Pro Pyme** regime (Art. 14D LIR) are taxed at a
reduced **25%** rate. Reform proposals contemplate a transitory 12.5% Pro
Pyme rate for 2025-2027; this estimator uses the statutory 25% (note only).

Under the semi-integrated regime, final shareholders may credit 65% of the
First Category Tax against their final taxes (partial integration).
VAT (IVA) applies at 19%.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultCL:
    winst: float
    jaar: int
    pro_pyme: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_chili(
    winst: float,
    jaar: int,
    pro_pyme: bool = False,
) -> CITResultCL:
    """Bereken Chileense vennootschapsbelasting (First Category Tax).

    Args:
        winst: Belastbare winst in CLP.
        jaar: Belastingjaar (bijv. 2025).
        pro_pyme: True voor het Pro Pyme MKB-regime (Art. 14D LIR, 25%);
            False voor het semi-geïntegreerde algemene regime (Art. 14A, 27%).

    Returns:
        CITResultCL dataclass.
    """
    cit_rate = 0.25 if pro_pyme else 0.27

    if winst <= 0:
        return CITResultCL(
            winst=winst, jaar=jaar, pro_pyme=pro_pyme,
            cit_rate=cit_rate, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = winst * cit_rate
    effectief_tarief = cit_totaal / winst

    return CITResultCL(
        winst=winst,
        jaar=jaar,
        pro_pyme=pro_pyme,
        cit_rate=cit_rate,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
