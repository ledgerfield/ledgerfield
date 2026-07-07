"""Côte d'Ivoire corporate income tax calculator (impôt sur les bénéfices, BIC).

Côte d'Ivoire levies a flat **25%** corporate income tax on industrial and
commercial profits (Code Général des Impôts de Côte d'Ivoire), administered
by the DGI — Direction Générale des Impôts (https://www.dgi.gouv.ci/).
Telecommunications, IT and communication companies are taxed at **30%**
(sector rate, noted in params.json — out of scope for this SME estimator).
Côte d'Ivoire is an OHADA member state and reports under the shared
SYSCOHADA chart of accounts.

A minimum tax — the *impôt minimum forfaitaire* (IMF) — of **0.5% of
turnover** applies, subject to national floor and cap amounts (bounds
documented in params.json). VAT (TVA) is 18%.
"""
from __future__ import annotations

from ledgerfield.tax._ohada.base import CITResultOHADA, OHADACITBase


class CoteDivoireCIT(OHADACITBase):
    """Côte d'Ivoire BIC: flat 25% on taxable profit (CGI CI)."""

    LAND = "CI"
    CIT_RATE = 0.25
    # IMF: 0.5% of turnover, subject to floor/cap bounds (see params.json).
    MINIMUM_TAX_RATE = 0.005
    #: Sector rate for telecom/IT/communication companies (note only).
    TELECOM_RATE = 0.30


def bereken_cit_ivoorkust(winst: float, jaar: int) -> CITResultOHADA:
    """Bereken Ivoriaanse vennootschapsbelasting (25% flat).

    Args:
        winst: Belastbare winst in XOF (FCFA).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultOHADA dataclass.
    """
    return CoteDivoireCIT.bereken(winst, jaar)
