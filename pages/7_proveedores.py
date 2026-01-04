import streamlit as st
import pandas as pd
from core.db import get_connection

st.title("🚚 Proveedores")

conn = get_connection()

with st.form("nuevo_proveedor"):
    nombre = st.text_input("Nombre")
    contacto = st.text_input("Contacto")
    telefono = st.text_input("Teléfono")
    email = st.text_input("Email")

    submit = st.form_submit_button("Guardar")

    if submit:
        conn.execute(
            """INSERT INTO proveedores (nombre, contacto, telefono, email)
               VALUES (?, ?, ?, ?)""",
            (nombre, contacto, telefono, email)
        )
        conn.commit()
        st.success("Proveedor registrado")
