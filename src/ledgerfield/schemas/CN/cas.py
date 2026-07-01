"""
China Accounting Standards (CAS) chart of accounts.
企业会计准则 (Enterprise Accounting Standards) — MOF
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CASAccount:
    code: str
    name_zh: str
    name_en: str
    account_class: str


_ACCOUNTS_RAW: List[Dict[str, str]] = [
    # 资产类 Assets (1xxx)
    {"code": "1001", "name_zh": "库存现金",         "name_en": "Cash on hand",                    "account_class": "Assets"},
    {"code": "1002", "name_zh": "银行存款",          "name_en": "Bank deposits",                   "account_class": "Assets"},
    {"code": "1012", "name_zh": "其他货币资金",      "name_en": "Other monetary assets",            "account_class": "Assets"},
    {"code": "1101", "name_zh": "交易性金融资产",    "name_en": "Trading financial assets",         "account_class": "Assets"},
    {"code": "1121", "name_zh": "应收票据",          "name_en": "Bills receivable",                 "account_class": "Assets"},
    {"code": "1122", "name_zh": "应收账款",          "name_en": "Accounts receivable",              "account_class": "Assets"},
    {"code": "1123", "name_zh": "预付账款",          "name_en": "Advance payments",                 "account_class": "Assets"},
    {"code": "1131", "name_zh": "应收股利",          "name_en": "Dividends receivable",             "account_class": "Assets"},
    {"code": "1132", "name_zh": "应收利息",          "name_en": "Interest receivable",              "account_class": "Assets"},
    {"code": "1221", "name_zh": "其他应收款",        "name_en": "Other receivables",                "account_class": "Assets"},
    {"code": "1401", "name_zh": "材料采购",          "name_en": "Material purchases",               "account_class": "Assets"},
    {"code": "1402", "name_zh": "在途物资",          "name_en": "Goods in transit",                 "account_class": "Assets"},
    {"code": "1403", "name_zh": "原材料",            "name_en": "Raw materials",                    "account_class": "Assets"},
    {"code": "1405", "name_zh": "库存商品",          "name_en": "Merchandise inventory",            "account_class": "Assets"},
    {"code": "1411", "name_zh": "周转材料",          "name_en": "Turnover materials",               "account_class": "Assets"},
    {"code": "1461", "name_zh": "消耗性生物资产",    "name_en": "Consumable biological assets",     "account_class": "Assets"},
    {"code": "1501", "name_zh": "持有至到期投资",    "name_en": "HTM investments",                  "account_class": "Assets"},
    {"code": "1511", "name_zh": "可供出售金融资产",  "name_en": "AFS assets",                       "account_class": "Assets"},
    {"code": "1521", "name_zh": "长期股权投资",      "name_en": "Long-term equity investments",     "account_class": "Assets"},
    {"code": "1601", "name_zh": "固定资产",          "name_en": "Fixed assets",                     "account_class": "Assets"},
    {"code": "1602", "name_zh": "累计折旧",          "name_en": "Accumulated depreciation",         "account_class": "Assets"},
    {"code": "1604", "name_zh": "在建工程",          "name_en": "Construction in progress",         "account_class": "Assets"},
    {"code": "1605", "name_zh": "工程物资",          "name_en": "Construction materials",           "account_class": "Assets"},
    {"code": "1611", "name_zh": "固定资产清理",      "name_en": "Fixed asset disposal",             "account_class": "Assets"},
    {"code": "1701", "name_zh": "无形资产",          "name_en": "Intangible assets",                "account_class": "Assets"},
    {"code": "1702", "name_zh": "累计摊销",          "name_en": "Accumulated amortization",         "account_class": "Assets"},
    {"code": "1711", "name_zh": "商誉",              "name_en": "Goodwill",                         "account_class": "Assets"},
    {"code": "1801", "name_zh": "长期待摊费用",      "name_en": "Long-term deferred expenses",      "account_class": "Assets"},
    {"code": "1811", "name_zh": "递延所得税资产",    "name_en": "Deferred tax assets",              "account_class": "Assets"},

    # 负债类 Liabilities (2xxx)
    {"code": "2001", "name_zh": "短期借款",          "name_en": "Short-term loans",                 "account_class": "Liabilities"},
    {"code": "2201", "name_zh": "应付票据",          "name_en": "Bills payable",                    "account_class": "Liabilities"},
    {"code": "2202", "name_zh": "应付账款",          "name_en": "Accounts payable",                 "account_class": "Liabilities"},
    {"code": "2203", "name_zh": "预收账款",          "name_en": "Advance receipts",                 "account_class": "Liabilities"},
    {"code": "2211", "name_zh": "应付职工薪酬",      "name_en": "Employee compensation payable",    "account_class": "Liabilities"},
    {"code": "2221", "name_zh": "应交税费",          "name_en": "Taxes payable (VAT/CIT/IIT)",      "account_class": "Liabilities"},
    {"code": "2231", "name_zh": "应付利息",          "name_en": "Interest payable",                 "account_class": "Liabilities"},
    {"code": "2232", "name_zh": "应付股利",          "name_en": "Dividends payable",                "account_class": "Liabilities"},
    {"code": "2241", "name_zh": "其他应付款",        "name_en": "Other payables",                   "account_class": "Liabilities"},
    {"code": "2401", "name_zh": "长期借款",          "name_en": "Long-term loans",                  "account_class": "Liabilities"},
    {"code": "2411", "name_zh": "应付债券",          "name_en": "Bonds payable",                    "account_class": "Liabilities"},
    {"code": "2501", "name_zh": "长期应付款",        "name_en": "Long-term payables",               "account_class": "Liabilities"},
    {"code": "2502", "name_zh": "未确认融资费用",    "name_en": "Unrecognized finance costs",        "account_class": "Liabilities"},
    {"code": "2601", "name_zh": "递延收益",          "name_en": "Deferred income",                  "account_class": "Liabilities"},
    {"code": "2701", "name_zh": "递延所得税负债",    "name_en": "Deferred tax liabilities",         "account_class": "Liabilities"},

    # 所有者权益 Equity (4xxx)
    {"code": "4001", "name_zh": "实收资本",          "name_en": "Paid-in capital",                  "account_class": "Equity"},
    {"code": "4002", "name_zh": "资本公积",          "name_en": "Capital surplus",                  "account_class": "Equity"},
    {"code": "4101", "name_zh": "盈余公积",          "name_en": "Surplus reserve",                  "account_class": "Equity"},
    {"code": "4103", "name_zh": "本年利润",          "name_en": "Current year profit",              "account_class": "Equity"},
    {"code": "4104", "name_zh": "利润分配",          "name_en": "Profit distribution",              "account_class": "Equity"},

    # 成本类 Cost (5xxx)
    {"code": "5001", "name_zh": "生产成本",          "name_en": "Production cost",                  "account_class": "Cost"},
    {"code": "5101", "name_zh": "制造费用",          "name_en": "Manufacturing overhead",            "account_class": "Cost"},
    {"code": "5201", "name_zh": "劳务成本",          "name_en": "Service cost",                     "account_class": "Cost"},
    {"code": "5301", "name_zh": "研发支出",          "name_en": "R&D expenditure",                  "account_class": "Cost"},

    # 损益类 P&L (6xxx)
    {"code": "6001", "name_zh": "主营业务收入",      "name_en": "Main business revenue",            "account_class": "P&L"},
    {"code": "6051", "name_zh": "其他业务收入",      "name_en": "Other business revenue",           "account_class": "P&L"},
    {"code": "6101", "name_zh": "公允价值变动损益",  "name_en": "Fair value changes",               "account_class": "P&L"},
    {"code": "6111", "name_zh": "投资收益",          "name_en": "Investment income",                "account_class": "P&L"},
    {"code": "6301", "name_zh": "主营业务成本",      "name_en": "Main business cost",               "account_class": "P&L"},
    {"code": "6401", "name_zh": "税金及附加",        "name_en": "Taxes and surcharges",             "account_class": "P&L"},
    {"code": "6601", "name_zh": "销售费用",          "name_en": "Selling expenses",                 "account_class": "P&L"},
    {"code": "6602", "name_zh": "管理费用",          "name_en": "Admin expenses",                   "account_class": "P&L"},
    {"code": "6603", "name_zh": "研发费用",          "name_en": "R&D expenses",                     "account_class": "P&L"},
    {"code": "6711", "name_zh": "营业外收入",        "name_en": "Non-operating income",             "account_class": "P&L"},
    {"code": "6801", "name_zh": "营业外支出",        "name_en": "Non-operating expenses",           "account_class": "P&L"},
    {"code": "6901", "name_zh": "所得税费用",        "name_en": "Income tax expense",               "account_class": "P&L"},
]

CAS_CN: List[CASAccount] = [
    CASAccount(
        code=r["code"],
        name_zh=r["name_zh"],
        name_en=r["name_en"],
        account_class=r["account_class"],
    )
    for r in _ACCOUNTS_RAW
]

_INDEX: Dict[str, CASAccount] = {a.code: a for a in CAS_CN}


def get_account(code: str) -> Optional[CASAccount]:
    """Return the CASAccount for the given 4-digit code, or None."""
    return _INDEX.get(code)


def accounts_by_class(account_class: str) -> List[CASAccount]:
    """Return all accounts belonging to *account_class* (case-sensitive)."""
    return [a for a in CAS_CN if a.account_class == account_class]


# ---------------------------------------------------------------------------
# JSON export
# ---------------------------------------------------------------------------

def schema_payload() -> dict[str, object]:
    """Return a JSON-serializable CAS schema payload."""

    return {
        "jurisdiction": "CN",
        "standard": "企业会计准则 (CAS)",
        "issuer": "Ministry of Finance of China (MOF)",
        "account_classes": ["Assets", "Liabilities", "Equity", "Cost", "P&L"],
        "accounts": [
            {
                "code": a.code,
                "name_zh": a.name_zh,
                "name_en": a.name_en,
                "account_class": a.account_class,
            }
            for a in CAS_CN
        ],
    }


def write_json_schema(path: str | Path | None = None) -> Path:
    """Write the CAS schema JSON to ``path`` and return the output path."""

    out = Path(path) if path is not None else Path(__file__).with_name("cas_schema.json")
    out.write_text(json.dumps(schema_payload(), ensure_ascii=False, indent=2), encoding="utf-8")
    return out
