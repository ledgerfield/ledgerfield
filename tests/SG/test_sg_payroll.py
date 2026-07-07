"""Tests for the Singapore payroll/payslip module (2025)."""
import json

import pytest

from ledgerfield.payroll.SG.payslip import (
    AgeBand,
    Employee,
    Payslip,
    PayslipLine,
    PayslipLineType,
    generate_payslip,
)


def _emp(gross, **kw):
    return Employee(id="E1", name="Tan Ah Kow", gross_salary=gross, **kw)


def test_cpf_employee_and_employer_6000():
    slip = generate_payslip(_emp(6000.0), "2025-01")
    assert slip.gross_salary() == 6000.0
    assert slip.cpf_employee() == pytest.approx(1200.0)   # 20%
    assert slip.cpf_employer() == pytest.approx(1020.0)   # 17%
    assert slip.net_salary() == pytest.approx(4800.0)


def test_ceiling_applied_10000():
    slip = generate_payslip(_emp(10000.0), "2025-01")
    # CPF only on capped 7,400
    assert slip.cpf_employee() == pytest.approx(1480.0)   # 20% x 7400
    assert slip.cpf_employer() == pytest.approx(1258.0)   # 17% x 7400
    assert slip.net_salary() == pytest.approx(8520.0)     # 10000 - 1480


def test_ceiling_boundary_exactly_7400():
    slip = generate_payslip(_emp(7400.0), "2025-01")
    assert slip.cpf_employee() == pytest.approx(1480.0)
    assert slip.net_salary() == pytest.approx(5920.0)


def test_age_band_parameter_above_55():
    slip = generate_payslip(_emp(6000.0, age_band=AgeBand.ABOVE_55_TO_60), "2025-01")
    assert slip.cpf_employee() == pytest.approx(1020.0)   # 17%
    assert slip.cpf_employer() == pytest.approx(930.0)    # 15.5%
    # Older band -> lower employee rate -> higher net than default 20%
    assert slip.net_salary() == pytest.approx(4980.0)


def test_no_income_tax_withheld_net_is_gross_minus_cpf():
    slip = generate_payslip(_emp(8888.0), "2025-01")
    assert slip.net_salary() == pytest.approx(
        slip.gross_salary() - slip.cpf_employee()
    )
    # No withholding line type exists at all.
    types = {ln.line_type for ln in slip.lines}
    assert PayslipLineType.NET_SALARY in types
    assert slip.income_tax_note != ""
    assert "annually" in slip.income_tax_note.lower()


def test_zero_gross_yields_zero():
    slip = generate_payslip(_emp(0.0), "2025-01")
    assert slip.gross_salary() == 0.0
    assert slip.cpf_employee() == 0.0
    assert slip.cpf_employer() == 0.0
    assert slip.sdl_employer() == 0.0
    assert slip.net_salary() == 0.0


def test_non_cpf_eligible_no_cpf():
    slip = generate_payslip(_emp(6000.0, is_cpf_eligible=False), "2025-01")
    assert slip.cpf_employee() == 0.0
    assert slip.cpf_employer() == 0.0
    assert slip.net_salary() == pytest.approx(6000.0)


def test_sdl_note_present_and_capped():
    slip = generate_payslip(_emp(10000.0), "2025-01")
    sdl_lines = [ln for ln in slip.lines
                 if ln.line_type is PayslipLineType.SDL_EMPLOYER]
    assert len(sdl_lines) == 1
    assert "Skills Development Levy" in sdl_lines[0].description
    # 0.25% x 10000 = 25 -> capped at 11.25
    assert slip.sdl_employer() == pytest.approx(11.25)


def test_sdl_minimum_applied():
    # 0.25% x 500 = 1.25 -> floored at min 2.00
    slip = generate_payslip(_emp(500.0), "2025-01")
    assert slip.sdl_employer() == pytest.approx(2.0)


def test_to_json_round_trips():
    slip = generate_payslip(_emp(6000.0), "2025-03")
    payload = slip.to_json()
    data = json.loads(payload)
    assert data["gross_salary"] == 6000.0
    assert data["cpf_employee"] == 1200.0
    assert data["cpf_employer"] == 1020.0
    assert data["net_salary"] == 4800.0
    assert data["income_tax_note"]
    assert isinstance(data["lines"], list) and len(data["lines"]) == 5


def test_enum_and_dataclass_types():
    slip = generate_payslip(_emp(6000.0), "2025-01")
    assert isinstance(slip, Payslip)
    assert all(isinstance(ln, PayslipLine) for ln in slip.lines)
    assert all(isinstance(ln.line_type, PayslipLineType) for ln in slip.lines)
    assert isinstance(AgeBand.UP_TO_55, AgeBand)
    assert AgeBand.UP_TO_55.employee_rate == 0.20
    assert AgeBand.UP_TO_55.employer_rate == 0.17


def test_deterministic():
    a = generate_payslip(_emp(6000.0), "2025-01").to_json()
    b = generate_payslip(_emp(6000.0), "2025-01").to_json()
    assert a == b


def test_lines_have_expected_types():
    slip = generate_payslip(_emp(6000.0), "2025-01")
    types = [ln.line_type for ln in slip.lines]
    assert types == [
        PayslipLineType.GROSS_SALARY,
        PayslipLineType.CPF_EMPLOYEE,
        PayslipLineType.CPF_EMPLOYER,
        PayslipLineType.SDL_EMPLOYER,
        PayslipLineType.NET_SALARY,
    ]
