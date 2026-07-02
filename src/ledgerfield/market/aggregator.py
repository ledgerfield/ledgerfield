"""K-anonymised statistical aggregation of ledger data.

Guarantees: a DataPoint is only published when >= K_MIN distinct
node IDs contributed to it. Published stats use at most one value per node
per aggregate key so a single node cannot flood the sample. Raw values are
never stored or returned.
"""
from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Optional

from .consent import DataCategory

__all__ = ["K_MIN", "AggregateStats", "DataPoint", "Aggregator"]

K_MIN = 5  # minimum contributors — do NOT lower without privacy review


@dataclass(frozen=True)
class AggregateStats:
    count: int
    sample_count: int
    distinct_contributor_count: int
    mean: float
    median: float
    p25: float
    p75: float
    std: float
    min_val: float
    max_val: float

    def to_dict(self) -> dict:
        return {
            "count": self.count,
            "sample_count": self.sample_count,
            "distinct_contributor_count": self.distinct_contributor_count,
            "mean": round(self.mean, 4),
            "median": round(self.median, 4),
            "p25": round(self.p25, 4),
            "p75": round(self.p75, 4),
            "std": round(self.std, 4),
            "min": round(self.min_val, 4),
            "max": round(self.max_val, 4),
        }


@dataclass
class DataPoint:
    """A single contributed value plus the contributor's node ID (not exported)."""
    node_id: str
    value: float


class Aggregator:
    """Collect raw DataPoints and produce k-anonymous AggregateStats."""

    def __init__(self) -> None:
        # (category, jurisdiction, sector, fiscal_year) → list[DataPoint]
        self._pool: dict[tuple, list[DataPoint]] = {}

    # ── ingestion ────────────────────────────────────────────────────────────

    def contribute(
        self,
        node_id: str,
        category: DataCategory,
        jurisdiction: str,
        sector: str,
        fiscal_year: int,
        value: float,
    ) -> None:
        """Add one data point.  Caller must have verified consent before calling."""
        key = (category, jurisdiction, sector, fiscal_year)
        if key not in self._pool:
            self._pool[key] = []
        self._pool[key].append(DataPoint(node_id, value))

    # ── aggregation ──────────────────────────────────────────────────────────

    def aggregate(
        self,
        category: DataCategory,
        jurisdiction: str,
        sector: str,
        fiscal_year: int,
    ) -> Optional[AggregateStats]:
        """Return stats, or None if fewer than K_MIN distinct contributors."""
        key = (category, jurisdiction, sector, fiscal_year)
        points = self._pool.get(key, [])
        # k-anonymity: one published value per distinct node_id.
        first_value_by_node: dict[str, float] = {}
        for point in points:
            first_value_by_node.setdefault(point.node_id, point.value)
        distinct = len(first_value_by_node)
        if distinct < K_MIN:
            return None
        values = sorted(first_value_by_node.values())
        n = len(values)
        return AggregateStats(
            count=n,
            sample_count=len(points),
            distinct_contributor_count=distinct,
            mean=statistics.mean(values),
            median=statistics.median(values),
            p25=_percentile(values, 25),
            p75=_percentile(values, 75),
            std=statistics.stdev(values) if n > 1 else 0.0,
            min_val=values[0],
            max_val=values[-1],
        )

    def available_keys(self) -> list[tuple]:
        """Return keys that have >= K_MIN distinct contributors."""
        result = []
        for key, points in self._pool.items():
            if len({p.node_id for p in points}) >= K_MIN:
                result.append(key)
        return result


def _percentile(sorted_vals: list[float], pct: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = (len(sorted_vals) - 1) * pct / 100
    lo, hi = int(idx), min(int(idx) + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (idx - lo)
