"""UK tax return helpers for HMRC filings (Corporation Tax & Self Assessment)."""
from __future__ import annotations
from dataclasses import dataclass
import json
import datetime

__all__ = [
    "CT600Return",
    "SelfAssessmentReturn",
    "generate_ct600",
    "generate_self_assessment",
]

# ---------------------------------------------------------------------------
# Corporation Tax rates FY2025 (Finance Act 2021, from 1 April 2023 onwards)
#   Small profits rate:  19%  for taxable total profits <= £50,000
#   Main rate:           25%  for taxable total profits >  £250,000
#   Marginal relief between £50,000 and £250,000 (fraction 3/200)
# ---------------------------------------------------------------------------
_CT_SMALL_PROFITS_LIMIT = 50_000.0
_CT_UPPER_LIMIT = 250_000.0
_CT_SMALL_PROFITS_RATE = 0.19
_CT_MAIN_RATE = 0.25
_CT_MARGINAL_RELIEF_FRACTION = 3.0 / 200.0

# ---------------------------------------------------------------------------
# Income Tax bands 2025/26 (rest of UK, excludes Scottish rates)
#   Personal allowance: £12,570, tapered £1 for every £2 of income over £100,000
#   Basic rate  20% on the first £37,700 above the allowance
#   Higher rate 40% up to £125,140
#   Additional rate 45% above £125,140
# ---------------------------------------------------------------------------
_PERSONAL_ALLOWANCE = 12_570.0
_PA_TAPER_THRESHOLD = 100_000.0
_BASIC_RATE_LIMIT = 37_700.0      # width of the basic-rate band above the allowance
_HIGHER_RATE_LIMIT = 125_140.0    # income level at which additional rate begins
_BASIC_RATE = 0.20
_HIGHER_RATE = 0.40
_ADDITIONAL_RATE = 0.45


@dataclass
class CT600Return:
    """Corporation Tax return (HMRC form CT600), simplified."""
    company_id: str
    company_registration_number: str    # Companies House CRN
    period_end: str                      # accounting period end, ISO date "YYYY-MM-DD"
    # Profit & Loss account (simplified)
    turnover: float = 0.0
    cost_of_sales: float = 0.0
    gross_profit: float = 0.0
    admin_expenses: float = 0.0
    operating_profit: float = 0.0
    trading_profit: float = 0.0
    capital_allowances: float = 0.0
    taxable_total_profits: float = 0.0
    # Corporation Tax computation
    corporation_tax: float = 0.0
    marginal_relief: float = 0.0
    tax_payable: float = 0.0
    # Filing deadline (12 months after period end)
    filing_deadline: str = ""

    def bereken(self) -> "CT600Return":
        """Recompute all derived fields."""
        # P&L
        self.gross_profit = self.turnover - self.cost_of_sales
        self.operating_profit = self.gross_profit - self.admin_expenses
        self.trading_profit = self.operating_profit
        self.taxable_total_profits = max(
            0.0, self.trading_profit - self.capital_allowances
        )

        profit = self.taxable_total_profits

        # Corporation Tax computation with marginal relief (CTA 2010, Part 3A)
        if profit <= _CT_SMALL_PROFITS_LIMIT:
            self.corporation_tax = profit * _CT_SMALL_PROFITS_RATE
            self.marginal_relief = 0.0
            self.tax_payable = self.corporation_tax
        elif profit > _CT_UPPER_LIMIT:
            self.corporation_tax = profit * _CT_MAIN_RATE
            self.marginal_relief = 0.0
            self.tax_payable = self.corporation_tax
        else:
            # Full main-rate charge, then deduct marginal relief.
            # Assuming augmented profits == taxable total profits:
            #   relief = (upper_limit - profit) * 3/200
            self.corporation_tax = profit * _CT_MAIN_RATE
            self.marginal_relief = (
                (_CT_UPPER_LIMIT - profit) * _CT_MARGINAL_RELIEF_FRACTION
            )
            self.tax_payable = self.corporation_tax - self.marginal_relief

        # Filing deadline: 12 months after the accounting period end
        self.filing_deadline = self._plus_one_year(self.period_end)

        return self

    @staticmethod
    def _plus_one_year(iso_date: str) -> str:
        try:
            d = datetime.date.fromisoformat(iso_date)
        except (ValueError, TypeError):
            return ""
        try:
            return d.replace(year=d.year + 1).isoformat()
        except ValueError:
            # 29 Feb -> 28 Feb next (non-leap) year
            return d.replace(year=d.year + 1, day=28).isoformat()

    def to_dict(self) -> dict:
        return {
            "company_id": self.company_id,
            "company_registration_number": self.company_registration_number,
            "period_end": self.period_end,
            "turnover": self.turnover,
            "cost_of_sales": self.cost_of_sales,
            "gross_profit": self.gross_profit,
            "admin_expenses": self.admin_expenses,
            "operating_profit": self.operating_profit,
            "trading_profit": self.trading_profit,
            "capital_allowances": self.capital_allowances,
            "taxable_total_profits": self.taxable_total_profits,
            "corporation_tax": self.corporation_tax,
            "marginal_relief": self.marginal_relief,
            "tax_payable": self.tax_payable,
            "filing_deadline": self.filing_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, simplified) for a CT600 return."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:UK">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.company_registration_number}</TaxRegistrationNumber>\n'
            f'    <PeriodEnd>{self.period_end}</PeriodEnd>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <GeneralLedger>\n"
            f'    <Turnover>{self.turnover:.2f}</Turnover>\n'
            f'    <CostOfSales>{self.cost_of_sales:.2f}</CostOfSales>\n'
            f'    <GrossProfit>{self.gross_profit:.2f}</GrossProfit>\n'
            f'    <AdminExpenses>{self.admin_expenses:.2f}</AdminExpenses>\n'
            f'    <OperatingProfit>{self.operating_profit:.2f}</OperatingProfit>\n'
            f'    <TradingProfit>{self.trading_profit:.2f}</TradingProfit>\n'
            "  </GeneralLedger>\n"
            '  <TaxReturn type="CT600">\n'
            f'    <CapitalAllowances>{self.capital_allowances:.2f}</CapitalAllowances>\n'
            f'    <TaxableTotalProfits>{self.taxable_total_profits:.2f}</TaxableTotalProfits>\n'
            f'    <CorporationTax>{self.corporation_tax:.2f}</CorporationTax>\n'
            f'    <MarginalRelief>{self.marginal_relief:.2f}</MarginalRelief>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <FilingDeadline>{self.filing_deadline}</FilingDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


