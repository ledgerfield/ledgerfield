"""Chart of accounts — Mexico (Mexican FRS / NIF, IFRS-aligned)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class MXAccount:
    code: str
    name: str
    account_type: str  # "asset","liability","equity","revenue","expense"


MX_ACCOUNTS: dict[str, MXAccount] = {
    # Activo (Assets)
    "1010": MXAccount("1010", "Caja y Equivalentes de Efectivo (Cash)", "asset"),
    "1020": MXAccount("1020", "Cuentas por Cobrar (Accounts Receivable)", "asset"),
    "1030": MXAccount("1030", "Inventarios (Inventory)", "asset"),
    "1040": MXAccount("1040", "Pagos Anticipados (Prepaid Expenses)", "asset"),
    "1050": MXAccount("1050", "Propiedades, Planta y Equipo (Fixed Assets)", "asset"),
    "1060": MXAccount("1060", "Activos Intangibles (Intangible Assets)", "asset"),
    "1070": MXAccount("1070", "IVA Acreditable (VAT Receivable / Input Tax)", "asset"),
    "1080": MXAccount("1080", "ISR Diferido (Deferred Income Tax Asset)", "asset"),
    # Pasivo (Liabilities)
    "2010": MXAccount("2010", "Proveedores (Accounts Payable)", "liability"),
    "2020": MXAccount("2020", "ISR por Pagar (Corporate Tax Payable)", "liability"),
    "2030": MXAccount("2030", "IVA por Pagar (VAT Payable)", "liability"),
    "2040": MXAccount("2040", "Cuotas IMSS / INFONAVIT por Pagar (Social Security)", "liability"),
    "2050": MXAccount("2050", "PTU por Pagar (Employee Profit Sharing)", "liability"),
    "2060": MXAccount("2060", "Préstamos a Largo Plazo (Long-term Loans)", "liability"),
    "2070": MXAccount("2070", "Pasivo por Impuesto Diferido (Deferred Tax Liability)", "liability"),
    # Capital Contable (Equity)
    "3010": MXAccount("3010", "Capital Social (Share Capital)", "equity"),
    "3020": MXAccount("3020", "Utilidades Retenidas (Retained Earnings)", "equity"),
    "3030": MXAccount("3030", "Resultado del Ejercicio (Current Year Profit)", "equity"),
    "3040": MXAccount("3040", "Reserva Legal (Legal Reserve)", "equity"),
    # Ingresos (Revenue)
    "4010": MXAccount("4010", "Ingresos por Ventas (Sales Revenue)", "revenue"),
    "4020": MXAccount("4020", "Ingresos por Servicios (Service Revenue)", "revenue"),
    "4030": MXAccount("4030", "Otros Ingresos (Other Income)", "revenue"),
    # Gastos (Expenses)
    "5010": MXAccount("5010", "Costo de Ventas (Cost of Goods Sold)", "expense"),
    "5020": MXAccount("5020", "Sueldos y Salarios (Salaries & Wages)", "expense"),
    "5030": MXAccount("5030", "Cuotas Patronales IMSS (Employer Social Security)", "expense"),
    "5040": MXAccount("5040", "Rentas y Servicios (Rent & Utilities)", "expense"),
    "5050": MXAccount("5050", "Honorarios Profesionales (Professional Fees)", "expense"),
    "5060": MXAccount("5060", "Depreciacion y Amortizacion (Depreciation)", "expense"),
    "5070": MXAccount("5070", "ISR del Ejercicio (Corporate Income Tax Expense)", "expense"),
    "5080": MXAccount("5080", "PTU del Ejercicio (Employee Profit Sharing Expense)", "expense"),
}

get_account = MX_ACCOUNTS.get
