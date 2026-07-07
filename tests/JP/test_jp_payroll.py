"""Tests for the JP 給与明細 (kyuyo meisai) payroll module."""
import json

import pytest

from ledgerfield.payroll.JP.kyuyo_meisai import (
    Employee,
    PayslipLine,
    PayslipLineType,
    generate_payslip,
)


def _emp(gross=400_000, **kw):
    return Employee(id="e1", name="Tanaka Taro", gross_salary=gross, **kw)


def test_400k_social_insurance_amounts():
    p = generate_payslip(_emp(400_000), "2025-07")
    by_type = {ln.line_type: ln.amount for ln in p.lines}
    assert by_type[PayslipLineType.HEALTH_INSURANCE] == pytest.approx(-19_960, abs=1)
    assert by_type[PayslipLineType.PENSION] == pytest.approx(-36_600, abs=1)
    assert by_type[PayslipLineType.EMPLOYMENT_INSURANCE] == pytest.approx(-2_400, abs=1)


def test_net_equals_gross_minus_deductions():
    p = generate_payslip(_emp(400_000), "2025-07")
    assert p.net() == pytest.approx(p.gross() - p.deductions(), abs=1e-6)


def test_income_tax_positive_and_less_than_gross():
    p = generate_payslip(_emp(400_000), "2025-07")
    tax = next(
        -ln.amount for ln in p.lines
        if ln.line_type == PayslipLineType.INCOME_TAX_WITHHOLDING
    )
    assert tax > 0
    assert tax < p.gross()


def test_zero_salary_zero_deductions():
    p = generate_payslip(_emp(0), "2025-07")
    assert p.gross() == 0
    assert p.deductions() == pytest.approx(0.0, abs=1e-9)
    assert p.net() == pytest.approx(0.0, abs=1e-9)


def test_to_json_round_trips():
    p = generate_payslip(_emp(400_000), "2025-07")
    s = p.to_json()
    data = json.loads(s)
    assert data == p.to_dict()
    assert data["net"] == round(p.net(), 2)
    assert data["gross"] == 400_000


def test_enum_line_types_present():
    p = generate_payslip(_emp(400_000), "2025-07")
    present = {ln.line_type for ln in p.lines}
    for expected in {
        PayslipLineType.GROSS_SALARY,
        PayslipLineType.HEALTH_INSURANCE,
        PayslipLineType.PENSION,
        PayslipLineType.EMPLOYMENT_INSURANCE,
        PayslipLineType.INCOME_TAX_WITHHOLDING,
        PayslipLineType.EMPLOYER_COST,
    }:
        assert expected in present


def test_surtax_included():
    # Withholding must exceed the plain national tax by the 2.1% surtax factor.
    from ledgerfield.payroll.JP.kyuyo_meisai import (
        _annual_income_tax_withholding,
        _national_income_tax,
        _employment_income_deduction,
        BASIC_DEDUCTION,
    )
    gross = 400_000
    annual_gross = gross * 12
    # social insurance annual for this gross
    p = generate_payslip(_emp(gross), "2025-07")
    annual_social = p.deductions() * 0  # placeholder, recompute below
    social_month = (
        gross * 0.0499 + gross * 0.0915 + gross * 0.006
    )
    annual_social = social_month * 12
    with_surtax = _annual_income_tax_withholding(annual_gross, annual_social)
    taxable = annual_gross - annual_social - _employment_income_deduction(annual_gross) - BASIC_DEDUCTION
    base = _national_income_tax(max(0.0, taxable))
    assert with_surtax == pytest.approx(base * 1.021, rel=1e-9)
    assert with_surtax > base


def test_deterministic():
    a = generate_payslip(_emp(555_000), "2025-07").to_json()
    b = generate_payslip(_emp(555_000), "2025-07").to_json()
    assert a == b


def test_my_number_not_in_json_plaintext():
    e = _emp(400_000)
    e.my_number_note = "encrypted-in-vault"
    p = generate_payslip(e, "2025-07")
    blob = p.to_json()
    # The raw My Number must never appear; only the note/id are serialized.
    assert "123456789012" not in blob
    assert "my_number" not in blob.lower()


def test_employer_cost_is_informational_not_in_net():
    p = generate_payslip(_emp(400_000), "2025-07")
    assert p.employer_cost() > 0
    net_from_lines = sum(
        ln.amount for ln in p.lines
        if ln.line_type != PayslipLineType.EMPLOYER_COST
    )
    assert p.net() == pytest.approx(net_from_lines, abs=1e-9)


def test_resident_tax_note_present_not_withheld():
    p = generate_payslip(_emp(400_000), "2025-07")
    assert "住民税" in p.resident_tax_note
    # resident tax must not be a deduction line
    assert all("住民税" not in ln.label for ln in p.lines)


def test_higher_salary_higher_tax():
    low = generate_payslip(_emp(300_000), "2025-07")
    high = generate_payslip(_emp(900_000), "2025-07")
    def tax(p):
        return next(
            -ln.amount for ln in p.lines
            if ln.line_type == PayslipLineType.INCOME_TAX_WITHHOLDING
        )
    assert tax(high) > tax(low)


def test_payslip_line_dataclass_fields():
    ln = PayslipLine(PayslipLineType.GROSS_SALARY, "総支給額", 400_000)
    assert ln.line_type == PayslipLineType.GROSS_SALARY
    assert ln.amount == 400_000