@dataclass
class SelfAssessmentReturn:
    """Self Assessment individual return (HMRC form SA100), simplified."""
    taxpayer_id: str
    national_insurance_number_encrypted: str    # vault-encrypted NINO
    tax_year_end: int                            # e.g. 2026 for the 2025/26 tax year
    # Income
    employment_income: float = 0.0
    self_employment_income: float = 0.0
    property_income: float = 0.0
    other_income: float = 0.0
    total_income: float = 0.0
    # Allowances
    personal_allowance: float = 0.0
    taxable_income: float = 0.0
    # Income Tax by band
    basic_rate_tax: float = 0.0
    higher_rate_tax: float = 0.0
    additional_rate_tax: float = 0.0
    income_tax: float = 0.0
    # National Insurance (Class 4 for the self-employed) — informational
    class4_nic_note: str = "Class 4 NIC may apply on self-employment profits."
    tax_already_paid: float = 0.0
    tax_payable: float = 0.0
    # Payment deadline: 31 January following the tax year end
    payment_deadline: str = ""

    def bereken(self) -> "SelfAssessmentReturn":
        """Recompute all derived fields."""
        self.total_income = (
            self.employment_income
            + self.self_employment_income
            + self.property_income
            + self.other_income
        )

        # Personal allowance with taper: £1 lost for every £2 over £100,000
        allowance = _PERSONAL_ALLOWANCE
        if self.total_income > _PA_TAPER_THRESHOLD:
            reduction = (self.total_income - _PA_TAPER_THRESHOLD) / 2.0
            allowance = max(0.0, _PERSONAL_ALLOWANCE - reduction)
        self.personal_allowance = allowance

        self.taxable_income = max(0.0, self.total_income - allowance)

        # Band thresholds measured on income above the personal allowance.
        # Basic-rate band: first £37,700 of taxable income.
        # Higher-rate band: up to income of £125,140 (i.e. taxable income up to
        #   £125,140 - allowance). Above that, additional rate.
        ti = self.taxable_income
        basic_band = _BASIC_RATE_LIMIT
        higher_band_top = max(0.0, _HIGHER_RATE_LIMIT - allowance)

        basic_amount = min(ti, basic_band)
        higher_amount = min(max(0.0, ti - basic_band), max(0.0, higher_band_top - basic_band))
        additional_amount = max(0.0, ti - higher_band_top)

        self.basic_rate_tax = basic_amount * _BASIC_RATE
        self.higher_rate_tax = higher_amount * _HIGHER_RATE
        self.additional_rate_tax = additional_amount * _ADDITIONAL_RATE

        self.income_tax = (
            self.basic_rate_tax + self.higher_rate_tax + self.additional_rate_tax
        )
        self.tax_payable = self.income_tax - self.tax_already_paid

        # Payment deadline: 31 January following the tax year end
        self.payment_deadline = f"{self.tax_year_end + 1}-01-31"

        return self

    def to_dict(self) -> dict:
        return {
            "taxpayer_id": self.taxpayer_id,
            "national_insurance_number_encrypted": self.national_insurance_number_encrypted,
            "tax_year_end": self.tax_year_end,
            "employment_income": self.employment_income,
            "self_employment_income": self.self_employment_income,
            "property_income": self.property_income,
            "other_income": self.other_income,
            "total_income": self.total_income,
            "personal_allowance": self.personal_allowance,
            "taxable_income": self.taxable_income,
            "basic_rate_tax": self.basic_rate_tax,
            "higher_rate_tax": self.higher_rate_tax,
            "additional_rate_tax": self.additional_rate_tax,
            "income_tax": self.income_tax,
            "class4_nic_note": self.class4_nic_note,
            "tax_already_paid": self.tax_already_paid,
            "tax_payable": self.tax_payable,
            "payment_deadline": self.payment_deadline,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def to_xml_saf_t(self) -> str:
        """SAF-T XML skeleton (OECD SAF-T, simplified) for an SA100 return."""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<AuditFile xmlns="urn:StandardAuditFile-Taxation:UK">\n'
            "  <Header>\n"
            f'    <TaxRegistrationNumber>{self.national_insurance_number_encrypted}</TaxRegistrationNumber>\n'
            f'    <TaxYearEnd>{self.tax_year_end}</TaxYearEnd>\n'
            f'    <CreationDate>{datetime.date.today().isoformat()}</CreationDate>\n'
            "  </Header>\n"
            "  <Income>\n"
            f'    <EmploymentIncome>{self.employment_income:.2f}</EmploymentIncome>\n'
            f'    <SelfEmploymentIncome>{self.self_employment_income:.2f}</SelfEmploymentIncome>\n'
            f'    <PropertyIncome>{self.property_income:.2f}</PropertyIncome>\n'
            f'    <OtherIncome>{self.other_income:.2f}</OtherIncome>\n'
            f'    <TotalIncome>{self.total_income:.2f}</TotalIncome>\n'
            "  </Income>\n"
            '  <TaxReturn type="SA100">\n'
            f'    <PersonalAllowance>{self.personal_allowance:.2f}</PersonalAllowance>\n'
            f'    <TaxableIncome>{self.taxable_income:.2f}</TaxableIncome>\n'
            f'    <BasicRateTax>{self.basic_rate_tax:.2f}</BasicRateTax>\n'
            f'    <HigherRateTax>{self.higher_rate_tax:.2f}</HigherRateTax>\n'
            f'    <AdditionalRateTax>{self.additional_rate_tax:.2f}</AdditionalRateTax>\n'
            f'    <IncomeTax>{self.income_tax:.2f}</IncomeTax>\n'
            f'    <TaxPayable>{self.tax_payable:.2f}</TaxPayable>\n'
            f'    <PaymentDeadline>{self.payment_deadline}</PaymentDeadline>\n'
            "  </TaxReturn>\n"
            "</AuditFile>\n"
        )


