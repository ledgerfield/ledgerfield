"""DataMarket — list, discover and purchase aggregate data packages."""
from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from typing import Optional

from .dataset import DataPackage
from .consent import DataCategory

__all__ = ["Listing", "PurchaseReceipt", "DataMarket"]


@dataclass
class Listing:
    package: DataPackage
    seller_node_id: str
    listed_at: float = field(default_factory=time.time)
    active: bool = True

    def to_dict(self) -> dict:
        return {
            "package_id": self.package.package_id,
            "seller_node_id": self.seller_node_id,
            "listed_at": self.listed_at,
            "active": self.active,
            "price_tokens": self.package.price_tokens,
            "category": self.package.category.value,
            "jurisdiction": self.package.jurisdiction,
            "sector": self.package.sector,
            "fiscal_year": self.package.fiscal_year,
            "contributor_count": self.package.contributor_count,
            "description": self.package.description,
        }


@dataclass
class PurchaseReceipt:
    receipt_id: str
    package_id: str
    buyer_node_id: str
    seller_node_id: str
    price_tokens: float
    purchased_at: float

    def to_dict(self) -> dict:
        return {
            "receipt_id": self.receipt_id,
            "package_id": self.package_id,
            "buyer_node_id": self.buyer_node_id,
            "seller_node_id": self.seller_node_id,
            "price_tokens": self.price_tokens,
            "purchased_at": self.purchased_at,
        }


class DataMarket:
    """Local market node: list packages, handle discovery and purchases."""

    def __init__(self, node_id: str) -> None:
        self.node_id = node_id
        self._listings: dict[str, Listing] = {}          # package_id → Listing
        self._receipts: list[PurchaseReceipt] = []
        # simple ledger: how many tokens each node has earned/spent
        self._balances: dict[str, float] = {}

    # ── listing ──────────────────────────────────────────────────────────────

    def list_package(self, package: DataPackage) -> Listing:
        listing = Listing(package, self.node_id)
        self._listings[package.package_id] = listing
        return listing

    def delist(self, package_id: str) -> None:
        if package_id in self._listings:
            self._listings[package_id].active = False

    # ── discovery ────────────────────────────────────────────────────────────

    def search(
        self,
        category: Optional[DataCategory] = None,
        jurisdiction: Optional[str] = None,
        sector: Optional[str] = None,
        fiscal_year: Optional[int] = None,
        max_price: Optional[float] = None,
    ) -> list[Listing]:
        results = []
        for listing in self._listings.values():
            if not listing.active:
                continue
            p = listing.package
            if category and p.category != category:
                continue
            if jurisdiction and p.jurisdiction != jurisdiction:
                continue
            if sector and p.sector != sector:
                continue
            if fiscal_year and p.fiscal_year != fiscal_year:
                continue
            if max_price is not None and p.price_tokens > max_price:
                continue
            results.append(listing)
        return sorted(results, key=lambda l: l.package.price_tokens)

    # ── purchase ─────────────────────────────────────────────────────────────

    def purchase(self, package_id: str, buyer_node_id: str) -> Optional[PurchaseReceipt]:
        """Deduct tokens from buyer, credit seller, return receipt + package access."""
        listing = self._listings.get(package_id)
        if not listing or not listing.active:
            return None
        price = listing.package.price_tokens
        # check buyer balance (default 0 → allow negative for simplicity, settle later)
        receipt_id = "rcpt:" + hashlib.sha256(
            f"{package_id}{buyer_node_id}{time.time()}".encode()
        ).hexdigest()[:16]
        self._balances[buyer_node_id] = self._balances.get(buyer_node_id, 0.0) - price
        self._balances[listing.seller_node_id] = self._balances.get(listing.seller_node_id, 0.0) + price
        receipt = PurchaseReceipt(
            receipt_id=receipt_id,
            package_id=package_id,
            buyer_node_id=buyer_node_id,
            seller_node_id=listing.seller_node_id,
            price_tokens=price,
            purchased_at=time.time(),
        )
        self._receipts.append(receipt)
        return receipt

    # ── balances + audit ──────────────────────────────────────────────────────

    def balance(self, node_id: str) -> float:
        return self._balances.get(node_id, 0.0)

    def receipts(self, node_id: Optional[str] = None) -> list[PurchaseReceipt]:
        if node_id is None:
            return list(self._receipts)
        return [r for r in self._receipts if r.buyer_node_id == node_id or r.seller_node_id == node_id]

    def active_listings(self) -> list[Listing]:
        return [l for l in self._listings.values() if l.active]
