"""Legal entity with multi-jurisdiction support."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__all__ = ["EntityType", "Entity"]


class EntityType(Enum):
    BV = "bv"
    HOLDING = "holding"
    EENMANSZAAK = "eenmanszaak"  # ZZP
    VOF = "vof"
    LTD = "ltd"
    LLC = "llc"
    CORP = "corp"
    GMBH = "gmbh"
    SARL = "sarl"
    SA = "sa"
    PTY = "pty"        # Australian
    INDIVIDUAL = "individual"

    # Convenience set for corporate checks
    _CORPORATE = frozenset()  # populated after class body


_CORPORATE_TYPES = frozenset({
    "bv", "holding", "ltd", "llc", "corp", "gmbh", "sarl", "sa", "pty", "vof",
})


@dataclass
class Entity:
    id: str
    legal_name: str
    entity_type: EntityType
    jurisdiction: str               # ISO 3166-1 alpha-2
    registration_number: str = ""   # KvK / Companies House / EIN / SIREN
    vat_number: str = ""
    fiscal_year_start_month: int = 1
    parent_entity_id: str = ""      # for holding structures
    subsidiaries: list[str] = field(default_factory=list)

    # ── Predicates ────────────────────────────────────────────────────

    def is_corporate(self) -> bool:
        return self.entity_type.value in _CORPORATE_TYPES

    def is_holding(self) -> bool:
        return self.entity_type == EntityType.HOLDING or bool(self.subsidiaries)

    # ── Serialisation ─────────────────────────────────────────────────

    def to_record(self) -> dict:
        return {
            "id": self.id,
            "legal_name": self.legal_name,
            "entity_type": self.entity_type.value,
            "jurisdiction": self.jurisdiction,
            "registration_number": self.registration_number,
            "vat_number": self.vat_number,
            "fiscal_year_start_month": self.fiscal_year_start_month,
            "parent_entity_id": self.parent_entity_id,
            "subsidiaries": list(self.subsidiaries),
        }

    @classmethod
    def from_record(cls, d: dict) -> "Entity":
        return cls(
            id=d["id"],
            legal_name=d["legal_name"],
            entity_type=EntityType(d["entity_type"]),
            jurisdiction=d["jurisdiction"],
            registration_number=d.get("registration_number", ""),
            vat_number=d.get("vat_number", ""),
            fiscal_year_start_month=d.get("fiscal_year_start_month", 1),
            parent_entity_id=d.get("parent_entity_id", ""),
            subsidiaries=d.get("subsidiaries", []),
        )
