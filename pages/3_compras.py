import streamlit as st
import pandas as pd
from core.db import get_connection
from datetime import date
from core.costing import actualizar_costo_promedio

st.header("🚚 Compras de canal / insumos")

conn = get_connection()
productos = pd.read_sql("SELECT * FROM productos", conn)

producto = st.selectbox("Producto", productos["nombre"])
proveedor = st.text_input("Proveedor")
kg = st.number_input("Kg comprados", min_value=0.0)
costo_total = st.number_input("Costo total ($)", min_value=0.0)
fecha = st.date_input("Fecha", date.today())

if st.button("Registrar compra"):
    p = productos[productos["nombre"] == producto].iloc[0]

    conn.execute(
        "INSERT INTO compras (fecha, proveedor, kg, costo_total) VALUES (?, ?, ?, ?)",
        (str(fecha), proveedor, kg, costo_total)
    )

    actualizar_costo_promedio(p["id"], kg, costo_total)

    conn.execute(
        "UPDATE productos SET stock_kg = stock_kg + ? WHERE id = ?",
        (kg, p["id"])
    )

    conn.execute(
        "INSERT INTO caja (fecha, tipo, monto, descripcion) VALUES (?, ?, ?, ?)",
        (str(fecha), "egreso", costo_total, f"Compra de {producto}")
    )

    conn.commit()


