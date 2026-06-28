"""ledgerfield.market — aggregate data marketplace.

Privacy model (CRITICAL):
- Raw PII (BSN, IBAN, names, exact salaries) NEVER leaves the vault
- Only k-anonymised aggregates (k >= K_MIN contributors) are published
- Every category requires explicit opt-in via ConsentManager
- Each sale generates a local audit event
"""
from .consent import DataCategory, ConsentManager, ConsentRecord
from .aggregator import AggregateStats, Aggregator, K_MIN
from .dataset import DataPackage, build_package
from .market import DataMarket, Listing, PurchaseReceipt
from .revenue import RevenueDistributor, ContributorShare

__all__ = [
    "DataCategory", "ConsentManager", "ConsentRecord",
    "AggregateStats", "Aggregator", "K_MIN",
    "DataPackage", "build_package",
    "DataMarket", "Listing", "PurchaseReceipt",
    "RevenueDistributor", "ContributorShare",
]
