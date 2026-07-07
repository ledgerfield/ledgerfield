"""UK filing module tests — CT600 & SA100, FY2025 (tax year 2025/26)."""
import json

import pytest

from ledgerfield.filing.UK.returns import (
    CT600Return,
    SelfAssessmentReturn,
    generate_ct600,
    generate_self_assessment,
)


# --- CT600 Corporation Tax ---

def test_ct600_small_profits_rate():
    r = generate_ct600("c1", "12345678", "2025-12-31", {"turnover": 40_000})
    assert r.taxable_total_profits == pytest.approx(40_000.0)
    assert r.tax_payable == pytest.approx(7_600.0)      # 19% of 40k
    assert r.marginal_relief == pytest.approx(0.0)


def test_ct600_main_rate():
    r = generate_ct600("c2", "12345678", "2025-12-31", {"turnover": 300_000})
    assert r.tax_payable == pytest.approx(75_000.0)     # 25% of 300k
    assert r.marginal_relief == pytest.approx(0.0)


def test_ct600_marginal_relief():
    r = generate_ct600("c3", "12345678", "2025-12-31", {"turnover": 100_000})
    # 25% * 100k - (250k - 100k) * 3/200 = 25,000 - 2,250 = 22,750
    assert r.corporation_tax == pytest.approx(25_000.0)
    assert r.marginal_relief == pytest.approx(2_250.0)
    assert r.tax_payable == pytest.approx(22_750.0)


def test_ct600_zero_profit():
    r = generate_ct600("c4", "12345678", "2025-12-31", {"turnover": 0})
    assert r.tax_payable == pytest.approx(0.0)


def test_ct600_negative_profit():
    r = generate_ct600(
        "c5", "12345678", "2025-12-31",
        {"turnover": 50_000, "cost_of_sales": 80_000},
    )
    assert r.taxable_total_profits == pytest.approx(0.0)
    assert r.tax_payable == pytest.approx(0.0)


def test_ct600_pandl_derivation():
    r = generate_ct600(
        "c6", "12345678", "2025-12-31",
        {"turnover": 500_000, "cost_of_sales": 200_000, "admin_expenses": 50_000,
         "capital_allowances": 10_000},
    )
    assert r.gross_profit == pytest.approx(300_000.0)
    assert r.operating_profit == pytest.approx(250_000.0)
    assert r.trading_profit == pytest.approx(250_000.0)
    assert r.taxable_total_profits == pytest.approx(240_000.0)


def test_ct600_filing_deadline():
    r = generate_ct600("c7", "12345678", "2025-12-31", {"turnover": 40_000})
    assert r.filing_deadline == "2026-12-31"


def test_ct600_json_roundtrip():
    r = generate_ct600("c8", "12345678", "2025-12-31", {"turnover": 100_000})
    parsed = json.loads(r.to_json())
    assert parsed["tax_payable"] == pytest.approx(22_750.0)
    assert parsed["company_registration_number"] == "12345678"


def test_ct600_xml_contains_form_type():
    r = generate_ct600("c9", "12345678", "2025-12-31", {"turnover": 40_000})
    xml = r.to_xml_saf_t()
    assert 'type="CT600"' in xml
    assert xml.startswith("<?xml")


# --- SA100 Self Assessment ---

def test_sa_personal_allowance_taper():
    r = generate_self_assessment("p1", "enc", 2026, {"employment_income": 120_000})
    # allowance = 12,570 - (120,000 - 100,000) / 2 = 2,570
    assert r.personal_allowance == pytest.approx(2_570.0)


def test_sa_basic_rate_case():
    r = generate_self_assessment("p2", "enc", 2026, {"employment_income": 30_000})
    # taxable = 30,000 - 12,570 = 17,430 ; 20% = 3,486
    assert r.taxable_income == pytest.approx(17_430.0)
    assert r.income_tax == pytest.approx(3_486.0)
    assert r.higher_rate_tax == pytest.approx(0.0)


def test_sa_higher_rate_case():
    r = generate_self_assessment("p3", "enc", 2026, {"employment_income": 60_000})
    # taxable = 47,430 ; basic 37,700*20% = 7,540 ; higher 9,730*40% = 3,892
    assert r.basic_rate_tax == pytest.approx(7_540.0)
    assert r.higher_rate_tax == pytest.approx(3_892.0)
    assert r.income_tax == pytest.approx(11_432.0)


def test_sa_full_allowance_below_threshold():
    r = generate_self_assessment("p4", "enc", 2026, {"employment_income": 50_000})
    assert r.personal_allowance == pytest.approx(12_570.0)


def test_sa_payment_deadline():
    r = generate_self_assessment("p5", "enc", 2026, {"employment_income": 30_000})
    assert r.payment_deadline == "2027-01-31"


def test_sa_zero_income():
    r = generate_self_assessment("p6", "enc", 2026, {})
    assert r.income_tax == pytest.approx(0.0)
    assert r.taxable_income == pytest.approx(0.0)


def test_sa_json_roundtrip():
    r = generate_self_assessment("p7", "enc", 2026, {"employment_income": 30_000})
    parsed = json.loads(r.to_json())
    assert parsed["income_tax"] == pytest.approx(3_486.0)
    assert parsed["tax_year_end"] == 2026


def test_sa_xml_contains_form_type():
    r = generate_self_assessment("p8", "enc", 2026, {"employment_income": 30_000})
    xml = r.to_xml_saf_t()
    assert 'type="SA100"' in xml
    assert xml.startswith("<?xml")


def test_dataclass_direct_bereken():
    r = CT600Return("c", "999", "2025-06-30", turnover=40_000).bereken()
    assert r.tax_payable == pytest.approx(7_600.0)
    assert r.filing_deadline == "2026-06-30"
    s = SelfAssessmentReturn("p", "enc", 2026, employment_income=30_000).bereken()
    assert s.income_tax == pytest.approx(3_486.0)
