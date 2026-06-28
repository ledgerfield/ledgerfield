"""Double-entry ledger engine with national CoA schema support."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable

__all__ = ["AccountType", "Account", "JournalEntry", "Ledger", "Period"]


class AccountType(Enum):
    ASSET = "asset"
    LIABILITY = "liability"
    EQUITY = "equity"
    REVENUE = "revenue"
    EXPENSE = "expense"


@dataclass
class Account:
    code: str           # RGS/FRS/GAAP account code
    name: str
    account_type: AccountType
    balance: float = 0.0

    def debit(self, amount: float) -> None:
        if self.account_type in {AccountType.ASSET, AccountType.EXPENSE}:
            self.balance += amount
        else:
            self.balance -= amount

    def credit(self, amount: float) -> None:
        if self.account_type in {AccountType.ASSET, AccountType.EXPENSE}:
            self.balance -= amount
        else:
            self.balance += amount


@dataclass
class JournalEntry:
    id: str
    timestamp: float
    description: str
    debit_account: str
    credit_account: str
    amount: float
    period: str = ""        # YYYY-MM or YYYY
    category: str = ""      # transaction category
    tags: tuple = ()
    document_ref: str = ""  # invoice number, receipt ID, etc.


@dataclass
class Period:
    year: int
    month: int | None = None

    @property
    def label(self) -> str:
        return f"{self.year}-{self.month:02d}" if self.month else str(self.year)


def _account_type_from_rgs(rgs_account) -> AccountType:
    """Map RGSAccount properties to AccountType."""
    if rgs_account.is_asset:
        return AccountType.ASSET
    if rgs_account.is_liability:
        return AccountType.LIABILITY
    if rgs_account.is_revenue:
        return AccountType.REVENUE
    if rgs_account.is_expense:
        return AccountType.EXPENSE
    # Fallback: Passiva that is not explicitly liability → equity
    return AccountType.EQUITY


def _account_type_from_frs(frs_account) -> AccountType:
    """Map FRSAccount properties to AccountType."""
    if frs_account.is_asset:
        return AccountType.ASSET
    if frs_account.is_liability:
        return AccountType.LIABILITY
    if getattr(frs_account, "is_equity", False):
        return AccountType.EQUITY
    if frs_account.is_revenue:
        return AccountType.REVENUE
    if frs_account.is_expense:
        return AccountType.EXPENSE
    return AccountType.EQUITY


def _entry_in_period(entry: JournalEntry, period: Period | None) -> bool:
    if period is None:
        return True
    if period.month is not None:
        label = f"{period.year}-{period.month:02d}"
        return entry.period == label or entry.period.startswith(label)
    return entry.period.startswith(str(period.year))


class Ledger:
    def __init__(self, entity_id: str, jurisdiction: str) -> None:
        self.entity_id = entity_id
        self.jurisdiction = jurisdiction
        self._accounts: dict[str, Account] = {}
        self._entries: list[JournalEntry] = []

    # ── Account management ────────────────────────────────────────────

    def add_account(self, account: Account) -> None:
        self._accounts[account.code] = account

    def load_schema(self, schema: dict) -> None:
        """Load all accounts from a national schema (RGS_NL, FRS_UK, etc.).

        ``schema`` may be a dict of RGSAccount, FRSAccount, or plain Account
        objects keyed by account code.
        """
        for code, src in schema.items():
            if isinstance(src, Account):
                self._accounts[code] = src
                continue
            # Detect schema type by available properties
            if hasattr(src, "is_asset"):
                # RGS / FRS style
                if hasattr(src, "group"):
                    atype = _account_type_from_frs(src)
                else:
                    atype = _account_type_from_rgs(src)
                acc = Account(code=src.code, name=src.name, account_type=atype)
                self._accounts[code] = acc
            else:
                raise TypeError(f"Unknown schema account type: {type(src)}")

    # ── Posting ───────────────────────────────────────────────────────

    def post(self, entry: JournalEntry) -> JournalEntry:
        if entry.debit_account not in self._accounts:
            raise KeyError(f"Debit account not found: {entry.debit_account!r}")
        if entry.credit_account not in self._accounts:
            raise KeyError(f"Credit account not found: {entry.credit_account!r}")
        if entry.amount <= 0:
            raise ValueError(f"Amount must be positive; got {entry.amount}")

        self._accounts[entry.debit_account].debit(entry.amount)
        self._accounts[entry.credit_account].credit(entry.amount)
        self._entries.append(entry)
        return entry

    # ── Reports ───────────────────────────────────────────────────────

    def trial_balance(self) -> dict[str, float]:
        return {code: acc.balance for code, acc in self._accounts.items()}

    def statement(
        self,
        account_code: str,
        since: float = 0,
        until: float = float("inf"),
    ) -> list[JournalEntry]:
        return [
            e for e in self._entries
            if (e.debit_account == account_code or e.credit_account == account_code)
            and since <= e.timestamp <= until
        ]

    def profit_and_loss(self, period: Period | None = None) -> dict:
        revenue = 0.0
        expenses = 0.0
        for code, acc in self._accounts.items():
            if acc.account_type == AccountType.REVENUE:
                # Revenue accounts: credit increases balance (positive = earned)
                revenue += acc.balance if period is None else self._account_period_balance(code, period)
            elif acc.account_type == AccountType.EXPENSE:
                expenses += acc.balance if period is None else self._account_period_balance(code, period)

        gross_profit = revenue - expenses
        return {
            "revenue": revenue,
            "expenses": expenses,
            "gross_profit": gross_profit,
            "net_profit": gross_profit,  # extend for tax deductions later
        }

    def _account_period_balance(self, code: str, period: Period) -> float:
        """Compute net movement on account within period from journal entries."""
        acc = self._accounts[code]
        balance = 0.0
        for e in self._entries:
            if not _entry_in_period(e, period):
                continue
            if e.debit_account == code:
                if acc.account_type in {AccountType.ASSET, AccountType.EXPENSE}:
                    balance += e.amount
                else:
                    balance -= e.amount
            elif e.credit_account == code:
                if acc.account_type in {AccountType.ASSET, AccountType.EXPENSE}:
                    balance -= e.amount
                else:
                    balance += e.amount
        return balance

    def balance_sheet(self) -> dict:
        assets = sum(
            acc.balance for acc in self._accounts.values()
            if acc.account_type == AccountType.ASSET
        )
        liabilities = sum(
            acc.balance for acc in self._accounts.values()
            if acc.account_type == AccountType.LIABILITY
        )
        equity = sum(
            acc.balance for acc in self._accounts.values()
            if acc.account_type == AccountType.EQUITY
        )
        # retained earnings (net profit) flow into equity
        pnl = self.profit_and_loss()
        equity += pnl["net_profit"]
        balanced = abs(assets - (liabilities + equity)) < 1e-6
        return {
            "assets": assets,
            "liabilities": liabilities,
            "equity": equity,
            "balanced": balanced,
        }

    def cashflow(self, period: Period | None = None) -> dict:
        """Simplified cashflow: sum of cash/bank account movements."""
        cash_codes = [
            code for code, acc in self._accounts.items()
            if acc.account_type == AccountType.ASSET
            and any(k in acc.name.lower() for k in ("cash", "bank", "kas", "rekening"))
        ]
        inflows = 0.0
        outflows = 0.0
        for e in self._entries:
            if not _entry_in_period(e, period):
                continue
            if e.debit_account in cash_codes:
                inflows += e.amount
            if e.credit_account in cash_codes:
                outflows += e.amount
        return {
            "inflows": inflows,
            "outflows": outflows,
            "net": inflows - outflows,
        }

    def net_position(self) -> float:
        bs = self.balance_sheet()
        return bs["assets"] - bs["liabilities"]

    # ── Export ────────────────────────────────────────────────────────

    def export_csv(self) -> str:
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow([
            "id", "timestamp", "description",
            "debit_account", "credit_account", "amount",
            "period", "category", "document_ref",
        ])
        for e in self._entries:
            writer.writerow([
                e.id, e.timestamp, e.description,
                e.debit_account, e.credit_account, e.amount,
                e.period, e.category, e.document_ref,
            ])
        return buf.getvalue()

    def export_saf_t(self, company_name: str) -> str:
        """Export minimal SAF-T (Standard Audit File for Tax) XML string."""
        now = time.strftime("%Y-%m-%dT%H:%M:%S")
        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:NO">',
            "  <Header>",
            f"    <CompanyName>{company_name}</CompanyName>",
            f"    <TaxRegistrationNumber>{self.entity_id}</TaxRegistrationNumber>",
            f"    <AuditFileVersion>1.10</AuditFileVersion>",
            f"    <DateCreated>{now}</DateCreated>",
            f"    <Jurisdiction>{self.jurisdiction}</Jurisdiction>",
            "  </Header>",
            "  <MasterFiles>",
            "    <GeneralLedgerAccounts>",
        ]
        for acc in self._accounts.values():
            lines += [
                "      <Account>",
                f"        <AccountID>{acc.code}</AccountID>",
                f"        <AccountDescription>{acc.name}</AccountDescription>",
                f"        <AccountType>{acc.account_type.value}</AccountType>",
                f"        <OpeningDebitBalance>0</OpeningDebitBalance>",
                f"        <ClosingDebitBalance>{acc.balance}</ClosingDebitBalance>",
                "      </Account>",
            ]
        lines += [
            "    </GeneralLedgerAccounts>",
            "  </MasterFiles>",
            "  <GeneralLedgerEntries>",
        ]
        for e in self._entries:
            lines += [
                "    <Journal>",
                f"      <JournalID>{e.id}</JournalID>",
                f"      <Description>{e.description}</Description>",
                "      <Transaction>",
                f"        <TransactionID>{e.id}</TransactionID>",
                f"        <Period>{e.period}</Period>",
                "        <Line>",
                f"          <AccountID>{e.debit_account}</AccountID>",
                f"          <DebitAmount>{e.amount}</DebitAmount>",
                "        </Line>",
                "        <Line>",
                f"          <AccountID>{e.credit_account}</AccountID>",
                f"          <CreditAmount>{e.amount}</CreditAmount>",
                "        </Line>",
                "      </Transaction>",
                "    </Journal>",
            ]
        lines += [
            "  </GeneralLedgerEntries>",
            "</AuditFile>",
        ]
        return "\n".join(lines)
