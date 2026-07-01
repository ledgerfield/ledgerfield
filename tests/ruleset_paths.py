"""Helpers for loading repository rulesets in tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_ruleset(jurisdiction: str, year: int = 2025) -> dict[str, Any]:
    """Load a tax ruleset from this checkout, independent of clone location."""

    path = REPO_ROOT / "rulesets" / f"{jurisdiction}_{year}.json"
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)
