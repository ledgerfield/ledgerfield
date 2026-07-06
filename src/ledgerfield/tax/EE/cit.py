"""Republic of Estonia corporate income tax calculator.

Estonia applies the **original Estonian model** of corporate taxation
(Tulumaksuseadus / Income Tax Act): there is NO annual corporate income tax
on retained or reinvested profit (0%). Tax arises ONLY at the moment profit
is DISTRIBUTED (dividends, deemed distributions, fringe benefits, gifts,
non-business expenses).

From 1 January 2025 the distribution tax is **22/78 of the NET distribution**
(raised from 20/80 by the 2025 tax package; the preferential 14/86 rate for
regularly paid dividends was abolished as of 2025).

Gross-up mechanics: the rate is expressed on the *net* amount paid out. A net
distribution of 78 carries tax of 22 (78 * 22/78), i.e. the gross profit used
is 100 and the statutory rate on the gross is 22%. The effective rate on the
net distribution is 22/78 ≈ 28.2%.

2026 note (security/defence levy package): the rate becomes **24/76** of the
net distribution from 1 January 2026 — informational note only, not modelled
here. Administered by the Estonian Tax and Customs Board (EMTA,
https://www.emta.ee/).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CITResultEE:
    distributie_netto: float
    jaar: int
    ingehouden: bool
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


def bereken_cit_estland(
    distributie_netto: float,
    jaar: int,
    ingehouden: bool = False,
) -> CITResultEE:
    """Bereken Estse vennootschapsbelasting (distributie-belasting, 22/78 netto).

    Estland kent géén jaarlijkse winstbelasting: ingehouden/geherinvesteerde
    winst wordt met 0% belast. Alleen bij winstuitkering is belasting
    verschuldigd: vanaf 1 januari 2025 22/78 van de NETTO-uitkering
    (bruteringsmechaniek: netto 78 → belasting 22 → bruto 100).

    Args:
        distributie_netto: Netto uitgekeerde winst in EUR (het bedrag dat de
            aandeelhouders daadwerkelijk ontvangen).
        jaar: Belastingjaar (bijv. 2025).
        ingehouden: True als de winst wordt ingehouden/geherinvesteerd in
            plaats van uitgekeerd — dan is de belasting 0.0 (kern van het
            Estse model).

    Returns:
        CITResultEE dataclass.
    """
    CIT_RATE = 22.0 / 78.0  # 22/78 van de netto-uitkering (vanaf 1-1-2025)

    if ingehouden or distributie_netto <= 0:
        return CITResultEE(
            distributie_netto=distributie_netto, jaar=jaar, ingehouden=ingehouden,
            cit_rate=CIT_RATE, cit_totaal=0.0, effectief_tarief=0.0,
        )

    cit_totaal = distributie_netto * 22.0 / 78.0
    effectief_tarief = cit_totaal / distributie_netto

    return CITResultEE(
        distributie_netto=distributie_netto,
        jaar=jaar,
        ingehouden=ingehouden,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
    )
