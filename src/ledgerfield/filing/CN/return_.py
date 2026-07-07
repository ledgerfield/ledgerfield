"""China (CN) tax-return filing helpers.

Mirrors the NL filing module (src/ledgerfield/filing/NL/aangifte.py) structure:
each return is a dataclass with compute()/to_dict()/to_json()/to_xml_saf_t(),
plus module-level generate_* factory functions.

Covers:
  - EnterpriseIncomeTaxReturn  企业所得税年度纳税申报表 (EIT annual return)
  - IndividualIncomeTaxReturn  个人所得税年度自行纳税申报表 (IIT annual return)
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import datetime

__all__ = [
    "EnterpriseIncomeTaxReturn",
    "IndividualIncomeTaxReturn",
    "generate_eit_return",
    "generate_iit_return",
]

# ---------------------------------------------------------------------------
# Enterprise Income Tax (企业所得税) rates — 2025
#   Standard rate (EIT Law art. 4): 25%
#   Small low-profit enterprises (小型微利企业): effective 5% on annual
#     taxable income <= ¥3,000,000 (25% of income taxed at 20% => effective 5%,
#     policy extended through 2027).
#   High/New Tech Enterprises (高新技术企业, HNTE): 15%.
# ---------------------------------------------------------------------------
_EIT_STANDARD_RATE = 0.25
_EIT_HNTE_RATE = 0.15
_EIT_SMALL_LOW_PROFIT_EFFECTIVE_RATE = 0.05
_EIT_SMALL_LOW_PROFIT_INCOME_CEILING = 3_000_000.0

# ---------------------------------------------------------------------------
# Individual Income Tax (个人所得税) — comprehensive income (综合所得) — 2025
#   Standard basic deduction (基本减除费用): ¥60,000 / year.
#   Annual progressive brackets on taxable income (after deductions),
#   using the quick-deduction method (速算扣除数):
#     3%   up to      36,000     quick-deduction        0
#     10%  up to     144,000     quick-deduction    2,520
#     20%  up to     300,000     quick-deduction   16,920
#     25%  up to     420,000     quick-deduction   31,920
#     30%  up to     660,000     quick-deduction   52,920
#     35%  up to     960,000     quick-deduction   85,920
#     45%  above     960,000     quick-deduction  181,920
# ---------------------------------------------------------------------------
_IIT_BASIC_DEDUCTION = 60_000.0

# (upper_bound, rate, quick_deduction)
_IIT_BRACKETS = [
    (36_000.0, 0.03, 0.0),
    (144_000.0, 0.10, 2_520.0),
    (300_000.0, 0.20, 16_920.0),
    (420_000.0, 0.25, 31_920.0),
    (660_000.0, 0.30, 52_920.0),
    (960_000.0, 0.35, 85_920.0),
    (float("inf"), 0.45, 181_920.0),
]


def _iit_tax(taxable_income: float) -> float:
    """Progressive IIT via the quick-deduction method (速算扣除数)."""
    if taxable_income <= 0:
        return 0.0
    for upper, rate, quick in _IIT_BRACKETS:
        if taxable_income <= upper:
            return taxable_income * rate - quick
    # Unreachable: last bracket has an infinite upper bound.
    return 0.0


@dataclass
class EnterpriseIncomeTaxReturn:
    """Enterprise Income Tax annual return (企业所得税年度纳税申报表)."""
    entity_id: str
    tax_id: str            # Unified Social Credit Code (统一社会信用代码)
    year: int
    # Profit & loss (利润表, simplified)
    revenue: float = 0.0
    cost_of_sales: float = 0.0
    gross_profit: float = 0.0
    period_expenses: float = 0.0
    total_profit: float = 0.0
    # Tax status flags
    small_low_profit: bool = False   # 小型微利企业
    hnte: bool = False               # 高新技术企业 (High/New Tech Enterprise)
    # Tax computation (纳税调整 & 应纳税额)
    tax_adjustments: float = 0.0     # non-deductible / add-back adjustments
    taxable_income: float = 0.0      # 应纳税所得额
    enterprise_income_tax: float = 0.0
    tax_incentives: float = 0.0      # 税收优惠 /减免税额
    tax_payable: float = 0.0         # 应纳税额
    filing_deadline: str = ""

    def compute(self) -> "EnterpriseIncomeTaxReturn":
        """Recompute all derived fields."""
        # P&L
        self.gross_profit = self.revenue - self.cost_of_sales
        self.total_profit = self.gross_profit - self.period_expenses

        # Taxable income (应纳税所得额) = accounting profit + tax adjustments.
        self.taxable_income = max(0.0, self.total_profit + self.tax_adjustments)

        # Rate selection.
        if self.small_low_profit and self.taxable_income <= _EIT_SMALL_LOW_PROFIT_INCOME_CEILING:
            effective_rate = _EIT_SMALL_LOW_PROFIT_EFFECTIVE_RATE
        elif self.hnte:
            effective_rate = _EIT_HNTE_RATE
        else:
            effective_rate = _EIT_STANDARD_RATE

        self.enterprise_income_tax = self.taxable_income * effective_rate
        self.tax_payable = max(0.0, self.enterprise_income_tax - self.tax_incentives)

        # Filing deadline: within 5 months after the year end => May 31 following year.
        self.filing_deadline = f"{self.year + 1}-05-31"

        return self

    def to_dict(self) -> dict:
        return {
            "entity_id": self.entity_id,
            "tax_id": self.tax_id,
            "year": self.year,
            "revenue": self.revenue,
            "cost_of_sales": self.cost_of_sales,
            "gross_profit": self.gross_profit,
            "period_expenses": self.period_expenses,
            "total_profit": self.total_profit,
            "small_low_profit": self.small_low_profit,
            "hnte": self.hnte,
            "tax_adjustments": self.tax_adjustments,
            "taxable_income": self.taxable_income,
            "enterprise_income_tax": self.enterprise_income_tax,
            "tax_incentives": self.tax_incentives,
            "tax_payable": self.tax_payable,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, simplified) for the EIT return."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:CN">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.tax_id}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.year}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <Revenue>{self.revenue:.2f}</Revenue>\n'
            f'    <CostOfSales>{self.cost_of_sales:.2f}</CostOfSales>\n'
            f'    <GrossProfit>{self.gross_profit:.2f}</GrossProfit>\n'
            f'    <PeriodExpenses>{self.period_expenses:.2f}</PeriodExpenses>\n'
            f'    <TotalProfit>{self.total_profit:.2f}</TotalProfit>\n'
            "  </GeneralLedger>\n"
            '  <TaxReturn type="EIT">\n'
            f'    <TaxAdjustments>{self.tax_adjustments:.2f}</TaxAdjustments>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            f'    <EnterpriseIncomeTax>{self.enterprise_income_tax:.2f}</EnterpriseIncomeTax>\n'
            f'    <TaxIncentives>{self.tax_incentives:.2f}</TaxIncentives>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class IndividualIncomeTaxReturn:
    """Individual Income Tax annual return (个人所得税年度自行纳税申报表).

    Comprehensive income (综合所得): wages/salaries, remuneration for services,
    author's remuneration and royalties, reconciled on the annual return.
    """
    person_id: str
    tax_id_encrypted: str   # vault-encrypted taxpayer ID (纳税人识别号)
    year: int
    # Income & deductions
    comprehensive_income: float = 0.0       # 综合所得收入额
    basic_deduction: float = 0.0            # 基本减除费用 (default ¥60,000)
    special_deductions: float = 0.0         # 专项及专项附加扣除
    taxable_income: float = 0.0             # 应纳税所得额
    # Tax
    individual_income_tax: float = 0.0      # 应纳税额
    tax_prepaid: float = 0.0                # 已预缴税额
    tax_payable: float = 0.0                # 应补(退)税额
    filing_deadline: str = ""

    def compute(self) -> "IndividualIncomeTaxReturn":
        """Recompute all derived fields."""
        if self.basic_deduction == 0.0:
            self.basic_deduction = _IIT_BASIC_DEDUCTION

        self.taxable_income = max(
            0.0,
            self.comprehensive_income - self.basic_deduction - self.special_deductions,
        )
        self.individual_income_tax = _iit_tax(self.taxable_income)
        self.tax_payable = self.individual_income_tax - self.tax_prepaid

        # Annual reconciliation window: March 1 – June 30 following year.
        self.filing_deadline = f"{self.year + 1}-06-30"

        return self

    def to_dict(self) -> dict:
        return {
            "person_id": self.person_id,
            "tax_id_encrypted": self.tax_id_encrypted,
            "year": self.year,
            "comprehensive_income": self.comprehensive_income,
            "basic_deduction": self.basic_deduction,
            "special_deductions": self.special_deductions,
            "taxable_income": self.taxable_income,
            "individual_income_tax": self.individual_income_tax,
            "tax_prepaid": self.tax_prepaid,
            "tax_payable": self.tax_payable,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, simplified) for the IIT return."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:CN">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.tax_id_encrypted}</TaxRegistrationNumber>\n'
            f'    <FiscalYear>{self.year}</FiscalYear>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            '  <TaxReturn type="IIT">\n'
            f'    <ComprehensiveIncome>{self.comprehensive_income:.2f}</ComprehensiveIncome>\n'
            f'    <BasicDeduction>{self.basic_deduction:.2f}</BasicDeduction>\n'
            f'    <SpecialDeductions>{self.special_deductions:.2f}</SpecialDeductions>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            f'    <IndividualIncomeTax>{self.individual_income_tax:.2f}</IndividualIncomeTax>\n'
            f'    <TaxPrepaid>{self.tax_prepaid:.2f}</TaxPrepaid>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


def generate_eit_return(
    entity_id: str,
    tax_id: str,
    year: int,
    ledger_data: dict,
) -> EnterpriseIncomeTaxReturn:
    """Generate an EIT annual return (企业所得税年度纳税申报表) from ledger P&L data.

    ledger_data keys (all optional):
      revenue, cost_of_sales, period_expenses, tax_adjustments,
      tax_incentives, small_low_profit (bool), hnte (bool)
    """
    ret = EnterpriseIncomeTaxReturn(
        entity_id=entity_id,
        tax_id=tax_id,
        year=year,
        revenue=float(ledger_data.get("revenue", 0.0)),
        cost_of_sales=float(ledger_data.get("cost_of_sales", 0.0)),
        period_expenses=float(ledger_data.get("period_expenses", 0.0)),
        tax_adjustments=float(ledger_data.get("tax_adjustments", 0.0)),
        tax_incentives=float(ledger_data.get("tax_incentives", 0.0)),
        small_low_profit=bool(ledger_data.get("small_low_profit", False)),
        hnte=bool(ledger_data.get("hnte", False)),
    )
    return ret.compute()


def generate_iit_return(
    person_id: str,
    tax_id_encrypted: str,
    year: int,
    income_data: dict,
) -> IndividualIncomeTaxReturn:
    """Generate an IIT annual return (个人所得税年度自行纳税申报表) for an individual.

    income_data keys (all optional):
      comprehensive_income, basic_deduction (default ¥60,000),
      special_deductions, tax_prepaid
    """
    ret = IndividualIncomeTaxReturn(
        person_id=person_id,
        tax_id_encrypted=tax_id_encrypted,
        year=year,
        comprehensive_income=float(income_data.get("comprehensive_income", 0.0)),
        basic_deduction=float(income_data.get("basic_deduction", 0.0)),
        special_deductions=float(income_data.get("special_deductions", 0.0)),
        tax_prepaid=float(income_data.get("tax_prepaid", 0.0)),
    )
    return ret.compute()
