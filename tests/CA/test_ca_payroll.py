"""Tests for the Canada (CA) payroll / paystub module — 2025 rules."""
import json

import pytest

from ledgerfield.payroll.CA.paystub import (
    Employee,
    LineType,
    Paystub,
    generate_paystub,
)


def _emp(gross, province="ON"):
    return Employee(id="E1", name="Jordan Tremblay", sin="000-000-000",
                    gross_annual=gross, province=province)


def test_cpp_80k():
    stub = generate_paystub(_emp(80_000))
    assert stub.cpp == pytest.approx(4034.10, abs=0.01)  # 5.95% of (71300-3500)


def test_cpp2_80k():
    stub = generate_paystub(_emp(80_000))
    assert stub.cpp2 == pytest.approx(348.0, abs=0.01)   # 4% of (80000-71300)


def test_ei_80k():
    stub = generate_paystub(_emp(80_000))
    assert stub.ei == pytest.approx(1077.48, abs=0.01)   # 1.64% of 65700


def test_federal_tax_80k():
    stub = generate_paystub(_emp(80_000))
    # 57375*0.15 + 22625*0.205 - 16129*0.15
    expected = 57375 * 0.15 + (80_000 - 57375) * 0.205 - 16129 * 0.15
    assert stub.federal_tax == pytest.approx(expected, abs=0.01)


def test_provincial_tax_ontario_80k():
    stub = generate_paystub(_emp(80_000))
    # 52886*0.0505 + 27114*0.0915 - 12747*0.0505
    expected = 52886 * 0.0505 + (80_000 - 52886) * 0.0915 - 12747 * 0.0505
    assert stub.provincial_tax == pytest.approx(expected, abs=0.01)


def test_net_is_gross_minus_all_deductions():
    stub = generate_paystub(_emp(80_000))
    total = stub.cpp + stub.cpp2 + stub.ei + stub.federal_tax + stub.provincial_tax
    assert stub.total_deductions() == pytest.approx(total, abs=0.01)
    assert stub.net_annual == pytest.approx(80_000 - total, abs=0.01)


def test_cpp_capped_at_ympe():
    # Very high earner: CPP frozen at (YMPE - exemption) * rate
    stub = generate_paystub(_emp(500_000))
    assert stub.cpp == pytest.approx((71300 - 3500) * 0.0595, abs=0.01)
    # CPP2 frozen at (YAMPE - YMPE) * rate
    assert stub.cpp2 == pytest.approx((81200 - 71300) * 0.04, abs=0.01)


def test_ei_capped():
    stub = generate_paystub(_emp(500_000))
    assert stub.ei == pytest.approx(65700 * 0.0164, abs=0.01)


def test_zero_gross_zero_everything():
    stub = generate_paystub(_emp(0))
    assert stub.gross() == 0
    assert stub.cpp == 0
    assert stub.cpp2 == 0
    assert stub.ei == 0
    assert stub.federal_tax == 0
    assert stub.provincial_tax == 0
    assert stub.net_annual == 0


def test_below_cpp_exemption_no_cpp():
    stub = generate_paystub(_emp(3000))
    assert stub.cpp == 0          # below 3500 basic exemption
    assert stub.cpp2 == 0


def test_to_json_round_trips():
    stub = generate_paystub(_emp(80_000))
    data = json.loads(stub.to_json())
    assert data["gross_annual"] == pytest.approx(80_000, abs=0.01)
    assert data["cpp"] == pytest.approx(4034.10, abs=0.01)
    assert data["province"] == "ON"
    assert len(data["lines"]) == 6
    assert data == stub.to_dict()


def test_province_parameter_overrides_default():
    stub = generate_paystub(_emp(80_000, province="ON"), province="ON")
    assert stub.province == "ON"
    # unsupported province raises (documented: extend table for others)
    with pytest.raises(ValueError):
        generate_paystub(_emp(80_000), province="QC")


def test_deterministic():
    a = generate_paystub(_emp(80_000)).to_json()
    b = generate_paystub(_emp(80_000)).to_json()
    assert a == b


def test_lines_have_expected_kinds():
    stub = generate_paystub(_emp(80_000))
    kinds = [l.kind for l in stub.lines]
    assert kinds == [
        LineType.GROSS_PAY, LineType.CPP, LineType.CPP2,
        LineType.EI, LineType.FEDERAL_TAX, LineType.PROVINCIAL_TAX,
    ]


def test_net_equals_line_sum():
    stub = generate_paystub(_emp(120_000))
    assert stub.net() == pytest.approx(sum(l.amount for l in stub.lines), abs=1e-9)
