"""Chart of accounts — Taiwan (Taiwan IFRS - TIFRS)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class TWAccount:
    code: str
    name: str
    type: str  # asset | liability | equity | revenue | expense


TW_ACCOUNTS: dict[str, TWAccount] = {
    # Assets
    "1010": TWAccount("1010", "現金及約當現金 (Cash / Bank)", "asset"),
    "1020": TWAccount("1020", "應收帳款 (Accounts Receivable)", "asset"),
    "1030": TWAccount("1030", "存貨 (Inventory)", "asset"),
    "1040": TWAccount("1040", "預付款項 (Prepaid Expenses)", "asset"),
    "1050": TWAccount("1050", "不動產廠房及設備 (Fixed Assets)", "asset"),
    "1060": TWAccount("1060", "無形資產 (Intangible Assets)", "asset"),
    "1070": TWAccount("1070", "留抵稅額 (VAT Receivable)", "asset"),
    # Liabilities
    "2010": TWAccount("2010", "應付帳款 (Accounts Payable)", "liability"),
    "2020": TWAccount("2020", "應付所得稅 (Corporate Tax Payable)", "liability"),
    "2030": TWAccount("2030", "應付營業稅 (VAT Payable)", "liability"),
    "2040": TWAccount("2040", "代扣薪資稅款 (Payroll Tax Payable)", "liability"),
    "2050": TWAccount("2050", "勞健保費用應付 (Social Insurance Payable)", "liability"),
    "2060": TWAccount("2060", "長期借款 (Long-term Loans)", "liability"),
    # Equity
    "3010": TWAccount("3010", "股本 (Share Capital)", "equity"),
    "3020": TWAccount("3020", "保留盈餘 (Retained Earnings)", "equity"),
    "3030": TWAccount("3030", "本期損益 (Current Year Profit)", "equity"),
    # Revenue
    "4010": TWAccount("4010", "銷貨收入 (Sales Revenue)", "revenue"),
    "4020": TWAccount("4020", "勞務收入 (Service Revenue)", "revenue"),
    "4030": TWAccount("4030", "其他收入 (Other Income)", "revenue"),
    # Expenses
    "5010": TWAccount("5010", "銷貨成本 (Cost of Goods Sold)", "expense"),
    "5020": TWAccount("5020", "薪資費用 (Salaries & Wages)", "expense"),
    "5030": TWAccount("5030", "勞健保費 (Employer Social Insurance)", "expense"),
    "5040": TWAccount("5040", "租金及水電費 (Rent & Utilities)", "expense"),
    "5050": TWAccount("5050", "專業服務費 (Professional Fees)", "expense"),
    "5060": TWAccount("5060", "折舊及攤銷 (Depreciation)", "expense"),
    "5070": TWAccount("5070", "所得稅費用 (Corporate Income Tax Expense)", "expense"),
    "5080": TWAccount("5080", "不可扣抵稅款 (VAT/Indirect Tax Expense)", "expense"),
}


def get_account(code: str) -> TWAccount:
    return TW_ACCOUNTS[code]
