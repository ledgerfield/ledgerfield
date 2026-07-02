"""Tests for ledgerfield.market — aggregate data marketplace."""
import pytest
from ledgerfield.market import (
    DataCategory, ConsentManager,
    Aggregator, K_MIN, AggregateStats,
    DataMarket, build_package,
    RevenueDistributor,
)


# ── consent ──────────────────────────────────────────────────────────────────

def test_consent_grant_and_query():
    cm = ConsentManager()
    cm.grant(DataCategory.SALARY_BENCHMARKS, "NL")
    assert cm.is_consented(DataCategory.SALARY_BENCHMARKS, "NL")

def test_consent_wildcard_covers_any_jurisdiction():
    cm = ConsentManager()
    cm.grant(DataCategory.COST_RATIOS)          # defaults to "*"
    assert cm.is_consented(DataCategory.COST_RATIOS, "DE")
    assert cm.is_consented(DataCategory.COST_RATIOS, "US")

def test_consent_revoke():
    cm = ConsentManager()
    cm.grant(DataCategory.MARGIN_BENCHMARKS)
    cm.revoke(DataCategory.MARGIN_BENCHMARKS)
    assert not cm.is_consented(DataCategory.MARGIN_BENCHMARKS, "NL")

def test_consent_roundtrip():
    cm = ConsentManager()
    cm.grant(DataCategory.SALARY_BENCHMARKS, "JP")
    d = cm.to_dict()
    cm2 = ConsentManager.from_dict(d)
    assert cm2.is_consented(DataCategory.SALARY_BENCHMARKS, "JP")


# ── aggregator k-anonymity ────────────────────────────────────────────────────

def _fill(agg, n, category=DataCategory.SALARY_BENCHMARKS, jur="NL", sector="tech", year=2025):
    for i in range(n):
        agg.contribute(f"node_{i}", category, jur, sector, year, 50_000 + i * 1000)

def test_aggregator_below_k_returns_none():
    agg = Aggregator()
    _fill(agg, K_MIN - 1)
    assert agg.aggregate(DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025) is None

def test_aggregator_at_k_returns_stats():
    agg = Aggregator()
    _fill(agg, K_MIN)
    stats = agg.aggregate(DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025)
    assert isinstance(stats, AggregateStats)
    assert stats.count == K_MIN

def test_aggregator_stats_values():
    agg = Aggregator()
    # 5 nodes each contribute 10 values → distinct = 5 = K_MIN
    for i in range(5):
        agg.contribute(f"n{i}", DataCategory.SALARY_BENCHMARKS, "NL", "finance", 2025, float(10 + i * 10))
    stats = agg.aggregate(DataCategory.SALARY_BENCHMARKS, "NL", "finance", 2025)
    assert stats is not None
    assert stats.mean == pytest.approx(30.0)
    assert stats.median == 30.0
    assert stats.min_val == 10.0
    assert stats.max_val == 50.0

def test_aggregator_duplicate_node_counted_once_for_k():
    agg = Aggregator()
    # same node contributes 10 times — still only 1 distinct node → below K_MIN
    for _ in range(10):
        agg.contribute("same_node", DataCategory.SALARY_BENCHMARKS, "NL", "legal", 2025, 60_000)
    assert agg.aggregate(DataCategory.SALARY_BENCHMARKS, "NL", "legal", 2025) is None


# ── dataset / build_package ───────────────────────────────────────────────────

def test_build_package_returns_none_below_k():
    agg = Aggregator()
    _fill(agg, 3)
    pkg = build_package(agg, DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025)
    assert pkg is None

def test_build_package_has_cid():
    agg = Aggregator()
    _fill(agg, K_MIN)
    pkg = build_package(agg, DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025)
    assert pkg is not None
    assert pkg.package_id.startswith("sha256:")

def test_build_package_cid_deterministic():
    agg = Aggregator()
    _fill(agg, K_MIN)
    p1 = build_package(agg, DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025)
    p2 = build_package(agg, DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025)
    assert p1.package_id == p2.package_id

def test_build_package_roundtrip():
    agg = Aggregator()
    _fill(agg, K_MIN)
    pkg = build_package(agg, DataCategory.SALARY_BENCHMARKS, "NL", "tech", 2025)
    from ledgerfield.market.dataset import DataPackage
    restored = DataPackage.from_dict(pkg.to_dict())
    assert restored.package_id == pkg.package_id
    assert restored.stats.mean == pytest.approx(pkg.stats.mean)


