"""Tests for the China payroll module (工资明细)."""
import json

import pytest

from ledgerfield.payroll.CN.gongzi_mingxi import (
    Employee,
    PayslipLine,
    PayslipLineType,
    Payslip,
    generate_payslip,
)


def _payslip_30k():
    emp = Employee(id="E1", name="张伟", gross_salary=30000.0)
    return emp, generate_payslip(emp, "2025-06", employer_id="ACME-CN")


def test_social_insurance_components_30k():
    _, ps = _payslip_30k()
    assert ps.pension == pytest.approx(2400.0)
    assert ps.medical == pytest.approx(600.0)
    assert ps.unemployment == pytest.approx(150.0)
    assert ps.housing_fund == pytest.approx(2100.0)


def test_social_total_30k():
    _, ps = _payslip_30k()
    # 2400 + 600 + 150 + 2100 = 5250 (17.5% of 30000)
    assert ps.social_insurance_and_housing == pytest.approx(5250.0)


def test_iit_30k_case():
    _, ps = _payslip_30k()
    # taxable = 30000 - 5250 - 5000 = 19750 → 20% bracket, QD 1410
    # IIT = 19750 * 0.20 - 1410 = 2540
    assert ps.iit_withholding == pytest.approx(2540.0)


def test_net_salary_30k():
    _, ps = _payslip_30k()
    # net = 30000 - 5250 - 2540 = 22210
    assert ps.net_salary == pytest.approx(22210.0)
    assert ps.net_salary == pytest.approx(
        ps.gross_salary - ps.social_insurance_and_housing - ps.iit_withholding
    )


def test_zero_salary_is_zero():
    emp = Employee(id="E0", name="零", gross_salary=0.0)
    ps = generate_payslip(emp, "2025-06")
    assert ps.gross_salary == 0.0
    assert ps.social_insurance_and_housing == 0.0
    assert ps.iit_withholding == 0.0
    assert ps.net_salary == 0.0


def test_5000_threshold_applied_no_tax_below():
    # Gross where taxable income falls to <= 0 after ¥5000 basic deduction.
    # gross 6000: social = 1050, taxable = 6000 - 1050 - 5000 = -50 → no IIT
    emp = Employee(id="E2", name="李", gross_salary=6000.0)
    ps = generate_payslip(emp, "2025-06")
    assert ps.iit_withholding == 0.0


def test_5000_threshold_boundary_lowest_bracket():
    # gross 8000: social = 1400, taxable = 8000 - 1400 - 5000 = 1600 → 3%
    # IIT = 1600 * 0.03 = 48
    emp = Employee(id="E3", name="王", gross_salary=8000.0)
    ps = generate_payslip(emp, "2025-06")
    assert ps.iit_withholding == pytest.approx(48.0)


def test_special_additional_deductions_reduce_iit():
    emp = Employee(id="E4", name="赵", gross_salary=30000.0,
                   special_additional_deductions=2000.0)
    ps = generate_payslip(emp, "2025-06")
    # taxable = 30000 - 5250 - 5000 - 2000 = 17750 → 20%, QD 1410
    # IIT = 17750 * 0.20 - 1410 = 2140
    assert ps.iit_withholding == pytest.approx(2140.0)


def test_to_json_round_trips():
    _, ps = _payslip_30k()
    payload = json.loads(ps.to_json())
    assert payload["employee_id"] == "E1"
    assert payload["gross_salary"] == 30000.0
    assert payload["net_salary"] == pytest.approx(22210.0)
    assert payload["iit_withholding"] == pytest.approx(2540.0)
    assert isinstance(payload["lines"], list)
    assert payload == ps.to_dict()


def test_enum_and_dataclass_types_present():
    _, ps = _payslip_30k()
    assert isinstance(ps, Payslip)
    assert all(isinstance(l, PayslipLine) for l in ps.lines)
    assert all(isinstance(l.line_type, PayslipLineType) for l in ps.lines)
    types = {l.line_type for l in ps.lines}
    assert PayslipLineType.GROSS_SALARY in types
    assert PayslipLineType.PENSION in types
    assert PayslipLineType.IIT_WITHHOLDING in types


def test_employer_contribution_line_excluded_from_net():
    _, ps = _payslip_30k()
    employer_lines = [l for l in ps.lines
                      if l.line_type == PayslipLineType.EMPLOYER_CONTRIBUTION]
    assert len(employer_lines) == 1
    assert employer_lines[0].amount > 0
    # Net must not include the employer note.
    assert ps.net_salary == pytest.approx(22210.0)


def test_deterministic():
    emp = Employee(id="E1", name="张伟", gross_salary=30000.0)
    a = generate_payslip(emp, "2025-06", employer_id="ACME-CN").to_json()
    b = generate_payslip(emp, "2025-06", employer_id="ACME-CN").to_json()
    assert a == b


def test_high_earner_top_bracket():
    # gross 200000: social = 35000, taxable = 200000 - 35000 - 5000 = 160000
    # > 80000 → 45%, QD 15160 → IIT = 160000*0.45 - 15160 = 56840
    emp = Employee(id="E5", name="高", gross_salary=200000.0)
    ps = generate_payslip(emp, "2025-06")
    assert ps.iit_withholding == pytest.approx(56840.0)
