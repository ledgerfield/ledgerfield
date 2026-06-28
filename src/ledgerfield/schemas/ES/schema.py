"""Chart of accounts — Spain (Spanish PGC, Plan General de Contabilidad)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ESAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"

ES_ACCOUNTS: dict[str, ESAccount] = {
    # Activo (Assets)
    "1010": ESAccount("1010", "Tesorería / Caja y Bancos (Cash / Bank)", "asset"),
    "1020": ESAccount("1020", "Clientes / Deudores (Accounts Receivable)", "asset"),
    "1030": ESAccount("1030", "Existencias (Inventory)", "asset"),
    "1040": ESAccount("1040", "Gastos Anticipados (Prepaid Expenses)", "asset"),
    "1050": ESAccount("1050", "Inmovilizado Material (Fixed Assets)", "asset"),
    "1060": ESAccount("1060", "Inmovilizado Intangible (Intangible Assets)", "asset"),
    "1070": ESAccount("1070", "IVA Soportado / Hacienda Pública (VAT Receivable)", "asset"),
    # Pasivo (Liabilities)
    "2010": ESAccount("2010", "Proveedores / Acreedores (Accounts Payable)", "liability"),
    "2020": ESAccount("2020", "Impuesto sobre Sociedades a Pagar (CIT Payable)", "liability"),
    "2030": ESAccount("2030", "IVA Repercutido a Pagar (VAT Payable)", "liability"),
    "2040": ESAccount("2040", "Retenciones IRPF / Seguridad Social Empresa (Payroll Tax)", "liability"),
    "2050": ESAccount("2050", "Cuotas Seguridad Social (Social Insurance Payable)", "liability"),
    "2060": ESAccount("2060", "Deudas a Largo Plazo (Long-term Loans)", "liability"),
    # Patrimonio Neto (Equity)
    "3010": ESAccount("3010", "Capital Social (Share Capital)", "equity"),
    "3020": ESAccount("3020", "Reservas / Resultados Ejercicios Anteriores (Retained Earnings)", "equity"),
    "3030": ESAccount("3030", "Resultado del Ejercicio (Current Year Profit)", "equity"),
    # Ingresos (Revenue)
    "4010": ESAccount("4010", "Ventas de Mercaderías (Sales Revenue)", "revenue"),
    "4020": ESAccount("4020", "Ingresos por Servicios (Service Revenue)", "revenue"),
    "4030": ESAccount("4030", "Otros Ingresos (Other Income)", "revenue"),
    # Gastos (Expenses)
    "5010": ESAccount("5010", "Coste de Ventas (Cost of Goods Sold)", "expense"),
    "5020": ESAccount("5020", "Sueldos y Salarios (Salaries & Wages)", "expense"),
    "5030": ESAccount("5030", "Seguridad Social Empresa (Employer Social Insurance)", "expense"),
    "5040": ESAccount("5040", "Arrendamientos y Suministros (Rent & Utilities)", "expense"),
    "5050": ESAccount("5050", "Servicios de Profesionales (Professional Fees)", "expense"),
    "5060": ESAccount("5060", "Amortizaciones (Depreciation)", "expense"),
    "5070": ESAccount("5070", "Impuesto sobre Sociedades (Corporate Income Tax Expense)", "expense"),
    "5080": ESAccount("5080", "IVA / Impuestos Indirectos (VAT/Indirect Tax Expense)", "expense"),
}

get_account = ES_ACCOUNTS.get
