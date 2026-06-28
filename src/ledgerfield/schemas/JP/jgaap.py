"""J-GAAP — Japan GAAP chart of accounts (会社法 / 金融商品取引法).

70+ accounts covering 流動資産/固定資産/流動負債/固定負債/純資産/売上高/売上原価/販管費/営業外損益.
"""
from __future__ import annotations
from dataclasses import dataclass

__all__ = ["JGAAPAccount", "JGAAP_JP", "get_account", "accounts_by_class"]


@dataclass(frozen=True)
class JGAAPAccount:
    code: str           # 4-digit account code
    name_ja: str        # Japanese account name
    name_en: str        # English account name
    account_class: str  # 流動資産, 固定資産, 流動負債, 固定負債, 純資産, 売上高, 売上原価, 販売費及び一般管理費, 営業外損益

    @property
    def is_asset(self) -> bool:
        return self.account_class in ("流動資産", "固定資産")

    @property
    def is_liability(self) -> bool:
        return self.account_class in ("流動負債", "固定負債")

    @property
    def is_equity(self) -> bool:
        return self.account_class == "純資産"

    @property
    def is_revenue(self) -> bool:
        return self.account_class == "売上高"

    @property
    def is_expense(self) -> bool:
        return self.account_class in ("売上原価", "販売費及び一般管理費", "営業外損益")


