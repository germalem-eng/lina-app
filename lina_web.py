import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN Y RELOJ ---
st.set_page_config(page_title="L.I.N.A. | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO (CERO ERRORES) ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""

# --- 3. RECURSOS VISUALES ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_robot_reparado_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_pagina_b64 = get_base64("Logos/fondo.jpg")

# --- 4. ESTILOS CSS (Fondo, Neón y Alineación Correcta) ---
st.markdown(f"""
<style>
    /* Fondo transparente en toda la página */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.92)),
                          url("data:image/jpeg;base64,{fondo_pagina_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
    }}

    /* Barra de Navegación Superior (Sin 'Soluciones MyM') */
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 8px; margin-bottom: 20px;
    }}

    /* Estilo para las etiquetas de Redes Sociales */
    .social-tag {{
        padding: 4px 12px; border-radius: 15px; text-decoration: none;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}

    /* Logo Redondo Perfecto con Neón Agua Marina */
    .logo-redondo {{
        width: 130px; height: 130px;
        border-radius: 50%; 
        border: 4px solid #7FFFD4;
        box-shadow: 0 0 15px #7FFFD4, 0 0 30px #7FFFD4;
        object-fit: cover;
    }}

    /* Título L.I.N.A. con Neón Azul Fluorescente (Centrado en su columna) */
    .titulo-lina-neon {{
        font-family: 'Comic Sans MS', cursive;
        font-size: clamp(40px, 8vw, 80px); color: #000;
        text-align: center;
        text-shadow: 0 0 10px #00FFFF, 0 0 20px #00FFFF;
        margin: 5px 0; line-height: 1;
    }}

    /* Subtítulos Centrados en su columna */
    .subtitulo-centrado {{
        text-align: center; font-family: sans-serif;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (RELOJ, REDES, LOGO Y TÍTULOS CORREGIDOS) ---

# Barra Superior Correcta (Sin 'Soluciones MyM')
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}
    </div>
    <div>
        <a href="#" class="social-tag" style="background-color: #FF0000;">YouTube</a>
        <a href="#" class="social-tag" style="background-color: #E1306C;">Instagram</a>
        <a href="#" class="social-tag" style="background-color: #4267B2;">Facebook</a>
        <a href="https://wa.me/573114759768" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="#" class="social-tag" style="background-color: #0088CC;">Telegram</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Alineación en Dos Columnas (Logo Izquierda, Títulos Derecha)
col_logo, col_titulos = st.columns([1, 3])

with col_logo:
    # Mostramos el logo redondo con destello neón
    if logo_robot_reparado_b64:
        st.markdown(f'<img src="data:image/jpeg;base64,{logo_robot_reparado_b64}" class="logo-redondo">', unsafe_allow_html=True)
    else:
        st.write("🤖") # Placeholder si no carga la imagen

with col_titulos:
    # Centramos el título y subtítulos dentro de esta columna
    st.markdown(f"""
    <div class="subtitulo-centrado">
        <h1 class="titulo-lina-neon">L.I.N.A.</h1>
        <div style="color: #008fb3; font-size: 22px; font-weight: bold; margin-bottom: 5px;">
            Soluciones Tecnológicas M Y M
        </div>
        <div style="font-size: 16px; color: #444;">
            Laboratorio de Inteligencia y Nuevos Algoritmos
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. NAVEGACIÓN ( Multiplataforma) ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("💰 COTIZADOR", use_container_width=True): st.session_state.seccion = "COTIZADOR"
with c2: 
    if st.button("⚖️ CASOS LEGALES", use_container_width=True): st.session_state.seccion = "GESTION"
with c3: 
    if st.button("📝 RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"
with c4: 
    if st.button("🏠 PRIVADO MyM", use_container_width=True): st.session_state.seccion = "FINANZAS"

st.divider()

# --- 7. LÓGICA DE SECCIONES (Contenido que fusionamos antes) ---
# (Se mantiene igual que en la V15.8 para no perder los datos del cotizador y la vivienda)

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador de Servicios MyM")
    col_precios, col_calc = st.columns([1, 2])
    
    with col_precios:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 2px solid #00d4ff; text-align: center;">
            <h4>📋 Lista de Precios</h4>
            <p><b>Revisión Técnica:</b> $40.000<br>(GRATIS si acepta servicio)</p>
            <p><b>Asesoría Legal:</b> $40.000<br>(GRATIS si inicia proceso)</p>
            <p><b>Recargo Domicilio:</b> $20.000</p>
        </div>
        """, unsafe_allow_html=True)

    with col_calc:
        tipo_servicio = st.selectbox("Tipo de Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal / Habeas Data"])
        modalidad = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        domicilio = 20000 if modalidad == "A Domicilio" else 0
        if tipo_servicio == "Asesoría Legal / Habeas Data":
            total = base + domicilio
            detalle = "Si inicias proceso legal, solo pagas el 10% del ahorro al finalizar. ¡Esta consulta es gratis si firmas!"
        else:
            total = (base * 1.20) + domicilio # 20% de recargo interno
            detalle = "¡La revisión es GRATIS! El valor incluye repuestos básicos y mano de obra calificada."
        st.metric("Total a Pagar", f"${total:,.0f} COP", f"+{domicilio} domicilio" if domicilio > 0 else "")
        st.caption(f"💡 {detalle}")
        st.link_button("📍 AGENDAR CITA EN WHATSAPP", "https://wa.me/573114759768?text=Hola%20Gerardo,%20quiero%20agendar%20una%20cita.")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Seguimiento de Casos y Cobros")
    
elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Nueva Radicación Legal")
    
elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Personal MyM")
    st.metric("Meta Sistecrédito", "$898.771")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: #f1f1f1; padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota de Honorarios:</b> Nuestros honorarios se basan estrictamente en el éxito conseguido. 
    Defensa Legal: 10% del ahorro. Mantenimiento: Revisión gratis si se realiza el proceso.
</div>
""", unsafe_allow_html=True)

st.caption(f"L.I.N.A. V16.0 | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
