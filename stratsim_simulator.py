import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="StratSim Simulator", layout="wide")
st.title("🎯 StratSim - Decisiones y Simulación Previa")

# --- Inputs por marca ---
st.sidebar.header("🔧 Configuración de marcas")
marcas = ["Brand S (Sonite)", "Brand V (Vodite)"]

decisiones = []

for marca in marcas:
    st.sidebar.subheader(marca)
    precio = st.sidebar.number_input(f"Precio de venta - {marca}", min_value=100.0, max_value=1000.0, value=400.0)
    produccion = st.sidebar.number_input(f"Unidades a producir - {marca}", min_value=0, step=1000, value=20000)
    pub_media = st.sidebar.number_input(f"Publicidad (Media) - {marca}", min_value=0.0, value=500.0)
    pub_research = st.sidebar.number_input(f"Publicidad (Research) - {marca}", min_value=0.0, value=100.0)
    segmento = st.sidebar.selectbox(f"Segmento objetivo - {marca}", options=["Shoppers", "HiEarners", "Others"])
    obj_x = st.sidebar.slider(f"Objetivo Percepción X - {marca}", -20.0, 20.0, 0.0)
    obj_y = st.sidebar.slider(f"Objetivo Percepción Y - {marca}", -20.0, 20.0, 0.0)

    decisiones.append({
        "Marca": marca,
        "Precio": precio,
        "Producción": produccion,
        "Publicidad Media": pub_media,
        "Publicidad Research": pub_research,
        "Segmento": segmento,
        "Obj_X": obj_x,
        "Obj_Y": obj_y
    })

# --- Simulación simple de resultados ---
sim_resultados = []

for d in decisiones:
    awareness = min((d["Publicidad Media"] * 0.05 + d["Publicidad Research"] * 0.1), 100)
    demanda_estim = int((d["Producción"] * (awareness / 100)) * np.random.uniform(0.9, 1.1))
    unidades_vendidas = min(d["Producción"], demanda_estim)
    costo_unitario = 150 if "Sonite" in d["Marca"] else 200
    ingresos = unidades_vendidas * d["Precio"]
    costos = unidades_vendidas * costo_unitario
    utilidad_bruta = ingresos - costos
    utilidad_neta = utilidad_bruta - (d["Publicidad Media"] + d["Publicidad Research"])

    sim_resultados.append({
        "Marca": d["Marca"],
        "Segmento": d["Segmento"],
        "Unidades Vendidas": unidades_vendidas,
        "Ingresos": ingresos,
        "Costos": costos,
        "Utilidad Bruta": utilidad_bruta,
        "Publicidad Total": d["Publicidad Media"] + d["Publicidad Research"],
        "Utilidad Neta Estimada": utilidad_neta
    })

# --- Mostrar resultados ---
st.subheader("📊 Resultados simulados por marca")
df_resultados = pd.DataFrame(sim_resultados)
st.dataframe(df_resultados.style.format({
    "Ingresos": "${:,.0f}",
    "Costos": "${:,.0f}",
    "Utilidad Bruta": "${:,.0f}",
    "Publicidad Total": "${:,.0f}",
    "Utilidad Neta Estimada": "${:,.0f}"
}))

# --- Placeholder visual para futuro: mapa perceptual ---
st.subheader("🗺️ (Próximamente) Mapa Perceptual Simulado")
st.info("Aquí se podrá visualizar la posición actual vs. objetivo de cada marca en el mapa perceptual.")
