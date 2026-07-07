"""US federal tax-return helpers for US entities and individuals.

Federal only. State income taxes are levied separately by each state and are
out of scope for this estimator.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import datetime

__all__ = [
    "Form1120Return",
    "Form1040Return",
    "genereer_form_1120",
    "genereer_form_1040",
]

# ---------------------------------------------------------------------------
# Form 1120 - C-corporation (TY2025, IRC Sec. 11)
# Flat 21% federal corporate income tax (TCJA).
# ---------------------------------------------------------------------------
_CORPORATE_TAX_RATE = 0.21

# Corporate Alternative Minimum Tax (CAMT, IRC Sec. 55): 15% minimum tax on
# adjusted financial statement income for "applicable corporations" with
# average annual book income over $1 billion. Out of estimator scope.
_CAMT_RATE = 0.15
_CAMT_BOOK_INCOME_THRESHOLD = 1_000_000_000.0

# ---------------------------------------------------------------------------
# Form 1040 - Individual (TY2025, single filer brackets)
# ---------------------------------------------------------------------------
# (upper_bound, rate) - use math.inf for the top bracket.
_INDIVIDUAL_BRACKETS_SINGLE = [
    (11_925.0, 0.10),
    (48_475.0, 0.12),
    (103_350.0, 0.22),
    (197_300.0, 0.24),
    (250_525.0, 0.32),
    (626_350.0, 0.35),
    (float("inf"), 0.37),
]

_STANDARD_DEDUCTION_SINGLE = 15_000.0


def _progressive_tax(taxable: float, brackets: list) -> float:
    """Compute progressive bracketed tax on a taxable amount."""
    tax = 0.0
    lower = 0.0
    for upper, rate in brackets:
        if taxable <= lower:
            break
        span = min(taxable, upper) - lower
        tax += span * rate
        lower = upper
    return tax


@dataclass
class Form1120Return:
    """US Form 1120 - C-corporation federal income tax return (simplified)."""
    entity_id: str
    ein: str
    year: int
    # Income statement (simplified)
    gross_receipts: float = 0.0
    cost_of_goods_sold: float = 0.0
    gross_profit: float = 0.0
    total_deductions: float = 0.0
    taxable_income: float = 0.0
    # Tax computation
    federal_tax: float = 0.0
    tax_credits: float = 0.0
    tax_payable: float = 0.0
    # Corporate AMT note (out of scope)
    camt_note: str = ""
    # Filing deadline
    filing_deadline: str = ""

    def bereken(self) -> "Form1120Return":
        """Recompute all derived fields."""
        self.gross_profit = self.gross_receipts - self.cost_of_goods_sold
        self.taxable_income = max(0.0, self.gross_profit - self.total_deductions)

        # Flat 21% federal corporate income tax (IRC Sec. 11).
        self.federal_tax = self.taxable_income * _CORPORATE_TAX_RATE
        self.tax_payable = max(0.0, self.federal_tax - self.tax_credits)

        # CAMT applies only to applicable corporations (>$1bn average book
        # income); it is out of the scope of this federal estimator.
        self.camt_note = (
            f"15% Corporate AMT (CAMT, IRC Sec. 55) may apply to applicable "
            f"corporations with average annual book income over "
            f"${_CAMT_BOOK_INCOME_THRESHOLD:,.0f}; out of estimator scope."
        )

        # Filing deadline: 15th day of the 4th month after year end.
        # For a calendar-year corporation that is April 15 of the following year.
        self.filing_deadline = f"April 15, {self.year + 1}"

        return self

    def to_dict(self) -> dict:
        return {
            "entity_id": self.entity_id,
            "ein": self.ein,
            "year": self.year,
            "gross_receipts": self.gross_receipts,
            "cost_of_goods_sold": self.cost_of_goods_sold,
            "gross_profit": self.gross_profit,
            "total_deductions": self.total_deductions,
            "taxable_income": self.taxable_income,
            "federal_tax": self.federal_tax,
            "tax_credits": self.tax_credits,
            "tax_payable": self.tax_payable,
            "camt_note": self.camt_note,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, simplified) for Form 1120."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:US">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.ein}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.year}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <GrossReceipts>{self.gross_receipts:.2f}</GrossReceipts>\n'
            f'    <CostOfGoodsSold>{self.cost_of_goods_sold:.2f}</CostOfGoodsSold>\n'
            f'    <GrossProfit>{self.gross_profit:.2f}</GrossProfit>\n'
            f'    <TotalDeductions>{self.total_deductions:.2f}</TotalDeductions>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            "  </GeneralLedger>\n"
            '  <TaxReturn type="Form1120">\n'
            f'    <FederalTax>{self.federal_tax:.2f}</FederalTax>\n'
            f'    <TaxCredits>{self.tax_credits:.2f}</TaxCredits>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <CAMTNote>{self.camt_note}</CAMTNote>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class Form1040Return:
    """US Form 1040 - individual federal income tax return (single filer)."""
    person_id: str
    ssn_encrypted: str    # vault-encrypted SSN
    year: int
    # Income
    adjusted_gross_income: float = 0.0
    standard_deduction: float = 0.0
    taxable_income: float = 0.0
    # Tax computation
    federal_tax: float = 0.0
    tax_credits: float = 0.0
    withholding: float = 0.0
    tax_payable: float = 0.0
    # Filing deadline
    filing_deadline: str = ""

    def bereken(self) -> "Form1040Return":
        """Recompute all derived fields."""
        if self.standard_deduction == 0.0:
            self.standard_deduction = _STANDARD_DEDUCTION_SINGLE

        self.taxable_income = max(0.0, self.adjusted_gross_income - self.standard_deduction)

        # Progressive bracketed tax (2025 single-filer brackets).
        gross_tax = _progressive_tax(self.taxable_income, _INDIVIDUAL_BRACKETS_SINGLE)
        self.federal_tax = max(0.0, gross_tax - self.tax_credits)
        self.tax_payable = self.federal_tax - self.withholding

        # Filing deadline: April 15 of the following year.
        self.filing_deadline = f"April 15, {self.year + 1}"

        return self

    def to_dict(self) -> dict:
        return {
            "person_id": self.person_id,
            "ssn_encrypted": self.ssn_encrypted,
            "year": self.year,
            "adjusted_gross_income": self.adjusted_gross_income,
            "standard_deduction": self.standard_deduction,
            "taxable_income": self.taxable_income,
            "federal_tax": self.federal_tax,
            "tax_credits": self.tax_credits,
            "withholding": self.withholding,
            "tax_payable": self.tax_payable,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, simplified) for Form 1040."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:US">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.ssn_encrypted}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.year}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <Individual>\n"
            f'    <AdjustedGrossIncome>{self.adjusted_gross_income:.2f}</AdjustedGrossIncome>\n'
            f'    <StandardDeduction>{self.standard_deduction:.2f}</StandardDeduction>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            "  </Individual>\n"
            '  <TaxReturn type="Form1040">\n'
            f'    <FederalTax>{self.federal_tax:.2f}</FederalTax>\n'
            f'    <TaxCredits>{self.tax_credits:.2f}</TaxCredits>\n'
            f'    <Withholding>{self.withholding:.2f}</Withholding>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


def genereer_form_1120(
    entity_id: str,
    ein: str,
    year: int,
    ledger_data: dict,
) -> Form1120Return:
    """Generate a Form 1120 return from P&L data in the ledger.

    ledger_data keys (all optional):
      gross_receipts, cost_of_goods_sold, total_deductions, tax_credits
    """
    return_ = Form1120Return(
        entity_id=entity_id,
        ein=ein,
        year=year,
        gross_receipts=float(ledger_data.get("gross_receipts", 0.0)),
        cost_of_goods_sold=float(ledger_data.get("cost_of_goods_sold", 0.0)),
        total_deductions=float(ledger_data.get("total_deductions", 0.0)),
        tax_credits=float(ledger_data.get("tax_credits", 0.0)),
    )
    return return_.bereken()


def genereer_form_1040(
    person_id: str,
    ssn_encrypted: str,
    year: int,
    income_data: dict,
) -> Form1040Return:
    """Generate a Form 1040 return for an individual (single filer).

    income_data keys (all optional):
      adjusted_gross_income, standard_deduction (default: statutory amount),
      tax_credits, withholding
    """
    return_ = Form1040Return(
        person_id=person_id,
        ssn_encrypted=ssn_encrypted,
        year=year,
        adjusted_gross_income=float(income_data.get("adjusted_gross_income", 0.0)),
        standard_deduction=float(income_data.get("standard_deduction", 0.0)),
        tax_credits=float(income_data.get("tax_credits", 0.0)),
        withholding=float(income_data.get("withholding", 0.0)),
    )
    return return_.bereken()
