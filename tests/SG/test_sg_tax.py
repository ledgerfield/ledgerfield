"""Singapore tax property tests — 10 tests."""
import json
import os

import pytest

from ledgerfield.schemas.SG.sg_gaap import SG_GAAP
from ledgerfield.tax.SG.cit import bereken_cit_singapore

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/SG/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage
def test_sg_schema_min_60_accounts():
    assert len(SG_GAAP) >= 60


# 2 — CIT flat rate = 17% (before exemptions)
def test_cit_flat_rate_17pct():
    assert _params()["cit"]["flat_rate"] == pytest.approx(0.17)


# 3 — effective rate is below 17% due to partial exemption
def test_effective_rate_below_17pct_due_to_exemption():
    result = bereken_cit_singapore(200_000.0, 2025)
    assert result.effectief_tarief < 0.17


# 4 — GST rate = 9%
def test_gst_rate_9pct():
    assert _params()["gst"]["rate"] == pytest.approx(0.09)


# 5 — CPF employer rate (age <=55) = 17%
def test_cpf_employer_rate_17pct():
    assert _params()["cpf"]["employer_rate_below_55"] == pytest.approx(0.17)


# 6 — CPF employee rate (age <=55) = 20%
def test_cpf_employee_rate_20pct():
    assert _params()["cpf"]["employee_rate_below_55"] == pytest.approx(0.20)


# 7 — first tranche exemption: SGD 10k * 75% = SGD 7,500
def test_first_tranche_exemption_7500():
    result = bereken_cit_singapore(200_000.0, 2025)
    assert result.exemption_first == pytest.approx(7_500.0)


# 8 — second tranche exemption: SGD 190k * 50% = SGD 95,000
def test_second_tranche_exemption_95000():
    result = bereken_cit_singapore(200_000.0, 2025)
    assert result.exemption_second == pytest.approx(95_000.0)


# 9 — zero profit returns zero CIT
def test_bereken_cit_singapore_zero_winst():
    result = bereken_cit_singapore(0.0, 2025)
    assert result.cit_totaal == pytest.approx(0.0)


# 10 — CIT on SGD 200k: taxable = 97,500; CIT = 97,500 * 0.17 = 16,575
def test_bereken_cit_singapore_total_on_200k():
    result = bereken_cit_singapore(200_000.0, 2025)
    expected = (200_000.0 - 7_500.0 - 95_000.0) * 0.17
    assert result.cit_totaal == pytest.approx(expected)
