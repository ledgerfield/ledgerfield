"""Republic of El Salvador chart of accounts (IFRS / NIIF as applied in El Salvador).

Salvadoran companies report under NIIF (IFRS) full or for SMEs; the economy is
dollarised (USD). This chart layers El Salvador-specific tax and labour
accounts on top of an IFRS structure:

ISR = Impuesto sobre la Renta (30% standard / 25% up to USD 150,000, LISR).
IVA = Impuesto a la Transferencia de Bienes Muebles y a la Prestación de
      Servicios (13% VAT).
Pago a Cuenta = monthly advance income-tax payment on gross income.
ISSS = Instituto Salvadoreño del Seguro Social; AFP = pension fund.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SVGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


SV_GAAP: list[SVGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    SVGAAPAccount("1010", "Caja General", "Asset", "Cash and Cash Equivalents", "Debit"),
    SVGAAPAccount("1015", "Caja Chica", "Asset", "Cash and Cash Equivalents", "Debit"),
    SVGAAPAccount("1020", "Banco Agrícola Cuenta Corriente (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SVGAAPAccount("1021", "Banco Cuscatlán Cuenta Corriente (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SVGAAPAccount("1022", "Banco Davivienda Cuenta Corriente (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SVGAAPAccount("1023", "Banco Hipotecario Cuenta Corriente (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    SVGAAPAccount("1040", "Depósitos a Plazo", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    SVGAAPAccount("1100", "Cuentas por Cobrar Clientes", "Asset", "Trade and Other Receivables", "Debit"),
    SVGAAPAccount("1110", "Estimación para Cuentas Incobrables", "Asset", "Trade and Other Receivables", "Credit"),
    SVGAAPAccount("1120", "Documentos por Cobrar", "Asset", "Trade and Other Receivables", "Debit"),
    SVGAAPAccount("1130", "Otras Cuentas por Cobrar", "Asset", "Trade and Other Receivables", "Debit"),
    SVGAAPAccount("1140", "Anticipos a Proveedores", "Asset", "Trade and Other Receivables", "Debit"),
    SVGAAPAccount("1150", "Préstamos a Empleados", "Asset", "Trade and Other Receivables", "Debit"),
    SVGAAPAccount("1160", "Gastos Pagados por Anticipado", "Asset", "Prepayments", "Debit"),
    SVGAAPAccount("1170", "IVA Crédito Fiscal (13%)", "Asset", "Tax Receivable", "Debit"),
    SVGAAPAccount("1180", "Pago a Cuenta ISR (Anticipos)", "Asset", "Tax Receivable", "Debit"),
    SVGAAPAccount("1185", "Retenciones ISR a Favor", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    SVGAAPAccount("1200", "Inventario — Materias Primas", "Asset", "Inventories", "Debit"),
    SVGAAPAccount("1210", "Inventario — Productos en Proceso", "Asset", "Inventories", "Debit"),
    SVGAAPAccount("1220", "Inventario — Productos Terminados", "Asset", "Inventories", "Debit"),
    SVGAAPAccount("1230", "Mercadería en Tránsito", "Asset", "Inventories", "Debit"),
    SVGAAPAccount("1240", "Estimación por Obsolescencia de Inventario", "Asset", "Inventories", "Credit"),
    # Non-current assets
    SVGAAPAccount("1500", "Terrenos", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1510", "Edificios", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1515", "Depreciación Acumulada — Edificios", "Asset", "Property, Plant and Equipment", "Credit"),
    SVGAAPAccount("1530", "Maquinaria y Equipo", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1535", "Depreciación Acumulada — Maquinaria y Equipo", "Asset", "Property, Plant and Equipment", "Credit"),
    SVGAAPAccount("1540", "Vehículos", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1545", "Depreciación Acumulada — Vehículos", "Asset", "Property, Plant and Equipment", "Credit"),
    SVGAAPAccount("1550", "Mobiliario y Equipo de Oficina", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1560", "Equipo de Cómputo", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1570", "Activo por Derecho de Uso (NIIF 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    SVGAAPAccount("1600", "Plusvalía (Goodwill)", "Asset", "Intangible Assets", "Debit"),
    SVGAAPAccount("1610", "Software y Licencias", "Asset", "Intangible Assets", "Debit"),
    SVGAAPAccount("1700", "Inversiones en Subsidiarias", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    SVGAAPAccount("2000", "Cuentas por Pagar Proveedores", "Liability", "Trade and Other Payables", "Credit"),
    SVGAAPAccount("2010", "Gastos Acumulados por Pagar", "Liability", "Trade and Other Payables", "Credit"),
    SVGAAPAccount("2020", "Otras Cuentas por Pagar", "Liability", "Trade and Other Payables", "Credit"),
    SVGAAPAccount("2030", "Anticipos de Clientes", "Liability", "Trade and Other Payables", "Credit"),
    SVGAAPAccount("2100", "IVA Débito Fiscal por Pagar (13%)", "Liability", "Tax Payable", "Credit"),
    SVGAAPAccount("2110", "ISR por Pagar (25%/30%)", "Liability", "Tax Payable", "Credit"),
    SVGAAPAccount("2115", "Pago a Cuenta por Pagar", "Liability", "Tax Payable", "Credit"),
    SVGAAPAccount("2120", "Retenciones ISR por Pagar (DGII)", "Liability", "Tax Payable", "Credit"),
    SVGAAPAccount("2130", "Impuestos Municipales por Pagar", "Liability", "Tax Payable", "Credit"),
    SVGAAPAccount("2200", "Sueldos y Salarios por Pagar", "Liability", "Employee Benefits", "Credit"),
    SVGAAPAccount("2210", "ISSS por Pagar", "Liability", "Employee Benefits", "Credit"),
    SVGAAPAccount("2220", "AFP por Pagar", "Liability", "Employee Benefits", "Credit"),
    SVGAAPAccount("2230", "Provisión Aguinaldo", "Liability", "Employee Benefits", "Credit"),
    SVGAAPAccount("2240", "Provisión Indemnización", "Liability", "Employee Benefits", "Credit"),
    SVGAAPAccount("2250", "Provisión Vacaciones", "Liability", "Employee Benefits", "Credit"),
    SVGAAPAccount("2300", "Sobregiro Bancario", "Liability", "Borrowings", "Credit"),
    SVGAAPAccount("2310", "Préstamos Bancarios Corto Plazo", "Liability", "Borrowings", "Credit"),
    SVGAAPAccount("2400", "Préstamos Bancarios Largo Plazo", "Liability", "Non-Current Liabilities", "Credit"),
    SVGAAPAccount("2410", "Pasivo por Arrendamiento (NIIF 16)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    SVGAAPAccount("3000", "Capital Social", "Equity", "Contributed Capital", "Credit"),
    SVGAAPAccount("3100", "Reserva Legal (7% Código de Comercio)", "Equity", "Reserves", "Credit"),
    SVGAAPAccount("3200", "Utilidades Retenidas", "Equity", "Retained Earnings", "Credit"),
    SVGAAPAccount("3210", "Utilidad / (Pérdida) del Ejercicio", "Equity", "Retained Earnings", "Credit"),
    SVGAAPAccount("3300", "Dividendos Decretados", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    SVGAAPAccount("4000", "Ingresos por Venta de Bienes", "Revenue", "Operating Revenue", "Credit"),
    SVGAAPAccount("4010", "Ingresos por Servicios", "Revenue", "Operating Revenue", "Credit"),
    SVGAAPAccount("4020", "Ingresos por Exportaciones (Tasa 0%)", "Revenue", "Operating Revenue", "Credit"),
    SVGAAPAccount("4100", "Devoluciones sobre Ventas", "Revenue", "Operating Revenue", "Debit"),
    SVGAAPAccount("4110", "Descuentos sobre Ventas", "Revenue", "Operating Revenue", "Debit"),
    SVGAAPAccount("4200", "Otros Ingresos Operativos", "Revenue", "Other Income", "Credit"),
    SVGAAPAccount("4210", "Ingresos Financieros", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    SVGAAPAccount("5000", "Costo de Ventas", "Expense", "Cost of Sales", "Debit"),
    SVGAAPAccount("5010", "Mano de Obra Directa", "Expense", "Cost of Sales", "Debit"),
    SVGAAPAccount("6000", "Sueldos y Salarios", "Expense", "Staff Costs", "Debit"),
    SVGAAPAccount("6010", "ISSS Patronal (7.5%)", "Expense", "Staff Costs", "Debit"),
    SVGAAPAccount("6020", "AFP Patronal (8.75%)", "Expense", "Staff Costs", "Debit"),
    SVGAAPAccount("6030", "Aguinaldo", "Expense", "Staff Costs", "Debit"),
    SVGAAPAccount("6040", "Indemnizaciones", "Expense", "Staff Costs", "Debit"),
    SVGAAPAccount("6100", "Alquiler de Oficina", "Expense", "Occupancy Costs", "Debit"),
    SVGAAPAccount("6110", "Energía Eléctrica y Agua (CAESS / ANDA)", "Expense", "Occupancy Costs", "Debit"),
    SVGAAPAccount("6200", "Tasas y Licencias Municipales", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6210", "Honorarios Profesionales y Auditoría", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6220", "Telecomunicaciones (Claro / Tigo)", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6230", "Publicidad y Mercadeo", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6240", "Comisiones Bancarias", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6250", "Depreciación", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6260", "Reparaciones y Mantenimiento", "Expense", "Administrative Expenses", "Debit"),
    SVGAAPAccount("6300", "Gastos Financieros", "Expense", "Finance Costs", "Debit"),
    SVGAAPAccount("6400", "Gasto por ISR (Impuesto sobre la Renta)", "Expense", "Tax Expense", "Debit"),
]
