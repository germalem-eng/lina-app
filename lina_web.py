import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN Y RELOJ ---
st.set_page_config(page_title="L.I.N.A. | MyM Soluciones", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO (EVITA ERRORES) ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""

# --- 3. RECURSOS VISUALES (LOGO Y FONDO) ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_robot_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_pagina_b64 = get_base64("Logos/fondo.jpg")

# --- 4. ESTILOS CSS (FONDO TRANSPARENTE, NEÓN Y CENTRADO) ---
st.markdown(f"""
<style>
    /* Fondo transparente en toda la página */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.92)),
                          url("data:image/jpeg;base64,{fondo_pagina_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
    }}

    /* Barra de Navegación Superior */
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 8px; margin-bottom: 20px;
    }}

    /* Logo Redondo con Neón Agua Marina */
    .logo-redondo {{
        display: block; margin: 0 auto;
        width: 140px; height: 140px;
        border-radius: 50%; 
        border: 4px solid #7FFFD4;
        box-shadow: 0 0 15px #7FFFD4, 0 0 30px #7FFFD4;
        object-fit: cover;
    }}

    /* Título L.I.N.A. con Neón Azul Fluorescente */
    .titulo-lina-neon {{
        font-family: 'Comic Sans MS', cursive;
        font-size: 80px; color: #000;
        text-align: center;
        text-shadow: 0 0 10px #00FFFF, 0 0 20px #00FFFF;
        margin: 5px 0; line-height: 1;
    }}

    .centrado-texto {{ text-align: center; margin-bottom: 20px; font-family: sans-serif; }}

    /* Etiquetas de Redes Sociales */
    .social-tag {{
        padding: 4px 12px; border-radius: 15px; text-decoration: none;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (RELOJ, REDES, LOGO Y TÍTULOS) ---

# Barra Superior
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | SOLUCIONES MyM
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

# Cuerpo Central Centrado
st.markdown(f"""
<div class="centrado-texto">
    <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo">
    <h1 class="titulo-lina-neon">L.I.N.A.</h1>
    <div style="color: #008fb3; font-size: 22px; font-weight: bold;">GESTIÓN PROFESIONAL MyM | DESDE 2007</div>
    <div style="font-size: 16px; color: #444;">Laboratorio de Inteligencia y Nuevos Algoritmos</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 6. NAVEGACIÓN (AQUÍ CONTINÚA TU CÓDIGO DE BOTONES) ---
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

# --- 7. MÓDULO COTIZADOR ---
if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador de Servicios MyM")
    
    col_precios, col_calc = st.columns([1, 2])
    
    with col_precios:
        st.markdown("""
        <div class="price-card">
            <h4>📋 Lista de Precios</h4>
            <p><b>Revisión Técnica:</b> $40.000<br>(GRATIS si acepta servicio)</p>
            <p><b>Asesoría Legal:</b> $40.000<br>(GRATIS si inicia proceso)</p>
            <p><b>Recargo Domicilio:</b> $20.000</p>
        </div>
        """, unsafe_allow_html=True)

    with col_calc:
        tipo_servicio = st.selectbox("Tipo de Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal / Habeas Data"])
        modalidad = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        
        # Lógica de Cobro
        base = 40000
        domicilio = 20000 if modalidad == "A Domicilio" else 0
        
        if tipo_servicio == "Asesoría Legal / Habeas Data":
            total = base + domicilio
            detalle = "Si inicias proceso legal, solo pagas el 10% del ahorro al finalizar. ¡Esta consulta es gratis si firmas!"
        else:
            # Estrategia 20% sobre el mínimo
            total = (base * 1.20) + domicilio
            detalle = "¡La revisión es GRATIS! El valor incluye repuestos básicos y mano de obra calificada."

        st.metric("Total a Pagar", f"${total:,.0f} COP", f"+{domicilio} domicilio" if domicilio > 0 else "")
        st.caption(f"💡 {detalle}")

        if st.button("📍 AGENDAR CITA AHORA"):
            st.success(f"Cita solicitada para {tipo_servicio} ({modalidad}). Nos comunicaremos al WhatsApp.")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Seguimiento de Casos y Cobros")
    # Monitor de 21 días
    f_rad = st.date_input("Fecha Radicación:", value=ahora.date())
    f_est = f_rad + timedelta(days=21)
    st.info(f"⏳ Vencimiento legal: {f_est.strftime('%d/%m/%Y')} (Faltan {(f_est - ahora.date()).days} días)")
    
    if os.path.exists(archivo_casos):
        st.dataframe(pd.read_csv(archivo_casos), use_container_width=True)

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Nueva Radicación Legal")
    u_nom = st.text_input("Nombre del Cliente:")
    u_aho = st.number_input("Ahorro Proyectado ($):", min_value=0)
    if st.button("Generar Registro"):
        hon = u_aho * 0.10
        st.success(f"Registrado. Honorarios por ganar: ${hon:,.0f}")

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

st.caption(f"L.I.N.A. V15.8 | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
