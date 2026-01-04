import pandas as pd
from core.db import get_connection

def kpis_globales():
    conn = get_connection()

    ventas = pd.read_sql("SELECT SUM(total) as total FROM ventas", conn).iloc[0,0] or 0
    compras = pd.read_sql("SELECT SUM(costo_total) as total FROM compras", conn).iloc[0,0] or 0
    stock = pd.read_sql("SELECT SUM(stock_kg) as total FROM productos", conn).iloc[0,0] or 0

    return {
        "ventas_totales": ventas,
        "compras_totales": compras,
        "stock_total_kg": stock,
        "margen_bruto": ventas - compras
    }

