"""Republic of Latvia corporate income tax (uzņēmumu ienākuma nodoklis)
calculator — Estonian model (distribution-only taxation).

Since 1 January 2018 Latvia applies the **Estonian model**: there is NO annual
corporate income tax on retained or reinvested profit (0%). Tax arises ONLY
when profit is DISTRIBUTED (dividends and deemed distributions), administered
by the State Revenue Service (VID, Valsts ieņēmumu dienests).

The 20% rate applies to the **GROSSED-UP** taxable base, not the net
distribution. The net distribution is divided by 0.8 to obtain the gross base:

    gross base = net distribution / 0.8
    CIT        = 20% × gross base = net distribution × 20 / 80

So a net distribution of EUR 800,000 gives a gross base of EUR 1,000,000 and
CIT of EUR 200,000 — an **effective 25% on the net amount** (20/80 = 0.25).

VAT (PVN, pievienotās vērtības nodoklis) is 21% standard. Latvia applies the
EU Pillar Two framework for large groups (see params.json) — out of scope for
this SME estimator.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultLV:
    distributie_netto: float
    jaar: int
    ingehouden: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief_op_netto: float


def bereken_cit_letland(
    distributie_netto: float,
    jaar: int,
    ingehouden: bool = False,
) -> CITResultLV:
    """Bereken Letse vennootschapsbelasting (Estisch model, 2025-regels).

    Ingehouden (niet-uitgekeerde) winst is belast tegen 0%. Alleen bij
    winstuitkering ontstaat belasting: 20% over de gebruteerde grondslag,
    d.w.z. ``distributie_netto * 20 / 80`` (effectief 25% op het nettobedrag).

    Args:
        distributie_netto: Netto winstuitkering in EUR (of, bij
            ``ingehouden=True``, de ingehouden winst waarover géén
            belasting verschuldigd is).
        jaar: Belastingjaar (bijv. 2025).
        ingehouden: True als de winst wordt ingehouden/geherinvesteerd —
            dan is de belasting 0.0 (kern van het Estische model).

    Returns:
        CITResultLV dataclass.
    """
    CIT_RATE = 0.20  # 20% op de gebruteerde (gross-up) grondslag

    if ingehouden or distributie_netto <= 0:
        return CITResultLV(
            distributie_netto=distributie_netto, jaar=jaar, ingehouden=ingehouden,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief_op_netto=0.0,
        )

    # Gross-up: 20% van (netto / 0.8) == netto * 20 / 80 (effectief 25% op netto).
    cit_totaal = distributie_netto * 20 / 80
    effectief_tarief_op_netto = cit_totaal / distributie_netto

    return CITResultLV(
        distributie_netto=distributie_netto,
        jaar=jaar,
        ingehouden=ingehouden,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief_op_netto=effectief_tarief_op_netto,
    )
