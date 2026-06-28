"""CID-addressed DataPackage — the unit sold on the market."""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Optional

from .consent import DataCategory
from .aggregator import AggregateStats, Aggregator

__all__ = ["DataPackage", "build_package"]


@dataclass
class DataPackage:
    package_id: str                # CID = sha256 of canonical payload
    category: DataCategory
    jurisdiction: str
    sector: str
    fiscal_year: int
    stats: AggregateStats
    contributor_count: int
    created_at: float
    price_tokens: float            # ledgerfield-token price
    description: str = ""

    def to_dict(self) -> dict:
        return {
            "package_id": self.package_id,
            "category": self.category.value,
            "jurisdiction": self.jurisdiction,
            "sector": self.sector,
            "fiscal_year": self.fiscal_year,
            "stats": self.stats.to_dict(),
            "contributor_count": self.contributor_count,
            "created_at": self.created_at,
            "price_tokens": self.price_tokens,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "DataPackage":
        return cls(
            package_id=d["package_id"],
            category=DataCategory(d["category"]),
            jurisdiction=d["jurisdiction"],
            sector=d["sector"],
            fiscal_year=d["fiscal_year"],
            stats=AggregateStats(**{k: v for k, v in d["stats"].items()
                                    if k not in ("min", "max")}
                                 | {"min_val": d["stats"]["min"], "max_val": d["stats"]["max"]}),
            contributor_count=d["contributor_count"],
            created_at=d["created_at"],
            price_tokens=d["price_tokens"],
            description=d.get("description", ""),
        )


def _cid(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(canonical.encode()).hexdigest()


def build_package(
    aggregator: Aggregator,
    category: DataCategory,
    jurisdiction: str,
    sector: str,
    fiscal_year: int,
    price_tokens: float = 10.0,
    description: str = "",
) -> Optional["DataPackage"]:
    """Build a DataPackage from aggregated data.  Returns None if k-anonymity fails."""
    stats = aggregator.aggregate(category, jurisdiction, sector, fiscal_year)
    if stats is None:
        return None
    payload = {
        "category": category.value,
        "jurisdiction": jurisdiction,
        "sector": sector,
        "fiscal_year": fiscal_year,
        "stats": stats.to_dict(),
    }
    return DataPackage(
        package_id=_cid(payload),
        category=category,
        jurisdiction=jurisdiction,
        sector=sector,
        fiscal_year=fiscal_year,
        stats=stats,
        contributor_count=stats.count,
        created_at=time.time(),
        price_tokens=price_tokens,
        description=description,
    )