def generate_ct600(
    company_id: str,
    company_registration_number: str,
    period_end: str,
    ledger_data: dict,
) -> CT600Return:
    """Generate a CT600 return from P&L data in the ledger.

    ledger_data keys (all optional):
      turnover, cost_of_sales, admin_expenses, capital_allowances
    """
    return CT600Return(
        company_id=company_id,
        company_registration_number=company_registration_number,
        period_end=period_end,
        turnover=float(ledger_data.get("turnover", 0.0)),
        cost_of_sales=float(ledger_data.get("cost_of_sales", 0.0)),
        admin_expenses=float(ledger_data.get("admin_expenses", 0.0)),
        capital_allowances=float(ledger_data.get("capital_allowances", 0.0)),
    ).bereken()


def generate_self_assessment(
    taxpayer_id: str,
    national_insurance_number_encrypted: str,
    tax_year_end: int,
    income_data: dict,
) -> SelfAssessmentReturn:
    """Generate an SA100 Self Assessment return for an individual.

    income_data keys (all optional):
      employment_income, self_employment_income, property_income,
      other_income, tax_already_paid
    """
    return SelfAssessmentReturn(
        taxpayer_id=taxpayer_id,
        national_insurance_number_encrypted=national_insurance_number_encrypted,
        tax_year_end=tax_year_end,
        employment_income=float(income_data.get("employment_income", 0.0)),
        self_employment_income=float(income_data.get("self_employment_income", 0.0)),
        property_income=float(income_data.get("property_income", 0.0)),
        other_income=float(income_data.get("other_income", 0.0)),
        tax_already_paid=float(income_data.get("tax_already_paid", 0.0)),
    ).bereken()
