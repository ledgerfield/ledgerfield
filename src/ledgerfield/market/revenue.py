"""Revenue distribution — pay contributors from data sale proceeds."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

__all__ = ["ContributorShare", "RevenueDistributor"]


@dataclass(frozen=True)
class ContributorShare:
    node_id: str
    tokens_earned: float
    share_pct: float


class RevenueDistributor:
    """Split sale proceeds across data contributors.

    Default strategy: equal split.  Pass a custom weight_fn to weight by
    contribution count, data quality score, etc.
    """

    def __init__(
        self,
        platform_fee_pct: float = 0.10,
        weight_fn: Callable[[str, int], float] | None = None,
    ) -> None:
        self.platform_fee_pct = platform_fee_pct
        self._weight_fn = weight_fn or (lambda node_id, count: 1.0)
        # accumulated earnings per node
        self._earnings: dict[str, float] = {}

    def distribute(
        self,
        sale_amount: float,
        contributors: dict[str, int],  # node_id → number of data points contributed
    ) -> list[ContributorShare]:
        """
        Distribute sale_amount (after platform fee) among contributors.
        Returns list of ContributorShare, one per contributor.
        """
        net = sale_amount * (1.0 - self.platform_fee_pct)
        weights = {nid: self._weight_fn(nid, cnt) for nid, cnt in contributors.items()}
        total_w = sum(weights.values())
        shares = []
        for nid, w in weights.items():
            pct = w / total_w if total_w > 0 else 0.0
            earned = net * pct
            self._earnings[nid] = self._earnings.get(nid, 0.0) + earned
            shares.append(ContributorShare(nid, round(earned, 6), round(pct * 100, 2)))
        return sorted(shares, key=lambda s: -s.tokens_earned)

    def total_earned(self, node_id: str) -> float:
        return self._earnings.get(node_id, 0.0)

    def leaderboard(self, top_n: int = 10) -> list[tuple[str, float]]:
        """Top N earners by accumulated tokens."""
        return sorted(self._earnings.items(), key=lambda x: -x[1])[:top_n]
