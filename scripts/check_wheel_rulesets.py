from __future__ import annotations

import sys
import zipfile
from pathlib import Path


MINIMUM_RULESETS = {
    "AU_2025.json",
    "CA_2025.json",
    "CN_2025.json",
    "JP_2025.json",
    "SG_2025.json",
}


def expected_rulesets(repo_root: Path) -> set[str]:
    rulesets_dir = repo_root / "rulesets"
    repo_rulesets = {path.name for path in rulesets_dir.glob("*.json")}
    return repo_rulesets | MINIMUM_RULESETS


def verify_wheel(wheel_path: Path, expected: set[str]) -> None:
    with zipfile.ZipFile(wheel_path) as wheel:
        names = set(wheel.namelist())

    missing = sorted(
        f"ledgerfield/rulesets/{name}"
        for name in expected
        if f"ledgerfield/rulesets/{name}" not in names
    )
    if missing:
        print(f"{wheel_path}: missing packaged rulesets:", file=sys.stderr)
        for name in missing:
            print(f"  - {name}", file=sys.stderr)
        raise SystemExit(1)

    packaged = sorted(
        name
        for name in names
        if name.startswith("ledgerfield/rulesets/") and name.endswith(".json")
    )
    print(f"{wheel_path}: verified {len(packaged)} packaged rulesets")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: check_wheel_rulesets.py dist/*.whl", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    expected = expected_rulesets(repo_root)
    for arg in argv[1:]:
        verify_wheel(Path(arg), expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
