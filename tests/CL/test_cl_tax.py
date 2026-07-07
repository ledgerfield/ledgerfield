"""Republic of Chile tax property tests — 11 tests."""
import json
import os

import pytest

from ledgerfield.schemas.CL.cl_gaap import CL_GAAP
from ledgerfield.tax.CL.cit import bereken_cit_chili

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/CL/params.json",
)


def _params():
    with open(PARAMS_PATH) as f:
        return json.load(f)


# 1 — schema coverage (incl. IVA accounts)
def test_cl_schema_min_60_accounts():
    assert len(CL_GAAP) >= 60
    names = " ".join(a.name for a in CL_GAAP)
    assert "IVA" in names


# 2 — First Category Tax rate = 27%
def test_cit_rate_27pct():
    assert _params()["cit"]["standard_rate"] == pytest.approx(0.27)


# 3 — general regime: 1,000,000 → 270,000
def test_general_regime_270k():
    result = bereken_cit_chili(1_000_000.0, 2025)
    assert result.cit_totaal == pytest.approx(270_000.0)
    assert result.cit_rate == pytest.approx(0.27)


# 4 — Pro Pyme SME regime: 1,000,000 → 250,000
def test_pro_pyme_250k():
    result = bereken_cit_chili(1_000_000.0, 2025, pro_pyme=True)
    assert result.cit_totaal == pytest.approx(250_000.0)
    assert result.cit_rate == pytest.approx(0.25)


# 5 — effectief tarief matches the applied rate
def test_effectief_tarief():
    assert bereken_cit_chili(2_000_000.0, 2025).effectief_tarief == pytest.approx(0.27)
    assert bereken_cit_chili(2_000_000.0, 2025, pro_pyme=True).effectief_tarief == pytest.approx(0.25)


# 6 — non-positive profit yields zero tax (defensive guard)
def test_non_positive_profit_zero_tax():
    assert bereken_cit_chili(0.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_chili(-50_000.0, 2025).cit_totaal == pytest.approx(0.0)
    assert bereken_cit_chili(-50_000.0, 2025).effectief_tarief == pytest.approx(0.0)


# 7 — VAT (IVA) = 19%
def test_vat_19pct():
    assert _params()["vat"]["standard_rate"] == pytest.approx(0.19)
    assert _params()["vat"]["implemented"] is True


# 8 — semi-integrated shareholder credit 65% note present
def test_partial_integration_credit_65pct():
    credit = _params()["cit"]["shareholder_credit"]
    assert credit["partial_integration_credit"] == pytest.approx(0.65)
    assert "65%" in credit["note"]


# 9 — Pro Pyme note mentions transitory 12.5% proposal
def test_pro_pyme_note_present():
    assert _params()["cit"]["pro_pyme_rate"] == pytest.approx(0.25)
    assert "12.5%" in _params()["cit"]["pro_pyme_note"]


# 10 — official source is the SII
def test_official_source_sii():
    sources = _params()["metadata"]["official_sources"]
    assert any("sii.cl" in s["url"] for s in sources)


# 11 — effective date range covers 2025
def test_effective_date_range_2025():
    rng = _params()["metadata"]["effective_date_range"]
    assert rng["start"] == "2025-01-01"
    assert rng["end"] == "2025-12-31"
