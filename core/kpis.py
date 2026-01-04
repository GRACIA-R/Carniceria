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

def margen_por_producto():
    conn = get_connection()

    return pd.read_sql("""
        SELECT
            p.nombre,
            p.costo_kg,
            p.precio_kg,
            (p.precio_kg - p.costo_kg) AS margen_kg,
            CASE 
                WHEN p.precio_kg > 0 
                THEN (p.precio_kg - p.costo_kg) / p.precio_kg * 100
                ELSE 0
            END AS margen_pct
        FROM productos p
    """, conn)

