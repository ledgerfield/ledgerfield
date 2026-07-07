"""Republic of Nicaragua chart of accounts (IFRS / NIIF as applied in Nicaragua).

Nicaraguan companies report under NIIF (IFRS) full or for SMEs. This chart
layers Nicaragua-specific tax and labour accounts on top of an IFRS structure:

IR = Impuesto sobre la Renta (30% CIT, Ley 822 LCT).
Pago Mínimo Definitivo = definitive minimum payment (1%-3% of gross income).
IVA = Impuesto al Valor Agregado (15% VAT).
INSS = Instituto Nicaragüense de Seguridad Social (social security).
INATEC = 2% training levy.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class NIGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


NI_GAAP: list[NIGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    NIGAAPAccount("1010", "Caja General", "Asset", "Cash and Cash Equivalents", "Debit"),
    NIGAAPAccount("1015", "Caja Chica", "Asset", "Cash and Cash Equivalents", "Debit"),
    NIGAAPAccount("1020", "Banco BAC Credomatic Cuenta Corriente (NIO)", "Asset", "Cash and Cash Equivalents", "Debit"),
    NIGAAPAccount("1021", "Banco Banpro Cuenta Corriente (NIO)", "Asset", "Cash and Cash Equivalents", "Debit"),
    NIGAAPAccount("1022", "Banco Lafise Bancentro Cuenta Corriente (NIO)", "Asset", "Cash and Cash Equivalents", "Debit"),
    NIGAAPAccount("1030", "Cuenta en Moneda Extranjera (USD)", "Asset", "Cash and Cash Equivalents", "Debit"),
    NIGAAPAccount("1040", "Depósitos a Plazo", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Receivables
    NIGAAPAccount("1100", "Cuentas por Cobrar Clientes", "Asset", "Trade and Other Receivables", "Debit"),
    NIGAAPAccount("1110", "Estimación para Cuentas Incobrables", "Asset", "Trade and Other Receivables", "Credit"),
    NIGAAPAccount("1120", "Documentos por Cobrar", "Asset", "Trade and Other Receivables", "Debit"),
    NIGAAPAccount("1130", "Otras Cuentas por Cobrar", "Asset", "Trade and Other Receivables", "Debit"),
    NIGAAPAccount("1140", "Anticipos a Proveedores", "Asset", "Trade and Other Receivables", "Debit"),
    NIGAAPAccount("1150", "Préstamos a Empleados", "Asset", "Trade and Other Receivables", "Debit"),
    NIGAAPAccount("1160", "Gastos Pagados por Anticipado", "Asset", "Prepayments", "Debit"),
    NIGAAPAccount("1170", "IVA Crédito Fiscal (15%)", "Asset", "Tax Receivable", "Debit"),
    NIGAAPAccount("1180", "Retenciones IR a Favor (Anticipos)", "Asset", "Tax Receivable", "Debit"),
    NIGAAPAccount("1185", "Pago Mínimo Definitivo Anticipado", "Asset", "Tax Receivable", "Debit"),
    # Inventory
    NIGAAPAccount("1200", "Inventario — Materias Primas", "Asset", "Inventories", "Debit"),
    NIGAAPAccount("1210", "Inventario — Productos en Proceso", "Asset", "Inventories", "Debit"),
    NIGAAPAccount("1220", "Inventario — Productos Terminados", "Asset", "Inventories", "Debit"),
    NIGAAPAccount("1230", "Mercadería en Tránsito", "Asset", "Inventories", "Debit"),
    NIGAAPAccount("1240", "Estimación por Obsolescencia de Inventario", "Asset", "Inventories", "Credit"),
    # Non-current assets
    NIGAAPAccount("1500", "Terrenos", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1510", "Edificios", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1515", "Depreciación Acumulada — Edificios", "Asset", "Property, Plant and Equipment", "Credit"),
    NIGAAPAccount("1530", "Maquinaria y Equipo", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1535", "Depreciación Acumulada — Maquinaria y Equipo", "Asset", "Property, Plant and Equipment", "Credit"),
    NIGAAPAccount("1540", "Equipo Rodante (Vehículos)", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1545", "Depreciación Acumulada — Equipo Rodante", "Asset", "Property, Plant and Equipment", "Credit"),
    NIGAAPAccount("1550", "Mobiliario y Equipo de Oficina", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1560", "Equipo de Cómputo", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1570", "Activo por Derecho de Uso (NIIF 16)", "Asset", "Property, Plant and Equipment", "Debit"),
    NIGAAPAccount("1600", "Plusvalía (Goodwill)", "Asset", "Intangible Assets", "Debit"),
    NIGAAPAccount("1610", "Software y Licencias", "Asset", "Intangible Assets", "Debit"),
    NIGAAPAccount("1700", "Inversiones en Subsidiarias", "Asset", "Investments", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    NIGAAPAccount("2000", "Cuentas por Pagar Proveedores", "Liability", "Trade and Other Payables", "Credit"),
    NIGAAPAccount("2010", "Gastos Acumulados por Pagar", "Liability", "Trade and Other Payables", "Credit"),
    NIGAAPAccount("2020", "Otras Cuentas por Pagar", "Liability", "Trade and Other Payables", "Credit"),
    NIGAAPAccount("2030", "Anticipos de Clientes", "Liability", "Trade and Other Payables", "Credit"),
    NIGAAPAccount("2100", "IVA Débito Fiscal por Pagar (15%)", "Liability", "Tax Payable", "Credit"),
    NIGAAPAccount("2110", "IR Anual por Pagar (30%)", "Liability", "Tax Payable", "Credit"),
    NIGAAPAccount("2115", "Pago Mínimo Definitivo por Pagar", "Liability", "Tax Payable", "Credit"),
    NIGAAPAccount("2120", "Retenciones IR por Pagar (DGI)", "Liability", "Tax Payable", "Credit"),
    NIGAAPAccount("2130", "Impuesto Municipal sobre Ingresos por Pagar", "Liability", "Tax Payable", "Credit"),
    NIGAAPAccount("2200", "Sueldos y Salarios por Pagar", "Liability", "Employee Benefits", "Credit"),
    NIGAAPAccount("2210", "INSS Laboral y Patronal por Pagar", "Liability", "Employee Benefits", "Credit"),
    NIGAAPAccount("2220", "INATEC por Pagar (2%)", "Liability", "Employee Benefits", "Credit"),
    NIGAAPAccount("2230", "Provisión Aguinaldo (Décimo Tercer Mes)", "Liability", "Employee Benefits", "Credit"),
    NIGAAPAccount("2240", "Provisión Indemnización por Antigüedad", "Liability", "Employee Benefits", "Credit"),
    NIGAAPAccount("2250", "Provisión Vacaciones", "Liability", "Employee Benefits", "Credit"),
    NIGAAPAccount("2300", "Sobregiro Bancario", "Liability", "Borrowings", "Credit"),
    NIGAAPAccount("2310", "Préstamos Bancarios Corto Plazo", "Liability", "Borrowings", "Credit"),
    NIGAAPAccount("2400", "Préstamos Bancarios Largo Plazo", "Liability", "Non-Current Liabilities", "Credit"),
    NIGAAPAccount("2410", "Pasivo por Arrendamiento (NIIF 16)", "Liability", "Non-Current Liabilities", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    NIGAAPAccount("3000", "Capital Social", "Equity", "Contributed Capital", "Credit"),
    NIGAAPAccount("3100", "Reserva Legal", "Equity", "Reserves", "Credit"),
    NIGAAPAccount("3200", "Utilidades Retenidas", "Equity", "Retained Earnings", "Credit"),
    NIGAAPAccount("3210", "Utilidad / (Pérdida) del Ejercicio", "Equity", "Retained Earnings", "Credit"),
    NIGAAPAccount("3300", "Dividendos Decretados", "Equity", "Distributions", "Debit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    NIGAAPAccount("4000", "Ingresos por Venta de Bienes", "Revenue", "Operating Revenue", "Credit"),
    NIGAAPAccount("4010", "Ingresos por Servicios", "Revenue", "Operating Revenue", "Credit"),
    NIGAAPAccount("4020", "Ingresos por Exportaciones (Tasa 0%)", "Revenue", "Operating Revenue", "Credit"),
    NIGAAPAccount("4100", "Devoluciones sobre Ventas", "Revenue", "Operating Revenue", "Debit"),
    NIGAAPAccount("4110", "Descuentos sobre Ventas", "Revenue", "Operating Revenue", "Debit"),
    NIGAAPAccount("4200", "Otros Ingresos Operativos", "Revenue", "Other Income", "Credit"),
    NIGAAPAccount("4210", "Ganancia Cambiaria (Deslizamiento NIO)", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx–6xxx ───────────────────────────────────────────────────
    NIGAAPAccount("5000", "Costo de Ventas", "Expense", "Cost of Sales", "Debit"),
    NIGAAPAccount("5010", "Mano de Obra Directa", "Expense", "Cost of Sales", "Debit"),
    NIGAAPAccount("6000", "Sueldos y Salarios", "Expense", "Staff Costs", "Debit"),
    NIGAAPAccount("6010", "INSS Patronal", "Expense", "Staff Costs", "Debit"),
    NIGAAPAccount("6020", "Aporte INATEC (2%)", "Expense", "Staff Costs", "Debit"),
    NIGAAPAccount("6030", "Aguinaldo (Décimo Tercer Mes)", "Expense", "Staff Costs", "Debit"),
    NIGAAPAccount("6040", "Indemnización por Antigüedad", "Expense", "Staff Costs", "Debit"),
    NIGAAPAccount("6100", "Alquiler de Oficina", "Expense", "Occupancy Costs", "Debit"),
    NIGAAPAccount("6110", "Energía Eléctrica y Agua (Disnorte-Dissur / ENACAL)", "Expense", "Occupancy Costs", "Debit"),
    NIGAAPAccount("6200", "Matrícula Municipal y Alcaldía", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6210", "Honorarios Profesionales y Auditoría", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6220", "Telecomunicaciones (Claro / Tigo)", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6230", "Publicidad y Mercadeo", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6240", "Comisiones Bancarias", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6250", "Depreciación", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6260", "Reparaciones y Mantenimiento", "Expense", "Administrative Expenses", "Debit"),
    NIGAAPAccount("6300", "Gastos Financieros", "Expense", "Finance Costs", "Debit"),
    NIGAAPAccount("6310", "Pérdida Cambiaria (Deslizamiento NIO)", "Expense", "Finance Costs", "Debit"),
    NIGAAPAccount("6400", "Gasto por IR (Impuesto sobre la Renta)", "Expense", "Tax Expense", "Debit"),
    NIGAAPAccount("6410", "Gasto por Pago Mínimo Definitivo", "Expense", "Tax Expense", "Debit"),
]
