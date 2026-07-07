"""Senegal corporate income tax calculator (impôt sur les sociétés, IS).

Senegal levies a flat **30%** corporate income tax (Code Général des Impôts
du Sénégal), administered by the DGID — Direction générale des Impôts et des
Domaines (https://www.dgid.sn/). Senegal is an OHADA member state and reports
under the shared SYSCOHADA chart of accounts.

A minimum tax — the *impôt minimum forfaitaire* (IMF) — of **0.5% of
turnover** applies when it exceeds the profit-based IS (national floor/cap
bounds documented in params.json). VAT (TVA) is 18%.
"""
from __future__ import annotations

from ledgerfield.tax._ohada.base import CITResultOHADA, OHADACITBase


class SenegalCIT(OHADACITBase):
    """Senegal IS: flat 30% on taxable profit (CGI Sénégal)."""

    LAND = "SN"
    CIT_RATE = 0.30
    # IMF: 0.5% of turnover (shared OHADA pattern, base default).
    MINIMUM_TAX_RATE = 0.005


def bereken_cit_senegal(winst: float, jaar: int) -> CITResultOHADA:
    """Bereken Senegalese vennootschapsbelasting (30% flat).

    Args:
        winst: Belastbare winst in XOF (FCFA).
        jaar: Belastingjaar (bijv. 2025).

    Returns:
        CITResultOHADA dataclass.
    """
    return SenegalCIT.bereken(winst, jaar)
