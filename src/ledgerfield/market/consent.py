"""Explicit opt-in consent management for data sharing."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__all__ = ["DataCategory", "ConsentRecord", "ConsentManager"]


class DataCategory(Enum):
    SALARY_BENCHMARKS     = "salary_benchmarks"       # median/p25/p75 salaries by sector+country
    COST_RATIOS           = "cost_ratios"              # opex/revenue ratios by industry
    MARGIN_BENCHMARKS     = "margin_benchmarks"        # gross/net margin distributions
    TAX_EFFECTIVE_RATES   = "tax_effective_rates"      # effective CIT/IIT rates actually paid
    CASH_FLOW_PATTERNS    = "cash_flow_patterns"       # monthly cash-flow seasonality indices
    PAYROLL_COSTS         = "payroll_costs"            # employer burden ratios by country
    INVOICE_CYCLES        = "invoice_cycles"           # average days-to-payment by sector


@dataclass
class ConsentRecord:
    category: DataCategory
    jurisdiction: str              # ISO country code or "*" for all
    consented: bool
    granted_at: float              # epoch seconds
    revoked_at: Optional[float] = None

    def is_active(self) -> bool:
        return self.consented and self.revoked_at is None


class ConsentManager:
    """Persistent in-memory consent store.  Serialize via to_dict()/from_dict()."""

    def __init__(self) -> None:
        # (category, jurisdiction) → ConsentRecord
        self._records: dict[tuple[DataCategory, str], ConsentRecord] = {}

    # ── write ────────────────────────────────────────────────────────────────

    def grant(self, category: DataCategory, jurisdiction: str = "*") -> ConsentRecord:
        rec = ConsentRecord(category, jurisdiction, True, time.time())
        self._records[(category, jurisdiction)] = rec
        return rec

    def revoke(self, category: DataCategory, jurisdiction: str = "*") -> None:
        key = (category, jurisdiction)
        if key in self._records:
            self._records[key].consented = False
            self._records[key].revoked_at = time.time()

    # ── query ────────────────────────────────────────────────────────────────

    def is_consented(self, category: DataCategory, jurisdiction: str) -> bool:
        """True when there is an active consent for (category, jurisdiction) or (category, '*')."""
        for jur in (jurisdiction, "*"):
            rec = self._records.get((category, jur))
            if rec and rec.is_active():
                return True
        return False

    def active_categories(self) -> list[DataCategory]:
        return [r.category for r in self._records.values() if r.is_active()]

    # ── persistence ──────────────────────────────────────────────────────────

    def to_dict(self) -> list[dict]:
        return [
            {
                "category": r.category.value,
                "jurisdiction": r.jurisdiction,
                "consented": r.consented,
                "granted_at": r.granted_at,
                "revoked_at": r.revoked_at,
            }
            for r in self._records.values()
        ]

    @classmethod
    def from_dict(cls, records: list[dict]) -> "ConsentManager":
        cm = cls()
        for d in records:
            cat = DataCategory(d["category"])
            rec = ConsentRecord(cat, d["jurisdiction"], d["consented"], d["granted_at"], d.get("revoked_at"))
            cm._records[(cat, d["jurisdiction"])] = rec
        return cm
