"""Cameroon corporate income tax calculator (impôt sur les sociétés, IS).

Cameroon levies a **33% effective** corporate income tax, decomposed as a
**30% principal rate** plus **10% additional council centimes** (centimes
additionnels communaux, CAC) levied *on the tax itself*:
30% + (10% x 30%) = 33% (Code Général des Impôts du Cameroun), administered
by the DGI — Direction Générale des Impôts (https://www.impots.cm/).

Reduced regimes (turnover bands, noted in params.json, out of scope for this
SME estimator): companies with turnover up to XAF 3 billion pay a 25%
principal rate, i.e. **27.5% including CAC** (25% + 10% CAC = 27.5%).

Cameroon is an OHADA member state and reports under the shared SYSCOHADA
chart of accounts. A minimum tax on turnover applies (2.2% incl. CAC for the
standard regime — see params.json; this differs from the 0.5% pattern
elsewhere in the OHADA zone). VAT is **19.25%** = 17.5% principal + 10% CAC.
"""
from __future__ import annotations

from dataclasses import dataclass

from ledgerfield.tax._ohada.base import CITResultOHADA, OHADACITBase


@dataclass
class CITResultCM(CITResultOHADA):
    """Cameroon result with the 30% + 10%-CAC decomposition exposed."""

    #: Principal IS at 30% of taxable profit.
    cit_principal: float = 0.0
    #: Centimes additionnels communaux: 10% of the principal IS.
    cac_bedrag: float = 0.0


class CameroonCIT(OHADACITBase):
    """Cameroon IS: 33% effective = 30% principal + 10% CAC on the tax."""

    LAND = "CM"
    #: Effective rate including CAC: 0.30 * 1.10 = 0.33.
    CIT_RATE = 0.33
    #: Principal IS rate (before CAC).
    PRINCIPAL_RATE = 0.30
    #: Centimes additionnels communaux, applied to the principal tax.
    CAC_RATE = 0.10
    #: Cameroon minimum tax: 2.2% of turnover incl. CAC (2% + 10% CAC),
    #: standard regime — overrides the common 0.5% OHADA pattern.
    MINIMUM_TAX_RATE = 0.022

    @classmethod
    def _maak_resultaat(
        cls, winst: float, jaar: int, cit_totaal: float
    ) -> CITResultCM:
        """Extend the shared result with the principal/CAC decomposition."""
        if winst > 0:
            cit_principal = winst * cls.PRINCIPAL_RATE
            cac_bedrag = cit_principal * cls.CAC_RATE
        else:
            cit_principal = 0.0
            cac_bedrag = 0.0
        return CITResultCM(
            winst=winst,
            jaar=jaar,
            land=cls.LAND,
            cit_rate=cls.CIT_RATE,
            cit_totaal=cit_totaal,
            effectief_tarief=cit_totaal / winst if winst > 0 else 0.0,
            cit_principal=cit_principal,
            cac_bedrag=cac_bedrag,
        )


def bereken_cit_kameroen(winst: float, jaar: int) -> CITResultCM:
    """Bereken Kameroense vennootschapsbelasting (33% incl. CAC).

    Args:
        winst: Belastbare winst in XAF (FCFA).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultCM dataclass (incl. cit_principal en cac_bedrag).
    """
    result = CameroonCIT.bereken(winst, jaar)
    assert isinstance(result, CITResultCM)
    return result
