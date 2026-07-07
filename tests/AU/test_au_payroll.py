"""Australia payroll/payslip tests — annual estimator (FY2024-25 Stage 3)."""
import json

import pytest

from ledgerfield.payroll.AU.payslip import (
    Employee,
    Payslip,
    PayslipLine,
    PayslipLineType,
    generate_payslip,
)


def _emp(gross: float, **kw) -> Employee:
    return Employee(id="E1", name="Alice", gross_annual=gross, **kw)


# 1 — $90,000 PAYG = 16%*(45,000-18,200) + 30%*(90,000-45,000) = 17,788
def test_payg_90k():
    ps = generate_payslip(_emp(90_000.0))
    assert ps.income_tax_payg() == pytest.approx(17_788.0)


# 2 — Medicare levy 2% of 90,000 = 1,800
def test_medicare_90k():
    ps = generate_payslip(_emp(90_000.0))
    assert ps.medicare_levy() == pytest.approx(1_800.0)


# 3 — net = 90,000 - 17,788 - 1,800 = 70,412
def test_net_90k():
    ps = generate_payslip(_emp(90_000.0))
    assert ps.net_annual() == pytest.approx(70_412.0)


# 4 — super 12% of 90,000 = 10,800 (employer, NOT deducted from net)
def test_super_90k_not_in_net():
    ps = generate_payslip(_emp(90_000.0))
    assert ps.superannuation() == pytest.approx(10_800.0)
    # super must not reduce take-home pay
    assert ps.net_annual() == pytest.approx(70_412.0)
    assert ps.employer_cost() == pytest.approx(100_800.0)


# 5 — tax-free threshold: income at/below $18,200 => 0 PAYG
def test_tax_free_threshold_zero_tax():
    ps = generate_payslip(_emp(18_200.0))
    assert ps.income_tax_payg() == pytest.approx(0.0)


# 6 — zero income => everything zero
def test_zero_income():
    ps = generate_payslip(_emp(0.0))
    assert ps.gross() == 0.0
    assert ps.income_tax_payg() == 0.0
    assert ps.medicare_levy() == 0.0
    assert ps.superannuation() == 0.0
    assert ps.net_annual() == 0.0
    assert ps.employer_cost() == 0.0


# 7 — super_rate parameter override (10% -> 9,000)
def test_super_rate_override():
    ps = generate_payslip(_emp(90_000.0), super_rate=0.10)
    assert ps.superannuation() == pytest.approx(9_000.0)
    # net unaffected by super rate
    assert ps.net_annual() == pytest.approx(70_412.0)


# 8 — to_json round-trips to identical dict
def test_to_json_roundtrip():
    ps = generate_payslip(_emp(90_000.0))
    parsed = json.loads(ps.to_json())
    assert parsed == ps.to_dict()
    assert parsed["net_annual"] == pytest.approx(70_412.0)
    assert parsed["superannuation"] == pytest.approx(10_800.0)


# 9 — enum types on lines
def test_enum_line_types():
    ps = generate_payslip(_emp(90_000.0))
    types = {l.line_type for l in ps.lines}
    assert PayslipLineType.GROSS_SALARY in types
    assert PayslipLineType.INCOME_TAX_PAYG in types
    assert PayslipLineType.MEDICARE_LEVY in types
    assert PayslipLineType.SUPERANNUATION in types
    for l in ps.lines:
        assert isinstance(l, PayslipLine)
        assert isinstance(l.line_type, PayslipLineType)


# 10 — deterministic: two runs identical
def test_deterministic():
    a = generate_payslip(_emp(123_456.0)).to_dict()
    b = generate_payslip(_emp(123_456.0)).to_dict()
    assert a == b


# 11 — top bracket case: $200,000
#   16%*(45,000-18,200)=4,288; 30%*(135,000-45,000)=27,000;
#   37%*(190,000-135,000)=20,350; 45%*(200,000-190,000)=4,500 => 56,138
def test_payg_top_bracket_200k():
    ps = generate_payslip(_emp(200_000.0))
    assert ps.income_tax_payg() == pytest.approx(56_138.0)


# 12 — default super rate is 12%
def test_default_super_rate():
    ps = generate_payslip(_emp(50_000.0))
    assert ps.superannuation() == pytest.approx(6_000.0)


# 13 — employer_cost = gross + super, independent of deductions
def test_employer_cost_composition():
    ps = generate_payslip(_emp(90_000.0))
    assert ps.employer_cost() == pytest.approx(ps.gross() + ps.superannuation())


# 14 — Payslip carries metadata
def test_payslip_metadata():
    ps = generate_payslip(_emp(90_000.0), period="FY2025-26", year=2025)
    assert ps.employee_id == "E1"
    assert ps.period == "FY2025-26"
    assert ps.year == 2025
    assert isinstance(ps, Payslip)


# 15 — TFN stored on employee but not present in serialized payslip
def test_tfn_not_leaked_in_output():
    ps = generate_payslip(Employee(id="E2", name="Bob", tfn="123456789",
                                   gross_annual=90_000.0))
    assert "123456789" not in ps.to_json()
