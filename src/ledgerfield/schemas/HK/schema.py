"""Chart of accounts — Hong Kong (Hong Kong GAAP - HKFRS / HKAS)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class HKAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"


HK_ACCOUNTS: dict[str, HKAccount] = {
    # Assets 1xxx
    "1010": HKAccount("1010", "Cash & Bank Balances (現金及銀行存款)", "asset"),
    "1020": HKAccount("1020", "Trade and Other Receivables (應收賬款)", "asset"),
    "1030": HKAccount("1030", "Inventories (存貨)", "asset"),
    "1040": HKAccount("1040", "Prepayments & Deposits (預付款項)", "asset"),
    "1050": HKAccount("1050", "Property, Plant & Equipment (物業廠房及設備)", "asset"),
    "1060": HKAccount("1060", "Intangible Assets (無形資產)", "asset"),
    "1070": HKAccount("1070", "Other Tax Recoverable (其他應收稅款)", "asset"),
    # Liabilities 2xxx
    "2010": HKAccount("2010", "Trade and Other Payables (應付賬款)", "liability"),
    "2020": HKAccount("2020", "Profits Tax Payable (利得稅應付款)", "liability"),
    "2030": HKAccount("2030", "Accrued Liabilities (應計負債)", "liability"),
    "2040": HKAccount("2040", "Salaries Tax Withheld (薪俸稅代扣)", "liability"),
    "2050": HKAccount("2050", "MPF Contributions Payable (強積金應付款)", "liability"),
    "2060": HKAccount("2060", "Long-term Bank Loans (長期銀行貸款)", "liability"),
    # Equity 3xxx
    "3010": HKAccount("3010", "Share Capital (股本)", "equity"),
    "3020": HKAccount("3020", "Retained Profits (保留溢利)", "equity"),
    "3030": HKAccount("3030", "Profit / (Loss) for the Year (本年度溢利/虧損)", "equity"),
    # Revenue 4xxx
    "4010": HKAccount("4010", "Turnover / Sales (營業額)", "revenue"),
    "4020": HKAccount("4020", "Service Income (服務收入)", "revenue"),
    "4030": HKAccount("4030", "Other Revenue (其他收入)", "revenue"),
    # Expenses 5xxx
    "5010": HKAccount("5010", "Cost of Sales (銷售成本)", "expense"),
    "5020": HKAccount("5020", "Staff Costs / Salaries (員工成本/薪酬)", "expense"),
    "5030": HKAccount("5030", "Employer MPF Contributions (強積金供款)", "expense"),
    "5040": HKAccount("5040", "Rental & Utilities (租金及水電)", "expense"),
    "5050": HKAccount("5050", "Professional Fees (專業費用)", "expense"),
    "5060": HKAccount("5060", "Depreciation & Amortisation (折舊及攤銷)", "expense"),
    "5070": HKAccount("5070", "Profits Tax Charge (利得稅費用)", "expense"),
    "5080": HKAccount("5080", "Stamp Duty & Other Levies (印花稅及其他徵費)", "expense"),
}


def get_account(code: str) -> HKAccount | None:
    return HK_ACCOUNTS.get(code)
