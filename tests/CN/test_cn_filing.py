"""Tests for the China (CN) tax-return filing module — 15 tests."""
import json

from ledgerfield.filing.CN.return_ import (
    EnterpriseIncomeTaxReturn,
    IndividualIncomeTaxReturn,
    generate_eit_return,
    generate_iit_return,
)


# --- Enterprise Income Tax (EIT, 企业所得税) ---

def test_eit_standard_rate():
    ret = generate_eit_return(
        "e1", "91310000MA1", 2025,
        {"revenue": 1_000_000, "cost_of_sales": 0, "period_expenses": 0},
    )
    assert ret.taxable_income == 1_000_000
    assert ret.enterprise_income_tax == 250_000
    assert ret.tax_payable == 250_000


def test_eit_small_low_profit_effective_5pct():
    ret = generate_eit_return(
        "e2", "91310000MA2", 2025,
        {"revenue": 1_000_000, "small_low_profit": True},
    )
    assert ret.enterprise_income_tax == 50_000  # effective 5%


def test_eit_small_low_profit_over_ceiling_uses_standard():
    # Above ¥3,000,000 the small-low-profit relief no longer applies.
    ret = generate_eit_return(
        "e3", "91310000MA3", 2025,
        {"revenue": 4_000_000, "small_low_profit": True},
    )
    assert ret.enterprise_income_tax == 1_000_000  # 25%


def test_eit_hnte_rate_15pct():
    ret = generate_eit_return(
        "e4", "91310000MA4", 2025,
        {"revenue": 1_000_000, "hnte": True},
    )
    assert ret.enterprise_income_tax == 150_000  # 15%


def test_eit_pnl_derivation():
    ret = generate_eit_return(
        "e5", "91310000MA5", 2025,
        {"revenue": 500_000, "cost_of_sales": 200_000, "period_expenses": 100_000},
    )
    assert ret.gross_profit == 300_000
    assert ret.total_profit == 200_000
    assert ret.taxable_income == 200_000


def test_eit_negative_profit_zero_tax():
    ret = generate_eit_return(
        "e6", "91310000MA6", 2025,
        {"revenue": 100_000, "cost_of_sales": 300_000},
    )
    assert ret.taxable_income == 0.0
    assert ret.enterprise_income_tax == 0.0
    assert ret.tax_payable == 0.0


def test_eit_incentives_reduce_payable():
    ret = generate_eit_return(
        "e7", "91310000MA7", 2025,
        {"revenue": 1_000_000, "tax_incentives": 50_000},
    )
    assert ret.enterprise_income_tax == 250_000
    assert ret.tax_payable == 200_000


def test_eit_deadline_may_31():
    ret = generate_eit_return("e8", "91310000MA8", 2025, {"revenue": 10_000})
    assert ret.filing_deadline == "2026-05-31"


def test_eit_to_json_round_trip():
    ret = generate_eit_return("e9", "91310000MA9", 2025, {"revenue": 1_000_000})
    parsed = json.loads(ret.to_json())
    assert parsed["taxable_income"] == 1_000_000
    assert parsed["enterprise_income_tax"] == 250_000
    assert parsed == ret.to_dict()


def test_eit_to_xml_saf_t_present():
    ret = generate_eit_return("e10", "91310000MAA", 2025, {"revenue": 1_000_000})
    xml = ret.to_xml_saf_t()
    assert xml.startswith("<?xml")
    assert 'type="EIT"' in xml
    assert "<TaxableIncome>1000000.00</TaxableIncome>" in xml


# --- Individual Income Tax (IIT, 个人所得税综合所得) ---

def test_iit_bracketed_case_with_basic_deduction():
    # comprehensive 200,000 - 60,000 = 140,000 taxable => 10% bracket.
    # 140,000 * 0.10 - 2,520 = 11,480
    ret = generate_iit_return("p1", "enc-1", 2025, {"comprehensive_income": 200_000})
    assert ret.basic_deduction == 60_000
    assert ret.taxable_income == 140_000
    assert ret.individual_income_tax == 11_480


def test_iit_top_band_45pct():
    # comprehensive 1,060,000 - 60,000 = 1,000,000 taxable => 45% band.
    # 1,000,000 * 0.45 - 181,920 = 268,080
    ret = generate_iit_return("p2", "enc-2", 2025, {"comprehensive_income": 1_060_000})
    assert ret.taxable_income == 1_000_000
    assert ret.individual_income_tax == 268_080


def test_iit_special_deductions_and_prepaid():
    ret = generate_iit_return(
        "p3", "enc-3", 2025,
        {"comprehensive_income": 200_000, "special_deductions": 20_000, "tax_prepaid": 5_000},
    )
    # taxable = 200,000 - 60,000 - 20,000 = 120,000 => 10% bracket
    # 120,000 * 0.10 - 2,520 = 9,480 ; payable = 9,480 - 5,000 = 4,480
    assert ret.taxable_income == 120_000
    assert ret.individual_income_tax == 9_480
    assert ret.tax_payable == 4_480


def test_iit_below_threshold_zero_tax():
    ret = generate_iit_return("p4", "enc-4", 2025, {"comprehensive_income": 50_000})
    assert ret.taxable_income == 0.0
    assert ret.individual_income_tax == 0.0


def test_iit_deadline_and_json_and_xml():
    ret = generate_iit_return("p5", "enc-5", 2025, {"comprehensive_income": 200_000})
    assert ret.filing_deadline == "2026-06-30"
    parsed = json.loads(ret.to_json())
    assert parsed == ret.to_dict()
    xml = ret.to_xml_saf_t()
    assert xml.startswith("<?xml")
    assert 'type="IIT"' in xml


def test_dataclasses_compute_directly():
    eit = EnterpriseIncomeTaxReturn("e", "t", 2025, revenue=1_000_000).compute()
    assert eit.enterprise_income_tax == 250_000
    iit = IndividualIncomeTaxReturn("p", "t", 2025, comprehensive_income=200_000).compute()
    assert iit.individual_income_tax == 11_480
