import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V16.7 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
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
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 4. ESTILOS CSS (DISEÑO MONUMENTAL Y FONDO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
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
        font-size: clamp(70px, 12vw, 130px);
        color: #000; text-shadow: 0 0 20px #7FFFD4, 0 0 40px #7FFFD4; 
        margin: 0; line-height: 1; text-align: center;
    }}
    .logo-redondo-final {{
        width: 190px; height: 190px;
        border-radius: 50%; border: 5px solid #7FFFD4; 
        box-shadow: 0 0 25px #7FFFD4; object-fit: cover;
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
        st.markdown(f'<div style="display:flex; justify-content:center; align-items:center; height:100%;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_titulos:
    st.markdown(f"""
    <div style="display:flex; flex-direction:column; justify-content:center; text-align:center;">
        <h1 class="titulo-lina-final">L.I.N.A.</h1>
        <div style="color:#008fb3; font-size:26px; font-weight:bold;">Laboratorio de Inteligencia y Nuevos Algoritmos</div>
        <div style="color:#444; font-size:18px;">Soluciones Tecnológicas M Y M | Desde 2007</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. NAVEGACIÓN (Sintaxis Corregida) ---
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

# --- 7. LÓGICA DE SECCIONES (COTIZADOR RESTAURADO) ---
if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente de Servicios")
    
    col_precios, col_calc = st.columns([1, 2])
    
    with col_precios:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 2px solid #00d4ff;">
            <h4 style="text-align:center;">📋 Tarifas Oficiales</h4>
            <ul style="font-size: 14px;">
                <li><b>Revisión Técnica:</b> $40.000<br><small>(Bonificada al 100% si acepta el servicio)</small></li>
                <li><b>Trámite Legal:</b> 10% del ahorro conseguido.</li>
                <li><b>Recargo Domicilio:</b> $20.000</li>
                <li><b>Mantenimientos:</b> Incluyen peritaje técnico especializado.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_calc:
        tipo_ser = st.selectbox("Seleccione el Servicio:", 
                                ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal / Habeas Data"])
        modalidad = st.radio("Modalidad de atención:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        
        # LÓGICA DE COBRO GERARDO
        base_revision = 40000
        recargo_dom = 20000 if modalidad == "A Domicilio" else 0
        
        if "Mantenimiento" in tipo_ser:
            # Estrategia: Decimos revisión gratis, pero sumamos 20% sobre el mínimo internamente
            total = (base_revision * 1.20) + recargo_dom
            nota = "✅ **¡REVISIÓN GRATIS!** El valor mostrado incluye la mano de obra y el peritaje técnico."
        elif "Legal" in tipo_ser:
            total = base_revision + recargo_dom
            nota = "⚖️ **ASESORÍA PROFESIONAL:** Si iniciamos el proceso, el costo de esta consulta se abona al éxito del caso (10%)."
        
        st.metric("Inversión Total Estimada", f"${total:,.0f} COP", f"+{recargo_dom} por domicilio" if recargo_dom > 0 else None)
        st.info(nota)
        
        # Botón de Agendamiento Directo
        msg = f"Hola Gerardo, deseo agendar un {tipo_ser} en modalidad {modalidad}."
        st.link_button("📅 AGENDAR CITA EN WHATSAPP", f"https://wa.me/573114759768?text={msg.replace(' ', '%20')}")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Seguimiento a Casos Generados")
    if os.path.exists(archivo_casos):
        st.dataframe(pd.read_csv(archivo_casos), use_container_width=True)
    else:
        st.info("No hay registros de casos pendientes.")

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Generador de Peticiones Legales")
    st.text_area("Vista Previa:", value=st.session_state.doc_final, height=300)

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Personal - Metas Vivienda")
    st.metric("Saldo Sistecrédito", "$898.771")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: #f1f1f1; padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>Soluciones Tecnológicas M Y M</b><br>
    Expertos en Soporte Técnico y Soluciones Legales desde 2007.
</div>
""", unsafe_allow_html=True)
