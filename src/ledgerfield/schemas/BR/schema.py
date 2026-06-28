"""Brazil NBC TG (CPC, IFRS-aligned) chart of accounts.

NBC TG = Normas Brasileiras de Contabilidade — Técnicas Gerais, issued by CFC.
CPC = Comite de Pronunciamentos Contabeis (aligns with IFRS as issued by IASB).
Currency: BRL (Brazilian Real).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BRNBCTGAccount:
    code: str
    name: str
    name_pt: str  # Portuguese name
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


BR_NBC_TG: list[BRNBCTGAccount] = [
    # ── Ativo (Assets) 1xxx ─────────────────────────────────────────────────
    # Ativo Circulante — Disponibilidades (Cash and Equivalents)
    BRNBCTGAccount("1.01.01", "Cash on Hand", "Caixa", "Asset", "Cash and Cash Equivalents", "Debit"),
    BRNBCTGAccount("1.01.02", "Bank — Current Account", "Bancos Conta Corrente", "Asset", "Cash and Cash Equivalents", "Debit"),
    BRNBCTGAccount("1.01.03", "Short-term Investments (up to 90 days)", "Aplicacoes Financeiras CP", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Ativo Circulante — Creditos (Receivables)
    BRNBCTGAccount("1.02.01", "Accounts Receivable — Trade", "Contas a Receber — Clientes", "Asset", "Trade Receivables", "Debit"),
    BRNBCTGAccount("1.02.02", "Allowance for Doubtful Accounts", "Provisao para Devedores Duvidosos", "Asset", "Trade Receivables", "Credit"),
    BRNBCTGAccount("1.02.03", "Accounts Receivable — Related Parties", "Contas a Receber — Partes Relacionadas", "Asset", "Trade Receivables", "Debit"),
    # Ativo Circulante — Estoques (Inventories)
    BRNBCTGAccount("1.03.01", "Inventory — Finished Goods", "Estoque — Produtos Acabados", "Asset", "Inventories", "Debit"),
    BRNBCTGAccount("1.03.02", "Inventory — Work in Progress", "Estoque — Produtos em Elaboracao", "Asset", "Inventories", "Debit"),
    BRNBCTGAccount("1.03.03", "Inventory — Raw Materials", "Estoque — Materias-Primas", "Asset", "Inventories", "Debit"),
    BRNBCTGAccount("1.03.04", "Inventory Write-down Allowance", "Provisao para Reducao ao Valor Realizavel", "Asset", "Inventories", "Credit"),
    # Ativo Circulante — Impostos a Recuperar (Tax Assets)
    BRNBCTGAccount("1.04.01", "ICMS Recoverable", "ICMS a Recuperar", "Asset", "Tax Receivables", "Debit"),
    BRNBCTGAccount("1.04.02", "PIS Recoverable", "PIS a Recuperar", "Asset", "Tax Receivables", "Debit"),
    BRNBCTGAccount("1.04.03", "COFINS Recoverable", "COFINS a Recuperar", "Asset", "Tax Receivables", "Debit"),
    BRNBCTGAccount("1.04.04", "IPI Recoverable", "IPI a Recuperar", "Asset", "Tax Receivables", "Debit"),
    BRNBCTGAccount("1.04.05", "CSLL Prepaid", "CSLL Antecipada", "Asset", "Tax Receivables", "Debit"),
    BRNBCTGAccount("1.04.06", "IRPJ Prepaid", "IRPJ Antecipado", "Asset", "Tax Receivables", "Debit"),
    # Ativo Circulante — Outros (Other Current)
    BRNBCTGAccount("1.05.01", "Prepaid Expenses", "Despesas Antecipadas", "Asset", "Prepayments", "Debit"),
    BRNBCTGAccount("1.05.02", "Loans to Officers", "Adiantamentos a Diretores", "Asset", "Other Receivables", "Debit"),
    BRNBCTGAccount("1.05.03", "Other Current Assets", "Outros Ativos Circulantes", "Asset", "Other Current Assets", "Debit"),
    # Ativo Nao Circulante — Realizavel LP (Long-term Receivables)
    BRNBCTGAccount("1.06.01", "Long-term Investments", "Aplicacoes Financeiras LP", "Asset", "Long-term Investments", "Debit"),
    BRNBCTGAccount("1.06.02", "Deferred Tax Asset — IRPJ", "Ativo Fiscal Diferido — IRPJ", "Asset", "Deferred Tax", "Debit"),
    BRNBCTGAccount("1.06.03", "Deferred Tax Asset — CSLL", "Ativo Fiscal Diferido — CSLL", "Asset", "Deferred Tax", "Debit"),
    # Ativo Nao Circulante — Investimentos (Investments)
    BRNBCTGAccount("1.07.01", "Equity Investment — Subsidiaries", "Participacoes em Controladas", "Asset", "Investments", "Debit"),
    BRNBCTGAccount("1.07.02", "Equity Investment — Associates", "Participacoes em Coligadas", "Asset", "Investments", "Debit"),
    BRNBCTGAccount("1.07.03", "Investment Property", "Propriedades para Investimento", "Asset", "Investments", "Debit"),
    # Ativo Nao Circulante — Imobilizado (PP&E)
    BRNBCTGAccount("1.08.01", "Land", "Terrenos", "Asset", "Property Plant and Equipment", "Debit"),
    BRNBCTGAccount("1.08.02", "Buildings", "Edificios e Benfeitorias", "Asset", "Property Plant and Equipment", "Debit"),
    BRNBCTGAccount("1.08.03", "Machinery and Equipment", "Maquinas e Equipamentos", "Asset", "Property Plant and Equipment", "Debit"),
    BRNBCTGAccount("1.08.04", "Vehicles", "Veiculos", "Asset", "Property Plant and Equipment", "Debit"),
    BRNBCTGAccount("1.08.05", "Furniture and Fixtures", "Moveis e Utensilios", "Asset", "Property Plant and Equipment", "Debit"),
    BRNBCTGAccount("1.08.06", "IT Equipment", "Equipamentos de Informatica", "Asset", "Property Plant and Equipment", "Debit"),
    BRNBCTGAccount("1.08.07", "Accumulated Depreciation", "Depreciacao Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    # Ativo Nao Circulante — Intangivel (Intangibles)
    BRNBCTGAccount("1.09.01", "Software / IT Licences", "Softwares e Licencas", "Asset", "Intangible Assets", "Debit"),
    BRNBCTGAccount("1.09.02", "Trademarks and Patents", "Marcas e Patentes", "Asset", "Intangible Assets", "Debit"),
    BRNBCTGAccount("1.09.03", "Goodwill (Agio por Expectativa)", "Agio por Expectativa de Rentabilidade Futura", "Asset", "Intangible Assets", "Debit"),
    BRNBCTGAccount("1.09.04", "Accumulated Amortisation", "Amortizacao Acumulada", "Asset", "Intangible Assets", "Credit"),

    # ── Passivo (Liabilities) 2xxx ──────────────────────────────────────────
    # Passivo Circulante — Fornecedores (Payables)
    BRNBCTGAccount("2.01.01", "Accounts Payable — Trade", "Fornecedores Nacionais", "Liability", "Trade Payables", "Credit"),
    BRNBCTGAccount("2.01.02", "Accounts Payable — Imports", "Fornecedores Estrangeiros", "Liability", "Trade Payables", "Credit"),
    BRNBCTGAccount("2.01.03", "Salaries and Wages Payable", "Salarios a Pagar", "Liability", "Payroll Liabilities", "Credit"),
    BRNBCTGAccount("2.01.04", "FGTS Payable", "FGTS a Recolher", "Liability", "Payroll Liabilities", "Credit"),
    BRNBCTGAccount("2.01.05", "INSS Payable — Employer", "INSS a Recolher — Empregador", "Liability", "Payroll Liabilities", "Credit"),
    BRNBCTGAccount("2.01.06", "INSS Payable — Employee (Withheld)", "INSS Retido na Fonte", "Liability", "Payroll Liabilities", "Credit"),
    # Passivo Circulante — Impostos a Pagar (Tax Liabilities)
    BRNBCTGAccount("2.02.01", "ICMS Payable", "ICMS a Recolher", "Liability", "Tax Liabilities", "Credit"),
    BRNBCTGAccount("2.02.02", "PIS Payable", "PIS a Recolher", "Liability", "Tax Liabilities", "Credit"),
    BRNBCTGAccount("2.02.03", "COFINS Payable", "COFINS a Recolher", "Liability", "Tax Liabilities", "Credit"),
    BRNBCTGAccount("2.02.04", "ISS Payable", "ISS a Recolher", "Liability", "Tax Liabilities", "Credit"),
    BRNBCTGAccount("2.02.05", "IRPJ Payable", "IRPJ a Recolher", "Liability", "Tax Liabilities", "Credit"),
    BRNBCTGAccount("2.02.06", "CSLL Payable", "CSLL a Recolher", "Liability", "Tax Liabilities", "Credit"),
    BRNBCTGAccount("2.02.07", "IPI Payable", "IPI a Recolher", "Liability", "Tax Liabilities", "Credit"),
    # Passivo Circulante — Outros (Other Current Liabilities)
    BRNBCTGAccount("2.03.01", "Short-term Loans", "Emprestimos e Financiamentos CP", "Liability", "Borrowings", "Credit"),
    BRNBCTGAccount("2.03.02", "Accrued Expenses", "Despesas a Pagar", "Liability", "Accruals", "Credit"),
    BRNBCTGAccount("2.03.03", "Customer Advances", "Adiantamentos de Clientes", "Liability", "Contract Liabilities", "Credit"),
    BRNBCTGAccount("2.03.04", "Dividends Payable", "Dividendos a Pagar", "Liability", "Other Current Liabilities", "Credit"),
    # Passivo Nao Circulante (Long-term Liabilities)
    BRNBCTGAccount("2.04.01", "Long-term Loans and Financing", "Emprestimos e Financiamentos LP", "Liability", "Long-term Borrowings", "Credit"),
    BRNBCTGAccount("2.04.02", "Deferred Tax Liability — IRPJ", "Passivo Fiscal Diferido — IRPJ", "Liability", "Deferred Tax", "Credit"),
    BRNBCTGAccount("2.04.03", "Deferred Tax Liability — CSLL", "Passivo Fiscal Diferido — CSLL", "Liability", "Deferred Tax", "Credit"),
    BRNBCTGAccount("2.04.04", "Provisions — Labour", "Provisao para Contingencias Trabalhistas", "Liability", "Provisions", "Credit"),
    BRNBCTGAccount("2.04.05", "Provisions — Tax", "Provisao para Contingencias Fiscais", "Liability", "Provisions", "Credit"),

    # ── Patrimonio Liquido (Equity) 3xxx ────────────────────────────────────
    BRNBCTGAccount("3.01.01", "Share Capital (Capital Social)", "Capital Social Subscrito", "Equity", "Share Capital", "Credit"),
    BRNBCTGAccount("3.01.02", "Capital to be Paid In", "(-) Capital a Realizar", "Equity", "Share Capital", "Debit"),
    BRNBCTGAccount("3.02.01", "Capital Reserve — Share Premium", "Reserva de Capital — Agio na Emissao", "Equity", "Capital Reserves", "Credit"),
    BRNBCTGAccount("3.03.01", "Profit Reserve — Legal (5%)", "Reserva Legal", "Equity", "Profit Reserves", "Credit"),
    BRNBCTGAccount("3.03.02", "Profit Reserve — Statutory", "Reserva Estatutaria", "Equity", "Profit Reserves", "Credit"),
    BRNBCTGAccount("3.03.03", "Retained Earnings / Accumulated Deficit", "Lucros ou Prejuizos Acumulados", "Equity", "Retained Earnings", "Credit"),
    BRNBCTGAccount("3.04.01", "Other Comprehensive Income — CPC 26", "Outros Resultados Abrangentes", "Equity", "Other Comprehensive Income", "Credit"),

    # ── Receita (Revenue) 4xxx ──────────────────────────────────────────────
    BRNBCTGAccount("4.01.01", "Gross Revenue — Goods", "Receita Bruta — Venda de Mercadorias", "Revenue", "Revenue from Contracts", "Credit"),
    BRNBCTGAccount("4.01.02", "Gross Revenue — Services", "Receita Bruta — Prestacao de Servicos", "Revenue", "Revenue from Contracts", "Credit"),
    BRNBCTGAccount("4.01.03", "Sales Returns and Allowances", "(-) Devolucoes e Abatimentos", "Revenue", "Revenue Deductions", "Debit"),
    BRNBCTGAccount("4.01.04", "Sales Taxes Deducted (ICMS/PIS/COFINS/ISS)", "(-) Deducoes da Receita", "Revenue", "Revenue Deductions", "Debit"),
    BRNBCTGAccount("4.02.01", "Other Operating Revenue", "Outras Receitas Operacionais", "Revenue", "Other Revenue", "Credit"),
    BRNBCTGAccount("4.02.02", "Financial Revenue", "Receitas Financeiras", "Revenue", "Financial Revenue", "Credit"),
    BRNBCTGAccount("4.02.03", "FX Gains", "Ganhos Cambiais", "Revenue", "Financial Revenue", "Credit"),

    # ── Custos e Despesas (Expenses) 5xxx ──────────────────────────────────
    # Custo das Mercadorias/Servicos (COGS)
    BRNBCTGAccount("5.01.01", "Cost of Goods Sold", "Custo das Mercadorias Vendidas (CMV)", "Expense", "Cost of Sales", "Debit"),
    BRNBCTGAccount("5.01.02", "Cost of Services Rendered", "Custo dos Servicos Prestados (CSP)", "Expense", "Cost of Sales", "Debit"),
    # Despesas Operacionais (Operating Expenses)
    BRNBCTGAccount("5.02.01", "Salaries — Administrative", "Salarios — Administrativo", "Expense", "Personnel Expenses", "Debit"),
    BRNBCTGAccount("5.02.02", "Salaries — Sales Force", "Salarios — Comercial", "Expense", "Personnel Expenses", "Debit"),
    BRNBCTGAccount("5.02.03", "FGTS Expense", "Encargos Sociais — FGTS", "Expense", "Personnel Expenses", "Debit"),
    BRNBCTGAccount("5.02.04", "INSS Expense — Employer", "Encargos Sociais — INSS Empregador", "Expense", "Personnel Expenses", "Debit"),
    BRNBCTGAccount("5.02.05", "PLR — Profit Sharing", "Participacao nos Lucros e Resultados (PLR)", "Expense", "Personnel Expenses", "Debit"),
    BRNBCTGAccount("5.02.06", "Rent Expense", "Despesas com Alugueis", "Expense", "Occupancy", "Debit"),
    BRNBCTGAccount("5.02.07", "Utilities", "Energia Eletrica e Agua", "Expense", "Occupancy", "Debit"),
    BRNBCTGAccount("5.02.08", "Depreciation Expense", "Despesas de Depreciacao", "Expense", "Depreciation and Amortisation", "Debit"),
    BRNBCTGAccount("5.02.09", "Amortisation Expense", "Despesas de Amortizacao", "Expense", "Depreciation and Amortisation", "Debit"),
    BRNBCTGAccount("5.02.10", "Marketing and Advertising", "Despesas de Marketing e Publicidade", "Expense", "Selling Expenses", "Debit"),
    BRNBCTGAccount("5.02.11", "Travel and Entertainment", "Despesas de Viagens e Representacao", "Expense", "General and Administrative", "Debit"),
    BRNBCTGAccount("5.02.12", "Professional Fees", "Honorarios Profissionais (Contabilidade/Juridico)", "Expense", "General and Administrative", "Debit"),
    BRNBCTGAccount("5.02.13", "Insurance", "Seguros", "Expense", "General and Administrative", "Debit"),
    BRNBCTGAccount("5.02.14", "IT and Telecoms", "Despesas com TI e Telecomunicacoes", "Expense", "General and Administrative", "Debit"),
    BRNBCTGAccount("5.02.15", "Bank Charges and IOF", "Despesas Bancarias e IOF", "Expense", "Financial Expenses", "Debit"),
    BRNBCTGAccount("5.02.16", "Interest Expense — Loans", "Juros sobre Emprestimos", "Expense", "Financial Expenses", "Debit"),
    BRNBCTGAccount("5.02.17", "FX Losses", "Perdas Cambiais", "Expense", "Financial Expenses", "Debit"),
    BRNBCTGAccount("5.02.18", "Allowance for Doubtful Debts Expense", "Despesas com PDD", "Expense", "Credit Losses", "Debit"),
    # Impostos sobre o Lucro (Income Taxes)
    BRNBCTGAccount("5.03.01", "IRPJ Current", "IRPJ Corrente", "Expense", "Income Tax Expense", "Debit"),
    BRNBCTGAccount("5.03.02", "IRPJ Deferred", "IRPJ Diferido", "Expense", "Income Tax Expense", "Debit"),
    BRNBCTGAccount("5.03.03", "CSLL Current", "CSLL Corrente", "Expense", "Income Tax Expense", "Debit"),
    BRNBCTGAccount("5.03.04", "CSLL Deferred", "CSLL Diferido", "Expense", "Income Tax Expense", "Debit"),
]
