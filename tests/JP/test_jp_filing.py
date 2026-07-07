"""Japan filing-module tests — 法人税申告書 / 確定申告書 (FY2025). 15 tests."""
import json

import pytest

from ledgerfield.filing.JP.return_ import (
    CorporateTaxReturn,
    IndividualTaxReturn,
    generate_corporate_return,
    generate_individual_return,
)


# ── Corporate: national corporation tax (法人税) ───────────────────────────────

def test_corporate_large_flat_rate():
    """Large corp (capital > ¥100m), income ¥10,000,000 → 23.2% = 2,320,000."""
    r = generate_corporate_return(
        "e1", "1234567890123", 2025,
        {"revenue": 10_000_000, "paid_in_capital": 200_000_000},
    )
    assert r.is_sme is False
    assert r.corporate_tax == pytest.approx(2_320_000.0)
    assert r.tax_payable == pytest.approx(2_320_000.0)


def test_corporate_sme_at_threshold():
    """SME, income exactly ¥8,000,000 → all at 15% = 1,200,000."""
    r = generate_corporate_return(
        "e2", "1234567890123", 2025,
        {"revenue": 8_000_000, "paid_in_capital": 10_000_000},
    )
    assert r.is_sme is True
    assert r.corporate_tax_reduced == pytest.approx(1_200_000.0)
    assert r.corporate_tax_standard == pytest.approx(0.0)
    assert r.corporate_tax == pytest.approx(1_200_000.0)


def test_corporate_sme_above_threshold_split():
    """SME, income ¥10,000,000 → 15%*8m + 23.2%*2m = 1,200,000 + 464,000 = 1,664,000."""
    r = generate_corporate_return(
        "e3", "1234567890123", 2025,
        {"revenue": 10_000_000, "paid_in_capital": 50_000_000},
    )
    assert r.corporate_tax_reduced == pytest.approx(1_200_000.0)
    assert r.corporate_tax_standard == pytest.approx(464_000.0)
    assert r.corporate_tax == pytest.approx(1_664_000.0)


def test_corporate_sme_boundary_capital():
    """Paid-in capital exactly ¥100m still qualifies as SME."""
    r = generate_corporate_return(
        "e4", "1234567890123", 2025,
        {"revenue": 4_000_000, "paid_in_capital": 100_000_000},
    )
    assert r.is_sme is True
    assert r.corporate_tax == pytest.approx(4_000_000 * 0.15)


def test_corporate_zero_and_negative_income():
    """Zero or negative taxable income → no tax."""
    r_zero = generate_corporate_return("e5", "1", 2025, {"revenue": 0})
    assert r_zero.corporate_tax == pytest.approx(0.0)
    r_neg = generate_corporate_return(
        "e6", "1", 2025, {"revenue": 1_000_000, "cost_of_sales": 3_000_000},
    )
    assert r_neg.taxable_income < 0
    assert r_neg.corporate_tax == pytest.approx(0.0)


def test_corporate_pl_chain():
    """gross_profit / operating_income / taxable_income derived correctly."""
    r = generate_corporate_return(
        "e7", "1", 2025,
        {"revenue": 20_000_000, "cost_of_sales": 8_000_000,
         "operating_expenses": 5_000_000, "non_operating_income": 1_000_000,
         "paid_in_capital": 200_000_000},
    )
    assert r.gross_profit == pytest.approx(12_000_000.0)
    assert r.operating_income == pytest.approx(7_000_000.0)
    assert r.taxable_income == pytest.approx(8_000_000.0)
    assert r.corporate_tax == pytest.approx(8_000_000 * 0.232)


def test_corporate_deadline_two_months_after_year_end():
    """Filing deadline is 2 months after fiscal year end."""
    r = generate_corporate_return(
        "e8", "1", 2025,
        {"revenue": 1_000_000, "fiscal_year_end": "2025-03-31"},
    )
    assert r.filing_deadline == "2025-05-31"


