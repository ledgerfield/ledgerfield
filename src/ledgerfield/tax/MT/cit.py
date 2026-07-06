"""Republic of Malta corporate income tax calculator.

Malta levies corporate income tax at a flat **35%** statutory rate (Income Tax
Act, Cap. 123). Under Malta's **full-imputation refund system**, however,
shareholders may — upon distribution of taxed profits — claim a refund of the
tax paid at company level, typically **6/7ths** of the tax on trading income.
For non-resident shareholders this brings the effective Maltese tax burden
down to approximately **5%**.

The refund is a *shareholder-level* mechanism: the company itself pays the
full 35% CIT, and the refund is paid to the shareholder after a dividend is
distributed. This module models the company-level 35% charge and, optionally,
the shareholder-level 6/7 refund via ``refund_6_7=True``.

VAT: 18% standard with reduced rates of 12%, 7% and 5%.
Administered by the Commissioner for Revenue (CFR).
"""
from __future__ import annotations

from dataclasses import dataclass

CIT_RATE = 0.35              # statutory company-level rate (Cap. 123)
REFUND_FRACTION = 6.0 / 7.0  # typical shareholder refund on trading income


@dataclass
class CITResultMT:
    winst: float
    jaar: int
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float
    refund_bedrag: float | None = None
    effectieve_druk: float | None = None
    note: str = ""


_REFUND_NOTE = (
    "The 6/7 refund is a shareholder-level mechanism under Malta's "
    "full-imputation system: the company pays the full 35% CIT and the "
    "shareholder claims the refund upon distribution of taxed profits, "
    "giving an effective burden of ~5% for non-resident shareholders."
)


def bereken_cit_malta(
    winst: float,
    jaar: int,
    refund_6_7: bool = False,
) -> CITResultMT:
    """Bereken Maltese vennootschapsbelasting (35% statutair).

    Args:
        winst: Belastbare winst in EUR.
        jaar: Belastingjaar (bijv. 2025).
        refund_6_7: Indien True wordt ook de 6/7-aandeelhoudersteruggave bij
            uitkering gemodelleerd (refund_bedrag en effectieve_druk gevuld).

    Returns:
        CITResultMT dataclass. cit_totaal is altijd de volledige 35% op
        vennootschapsniveau; de teruggave is een aandeelhouders-mechanisme.
    """
    if winst <= 0:
        return CITResultMT(
            winst=winst, jaar=jaar, cit_rate=CIT_RATE, cit_totaal=0.0,
            effectief_tarief=0.0,
            refund_bedrag=0.0 if refund_6_7 else None,
            effectieve_druk=0.0 if refund_6_7 else None,
            note=_REFUND_NOTE,
        )

    cit_totaal = winst * CIT_RATE
    effectief_tarief = cit_totaal / winst

    refund_bedrag: float | None = None
    effectieve_druk: float | None = None
    if refund_6_7:
        refund_bedrag = cit_totaal * REFUND_FRACTION
        effectieve_druk = (cit_totaal - refund_bedrag) / winst

    return CITResultMT(
        winst=winst,
        jaar=jaar,
        cit_rate=CIT_RATE,
        cit_totaal=cit_totaal,
        effectief_tarief=effectief_tarief,
        refund_bedrag=refund_bedrag,
        effectieve_druk=effectieve_druk,
        note=_REFUND_NOTE,
    )