# ── market ────────────────────────────────────────────────────────────────────

def _make_pkg(sector="tech"):
    agg = Aggregator()
    _fill(agg, K_MIN, sector=sector)
    return build_package(agg, DataCategory.SALARY_BENCHMARKS, "NL", sector, 2025, price_tokens=20.0)

def test_market_list_and_search():
    market = DataMarket("seller-1")
    market.list_package(_make_pkg())
    results = market.search(jurisdiction="NL")
    assert len(results) == 1

def test_market_search_filters_category():
    market = DataMarket("seller-1")
    market.list_package(_make_pkg())
    results = market.search(category=DataCategory.COST_RATIOS)
    assert len(results) == 0

def test_market_purchase_returns_receipt():
    market = DataMarket("seller-1")
    pkg = _make_pkg()
    market.list_package(pkg)
    market.credit_balance("buyer-1", 20.0)
    receipt = market.purchase(pkg.package_id, "buyer-1")
    assert receipt is not None
    assert receipt.price_tokens == 20.0

def test_market_purchase_updates_balances():
    market = DataMarket("seller-1")
    pkg = _make_pkg()
    market.list_package(pkg)
    market.credit_balance("buyer-1", 20.0)
    market.purchase(pkg.package_id, "buyer-1")
    assert market.balance("buyer-1") == pytest.approx(0.0)
    assert market.balance("seller-1") == pytest.approx(20.0)

def test_market_purchase_requires_prepaid_balance():
    market = DataMarket("seller-1")
    pkg = _make_pkg()
    market.list_package(pkg)
    receipt = market.purchase(pkg.package_id, "buyer-1")
    assert receipt is None
    assert market.balance("buyer-1") == pytest.approx(0.0)
    assert market.balance("seller-1") == pytest.approx(0.0)
    assert market.receipts() == []

def test_market_purchase_rejects_partial_balance_without_mutation():
    market = DataMarket("seller-1")
    pkg = _make_pkg()
    market.list_package(pkg)
    market.credit_balance("buyer-1", 19.99)
    receipt = market.purchase(pkg.package_id, "buyer-1")
    assert receipt is None
    assert market.balance("buyer-1") == pytest.approx(19.99)
    assert market.balance("seller-1") == pytest.approx(0.0)

def test_market_credit_balance_requires_positive_amount():
    market = DataMarket("seller-1")
    with pytest.raises(ValueError, match="credit amount must be positive"):
        market.credit_balance("buyer-1", 0.0)

def test_market_delist_hides_from_search():
    market = DataMarket("seller-1")
    pkg = _make_pkg()
    market.list_package(pkg)
    market.delist(pkg.package_id)
    assert market.search() == []

def test_market_purchase_unknown_package_returns_none():
    market = DataMarket("seller-1")
    assert market.purchase("sha256:nonexistent", "buyer-1") is None


# ── revenue distributor ───────────────────────────────────────────────────────

def test_revenue_equal_split():
    rd = RevenueDistributor(platform_fee_pct=0.0)
    contributors = {"n1": 3, "n2": 3, "n3": 3}
    shares = rd.distribute(90.0, contributors)
    for s in shares:
        assert s.tokens_earned == pytest.approx(30.0)

def test_revenue_platform_fee_deducted():
    rd = RevenueDistributor(platform_fee_pct=0.10)
    shares = rd.distribute(100.0, {"n1": 1, "n2": 1})
    total = sum(s.tokens_earned for s in shares)
    assert total == pytest.approx(90.0)

def test_revenue_weighted_by_count():
    rd = RevenueDistributor(platform_fee_pct=0.0, weight_fn=lambda nid, cnt: float(cnt))
    shares = rd.distribute(100.0, {"n1": 3, "n2": 1})
    by_node = {s.node_id: s.tokens_earned for s in shares}
    assert by_node["n1"] == pytest.approx(75.0)
    assert by_node["n2"] == pytest.approx(25.0)

def test_revenue_leaderboard():
    rd = RevenueDistributor(platform_fee_pct=0.0)
    rd.distribute(90.0, {"n1": 1, "n2": 1, "n3": 1})
    lb = rd.leaderboard(top_n=2)
    assert len(lb) == 2
    assert lb[0][1] == pytest.approx(30.0)
