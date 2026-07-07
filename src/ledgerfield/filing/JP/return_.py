"""Japan tax-return filing helpers (FY2025).

Mirrors the structure of the Netherlands filing module (``filing/NL/aangifte.py``)
but for Japanese returns:

- :class:`CorporateTaxReturn` — Corporation Tax Return (法人税申告書, *hōjinzei
  shinkokusho*). Computes the NATIONAL corporation tax (法人税). Local enterprise
  tax (事業税) and inhabitants tax (住民税) push the *effective* combined rate to
  roughly ~29.7%; those are documented via ``effective_rate_note`` /
  ``local_taxes_note`` but are not levied in this return.
- :class:`IndividualTaxReturn` — Final Income Tax Return (確定申告書, *kakutei
  shinkokusho*). Computes progressive national income tax (所得税) plus the 2.1%
  Special Reconstruction Income Tax surtax (復興特別所得税).
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import datetime

__all__ = [
    "CorporateTaxReturn",
    "IndividualTaxReturn",
    "generate_corporate_return",
    "generate_individual_return",
]

# ---------------------------------------------------------------------------
# National Corporation Tax (法人税) rates — FY2025
#   Large corporations (paid-in capital > ¥100m): flat 23.2%.
#   SMEs (paid-in capital ≤ ¥100m): reduced 15% on the first ¥8,000,000 of
#     taxable income; 23.2% on the remainder.
# The effective combined rate incl. local enterprise tax (事業税) and
# inhabitants tax (住民税) is roughly ~29.7%, but this return computes the
# national tax only.
# ---------------------------------------------------------------------------
_CIT_SME_THRESHOLD = 8_000_000.0
_CIT_SME_REDUCED_RATE = 0.15
_CIT_STANDARD_RATE = 0.232
_CIT_SME_CAPITAL_CEILING = 100_000_000.0   # paid-in capital ≤ ¥100m → SME
_CIT_EFFECTIVE_RATE_NOTE = (
    "Effective combined corporate rate is ~29.7% including local enterprise "
    "tax (事業税) and inhabitants tax (住民税); this return computes national "
    "corporation tax (法人税) only."
)

# ---------------------------------------------------------------------------
# Individual national income tax (所得税) — progressive brackets, FY2025.
# Each tuple: (upper_bound, marginal_rate). Final bound is math.inf.
#   5%  up to ¥1,950,000
#   10% up to ¥3,300,000
#   20% up to ¥6,950,000
#   23% up to ¥9,000,000
#   33% up to ¥18,000,000
#   40% up to ¥40,000,000
#   45% above
# Plus a 2.1% Special Reconstruction surtax (復興特別所得税) ON the income tax.
# Basic deduction (基礎控除): ¥480,000.
# ---------------------------------------------------------------------------
_IIT_BRACKETS = [
    (1_950_000.0, 0.05),
    (3_300_000.0, 0.10),
    (6_950_000.0, 0.20),
    (9_000_000.0, 0.23),
    (18_000_000.0, 0.33),
    (40_000_000.0, 0.40),
    (float("inf"), 0.45),
]
_IIT_BASIC_DEDUCTION = 480_000.0
_IIT_RECONSTRUCTION_SURTAX_RATE = 0.021


def _progressive_income_tax(taxable: float) -> float:
    """Apply the FY2025 progressive national income tax brackets."""
    if taxable <= 0:
        return 0.0
    tax = 0.0
    lower = 0.0
    for upper, rate in _IIT_BRACKETS:
        if taxable > upper:
            tax += (upper - lower) * rate
            lower = upper
        else:
            tax += (taxable - lower) * rate
            break
    return tax


@dataclass
class CorporateTaxReturn:
    """Corporation Tax Return (法人税申告書, hōjinzei shinkokusho) — FY2025.

    Computes national corporation tax (法人税). SMEs (paid-in capital ≤ ¥100m)
    get a reduced 15% rate on the first ¥8,000,000 of taxable income.
    """
    entity_id: str
    corporate_number: str   # 法人番号 (13-digit Corporate Number)
    fiscal_year: int
    fiscal_year_end: str = ""   # ISO date of fiscal year end, e.g. "2025-03-31"
    paid_in_capital: float = 0.0
    # Profit & loss (simplified)
    revenue: float = 0.0
    cost_of_sales: float = 0.0
    gross_profit: float = 0.0
    operating_expenses: float = 0.0
    operating_income: float = 0.0
    non_operating_income: float = 0.0
    taxable_income: float = 0.0
    # Corporation tax breakdown
    is_sme: bool = False
    corporate_tax_reduced: float = 0.0   # 15% tier
    corporate_tax_standard: float = 0.0  # 23.2% tier
    corporate_tax: float = 0.0
    tax_payable: float = 0.0
    # Documentation-only notes
    local_taxes_note: str = ""
    effective_rate_note: str = ""
    filing_deadline: str = ""

    def compute(self) -> "CorporateTaxReturn":
        """Recompute all derived fields."""
        self.gross_profit = self.revenue - self.cost_of_sales
        self.operating_income = self.gross_profit - self.operating_expenses
        self.taxable_income = self.operating_income + self.non_operating_income

        self.is_sme = self.paid_in_capital <= _CIT_SME_CAPITAL_CEILING

        income = max(0.0, self.taxable_income)
        if self.is_sme:
            if income <= _CIT_SME_THRESHOLD:
                self.corporate_tax_reduced = income * _CIT_SME_REDUCED_RATE
                self.corporate_tax_standard = 0.0
            else:
                self.corporate_tax_reduced = _CIT_SME_THRESHOLD * _CIT_SME_REDUCED_RATE
                self.corporate_tax_standard = (
                    (income - _CIT_SME_THRESHOLD) * _CIT_STANDARD_RATE
                )
        else:
            self.corporate_tax_reduced = 0.0
            self.corporate_tax_standard = income * _CIT_STANDARD_RATE

        self.corporate_tax = self.corporate_tax_reduced + self.corporate_tax_standard
        self.tax_payable = self.corporate_tax

        self.local_taxes_note = (
            "Local enterprise tax (事業税) and inhabitants tax (住民税) are filed "
            "separately and are not included in this national return."
        )
        self.effective_rate_note = _CIT_EFFECTIVE_RATE_NOTE

        # Filing deadline: 2 months after the fiscal year end.
        self.filing_deadline = self._deadline_from_year_end()

        return self

    def _deadline_from_year_end(self) -> str:
        """Deadline = 2 months after fiscal year end."""
        if self.fiscal_year_end:
            fye = datetime.date.fromisoformat(self.fiscal_year_end)
        else:
            # Default assumption: fiscal year ends 31 March of the following
            # calendar year (typical Japanese corporate fiscal year).
            fye = datetime.date(self.fiscal_year + 1, 3, 31)
            self.fiscal_year_end = fye.isoformat()
        # add 2 months
        month = fye.month + 2
        year = fye.year + (month - 1) // 12
        month = (month - 1) % 12 + 1
        # clamp day to end of target month
        if month == 12:
            next_month_first = datetime.date(year + 1, 1, 1)
        else:
            next_month_first = datetime.date(year, month + 1, 1)
        last_day = (next_month_first - datetime.timedelta(days=1)).day
        day = min(fye.day, last_day)
        return datetime.date(year, month, day).isoformat()

    def to_dict(self) -> dict:
        return {
            "form": "法人税申告書 (Corporation Tax Return, hōjinzei shinkokusho)",
            "entity_id": self.entity_id,
            "corporate_number": self.corporate_number,
            "fiscal_year": self.fiscal_year,
            "fiscal_year_end": self.fiscal_year_end,
            "paid_in_capital": self.paid_in_capital,
            "revenue": self.revenue,
            "cost_of_sales": self.cost_of_sales,
            "gross_profit": self.gross_profit,
            "operating_expenses": self.operating_expenses,
            "operating_income": self.operating_income,
            "non_operating_income": self.non_operating_income,
            "taxable_income": self.taxable_income,
            "is_sme": self.is_sme,
            "corporate_tax_reduced": self.corporate_tax_reduced,
            "corporate_tax_standard": self.corporate_tax_standard,
            "corporate_tax": self.corporate_tax,
            "tax_payable": self.tax_payable,
            "local_taxes_note": self.local_taxes_note,
            "effective_rate_note": self.effective_rate_note,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, Japan corporate return)."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:JP">\n'
            "  <Header>\n"
            f'    <CorporateNumber>{self.corporate_number}</CorporateNumber>\n'
            f'    <FiscalYear>{self.fiscal_year}</FiscalYear>\n'
            f'    <FiscalYearEnd>{self.fiscal_year_end}</FiscalYearEnd>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <Revenue>{self.revenue:.2f}</Revenue>\n'
            f'    <CostOfSales>{self.cost_of_sales:.2f}</CostOfSales>\n'
            f'    <GrossProfit>{self.gross_profit:.2f}</GrossProfit>\n'
            f'    <OperatingExpenses>{self.operating_expenses:.2f}</OperatingExpenses>\n'
            f'    <OperatingIncome>{self.operating_income:.2f}</OperatingIncome>\n'
            f'    <NonOperatingIncome>{self.non_operating_income:.2f}</NonOperatingIncome>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            "  </GeneralLedger>\n"
            '  <TaxReturn type="CorporateTax" form="法人税申告書">\n'
            f'    <IsSME>{str(self.is_sme).lower()}</IsSME>\n'
            f'    <CorporateTaxReduced>{self.corporate_tax_reduced:.2f}</CorporateTaxReduced>\n'
            f'    <CorporateTaxStandard>{self.corporate_tax_standard:.2f}</CorporateTaxStandard>\n'
            f'    <CorporateTax>{self.corporate_tax:.2f}</CorporateTax>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class IndividualTaxReturn:
    """Final Income Tax Return (確定申告書, kakutei shinkoku) — FY2025.

    Computes progressive national income tax (所得税) on income after the
    ¥480,000 basic deduction (基礎控除), plus the 2.1% Special Reconstruction
    Income Tax surtax (復興特別所得税) levied on the income tax.
    """
    person_id: str
    my_number_encrypted: str    # vault-encrypted My Number (マイナンバー)
    fiscal_year: int
    # Income & deductions
    employment_income: float = 0.0
    business_income: float = 0.0
    other_income: float = 0.0
    basic_deduction: float = 0.0
    additional_deductions: float = 0.0
    total_income: float = 0.0
    taxable_income: float = 0.0
    # Tax
    income_tax: float = 0.0
    reconstruction_surtax: float = 0.0   # 復興特別所得税 (2.1% of income_tax)
    total_tax: float = 0.0
    withholding_tax_paid: float = 0.0
    tax_payable: float = 0.0
    filing_deadline: str = ""

    def compute(self) -> "IndividualTaxReturn":
        """Recompute all derived fields."""
        self.total_income = (
            self.employment_income + self.business_income + self.other_income
        )
        if self.basic_deduction == 0.0:
            self.basic_deduction = _IIT_BASIC_DEDUCTION

        self.taxable_income = max(
            0.0,
            self.total_income - self.basic_deduction - self.additional_deductions,
        )

        self.income_tax = _progressive_income_tax(self.taxable_income)
        self.reconstruction_surtax = self.income_tax * _IIT_RECONSTRUCTION_SURTAX_RATE
        self.total_tax = self.income_tax + self.reconstruction_surtax
        self.tax_payable = self.total_tax - self.withholding_tax_paid

        # Final income tax return deadline: 15 March of the following year.
        self.filing_deadline = f"{self.fiscal_year + 1}-03-15"

        return self

    def to_dict(self) -> dict:
        return {
            "form": "確定申告書 (Final Income Tax Return, kakutei shinkoku)",
            "person_id": self.person_id,
            "my_number_encrypted": self.my_number_encrypted,
            "fiscal_year": self.fiscal_year,
            "employment_income": self.employment_income,
            "business_income": self.business_income,
            "other_income": self.other_income,
            "basic_deduction": self.basic_deduction,
            "additional_deductions": self.additional_deductions,
            "total_income": self.total_income,
            "taxable_income": self.taxable_income,
            "income_tax": self.income_tax,
            "reconstruction_surtax": self.reconstruction_surtax,
            "total_tax": self.total_tax,
            "withholding_tax_paid": self.withholding_tax_paid,
            "tax_payable": self.tax_payable,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, Japan individual return)."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:JP">\n'
            "  <Header>\n"
            f'    <PersonId>{self.person_id}</PersonId>\n'
            f'    <FiscalYear>{self.fiscal_year}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <Income>\n"
            f'    <EmploymentIncome>{self.employment_income:.2f}</EmploymentIncome>\n'
            f'    <BusinessIncome>{self.business_income:.2f}</BusinessIncome>\n'
            f'    <OtherIncome>{self.other_income:.2f}</OtherIncome>\n'
            f'    <TotalIncome>{self.total_income:.2f}</TotalIncome>\n'
            f'    <BasicDeduction>{self.basic_deduction:.2f}</BasicDeduction>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            "  </Income>\n"
            '  <TaxReturn type="IndividualIncomeTax" form="確定申告書">\n'
            f'    <IncomeTax>{self.income_tax:.2f}</IncomeTax>\n'
            f'    <ReconstructionSurtax>{self.reconstruction_surtax:.2f}</ReconstructionSurtax>\n'
            f'    <TotalTax>{self.total_tax:.2f}</TotalTax>\n'
            f'    <WithholdingTaxPaid>{self.withholding_tax_paid:.2f}</WithholdingTaxPaid>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


def generate_corporate_return(
    entity_id: str,
    corporate_number: str,
    fiscal_year: int,
    ledger_data: dict,
) -> CorporateTaxReturn:
    """Generate a Corporation Tax Return (法人税申告書) from ledger P&L data.

    ledger_data keys (all optional):
      revenue, cost_of_sales, operating_expenses, non_operating_income,
      paid_in_capital, fiscal_year_end
    """
    ret = CorporateTaxReturn(
        entity_id=entity_id,
        corporate_number=corporate_number,
        fiscal_year=fiscal_year,
        fiscal_year_end=str(ledger_data.get("fiscal_year_end", "")),
        paid_in_capital=float(ledger_data.get("paid_in_capital", 0.0)),
        revenue=float(ledger_data.get("revenue", 0.0)),
        cost_of_sales=float(ledger_data.get("cost_of_sales", 0.0)),
        operating_expenses=float(ledger_data.get("operating_expenses", 0.0)),
        non_operating_income=float(ledger_data.get("non_operating_income", 0.0)),
    )
    return ret.compute()


def generate_individual_return(
    person_id: str,
    my_number_encrypted: str,
    fiscal_year: int,
    income_data: dict,
) -> IndividualTaxReturn:
    """Generate a Final Income Tax Return (確定申告書) for an individual.

    income_data keys (all optional):
      employment_income, business_income, other_income,
      basic_deduction (default: statutory ¥480,000),
      additional_deductions, withholding_tax_paid
    """
    ret = IndividualTaxReturn(
        person_id=person_id,
        my_number_encrypted=my_number_encrypted,
        fiscal_year=fiscal_year,
        employment_income=float(income_data.get("employment_income", 0.0)),
        business_income=float(income_data.get("business_income", 0.0)),
        other_income=float(income_data.get("other_income", 0.0)),
        basic_deduction=float(income_data.get("basic_deduction", 0.0)),
        additional_deductions=float(income_data.get("additional_deductions", 0.0)),
        withholding_tax_paid=float(income_data.get("withholding_tax_paid", 0.0)),
    )
    return ret.compute()