def test_corporate_effective_rate_note_present():
    r = generate_corporate_return("e9", "1", 2025, {"revenue": 1_000_000})
    assert "29.7" in r.effective_rate_note
    assert r.local_taxes_note != ""


def test_corporate_json_roundtrip_and_xml():
    r = generate_corporate_return(
        "e10", "9998887776665", 2025,
        {"revenue": 10_000_000, "paid_in_capital": 200_000_000},
    )
    parsed = json.loads(r.to_json())
    assert parsed["corporate_tax"] == pytest.approx(2_320_000.0)
    assert "法人税申告書" in parsed["form"]
    xml = r.to_xml_saf_t()
    assert xml.startswith("<?xml")
    assert "<CorporateTax>2320000.00</CorporateTax>" in xml
    assert 'form="法人税申告書"' in xml


# ── Individual: national income tax (所得税) + reconstruction surtax ────────────

def test_individual_bracketed_with_surtax():
    """Income 5,480,000, basic deduction 480,000 → taxable 5,000,000.
    Progressive tax = 572,500; surtax = 572,500 * 0.021 = 12,022.5."""
    r = generate_individual_return(
        "p1", "enc", 2025, {"employment_income": 5_480_000},
    )
    assert r.taxable_income == pytest.approx(5_000_000.0)
    assert r.income_tax == pytest.approx(572_500.0)
    assert r.reconstruction_surtax == pytest.approx(572_500.0 * 0.021)
    assert r.reconstruction_surtax == pytest.approx(12_022.5)
    assert r.total_tax == pytest.approx(584_522.5)


def test_individual_basic_deduction_applied():
    """Default basic deduction of ¥480,000 is applied."""
    r = generate_individual_return("p2", "enc", 2025, {"employment_income": 1_000_000})
    assert r.basic_deduction == pytest.approx(480_000.0)
    assert r.taxable_income == pytest.approx(520_000.0)
    assert r.income_tax == pytest.approx(520_000 * 0.05)


def test_individual_surtax_is_2_1_percent_of_income_tax():
    r = generate_individual_return("p3", "enc", 2025, {"business_income": 12_000_000})
    assert r.reconstruction_surtax == pytest.approx(r.income_tax * 0.021)


def test_individual_zero_and_below_deduction():
    """Income below the basic deduction → zero tax."""
    r_zero = generate_individual_return("p4", "enc", 2025, {})
    assert r_zero.income_tax == pytest.approx(0.0)
    assert r_zero.total_tax == pytest.approx(0.0)
    r_low = generate_individual_return("p5", "enc", 2025, {"employment_income": 300_000})
    assert r_low.taxable_income == pytest.approx(0.0)
    assert r_low.income_tax == pytest.approx(0.0)


def test_individual_deadline_march_15():
    r = generate_individual_return("p6", "enc", 2025, {"employment_income": 1_000_000})
    assert r.filing_deadline == "2026-03-15"


def test_individual_withholding_and_json_xml():
    r = generate_individual_return(
        "p7", "enc", 2025,
        {"employment_income": 5_480_000, "withholding_tax_paid": 500_000},
    )
    assert r.tax_payable == pytest.approx(584_522.5 - 500_000)
    parsed = json.loads(r.to_json())
    assert parsed["income_tax"] == pytest.approx(572_500.0)
    assert "確定申告書" in parsed["form"]
    xml = r.to_xml_saf_t()
    assert xml.startswith("<?xml")
    assert "<ReconstructionSurtax>" in xml
    assert 'form="確定申告書"' in xml


def test_dataclasses_direct_compute():
    """Dataclasses compute() work without the generate_* helpers."""
    c = CorporateTaxReturn(
        entity_id="d1", corporate_number="1", fiscal_year=2025,
        revenue=10_000_000, paid_in_capital=200_000_000,
    ).compute()
    assert c.corporate_tax == pytest.approx(2_320_000.0)
    i = IndividualTaxReturn(
        person_id="d2", my_number_encrypted="enc", fiscal_year=2025,
        employment_income=5_480_000,
    ).compute()
    assert i.total_tax == pytest.approx(584_522.5)