JGAAP_JP: list[JGAAPAccount] = [
    # ── 流動資産 Current Assets ───────────────────────────────────────────────
    JGAAPAccount("1010", "現金",           "Cash",                         "流動資産"),
    JGAAPAccount("1020", "普通預金",        "Bank (ordinary deposit)",      "流動資産"),
    JGAAPAccount("1030", "定期預金",        "Time deposit",                 "流動資産"),
    JGAAPAccount("1110", "売掛金",          "Accounts receivable",          "流動資産"),
    JGAAPAccount("1120", "受取手形",        "Notes receivable",             "流動資産"),
    JGAAPAccount("1200", "棚卸資産",        "Inventory",                    "流動資産"),
    JGAAPAccount("1210", "製品",            "Finished goods",               "流動資産"),
    JGAAPAccount("1220", "仕掛品",          "Work in progress",             "流動資産"),
    JGAAPAccount("1230", "原材料",          "Raw materials",                "流動資産"),
    JGAAPAccount("1300", "前払費用",        "Prepaid expenses",             "流動資産"),
    JGAAPAccount("1310", "短期貸付金",      "Short-term loans receivable",  "流動資産"),
    JGAAPAccount("1400", "未収入金",        "Accrued income",               "流動資産"),
    JGAAPAccount("1410", "仮払消費税",      "VAT paid (input tax)",         "流動資産"),

    # ── 固定資産 Fixed Assets ─────────────────────────────────────────────────
    JGAAPAccount("2010", "建物",            "Buildings",                    "固定資産"),
    JGAAPAccount("2020", "機械装置",        "Machinery and equipment",      "固定資産"),
    JGAAPAccount("2030", "車両運搬具",      "Vehicles",                     "固定資産"),
    JGAAPAccount("2040", "工具器具備品",    "Tools and fixtures",           "固定資産"),
    JGAAPAccount("2050", "土地",            "Land",                         "固定資産"),
    JGAAPAccount("2060", "建設仮勘定",      "Construction in progress",     "固定資産"),
    JGAAPAccount("2110", "ソフトウェア",    "Software",                     "固定資産"),
    JGAAPAccount("2120", "特許権",          "Patents",                      "固定資産"),
    JGAAPAccount("2130", "のれん",          "Goodwill",                     "固定資産"),
    JGAAPAccount("2200", "投資有価証券",    "Investment securities",        "固定資産"),
    JGAAPAccount("2210", "関係会社株式",    "Subsidiary shares",            "固定資産"),
    JGAAPAccount("2220", "長期貸付金",      "Long-term loans receivable",   "固定資産"),
    JGAAPAccount("2230", "繰延税金資産",    "Deferred tax asset",           "固定資産"),

    # ── 流動負債 Current Liabilities ──────────────────────────────────────────
    JGAAPAccount("3010", "買掛金",          "Accounts payable",             "流動負債"),
    JGAAPAccount("3020", "支払手形",        "Notes payable",                "流動負債"),
    JGAAPAccount("3110", "未払費用",        "Accrued expenses",             "流動負債"),
    JGAAPAccount("3120", "未払法人税等",    "Corporation tax payable",      "流動負債"),
    JGAAPAccount("3130", "未払消費税",      "VAT payable (output tax)",     "流動負債"),
    JGAAPAccount("3140", "預り金",          "Deposits received",            "流動負債"),
    JGAAPAccount("3150", "前受金",          "Advance payments received",    "流動負債"),
    JGAAPAccount("3200", "短期借入金",      "Short-term loans payable",     "流動負債"),

    # ── 固定負債 Non-current Liabilities ─────────────────────────────────────
    JGAAPAccount("4010", "長期借入金",      "Long-term loans payable",      "固定負債"),
    JGAAPAccount("4020", "社債",            "Bonds payable",                "固定負債"),
    JGAAPAccount("4030", "退職給付引当金",  "Retirement benefit obligation","固定負債"),
    JGAAPAccount("4040", "繰延税金負債",    "Deferred tax liability",       "固定負債"),

    # ── 純資産 Net Assets / Equity ────────────────────────────────────────────
    JGAAPAccount("5010", "資本金",          "Capital stock",                "純資産"),
    JGAAPAccount("5020", "資本準備金",      "Capital surplus",              "純資産"),
    JGAAPAccount("5030", "利益準備金",      "Legal retained earnings",      "純資産"),
    JGAAPAccount("5040", "繰越利益剰余金",  "Retained earnings",            "純資産"),
    JGAAPAccount("5050", "当期純利益",      "Net income for period",        "純資産"),

    # ── 売上高 Revenue ────────────────────────────────────────────────────────
    JGAAPAccount("6010", "売上高",          "Sales revenue",                "売上高"),
    JGAAPAccount("6020", "サービス収益",    "Service revenue",              "売上高"),
    JGAAPAccount("6030", "受取利息",        "Interest income",              "売上高"),
    JGAAPAccount("6040", "受取配当金",      "Dividend income",              "売上高"),
    JGAAPAccount("6050", "雑収入",          "Miscellaneous income",         "売上高"),

    # ── 売上原価 Cost of Sales ────────────────────────────────────────────────
    JGAAPAccount("7010", "売上原価",        "Cost of goods sold",           "売上原価"),
    JGAAPAccount("7020", "外注費",          "Subcontracting costs",         "売上原価"),

    # ── 販管費 SG&A (販売費及び一般管理費) ───────────────────────────────────
    JGAAPAccount("8010", "給料手当",        "Salaries and wages",           "販売費及び一般管理費"),
    JGAAPAccount("8020", "役員報酬",        "Executive compensation",       "販売費及び一般管理費"),
    JGAAPAccount("8030", "法定福利費",      "Statutory welfare costs",      "販売費及び一般管理費"),
    JGAAPAccount("8040", "福利厚生費",      "Employee welfare costs",       "販売費及び一般管理費"),
    JGAAPAccount("8050", "地代家賃",        "Rent",                         "販売費及び一般管理費"),
    JGAAPAccount("8060", "水道光熱費",      "Utilities",                    "販売費及び一般管理費"),
    JGAAPAccount("8070", "通信費",          "Communications",               "販売費及び一般管理費"),
    JGAAPAccount("8080", "旅費交通費",      "Travel expenses",              "販売費及び一般管理費"),
    JGAAPAccount("8090", "交際費",          "Entertainment (tax-limited)",  "販売費及び一般管理費"),
    JGAAPAccount("8100", "広告宣伝費",      "Advertising",                  "販売費及び一般管理費"),
    JGAAPAccount("8110", "消耗品費",        "Consumables",                  "販売費及び一般管理費"),
    JGAAPAccount("8120", "減価償却費",      "Depreciation",                 "販売費及び一般管理費"),
    JGAAPAccount("8130", "支払手数料",      "Professional fees",            "販売費及び一般管理費"),
    JGAAPAccount("8140", "保険料",          "Insurance",                    "販売費及び一般管理費"),
    JGAAPAccount("8150", "租税公課",        "Taxes and dues",               "販売費及び一般管理費"),
    JGAAPAccount("8160", "研究開発費",      "R&D expenses",                 "販売費及び一般管理費"),

    # ── 営業外損益 Non-operating Income/Expense ───────────────────────────────
    JGAAPAccount("9010", "支払利息",        "Interest expense",             "営業外損益"),
    JGAAPAccount("9020", "為替差損益",      "Foreign exchange gain/loss",   "営業外損益"),
    JGAAPAccount("9030", "法人税等",        "Corporation tax expense",      "営業外損益"),
    JGAAPAccount("9040", "法人税等調整額",  "Deferred tax adjustment",      "営業外損益"),
]

_INDEX: dict[str, JGAAPAccount] = {a.code: a for a in JGAAP_JP}


def get_account(code: str) -> JGAAPAccount:
    """Return account by 4-digit code; raises KeyError if not found."""
    return _INDEX[code]


def accounts_by_class(account_class: str) -> list[JGAAPAccount]:
    """Return all accounts belonging to the given account_class."""
    return [a for a in JGAAP_JP if a.account_class == account_class]
