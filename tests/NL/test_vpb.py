"""VPB (Vennootschapsbelasting) tests — NL 2022-2025. 15 tests."""
import json
import os

import pytest

from ledgerfield.tax.NL.vpb import bereken_vpb, VPBResult

PARAMS_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../src/ledgerfield/tax/NL/params.json",
)


def _params(jaar):
    return json.load(open(PARAMS_PATH))["years"][str(jaar)]


# --- 2022 tarieven ---

def test_2022_schijf_1_tarief():
    assert _params(2022)["VPB"]["tarief_schijf_1"] == pytest.approx(0.15)


def test_2022_schijf_1_grens():
    assert _params(2022)["VPB"]["schijf_1_grens"] == 395000


# --- 2023 tarieven ---

def test_2023_schijf_1_tarief():
    assert _params(2023)["VPB"]["tarief_schijf_1"] == pytest.approx(0.19)


def test_2023_schijf_1_grens():
    assert _params(2023)["VPB"]["schijf_1_grens"] == 200000


# --- 2025 tarieven ---

def test_2025_schijf_1_tarief():
    assert _params(2025)["VPB"]["tarief_schijf_1"] == pytest.approx(0.19)


def test_2025_schijf_2_tarief():
    assert _params(2025)["VPB"]["tarief_schijf_2"] == pytest.approx(0.258)


# --- bereken_vpb resultaten ---

def test_vpb_200k_2025_totaal():
    result = bereken_vpb(200000, 2025)
    assert result.vpb_totaal == pytest.approx(38000.0)


def test_vpb_nul_winst():
    result = bereken_vpb(0, 2025)
    assert result.vpb_totaal == pytest.approx(0.0)


def test_vpb_400k_schijf_1():
    result = bereken_vpb(400000, 2025)
    assert result.vpb_schijf_1 == pytest.approx(38000.0)


def test_vpb_400k_schijf_2():
    result = bereken_vpb(400000, 2025)
    assert result.vpb_schijf_2 == pytest.approx(51600.0)


# --- effectief tarief ---

def test_effectief_tarief_200k():
    result = bereken_vpb(200000, 2025)
    assert result.effectief_tarief == pytest.approx(0.19, rel=1e-4)


def test_effectief_tarief_progressief():
    laag = bereken_vpb(200000, 2025)
    hoog = bereken_vpb(400000, 2025)
    assert hoog.effectief_tarief > laag.effectief_tarief


# --- Innovatiebox 2025 ---

def test_innovatiebox_aanwezig_2025():
    ibox = _params(2025)["Innovatiebox"]
    assert ibox["effectief_tarief"] == pytest.approx(0.09)


# --- WBSO 2025 ---

def test_wbso_2025_schijf_1_tarief():
    assert _params(2025)["WBSO"]["tarief_schijf_1"] == pytest.approx(0.36)


def test_wbso_2025_schijf_1_grens():
    assert _params(2025)["WBSO"]["schijf_1_grens"] == 380000
