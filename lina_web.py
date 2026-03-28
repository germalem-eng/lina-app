import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V19.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
archivo_casos = "database_casos_mym.csv"

# --- 3. RECURSOS VISUALES (RUTAS DIRECTAS) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS ACTUALIZADOS (CON RECUADRO CLARO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
    }}
    
    /* RECUADRO CLARO PARA TÍTULOS (EFECTO CRISTAL) */
    .recuadro-titulos {{
        background: rgba(255, 255, 255, 0.6); /* Fondo blanco traslúcido */
        backdrop-filter: blur(10px); /* Desenfoque sutil del fondo */
        padding: 30px;
        border-radius: 25px;
        border: 2px solid rgba(0, 255, 255, 0.3); /* Borde cyan suave */
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }}

    .titulo-lina-final {{
        font-family: 'Comic Sans MS', cursive; 
        font-size: 140px; color: #004d61; 
        text-shadow: 0 0 30px #00FFFF; margin: 0; line-height: 0.8;
    }}

    .sub-laboratorio {{
        color: #008fb3; font-size: 30px; font-weight: bold; line-height: 1.1; margin-top: 15px;
    }}

    .sub-mym {{
        color: #444; font-size: 20px; font-weight: 500; margin-top: 10px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (DENTRO DE LAS COLUMNAS) ---
# ... (Mantén tu barra plateada igual) ...

col_izq, col_der = st.columns([1.2, 2.3])

with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center; align-items:center; height:100%;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_der:
    # AQUÍ APLICAMOS EL NUEVO RECUADRO CLARO
    st.markdown(f"""
    <div class="recuadro-titulos">
        <h1 class="titulo-lina-final">L.I.N.A.</h1>
        <div class="sub-laboratorio">
            Laboratorio de Inteligencia<br>y Nuevos Algoritmos
        </div>
        <div class="sub-mym">
            Soluciones Tecnológicas MYM<br>Desde 2007
        </div>
    </div>
    """, unsafe_allow_html=True)
st.divider()

# --- 6. PANEL OPERATIVO ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("💰 COTIZADOR", use_container_width=True): st.session_state.seccion = "COTIZADOR"
with c2:
    if st.button("⚖️ GESTIÓN DE CASOS", use_container_width=True): st.session_state.seccion = "GESTION"
with c3:
    if st.button("📝 RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"
with c4:
    if st.button("🏠 PRIVADO MyM", use_container_width=True): st.session_state.seccion = "FINANZAS"

st.divider()

# --- 7. LÓGICA DE SECCIONES (ACTUALIZADO CON FORMATO COLOMBIANO) ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        dom = 20000 if mod == "A Domicilio" else 0
        total = (base * 1.20) + dom if "Mantenimiento" in ser else base + dom
        # Formato de moneda colombiana con separador de miles
        st.metric("Inversión Total", f"$ {total:,.0f}".replace(",", "."))
        
    with col_info:
        # Aquí eliminamos la 'k' y pusimos el formato correcto
        st.markdown("""
        <div style="background-color:rgba(248,249,250,0.7);padding:15px;border-radius:10px;border:2px solid #00d4ff;">
            <h4 style="text-align:center;">📋 Tarifas Oficiales</h4>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>📍 <b>Revisión:</b> $40.000</li>
                <li>⚖️ <b>Legal:</b> 10% del ahorro</li>
                <li>🏠 <b>Domicilio:</b> $20.000</li>
            </ul>
            <small>* La revisión es gratis si se realiza el servicio.</small>
        </div>
        """, unsafe_allow_html=True)

# --- (Las secciones de RADICACION, GESTION y FINANZAS se mantienen igual) ---

# --- 8. PIE DE PÁGINA (EJECUTIVO) ---
st.markdown(f"""
<div style="background-color: rgba(241, 241, 241, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota de Honorarios:</b> Nuestros honorarios se basan en el éxito conseguido (10% del ahorro legal) 
    o tarifas base de <b>$40.000</b> por revisión técnica.
</div>
""", unsafe_allow_html=True)

st.caption(f"LINA Core | © {ahora.year} Gerardo Martinez Lemus | Soluciones Tecnológicas M Y M")
