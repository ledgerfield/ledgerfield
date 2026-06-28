"""LedgerField P2P node — gossip tax rulesets via knitweb CIDs.

Privacy model:
- Tax rulesets (public parameters) → unencrypted CID records, gossipable
- Financial data (PII) → vault-encrypted, never auto-gossiped
- Sharing → explicit opt-in per record via LedgerVault.share_record()
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from typing import Any

__all__ = ["RulesetRegistry", "LedgerNode"]


def _canonical_json(obj: Any) -> bytes:
    """Deterministic JSON serialization for CID computation."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()


def _compute_cid(ruleset: dict) -> str:
    """SHA256 of canonical JSON, hex-encoded."""
    return hashlib.sha256(_canonical_json(ruleset)).hexdigest()


class RulesetRegistry:
    """Local cache of tax rulesets, addressable by CID."""

    def __init__(self, rulesets_dir: str) -> None:
        self._dir = rulesets_dir
        # {(jurisdiction, year): ruleset_dict}
        self._by_jy: dict[tuple[str, int], dict] = {}
        # {cid: ruleset_dict}
        self._by_cid: dict[str, dict] = {}

    def load_all(self) -> None:
        """Scan rulesets_dir for *.json files and load them."""
        if not os.path.isdir(self._dir):
            return
        for fname in os.listdir(self._dir):
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(self._dir, fname)
            try:
                with open(fpath, "r") as f:
                    ruleset = json.load(f)
                jur = ruleset.get("jurisdiction")
                year = ruleset.get("year")
                if jur and year:
                    cid = _compute_cid(ruleset)
                    self._by_jy[(str(jur), int(year))] = ruleset
                    self._by_cid[cid] = ruleset
            except (json.JSONDecodeError, KeyError, TypeError):
                continue

    def _register(self, ruleset: dict) -> str:
        jur = str(ruleset["jurisdiction"])
        year = int(ruleset["year"])
        cid = _compute_cid(ruleset)
        self._by_jy[(jur, year)] = ruleset
        self._by_cid[cid] = ruleset
        return cid

    def get(self, jurisdiction: str, year: int) -> dict | None:
        return self._by_jy.get((jurisdiction, int(year)))

    def get_by_cid(self, cid: str) -> dict | None:
        return self._by_cid.get(cid)

    def cid_for(self, jurisdiction: str, year: int) -> str | None:
        """SHA256 of canonical JSON for the given ruleset, or None if not found."""
        rs = self.get(jurisdiction, int(year))
        if rs is None:
            return None
        return _compute_cid(rs)

    def available_rulesets(self) -> list[dict]:
        """Return [{jurisdiction, year, cid}] for all loaded rulesets."""
        result = []
        for (jur, year), rs in self._by_jy.items():
            result.append({"jurisdiction": jur, "year": year, "cid": _compute_cid(rs)})
        return result

    def verify_cid(self, ruleset: dict, claimed_cid: str) -> bool:
        return _compute_cid(ruleset) == claimed_cid


class LedgerNode:
    """A LedgerField P2P node: manages rulesets + entities + vault."""

    def __init__(self, data_dir: str, password: str) -> None:
        self._data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

        vault_dir = os.path.join(data_dir, "vault")
        os.makedirs(vault_dir, exist_ok=True)

        rulesets_dir = os.path.join(data_dir, "rulesets")
        os.makedirs(rulesets_dir, exist_ok=True)

        # Lazy import to allow vault.py to stand alone
        from ledgerfield.p2p.vault import LedgerVault

        self._vault = LedgerVault(vault_dir, password)
        self._registry = RulesetRegistry(rulesets_dir)
        self._registry.load_all()

        self._rulesets_dir = rulesets_dir
        self._node_id: str | None = None
        self._created_at: float = self._load_or_create_timestamp()

    # ------------------------------------------------------------------
    # Timestamp persistence for stable node_id
    # ------------------------------------------------------------------

    def _load_or_create_timestamp(self) -> float:
        ts_file = os.path.join(self._data_dir, ".node_ts")
        if os.path.isfile(ts_file):
            with open(ts_file, "r") as f:
                return float(f.read().strip())
        ts = time.time()
        with open(ts_file, "w") as f:
            f.write(str(ts))
        return ts

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def vault(self) -> "LedgerVault":
        return self._vault

    @property
    def rulesets(self) -> RulesetRegistry:
        return self._registry

    # ------------------------------------------------------------------
    # Node identity
    # ------------------------------------------------------------------

    def node_id(self) -> str:
        """SHA256 of (data_dir + creation_timestamp) — not PII."""
        if self._node_id is None:
            raw = f"{self._data_dir}:{self._created_at}"
            self._node_id = hashlib.sha256(raw.encode()).hexdigest()
        return self._node_id

    # ------------------------------------------------------------------
    # Ruleset sync
    # ------------------------------------------------------------------

    def sync_ruleset(self, jurisdiction: str, year: int, peer_data: dict) -> bool:
        """Accept a peer ruleset only after CID verification.

        peer_data must be {cid, ruleset} as returned by publish_ruleset().
        Returns True if accepted, False if CID mismatch or missing fields.
        """
        try:
            claimed_cid = peer_data["cid"]
            ruleset = peer_data["ruleset"]
        except (KeyError, TypeError):
            return False

        if not self._registry.verify_cid(ruleset, claimed_cid):
            return False

        # Persist to disk
        fname = f"{jurisdiction}_{year}.json"
        fpath = os.path.join(self._rulesets_dir, fname)
        with open(fpath, "w") as f:
            json.dump(ruleset, f, indent=2, ensure_ascii=False)

        self._registry._register(ruleset)
        return True

    def publish_ruleset(self, jurisdiction: str, year: int) -> dict:
        """Return {cid, ruleset} for gossiping to peers.

        Only public tax parameters — no PII.
        Raises KeyError if ruleset not found.
        """
        rs = self._registry.get(jurisdiction, int(year))
        if rs is None:
            raise KeyError(f"Ruleset not found: {jurisdiction}/{year}")
        cid = self._registry.cid_for(jurisdiction, int(year))
        return {"cid": cid, "ruleset": rs}
