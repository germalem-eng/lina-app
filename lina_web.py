import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V18.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
archivo_casos = "database_casos_mym.csv"

# --- 3. RECURSOS VISUALES ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_robot_b64 = get_base64("Logos/logo_robot_2007.jpg")
# Usamos el fondo de código binario de image_3.png
fondo_binario_b64 = get_base64("Logos/fondo_binario.png")

# --- 4. ESTILOS CSS (FONDO BINARIO Y DISEÑO DE COLUMNAS) ---
def get_image_base64(path):
    import base64
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Cargamos el fondo desde la ruta Logos/fondo.jpg
fondo_path = "Logos/fondo.jpg"
fondo_b64 = get_image_base64(fondo_path)

st.markdown(f"""
<style>
    /* 1. FONDO CON TRANSPARENCIA DEL 50% */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
    }}
    
    /* 2. BARRA PLATEADA SUPERIOR */
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 8px; margin-bottom: 15px;
    }}
    
    /* 3. LOGO GIGANTE CON NEÓN AZUL */
    .logo-redondo-final {{
        width: 300px; height: 300px; /* Tamaño monumental */
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 30px #00FFFF, 0 0 60px #00FFFF;
        object-fit: cover;
    }}
    
    /* 4. BLOQUE DE TÍTULOS ESCALONADOS (DERECHA) */
    .contenedor-titulos {{
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; text-align: center; width: 100%; height: 100%;
    }}

    .titulo-lina-final {{
        font-family: 'Comic Sans MS', cursive; 
        font-size: clamp(100px, 18vw, 220px); /* LINA GIGANTE */
        color: #004d61; /* Azul Profundo MyM */
        text-shadow: 0 0 30px #00FFFF, 0 0 60px #00FFFF;
        margin: 0; line-height: 0.8;
    }}
    
    .sub-laboratorio {{
        color: #008fb3; font-size: 32px; font-weight: bold; line-height: 1.1; margin-top: 15px;
    }}
    
    .sub-mym {{
        color: #444; font-size: 22px; font-weight: 500; margin-top: 10px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO EN DOS COLUMNAS ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}</div>
    <div style="font-weight: bold; color: #333;">SOLUCIONES TECNOLÓGICAS M Y M</div>
</div>
""", unsafe_allow_html=True)

# Creamos las dos columnas para recuperar la estructura
col_logo, col_titulos = st.columns([1.2, 2.3])

with col_logo:
    # Mostramos el logo gigante a la izquierda
    if logo_robot_b64:
        st.markdown(f'<div style="display:flex; justify-content:center; align-items:center; height:100%;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_titulos:
    # Mostramos LINA y subtítulos a la derecha de forma escalonada
    st.markdown(f"""
    <div class="contenedor-titulos">
        <h1 class="titulo-lina-final">L.I.N.A.</h1>
        <div class="sub-laboratorio">
            Laboratorio

# --- 6. NAVEGACIÓN ---
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

# --- 7. LÓGICA DE SECCIONES (Mantenemos el Cotizador Funcional) ---
if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        dom = 20000 if mod == "A Domicilio" else 0
        total = (base * 1.20) + dom if "Mantenimiento" in ser else base + dom
        st.metric("Inversión Total", f"${total:,.0f} COP")
        st.link_button("📅 AGENDAR CITA", f"https://wa.me/573114759768")
        
    with col_info:
        st.markdown("""
        <div style="background-color: rgba(248, 249, 250, 0.7); padding: 15px; border-radius: 10px; border: 2px solid #00d4ff;">
            <h4 style="text-align:center;">📋 Tarifas MyM</h4>
            <ul style="font-size: 14px;">
                <li><b>Revisión:</b> $40.000 (Gratis con servicio)</li>
                <li><b>Legal:</b> 10% del ahorro</li>
                <li><b>Domicilio:</b> $20.000</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Personal")
    st.metric("Meta Sistecrédito", "$898.771")

# --- 8. PIE DE PÁGINA (EJECUTIVO) ---
st.markdown(f"""
<div style="background-color: rgba(241, 241, 241, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota de Honorarios:</b> Nuestros honorarios se basan estrictamente en el éxito conseguido. 
    Defensa Legal: 10% del ahorro. Mantenimiento: Revisión gratis si se realiza el proceso.
</div>
""", unsafe_allow_html=True)

st.caption(f"LINA Core | © {ahora.year} Gerardo Martinez Lemus | Soluciones Tecnológicas M Y M")
