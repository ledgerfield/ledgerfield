"""Argentina Argentine GAAP (RT/NIC) chart of accounts.

RT = Resoluciones Técnicas (Technical Resolutions) issued by FACPCE.
NIC = Normas Internacionales de Contabilidad (IAS adoptions).
CIT = Corporate Income Tax (Impuesto a las Ganancias) at 35%.
VAT = IVA (Impuesto al Valor Agregado): 21% standard / 10.5% reduced / 27% utilities.
Inflation adjustments (REI) are mandatory under RT 6/17 in hyperinflationary conditions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ARGAAPAccount:
    code: str
    name: str
    category: str  # Asset | Liability | Equity | Revenue | Expense
    subcategory: str
    normal_balance: str  # Debit | Credit


AR_GAAP: list[ARGAAPAccount] = [
    # ── Assets 1xxx ──────────────────────────────────────────────────────────
    # Cash and bank
    ARGAAPAccount("1010", "Caja (Cash on Hand)", "Asset", "Cash and Cash Equivalents", "Debit"),
    ARGAAPAccount("1020", "Banco Nacion — Cuenta Corriente", "Asset", "Cash and Cash Equivalents", "Debit"),
    ARGAAPAccount("1021", "Banco Galicia — Cuenta Corriente", "Asset", "Cash and Cash Equivalents", "Debit"),
    ARGAAPAccount("1022", "Banco Santander — Cuenta Corriente", "Asset", "Cash and Cash Equivalents", "Debit"),
    ARGAAPAccount("1023", "Banco BBVA — Cuenta Corriente", "Asset", "Cash and Cash Equivalents", "Debit"),
    ARGAAPAccount("1030", "Caja de Ahorro en Dolares", "Asset", "Cash and Cash Equivalents", "Debit"),
    # Short-term investments
    ARGAAPAccount("1040", "Plazo Fijo — Corriente (<=12 meses)", "Asset", "Short-term Investments", "Debit"),
    ARGAAPAccount("1041", "FCI — Fondos Comunes de Inversion", "Asset", "Short-term Investments", "Debit"),
    ARGAAPAccount("1042", "Letras del Tesoro (LETES)", "Asset", "Short-term Investments", "Debit"),
    # Trade receivables
    ARGAAPAccount("1100", "Deudores por Ventas — Comunes", "Asset", "Trade Receivables", "Debit"),
    ARGAAPAccount("1101", "Prevision para Deudores Incobrables", "Asset", "Trade Receivables", "Credit"),
    ARGAAPAccount("1102", "Deudores por Ventas — Partes Relacionadas", "Asset", "Trade Receivables", "Debit"),
    ARGAAPAccount("1103", "Documentos a Cobrar", "Asset", "Trade Receivables", "Debit"),
    # IVA / Tax receivables
    ARGAAPAccount("1110", "IVA Credito Fiscal", "Asset", "Tax Receivables", "Debit"),
    ARGAAPAccount("1111", "Impuesto a las Ganancias — Anticipo", "Asset", "Tax Receivables", "Debit"),
    ARGAAPAccount("1112", "Bienes Personales — Responsable Sustituto Saldo a Favor", "Asset", "Tax Receivables", "Debit"),
    ARGAAPAccount("1113", "IIBB Credito Fiscal (Ingresos Brutos)", "Asset", "Tax Receivables", "Debit"),
    # Inventory
    ARGAAPAccount("1200", "Mercaderias (Inventario — Bienes de Cambio)", "Asset", "Inventories", "Debit"),
    ARGAAPAccount("1201", "Produccion en Proceso", "Asset", "Inventories", "Debit"),
    ARGAAPAccount("1202", "Materias Primas", "Asset", "Inventories", "Debit"),
    ARGAAPAccount("1203", "Prevision Obsolescencia de Inventarios", "Asset", "Inventories", "Credit"),
    # Prepayments and other current assets
    ARGAAPAccount("1300", "Gastos Pagados por Adelantado — Alquiler", "Asset", "Prepayments", "Debit"),
    ARGAAPAccount("1301", "Gastos Pagados por Adelantado — Seguros", "Asset", "Prepayments", "Debit"),
    ARGAAPAccount("1302", "Gastos Pagados por Adelantado — Suscripciones", "Asset", "Prepayments", "Debit"),
    ARGAAPAccount("1310", "Otros Activos Corrientes", "Asset", "Other Current Assets", "Debit"),
    ARGAAPAccount("1320", "Prestamos a Directores / Accionistas", "Asset", "Other Receivables", "Debit"),
    ARGAAPAccount("1330", "Adelantos al Personal", "Asset", "Other Receivables", "Debit"),
    # REI — Inflation adjustment
    ARGAAPAccount("1350", "REI Activo — Ajuste por Inflacion", "Asset", "Inflation Adjustments", "Debit"),
    # Property, Plant and Equipment
    ARGAAPAccount("1500", "Terrenos y Edificios — Costo", "Asset", "Property Plant and Equipment", "Debit"),
    ARGAAPAccount("1501", "Terrenos y Edificios — Amortizacion Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    ARGAAPAccount("1510", "Mejoras en Inmuebles Alquilados — Costo", "Asset", "Property Plant and Equipment", "Debit"),
    ARGAAPAccount("1511", "Mejoras en Inmuebles Alquilados — Amortizacion Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    ARGAAPAccount("1520", "Maquinaria y Equipos — Costo", "Asset", "Property Plant and Equipment", "Debit"),
    ARGAAPAccount("1521", "Maquinaria y Equipos — Amortizacion Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    ARGAAPAccount("1530", "Muebles y Utiles — Costo", "Asset", "Property Plant and Equipment", "Debit"),
    ARGAAPAccount("1531", "Muebles y Utiles — Amortizacion Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    ARGAAPAccount("1540", "Equipos de Computacion — Costo", "Asset", "Property Plant and Equipment", "Debit"),
    ARGAAPAccount("1541", "Equipos de Computacion — Amortizacion Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    ARGAAPAccount("1550", "Rodados (Vehiculos) — Costo", "Asset", "Property Plant and Equipment", "Debit"),
    ARGAAPAccount("1551", "Rodados (Vehiculos) — Amortizacion Acumulada", "Asset", "Property Plant and Equipment", "Credit"),
    ARGAAPAccount("1560", "Activos por Derecho de Uso (RT 48 / NIC 16) — Costo", "Asset", "Right-of-Use Assets", "Debit"),
    ARGAAPAccount("1561", "Activos por Derecho de Uso — Amortizacion Acumulada", "Asset", "Right-of-Use Assets", "Credit"),
    # Intangibles
    ARGAAPAccount("1600", "Llave de Negocio (Goodwill)", "Asset", "Intangible Assets", "Debit"),
    ARGAAPAccount("1601", "Software — Costo", "Asset", "Intangible Assets", "Debit"),
    ARGAAPAccount("1602", "Software — Amortizacion Acumulada", "Asset", "Intangible Assets", "Credit"),
    ARGAAPAccount("1603", "Marcas y Patentes — Costo", "Asset", "Intangible Assets", "Debit"),
    ARGAAPAccount("1604", "Marcas y Patentes — Amortizacion Acumulada", "Asset", "Intangible Assets", "Credit"),
    # Investments
    ARGAAPAccount("1700", "Inversiones en Titulos y Acciones (FVTPL)", "Asset", "Financial Assets", "Debit"),
    ARGAAPAccount("1701", "Inversiones en Obligaciones Negociables", "Asset", "Financial Assets", "Debit"),
    ARGAAPAccount("1710", "Inversion en Subsidiarias", "Asset", "Financial Assets", "Debit"),
    ARGAAPAccount("1720", "Inversion en Empresas Vinculadas (VPP)", "Asset", "Financial Assets", "Debit"),
    # Deferred tax
    ARGAAPAccount("1800", "Impuesto Diferido — Activo", "Asset", "Deferred Tax", "Debit"),

    # ── Liabilities 2xxx ─────────────────────────────────────────────────────
    # Trade payables
    ARGAAPAccount("2010", "Proveedores — Cuentas a Pagar", "Liability", "Trade Payables", "Credit"),
    ARGAAPAccount("2011", "Proveedores — Partes Relacionadas", "Liability", "Trade Payables", "Credit"),
    ARGAAPAccount("2012", "Documentos a Pagar", "Liability", "Trade Payables", "Credit"),
    # Tax payables
    ARGAAPAccount("2100", "IVA Debito Fiscal", "Liability", "Tax Payables", "Credit"),
    ARGAAPAccount("2101", "Impuesto a las Ganancias a Pagar", "Liability", "Tax Payables", "Credit"),
    ARGAAPAccount("2102", "Retenciones Impuesto a las Ganancias", "Liability", "Tax Payables", "Credit"),
    ARGAAPAccount("2103", "Ingresos Brutos a Pagar", "Liability", "Tax Payables", "Credit"),
    ARGAAPAccount("2104", "Impuesto al Cheque a Pagar", "Liability", "Tax Payables", "Credit"),
    # Payroll
    ARGAAPAccount("2110", "Cargas Sociales Patronales a Pagar", "Liability", "Payroll Payables", "Credit"),
    ARGAAPAccount("2111", "Sueldos y Jornales a Pagar", "Liability", "Payroll Payables", "Credit"),
    ARGAAPAccount("2112", "Retenciones de Empleados — SIPA/INSSJP", "Liability", "Payroll Payables", "Credit"),
    ARGAAPAccount("2113", "SAC (Aguinaldo) Provision", "Liability", "Employee Entitlements", "Credit"),
    ARGAAPAccount("2114", "Vacaciones — Provision", "Liability", "Employee Entitlements", "Credit"),
    ARGAAPAccount("2115", "Indemnizacion — Provision", "Liability", "Employee Entitlements", "Credit"),
    # Accruals and other
    ARGAAPAccount("2200", "Gastos Acumulados (Accruals)", "Liability", "Accruals", "Credit"),
    ARGAAPAccount("2201", "Honorarios Directorio Provision", "Liability", "Accruals", "Credit"),
    ARGAAPAccount("2210", "Ingresos Diferidos", "Liability", "Deferred Income", "Credit"),
    ARGAAPAccount("2220", "Anticipos de Clientes", "Liability", "Other Payables", "Credit"),
    ARGAAPAccount("2230", "Dividendos a Pagar", "Liability", "Other Payables", "Credit"),
    # REI — Inflation adjustment
    ARGAAPAccount("2250", "REI Pasivo — Ajuste por Inflacion", "Liability", "Inflation Adjustments", "Credit"),
    # Loans and lease
    ARGAAPAccount("2300", "Descubierto Bancario", "Liability", "Borrowings", "Credit"),
    ARGAAPAccount("2310", "Prestamos Bancarios — Porcion Corriente", "Liability", "Borrowings", "Credit"),
    ARGAAPAccount("2311", "Prestamos Bancarios — Porcion No Corriente", "Liability", "Borrowings", "Credit"),
    ARGAAPAccount("2320", "Prestamos de Socios / Directores", "Liability", "Borrowings", "Credit"),
    ARGAAPAccount("2330", "Pasivo por Arrendamiento — Corriente (RT 48)", "Liability", "Lease Liabilities", "Credit"),
    ARGAAPAccount("2331", "Pasivo por Arrendamiento — No Corriente (RT 48)", "Liability", "Lease Liabilities", "Credit"),
    ARGAAPAccount("2340", "Obligaciones Negociables — Corriente", "Liability", "Borrowings", "Credit"),
    ARGAAPAccount("2341", "Obligaciones Negociables — No Corriente", "Liability", "Borrowings", "Credit"),
    # Deferred tax
    ARGAAPAccount("2400", "Impuesto Diferido — Pasivo", "Liability", "Deferred Tax", "Credit"),

    # ── Equity 3xxx ──────────────────────────────────────────────────────────
    ARGAAPAccount("3010", "Capital Social", "Equity", "Issued Capital", "Credit"),
    ARGAAPAccount("3020", "Prima de Emision", "Equity", "Issued Capital", "Credit"),
    ARGAAPAccount("3030", "Resultados No Asignados (Ejercicios Anteriores)", "Equity", "Retained Earnings", "Credit"),
    ARGAAPAccount("3040", "Resultado del Ejercicio", "Equity", "Retained Earnings", "Credit"),
    ARGAAPAccount("3050", "Reserva Legal", "Equity", "Reserves", "Credit"),
    ARGAAPAccount("3060", "Reserva Facultativa", "Equity", "Reserves", "Credit"),
    ARGAAPAccount("3070", "Dividendos Distribuidos", "Equity", "Retained Earnings", "Debit"),
    ARGAAPAccount("3080", "Ajuste Integral del Capital (REI)", "Equity", "Inflation Adjustments", "Credit"),
    ARGAAPAccount("3090", "Resultado por Tenencia — OCI", "Equity", "Reserves", "Credit"),

    # ── Revenue 4xxx ─────────────────────────────────────────────────────────
    ARGAAPAccount("4010", "Ventas de Mercancias", "Revenue", "Operating Revenue", "Credit"),
    ARGAAPAccount("4011", "Devoluciones y Bonificaciones sobre Ventas", "Revenue", "Operating Revenue", "Debit"),
    ARGAAPAccount("4020", "Ingresos por Servicios", "Revenue", "Operating Revenue", "Credit"),
    ARGAAPAccount("4030", "Ingresos por Alquileres", "Revenue", "Other Income", "Credit"),
    ARGAAPAccount("4040", "Intereses Ganados", "Revenue", "Other Income", "Credit"),
    ARGAAPAccount("4050", "Dividendos Cobrados", "Revenue", "Other Income", "Credit"),
    ARGAAPAccount("4060", "Resultado por Venta de Bienes de Uso", "Revenue", "Other Income", "Credit"),
    ARGAAPAccount("4070", "Diferencia de Cambio Positiva", "Revenue", "Other Income", "Credit"),
    ARGAAPAccount("4080", "Resultado por Inflacion (REI Positivo)", "Revenue", "Inflation Adjustments", "Credit"),
    ARGAAPAccount("4090", "Otros Ingresos", "Revenue", "Other Income", "Credit"),

    # ── Expenses 5xxx ────────────────────────────────────────────────────────
    # Cost of sales
    ARGAAPAccount("5010", "Costo de Mercancias Vendidas", "Expense", "Cost of Sales", "Debit"),
    ARGAAPAccount("5020", "Mano de Obra Directa", "Expense", "Cost of Sales", "Debit"),
    ARGAAPAccount("5030", "Gastos de Fabricacion", "Expense", "Cost of Sales", "Debit"),
    # Staff costs
    ARGAAPAccount("5100", "Sueldos y Jornales", "Expense", "Staff Costs", "Debit"),
    ARGAAPAccount("5101", "Cargas Sociales Patronales (SIPA/INSSJP/ART)", "Expense", "Staff Costs", "Debit"),
    ARGAAPAccount("5102", "Gratificaciones y Bonos", "Expense", "Staff Costs", "Debit"),
    ARGAAPAccount("5103", "SAC (Aguinaldo)", "Expense", "Staff Costs", "Debit"),
    ARGAAPAccount("5104", "Provision Vacaciones", "Expense", "Staff Costs", "Debit"),
    ARGAAPAccount("5105", "Provision Indemnizacion", "Expense", "Staff Costs", "Debit"),
    ARGAAPAccount("5106", "Capacitacion y Formacion", "Expense", "Staff Costs", "Debit"),
    # Premises
    ARGAAPAccount("5200", "Alquileres", "Expense", "Premises Costs", "Debit"),
    ARGAAPAccount("5201", "Amortizacion Activo Derecho de Uso", "Expense", "Premises Costs", "Debit"),
    ARGAAPAccount("5202", "Interes Pasivo por Arrendamiento", "Expense", "Finance Costs", "Debit"),
    ARGAAPAccount("5210", "Servicios Publicos — Electricidad", "Expense", "Premises Costs", "Debit"),
    ARGAAPAccount("5211", "Servicios Publicos — Gas y Agua", "Expense", "Premises Costs", "Debit"),
    ARGAAPAccount("5212", "Mantenimiento y Reparaciones", "Expense", "Premises Costs", "Debit"),
    # Professional fees
    ARGAAPAccount("5300", "Honorarios Auditoria", "Expense", "Professional Fees", "Debit"),
    ARGAAPAccount("5301", "Honorarios Impositivos", "Expense", "Professional Fees", "Debit"),
    ARGAAPAccount("5302", "Honorarios Legales", "Expense", "Professional Fees", "Debit"),
    ARGAAPAccount("5303", "Honorarios Directorio", "Expense", "Professional Fees", "Debit"),
    ARGAAPAccount("5304", "Honorarios Consultoria", "Expense", "Professional Fees", "Debit"),
    # Depreciation
    ARGAAPAccount("5400", "Amortizacion Bienes de Uso", "Expense", "Depreciation and Amortisation", "Debit"),
    ARGAAPAccount("5401", "Amortizacion Bienes Intangibles", "Expense", "Depreciation and Amortisation", "Debit"),
    ARGAAPAccount("5402", "Perdida por Deterioro (Impairment)", "Expense", "Depreciation and Amortisation", "Debit"),
    # Finance costs
    ARGAAPAccount("5500", "Intereses Bancarios", "Expense", "Finance Costs", "Debit"),
    ARGAAPAccount("5501", "Cargos y Comisiones Bancarias", "Expense", "Finance Costs", "Debit"),
    ARGAAPAccount("5502", "Diferencia de Cambio Negativa", "Expense", "Finance Costs", "Debit"),
    # Tax
    ARGAAPAccount("5600", "Impuesto a las Ganancias — Corriente", "Expense", "Taxation", "Debit"),
    ARGAAPAccount("5601", "Impuesto Diferido — Gasto / (Credito)", "Expense", "Taxation", "Debit"),
    ARGAAPAccount("5602", "Ingresos Brutos", "Expense", "Taxation", "Debit"),
    ARGAAPAccount("5603", "Impuesto al Cheque (Debitos y Creditos)", "Expense", "Taxation", "Debit"),
    # Inflation adjustment
    ARGAAPAccount("5700", "Resultado por Inflacion (REI Negativo)", "Expense", "Inflation Adjustments", "Debit"),
    # Other operating expenses
    ARGAAPAccount("5800", "Publicidad y Marketing", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5801", "Viajes y Representacion", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5802", "Licencias y Suscripciones IT", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5803", "Utiles y Papeleria", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5804", "Seguros", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5805", "Prevision Incobrables", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5806", "Gastos de Comunicaciones", "Expense", "Other Operating Expenses", "Debit"),
    ARGAAPAccount("5807", "Gastos Varios", "Expense", "Other Operating Expenses", "Debit"),
]
