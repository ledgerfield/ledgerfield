"""Schema modules should not write generated files during import."""

from __future__ import annotations

import builtins
import importlib
import json
import os
from pathlib import Path
import sys

import pytest

SCHEMA_MODULES = (
    "ledgerfield.schemas.CN.cas",
    "ledgerfield.schemas.UK.frs102",
    "ledgerfield.schemas.US.us_gaap",
)


def _is_schema_json(path: object) -> bool:
    return str(path).endswith(("cas_schema.json", "frs102_schema.json", "us_gaap_schema.json"))


@pytest.mark.parametrize("module_name", SCHEMA_MODULES)
def test_schema_modules_do_not_write_json_on_import(monkeypatch, module_name):
    """Importing schema modules must not mutate the source tree."""

    original_exists = Path.exists
    original_os_exists = os.path.exists
    original_open = builtins.open
    original_write_text = Path.write_text

    def guarded_path_exists(path: Path) -> bool:
        if _is_schema_json(path):
            return False
        return original_exists(path)

    def guarded_os_exists(path: str | os.PathLike[str]) -> bool:
        if _is_schema_json(path):
            return False
        return original_os_exists(path)

    def guarded_open(file, mode="r", *args, **kwargs):
        if _is_schema_json(file) and any(flag in mode for flag in ("w", "a", "+")):
            raise AssertionError(f"schema import attempted to write {file}")
        return original_open(file, mode, *args, **kwargs)

    def guarded_write_text(path: Path, *args, **kwargs):
        if _is_schema_json(path):
            raise AssertionError(f"schema import attempted to write {path}")
        return original_write_text(path, *args, **kwargs)

    monkeypatch.setattr(Path, "exists", guarded_path_exists)
    monkeypatch.setattr(os.path, "exists", guarded_os_exists)
    monkeypatch.setattr(builtins, "open", guarded_open)
    monkeypatch.setattr(Path, "write_text", guarded_write_text)
    sys.modules.pop(module_name, None)

    module = importlib.import_module(module_name)

    assert module is not None


def test_cn_schema_can_be_exported_explicitly(tmp_path):
    from ledgerfield.schemas.CN.cas import write_json_schema

    out = write_json_schema(tmp_path / "cas_schema.json")
    payload = json.loads(out.read_text(encoding="utf-8"))

    assert payload["jurisdiction"] == "CN"
    assert payload["accounts"]
