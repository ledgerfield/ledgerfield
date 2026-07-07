"""Republic of Nicaragua corporate income tax calculator.

Nicaragua levies a **30%** income tax (IR — Impuesto sobre la Renta) on net
taxable income under Ley No. 822, Ley de Concertación Tributaria (LCT),
administered by the Dirección General de Ingresos (DGI).

Alongside the 30% on net income, Nicaragua applies a *pago mínimo definitivo*
(definitive minimum payment) of **1%–3% of GROSS income**, tiered by taxpayer
size (large taxpayers 3%, medium 2%, small 1%). The IR payable for the year is
the **greater of** 30% of net income and the minimum on gross income. Because
the minimum is computed on gross income, a company with a net LOSS but
positive gross income still owes the gross minimum — this estimator models
that explicitly.

VAT (IVA) is 15%.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultNI:
    winst: float
    jaar: int
    bruto_inkomen: float | None
    minimum_pct: float
    cit_rate: float
    cit_regulier: float
    pago_minimo: float
    cit_totaal: float
    effectief_tarief: float
    minimum_toegepast: bool


def bereken_cit_nicaragua(
    winst: float,
    jaar: int,
    bruto_inkomen: float | None = None,
    minimum_pct: float = 0.03,
) -> CITResultNI:
    """Bereken Nicaraguaanse vennootschapsbelasting (IR, Ley 822 LCT).

    Verschuldigd is het MAXIMUM van:
      * 30% IR over de netto belastbare winst, en
      * het pago mínimo definitivo (1%–3%, naar omvang) over het BRUTO inkomen,
        indien ``bruto_inkomen`` is opgegeven.

    Let op: bij een netto VERLIES met positief bruto inkomen blijft het
    bruto-minimum verschuldigd (het pago mínimo is definitief en grijpt aan op
    bruto inkomen, niet op winst).

    Args:
        winst: Netto belastbare winst in NIO (córdoba). Mag negatief zijn.
        jaar: Belastingjaar (bijv. 2025).
        bruto_inkomen: Bruto inkomen in NIO voor het pago mínimo definitivo;
            None indien niet van toepassing / onbekend.
        minimum_pct: Pago-mínimo-percentage over bruto inkomen (0.01–0.03
            naar belastingplichtige-omvang; standaard 0.03 voor grote
            belastingplichtigen).

    Returns:
        CITResultNI dataclass; ``minimum_toegepast`` geeft aan of het
        bruto-minimum het reguliere 30%-bedrag heeft verdrongen.
    """
    if not 0.0 <= minimum_pct <= 1.0:
        raise ValueError("minimum_pct must be between 0.0 and 1.0")
    if bruto_inkomen is not None and bruto_inkomen < 0:
        raise ValueError("bruto_inkomen cannot be negative")

    CIT_RATE = 0.30

    cit_regulier = winst * CIT_RATE if winst > 0 else 0.0
    pago_minimo = bruto_inkomen * minimum_pct if bruto_inkomen is not None else 0.0

    if pago_minimo > cit_regulier:
        cit_totaal = pago_minimo
        minimum_toegepast = pago_minimo > 0.0
    else:
        cit_totaal = cit_regulier
        minimum_toegepast = False

    effectief_tarief = cit_totaal / winst if winst > 0 else 0.0

    return CITResultNI(
        winst=winst,
        jaar=jaar,
        bruto_inkomen=bruto_inkomen,
        minimum_pct=minimum_pct,
        cit_rate=CIT_RATE,
        cit_regulier=cit_regulier,
        pago_minimo=pago_minimo,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
        minimum_toegepast=minimum_toegepast,
    )
