"""Inkomstenbelasting (IB) tests — NL Box 1, 2, 3. 12 tests."""
import json
import os

import pytest

from ledgerfield.tax.NL.ib import (
    IBBox1Result,
    bereken_ib_box1,
    bereken_ib_box2,
    bereken_ib_box3,
)

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NL/params.json",
)


def _params(jaar):
    return json.load(open(PARAMS_PATH))["years"][str(jaar)]


# --- Box 1, 2025 ---

def test_box1_2025_tarief_schijf_1():
    assert _params(2025)["IB"]["tarief_schijf_1"] == pytest.approx(0.3550)


def test_box1_2025_schijf_1_grens():
    assert _params(2025)["IB"]["schijf_1_grens"] == 76817


def test_box1_belasting_groeit_met_inkomen():
    laag = bereken_ib_box1(40000, 2025)
    hoog = bereken_ib_box1(80000, 2025)
    assert hoog.ib_voor_heffingskortingen > laag.ib_voor_heffingskortingen


def test_box1_result_type():
    result = bereken_ib_box1(50000, 2025)
    assert isinstance(result, IBBox1Result)


# --- Box 2, 2025 ---

def test_box2_2025_tarief_schijf_1():
    result = bereken_ib_box2(10000, 2025)
    assert result.tarief_schijf_1 == pytest.approx(0.245)


def test_box2_2025_schijf_1_grens():
    result = bereken_ib_box2(10000, 2025)
    assert result.schijf_1_grens == pytest.approx(67804)


def test_box2_2025_tarief_schijf_2():
    result = bereken_ib_box2(10000, 2025)
    assert result.tarief_schijf_2 == pytest.approx(0.31)


# --- Box 3, 2025 ---

def test_box3_2025_heffingsvrij():
    result = bereken_ib_box3(57684, 2025)
    assert result.heffingsvrij == pytest.approx(57684)


def test_box3_2025_forfait():
    result = bereken_ib_box3(100000, 2025)
    assert result.forfaitair_rendement == pytest.approx(0.0588)


def test_box3_2025_tarief():
    p = _params(2025)["Box3"]
    assert p["tarief"] == pytest.approx(0.36)


def test_box3_onder_heffingsvrij_geen_belasting():
    result = bereken_ib_box3(57684, 2025)
    assert result.ib_box3 == pytest.approx(0.0)


def test_box3_boven_heffingsvrij_belasting_positief():
    result = bereken_ib_box3(100000, 2025)
    assert result.ib_box3 > 0
