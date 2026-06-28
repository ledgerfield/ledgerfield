"""LedgerField encrypted local vault — stdlib only.

Encryption scheme:
  PBKDF2-HMAC-SHA256 key derivation (100_000 iterations, 32-byte key)
  XOR stream cipher seeded from SHA256(key || nonce) blocks
  HMAC-SHA256 over (nonce || ciphertext) for authentication

Each entry in the JSON store: {salt_b64, nonce_b64, hmac_b64, data_b64}
"""
from __future__ import annotations

import base64
import hashlib
import hmac as _hmac
import json
import os
import threading
from typing import Any

__all__ = ["LedgerVault"]

_PBKDF2_ITERS = 100_000
_KEY_LEN = 32  # bytes


def _derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, _PBKDF2_ITERS, dklen=_KEY_LEN)


def _keystream(key: bytes, nonce: bytes, length: int) -> bytes:
    """Generate a keystream of `length` bytes via SHA256(key||nonce||counter) blocks."""
    stream = bytearray()
    counter = 0
    while len(stream) < length:
        block = hashlib.sha256(key + nonce + counter.to_bytes(4, "big")).digest()
        stream.extend(block)
        counter += 1
    return bytes(stream[:length])


def _encrypt(key: bytes, plaintext: bytes) -> tuple[bytes, bytes, bytes]:
    """Return (nonce, ciphertext, hmac_tag)."""
    nonce = os.urandom(16)
    ks = _keystream(key, nonce, len(plaintext))
    ciphertext = bytes(a ^ b for a, b in zip(plaintext, ks))
    tag = _hmac.new(key, nonce + ciphertext, hashlib.sha256).digest()
    return nonce, ciphertext, tag


def _decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes) -> bytes:
    """Verify HMAC then decrypt; raises ValueError on tamper."""
    expected = _hmac.new(key, nonce + ciphertext, hashlib.sha256).digest()
    if not _hmac.compare_digest(expected, tag):
        raise ValueError("HMAC verification failed — data tampered or wrong password")
    ks = _keystream(key, nonce, len(ciphertext))
    return bytes(a ^ b for a, b in zip(ciphertext, ks))


class LedgerVault:
    """Privacy vault: all PII encrypted locally. Opt-in P2P sharing only."""

    def __init__(self, store_path: str, password: str) -> None:
        self._store_path = store_path
        self._store_file = os.path.join(store_path, "vault.json")
        self._password = password
        self._locked = False
        self._lock = threading.Lock()
        self._store: dict[str, dict] = {}
        # Per-key derived-key cache: {key: (salt, derived_key)}
        self._key_cache: dict[str, tuple[bytes, bytes]] = {}
        self._load_store()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _load_store(self) -> None:
        if os.path.isfile(self._store_file):
            with open(self._store_file, "r") as f:
                self._store = json.load(f)
        else:
            self._store = {}

    def _save_store(self) -> None:
        with open(self._store_file, "w") as f:
            json.dump(self._store, f, indent=2)

    def _get_key(self, vault_key: str) -> tuple[bytes, bytes]:
        """Return (salt, derived_key) for a vault key; creates new salt on first use."""
        if vault_key in self._key_cache:
            return self._key_cache[vault_key]
        if vault_key in self._store:
            salt = base64.b64decode(self._store[vault_key]["salt_b64"])
        else:
            salt = os.urandom(16)
        dk = _derive_key(self._password, salt)
        self._key_cache[vault_key] = (salt, dk)
        return salt, dk

    def _check_unlocked(self) -> None:
        if self._locked:
            raise RuntimeError("Vault is locked; call unlock() first")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def store_entity(self, entity_id: str, record: dict) -> None:
        self._check_unlocked()
        key = f"entity:{entity_id}"
        with self._lock:
            salt, dk = self._get_key(key)
            plaintext = json.dumps(record, ensure_ascii=False).encode()
            nonce, ct, tag = _encrypt(dk, plaintext)
            self._store[key] = {
                "salt_b64": base64.b64encode(salt).decode(),
                "nonce_b64": base64.b64encode(nonce).decode(),
                "hmac_b64": base64.b64encode(tag).decode(),
                "data_b64": base64.b64encode(ct).decode(),
            }
            self._save_store()

    def load_entity(self, entity_id: str) -> dict | None:
        self._check_unlocked()
        key = f"entity:{entity_id}"
        return self._load_key(key)

    def store_payslip(self, employee_id: str, period: str, payslip: dict) -> None:
        self._check_unlocked()
        key = f"payslip:{employee_id}:{period}"
        with self._lock:
            salt, dk = self._get_key(key)
            plaintext = json.dumps(payslip, ensure_ascii=False).encode()
            nonce, ct, tag = _encrypt(dk, plaintext)
            self._store[key] = {
                "salt_b64": base64.b64encode(salt).decode(),
                "nonce_b64": base64.b64encode(nonce).decode(),
                "hmac_b64": base64.b64encode(tag).decode(),
                "data_b64": base64.b64encode(ct).decode(),
            }
            self._save_store()

    def load_payslip(self, employee_id: str, period: str) -> dict | None:
        self._check_unlocked()
        key = f"payslip:{employee_id}:{period}"
        return self._load_key(key)

    def store_aangifte(self, entity_id: str, jaar: int, tax_type: str, aangifte: dict) -> None:
        self._check_unlocked()
        key = f"aangifte:{entity_id}:{jaar}:{tax_type}"
        with self._lock:
            salt, dk = self._get_key(key)
            plaintext = json.dumps(aangifte, ensure_ascii=False).encode()
            nonce, ct, tag = _encrypt(dk, plaintext)
            self._store[key] = {
                "salt_b64": base64.b64encode(salt).decode(),
                "nonce_b64": base64.b64encode(nonce).decode(),
                "hmac_b64": base64.b64encode(tag).decode(),
                "data_b64": base64.b64encode(ct).decode(),
            }
            self._save_store()

    def load_aangifte(self, entity_id: str, jaar: int, tax_type: str) -> dict | None:
        self._check_unlocked()
        key = f"aangifte:{entity_id}:{jaar}:{tax_type}"
        return self._load_key(key)

    def _load_key(self, key: str) -> dict | None:
        with self._lock:
            entry = self._store.get(key)
            if entry is None:
                return None
            salt = base64.b64decode(entry["salt_b64"])
            dk = _derive_key(self._password, salt)
            nonce = base64.b64decode(entry["nonce_b64"])
            ct = base64.b64decode(entry["data_b64"])
            tag = base64.b64decode(entry["hmac_b64"])
            plaintext = _decrypt(dk, nonce, ct, tag)
            return json.loads(plaintext.decode())

    def list_keys(self) -> list[str]:
        self._check_unlocked()
        return list(self._store.keys())

    def export_encrypted_backup(self) -> dict:
        """Return entire encrypted store — safe to backup/share without exposing PII."""
        with self._lock:
            return dict(self._store)

    def share_record(self, key: str, confirm_password: str | None = None) -> dict | None:
        """Decrypt + return a single record for explicit P2P sharing.

        Requires re-entry of password as second confirmation step.
        Returns None if key not found or password wrong.
        """
        self._check_unlocked()
        if confirm_password is None or confirm_password != self._password:
            raise PermissionError(
                "share_record requires explicit password re-confirmation (confirm_password=)"
            )
        return self._load_key(key)

    def is_locked(self) -> bool:
        return self._locked

    def lock(self) -> None:
        self._locked = True
        self._key_cache.clear()

    def unlock(self, password: str) -> bool:
        if password == self._password:
            self._locked = False
            return True
        return False
