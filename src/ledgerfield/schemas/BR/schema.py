"""Chart of accounts — Brazil (NBC TG / CPC, IFRS-aligned)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class BRAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

BR_ACCOUNTS: dict[str, BRAccount] = {
    # Ativo (Assets)
    "1010": BRAccount("1010", "Caixa e Equivalentes de Caixa (Cash)", "asset"),
    "1020": BRAccount("1020", "Contas a Receber (Accounts Receivable)", "asset"),
    "1030": BRAccount("1030", "Estoques (Inventory)", "asset"),
    "1040": BRAccount("1040", "Despesas Antecipadas (Prepaid Expenses)", "asset"),
    "1050": BRAccount("1050", "Imobilizado (Fixed Assets)", "asset"),
    "1060": BRAccount("1060", "Intangível (Intangible Assets)", "asset"),
    "1070": BRAccount("1070", "ICMS / PIS / COFINS a Recuperar (Tax Credits)", "asset"),
    # Passivo (Liabilities)
    "2010": BRAccount("2010", "Fornecedores (Accounts Payable)", "liability"),
    "2020": BRAccount("2020", "IRPJ / CSLL a Pagar (Corporate Tax Payable)", "liability"),
    "2030": BRAccount("2030", "ICMS / ISS / PIS / COFINS a Pagar (Indirect Tax)", "liability"),
    "2040": BRAccount("2040", "IRRF / Contribuições Sociais a Pagar (Payroll Tax)", "liability"),
    "2050": BRAccount("2050", "FGTS / INSS a Pagar (Social Insurance)", "liability"),
    "2060": BRAccount("2060", "Empréstimos de Longo Prazo (Long-term Loans)", "liability"),
    # Patrimônio Líquido (Equity)
    "3010": BRAccount("3010", "Capital Social (Share Capital)", "equity"),
    "3020": BRAccount("3020", "Reservas de Lucros (Retained Earnings)", "equity"),
    "3030": BRAccount("3030", "Lucro / Prejuízo do Exercício (Current Year Profit)", "equity"),
    # Receita (Revenue)
    "4010": BRAccount("4010", "Receita Bruta de Vendas (Sales Revenue)", "revenue"),
    "4020": BRAccount("4020", "Receita de Serviços (Service Revenue)", "revenue"),
    "4030": BRAccount("4030", "Outras Receitas (Other Income)", "revenue"),
    # Despesas (Expenses)
    "5010": BRAccount("5010", "Custo das Mercadorias Vendidas (COGS)", "expense"),
    "5020": BRAccount("5020", "Salários e Ordenados (Salaries & Wages)", "expense"),
    "5030": BRAccount("5030", "INSS Patronal (Employer Social Insurance)", "expense"),
    "5040": BRAccount("5040", "Aluguéis e Utilidades (Rent & Utilities)", "expense"),
    "5050": BRAccount("5050", "Honorários Profissionais (Professional Fees)", "expense"),
    "5060": BRAccount("5060", "Depreciação e Amortização (Depreciation)", "expense"),
    "5070": BRAccount("5070", "IRPJ / CSLL (Corporate Income Tax Expense)", "expense"),
    "5080": BRAccount("5080", "PIS / COFINS / ICMS (Indirect Tax Expense)", "expense"),
}

get_account = BR_ACCOUNTS.get
