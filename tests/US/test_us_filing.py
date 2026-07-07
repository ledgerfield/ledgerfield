"""Tests for the US federal filing module (Form 1120 & Form 1040)."""
import json

from ledgerfield.filing.US.returns import (
    Form1120Return,
    Form1040Return,
    genereer_form_1120,
    genereer_form_1040,
)


# --------------------------------------------------------------------------
# Form 1120 (C-corporation)
# --------------------------------------------------------------------------
def test_1120_flat_21pct_on_one_million():
    r = Form1120Return(
        entity_id="e1", ein="12-3456789", year=2025,
        gross_receipts=1_000_000.0, cost_of_goods_sold=0.0,
        total_deductions=0.0,
    ).bereken()
    assert r.taxable_income == 1_000_000.0
    assert r.federal_tax == 210_000.0
    assert r.tax_payable == 210_000.0


def test_1120_zero_or_negative_income_no_tax():
    r = Form1120Return(
        entity_id="e2", ein="12-3456789", year=2025,
        gross_receipts=100_000.0, cost_of_goods_sold=60_000.0,
        total_deductions=80_000.0,  # deductions exceed gross profit
    ).bereken()
    assert r.taxable_income == 0.0
    assert r.federal_tax == 0.0
    assert r.tax_payable == 0.0


def test_1120_gross_profit_and_credits():
    r = genereer_form_1120("e3", "98-7654321", 2025, {
        "gross_receipts": 500_000.0,
        "cost_of_goods_sold": 200_000.0,
        "total_deductions": 100_000.0,
        "tax_credits": 5_000.0,
    })
    assert r.gross_profit == 300_000.0
    assert r.taxable_income == 200_000.0
    assert r.federal_tax == 42_000.0
    assert r.tax_payable == 37_000.0


def test_1120_deadline_calendar_year():
    r = Form1120Return("e4", "12-3456789", 2025).bereken()
    assert r.filing_deadline == "April 15, 2026"


def test_1120_camt_noted():
    r = Form1120Return("e5", "12-3456789", 2025).bereken()
    assert "CAMT" in r.camt_note
    assert "15%" in r.camt_note


def test_1120_xml_contains_form_id():
    r = Form1120Return("e6", "12-3456789", 2025, gross_receipts=1000.0).bereken()
    xml = r.to_xml_saf_t()
    assert "Form1120" in xml
    assert xml.startswith("<?xml")


def test_1120_json_round_trips():
    r = genereer_form_1120("e7", "12-3456789", 2025, {
        "gross_receipts": 800_000.0, "cost_of_goods_sold": 300_000.0,
        "total_deductions": 100_000.0,
    })
    data = json.loads(r.to_json())
    assert data == r.to_dict()
    assert data["federal_tax"] == r.federal_tax


# --------------------------------------------------------------------------
# Form 1040 (individual, single filer)
# --------------------------------------------------------------------------
def test_1040_single_agi_60000_bracketed_tax():
    r = genereer_form_1040("p1", "enc-ssn", 2025, {
        "adjusted_gross_income": 60_000.0,
    })
    # taxable = 60,000 - 15,000 = 45,000
    assert r.taxable_income == 45_000.0
    # 10% * 11,925 + 12% * (45,000 - 11,925) = 1,192.50 + 3,969 = 5,161.50
    assert round(r.federal_tax, 2) == 5_161.50


def test_1040_standard_deduction_applied_by_default():
    r = Form1040Return("p2", "enc-ssn", 2025, adjusted_gross_income=15_000.0).bereken()
    assert r.standard_deduction == 15_000.0
    assert r.taxable_income == 0.0
    assert r.federal_tax == 0.0


def test_1040_top_bracket_case():
    r = genereer_form_1040("p3", "enc-ssn", 2025, {
        "adjusted_gross_income": 1_015_000.0,  # taxable = 1,000,000
    })
    assert r.taxable_income == 1_000_000.0
    # Full stack up to 626,350 then 37% above.
    expected = (
        11_925.0 * 0.10
        + (48_475 - 11_925) * 0.12
        + (103_350 - 48_475) * 0.22
        + (197_300 - 103_350) * 0.24
        + (250_525 - 197_300) * 0.32
        + (626_350 - 250_525) * 0.35
        + (1_000_000 - 626_350) * 0.37
    )
    assert round(r.federal_tax, 2) == round(expected, 2)


def test_1040_deadline_following_year():
    r = Form1040Return("p4", "enc-ssn", 2025, adjusted_gross_income=50_000.0).bereken()
    assert r.filing_deadline == "April 15, 2026"


def test_1040_withholding_reduces_payable():
    r = genereer_form_1040("p5", "enc-ssn", 2025, {
        "adjusted_gross_income": 60_000.0,
        "withholding": 6_000.0,
    })
    assert round(r.tax_payable, 2) == round(5_161.50 - 6_000.0, 2)


def test_1040_json_round_trips():
    r = genereer_form_1040("p6", "enc-ssn", 2025, {"adjusted_gross_income": 90_000.0})
    data = json.loads(r.to_json())
    assert data == r.to_dict()


def test_1040_xml_contains_form_id():
    r = Form1040Return("p7", "enc-ssn", 2025, adjusted_gross_income=60_000.0).bereken()
    xml = r.to_xml_saf_t()
    assert "Form1040" in xml
    assert xml.startswith("<?xml")
