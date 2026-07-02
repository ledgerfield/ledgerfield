"""Tax/ruleset provenance metadata guards."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
JSON_PATHS = [
    *sorted((REPO_ROOT / "rulesets").glob("*.json")),
    *sorted((REPO_ROOT / "src/ledgerfield/rulesets").glob("*.json")),
    *sorted((REPO_ROOT / "src/ledgerfield/tax").glob("*/params.json")),
]


def test_every_shipped_tax_json_has_source_metadata():
    assert JSON_PATHS, "expected shipped tax/ruleset JSON files"

    for path in JSON_PATHS:
        payload = json.loads(path.read_text(encoding="utf-8"))
        metadata = payload.get("metadata")
        assert isinstance(metadata, dict), path
        assert metadata["source_status"] == "official_sources_referenced_estimate", path
        assert metadata["currency"], path
        assert metadata["rate_threshold_assumptions"], path
        assert metadata["limitations"], path

        reviewed = date.fromisoformat(metadata["last_reviewed"])
        assert reviewed.year >= 2026, path

        effective = metadata["effective_date_range"]
        assert date.fromisoformat(effective["start"]) <= date.fromisoformat(effective["end"]), path
        assert effective["basis"], path

        sources = metadata["official_sources"]
        assert sources, path
        for source in sources:
            assert source["name"], path
            assert source["url"].startswith("https://"), path
