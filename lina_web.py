import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V16.6 | Core MyM", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
if 'log_file' not in st.session_state: st.session_state.log_file = "registro_lina_mym.csv"

# --- 3. RECURSOS VISUALES ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_robot_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 4. ESTILOS CSS (DISEÑO MONUMENTAL) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 8px; margin-bottom: 10px;
    }}
    .social-tag {{
        padding: 4px 12px; border-radius: 15px; text-decoration: none;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
    .titulo-lina-final {{
        font-family: 'Comic Sans MS', cursive; 
        font-size: clamp(80px, 15vw, 150px); /* LINA Monumental */
        color: #000; text-shadow: 0 0 20px #7FFFD4, 0 0 40px #7FFFD4; 
        margin: 0; line-height: 1; text-align: center;
    }}
    .logo-redondo-final {{
        width: 220px; height: 220px; /* Logo más grande */
        border-radius: 50%; border: 5px solid #7FFFD4; 
        box-shadow: 0 0 25px #7FFFD4; object-fit: cover;
    }}
    .col-titulos-final {{
        display: flex; flex-direction: column; justify-content: center;
        text-align: center; height: 100%;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}</div>
    <div>
        <a href="#" class="social-tag" style="background-color: #FF0000;">YouTube</a>
        <a href="#" class="social-tag" style="background-color: #E1306C;">Instagram</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="#" class="social-tag" style="background-color: #0088CC;">Telegram</a>
    </div>
</div>
""", unsafe_allow_html=True)

col_logo, col_titulos = st.columns([1, 2.5])
with col_logo:
    if logo_robot_b64:
        st.markdown(f'<div style="display:flex; justify-content:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_titulos:
    st.markdown(f"""
    <div class="col-titulos-final">
        <h1 class="titulo-lina-final">L.I.N.A.</h1>
        <div style="color:#008fb3; font-size:28px; font-weight:bold;">Laboratorio de Inteligencia y Nuevos Algoritmos</div>
        <div style="color:#444; font-size:20px;">Soluciones Tecnológicas M Y M | Desde 2007</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. NAVEGACIÓN (CORREGIDA) ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("💰 COTIZADOR", use_container_width=True):
        st.session_state.seccion = "COTIZADOR"
with c2:
    if st.button("⚖️ GESTIÓN DE CASOS", use_container_width=True):
        st.session_state.seccion = "GESTION"
with c3:
    if st.button("📝 RADICACIÓN", use_container_width=True):
        st.session_state.seccion = "RADICACION"
with c4:
    if st.button("🏠 PRIVADO MyM", use_container_width=True):
        st.session_state.seccion = "FINANZAS"

st.divider()

# --- 7. LÓGICA DE SECCIONES ---
if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador de Servicios MyM")
    # ... (Resto del código del cotizador)
    st.info("Configuración de precios lista.")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Seguimiento a Casos")
    if os.path.exists(st.session_state.log_file):
        st.dataframe(pd.read_csv(st.session_state.log_file), use_container_width=True)

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Generador de Peticiones")
    st.text_area("📄 Vista Previa del Documento:", value=st.session_state.doc_final, height=250)

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Personal MyM")
    st.metric("Meta Sistecrédito", "$898.771")

st.caption(f"LINA Core | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
