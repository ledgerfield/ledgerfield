"""Shared OHADA / SYSCOHADA corporate income tax base.

OHADA (Organisation pour l'Harmonisation en Afrique du Droit des Affaires)
harmonises business law across its 17 West and Central African member states,
including Senegal (SN), Côte d'Ivoire (CI) and Cameroon (CM). Accounting in
the OHADA zone follows **SYSCOHADA** (Système Comptable OHADA, revised by the
AUDCIF uniform act, in force since 2018): one shared chart of accounts
organised in classes 1-7 (plus class 8 for HAO items and income tax), used
identically across all member states.

Corporate income tax itself remains *national* law (each member state's Code
Général des Impôts), but the OHADA members share a common structural pattern
that this abstract base captures:

* a flat CIT rate applied to taxable profit (per-country ``CIT_RATE``);
* a **minimum tax on turnover** — the *impôt minimum forfaitaire* (IMF),
  typically 0.5% of turnover, due when it exceeds the profit-based CIT
  (exposed here as the ``minimum_tax_op_omzet`` classmethod hook);
* no tax on non-positive profit (shared guard in ``bereken``).

Per-country subclasses only define ``LAND`` (ISO 3166-1 alpha-2 code),
``CIT_RATE`` and country specifics (e.g. Cameroon's 10% additional council
centimes, CAC).
"""
from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class CITResultOHADA:
    """Common CIT result for OHADA-zone calculators."""

    winst: float
    jaar: int
    land: str
    cit_rate: float
    cit_totaal: float
    effectief_tarief: float


class OHADACITBase(ABC):
    """Abstract base for OHADA-member corporate income tax calculators.

    Subclasses set ``LAND`` and ``CIT_RATE`` and may override
    ``MINIMUM_TAX_RATE``, ``minimum_tax_op_omzet`` or ``_maak_resultaat``
    for country specifics.
    """

    #: ISO 3166-1 alpha-2 country code — set by each subclass.
    LAND: ClassVar[str]
    #: Flat CIT rate on taxable profit — set by each subclass.
    CIT_RATE: ClassVar[float]
    #: Impôt minimum forfaitaire (IMF) rate on turnover — 0.5% is the common
    #: OHADA-zone pattern; subclasses may override.
    MINIMUM_TAX_RATE: ClassVar[float] = 0.005

    @classmethod
    def minimum_tax_op_omzet(cls, omzet: float) -> float:
        """Minimum tax (impôt minimum forfaitaire, IMF) on turnover.

        Shared OHADA-zone pattern: a small percentage of turnover
        (``MINIMUM_TAX_RATE``, typically 0.5%) acts as the floor for the
        profit-based CIT. National bounds (floors/caps) are documented in
        each country's ``params.json`` and are not modelled here.

        Args:
            omzet: Jaaromzet (turnover) in local currency.

        Returns:
            The IMF amount (0.0 for non-positive turnover).
        """
        if omzet <= 0:
            return 0.0
        return omzet * cls.MINIMUM_TAX_RATE

    @classmethod
    def bereken(cls, winst: float, jaar: int) -> CITResultOHADA:
        """Bereken de vennootschapsbelasting (shared OHADA logic).

        Args:
            winst: Belastbare winst in lokale valuta (XOF/XAF).
            jaar: Belastingjaar (bijv. 2025).

        Returns:
            CITResultOHADA (or a country-specific subclass thereof).
        """
        cit_totaal = 0.0 if winst <= 0 else cls._cit_op_winst(winst)
        return cls._maak_resultaat(winst, jaar, cit_totaal)

    @classmethod
    def _cit_op_winst(cls, winst: float) -> float:
        """Profit-based CIT for positive profit — flat rate by default."""
        return winst * cls.CIT_RATE

    @classmethod
    def _maak_resultaat(
        cls, winst: float, jaar: int, cit_totaal: float
    ) -> CITResultOHADA:
        """Assemble the result dataclass; subclasses may extend it."""
        return CITResultOHADA(
            winst=winst,
            jaar=jaar,
            land=cls.LAND,
            cit_rate=cls.CIT_RATE,
            cit_totaal=cit_totaal,
            effectief_tarief=cit_totaal / winst if winst > 0 else 0.0,
        )
