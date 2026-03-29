import streamlit as st
import os
import base64
import datetime
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")

# Ajuste de hora Colombia (UTC-5)
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "COTIZADOR"

# --- 3. RECURSOS VISUALES ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 25px;
    }}
    .logo-redondo-final {{
        width: 250px; height: 250px;
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .resaltado-blanco {{
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 8px; padding: 5px 15px; margin: 3px 0;
        display: inline-block; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 0.85; margin: 0; text-align: center;
    }}
    .social-tag {{
        padding: 5px 10px; border-radius: 10px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 11px; margin-left: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; color: #333;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | S T M Y M
    </div>
    <div style="display: flex; flex-wrap: wrap; justify-content: flex-end;">
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
        <a href="https://www.youtube.com/@gerardomartinezlemus7969" target="_blank" class="social-tag" style="background-color: #FF0000;">YouTube</a>
    </div>
</div>
""", unsafe_allow_html=True)

col_izq, col_der = st.columns([1, 2])
with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_der:
    st.markdown(f"""
    <div style="text-align: center; margin-top: -10px;">
        <h1 class="neon-imponente" style="font-size: 90px;">L.I.N.A.</h1>
        <div class="resaltado-blanco"><span style="color: #008fb3; font-size: 22px; font-weight: bold;">Laboratorio de Inteligencia y Nuevos Algoritmos</span></div><br>
        <div class="resaltado-blanco"><span style="color: #444; font-size: 16px; font-weight: bold;">Soluciones Tecnológicas M Y M - Desde 2007</span></div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. NUEVO PANEL OPERATIVO (6 BOTONES INDEPENDIENTES) ---
st.write("### 🚀 Seleccione el Servicio Requerido:")

# Creamos dos filas de 3 columnas para que los botones se vean grandes y claros
fila1_c1, fila1_c2, fila1_c3 = st.columns(3)
fila2_c1, fila2_c2, fila2_c3 = st.columns(3)

with fila1_c1:
    if st.button("🛠️ Mantenimiento Preventivo", use_container_width=True):
        st.session_state.seccion = "PREVENTIVO"
with fila1_c2:
    if st.button("🔧 Mantenimiento Correctivo", use_container_width=True):
        st.session_state.seccion = "CORRECTIVO"
with fila1_c3:
    if st.button("⚖️ Gestión Legal", use_container_width=True):
        st.session_state.seccion = "GESTION_LEGAL"

with fila2_c1:
    if st.button("📝 Radicación", use_container_width=True):
        st.session_state.seccion = "RADICACION"
with fila2_c2:
    if st.button("🛡️ Casos Legales", use_container_width=True):
        st.session_state.seccion = "CASOS_LEGALES"
with fila2_c3:
    if st.button("📁 Archivo", use_container_width=True):
        st.session_state.seccion = "ARCHIVO"

st.divider()

# --- 7. LÓGICA DE COTIZACIÓN SEGÚN SERVICIO SELECCIONADO ---

# Lista de secciones que comparten la misma lógica de cotización
servicios_cotizables = ["PREVENTIVO", "CORRECTIVO", "GESTION_LEGAL", "RADICACION", "CASOS_LEGALES", "ARCHIVO"]

if st.session_state.seccion in servicios_cotizables:
    st.subheader(f"💰 Cotizador: {st.session_state.seccion.replace('_', ' ')}")
    
    col_inputs, col_resultado = st.columns([2, 1])
    
    with col_inputs:
        # Selección de Modalidad
        mod = st.radio("Modalidad del Servicio:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        
        # Tipo de atención
        tipo_atencion = st.radio("Tipo de Atención:", ["Solo Consulta", "Tomar Asesoría/Servicio Completo"], horizontal=True)
        
        # Bloque condicional para Dirección y Horario
        if mod == "A Domicilio":
            st.info("📍 Ingrese los detalles para la visita técnica:")
            dir_visita = st.text_input("Dirección completa:")
            col_fecha, col_hora = st.columns(2)
            with col_fecha:
                fecha_visita = st.date_input("Fecha sugerida:", min_value=datetime.date.today())
            with col_hora:
                hora_visita = st.time_input("Hora sugerida:")

        # --- CÁLCULO DE VALORES ---
        base_consulta = 40000
        valor_domicilio = 20000
        total = 0

        if mod in ["Virtual", "En Oficina"]:
            total = base_consulta if tipo_atencion == "Solo Consulta" else 0
        elif mod == "A Domicilio":
            total = (base_consulta + valor_domicilio) if tipo_atencion == "Solo Consulta" else valor_domicilio

    with col_resultado:
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 15px; border: 3px solid #00d4ff; text-align: center;">
            <h3 style="color: #333; margin-bottom: 0;">Inversión Total</h3>
            <h1 style="color: #008fb3; font-size: 45px; margin-top: 10px;">$ {total:,.0f}</h1>
            <p style="font-size: 13px; color: #666;">
            <b>⚠️ MyM Nota:</b> Honorarios por éxito (10% ahorro) o tarifas base de $40.000.<br>
            <hr>
            <b>LINA Core V20.0</b><br>
            © {ahora.year} <b>ING. Gerardo Martinez Lemus</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if total > 0 and mod == "Virtual":
            st.warning("⚠️ Recuerde enviar el pantallazo de pago Nequi para habilitar la conexión remota.")

# --- 8. PIE DE PÁGINA (ESTO VA AL FINAL DE TODO EL SCRIPT) ---
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 40px;">
    <table style="width:100%; border:none;">
        <tr>
            <td style="width:70%; border:none;">
                <b style="color:#008fb3;">⚠️ Nota Legal Soluciones MyM:</b><br>
                Los honorarios por éxito corresponden al 10% del ahorro logrado en procesos legales. 
                Las tarifas base de revisión técnica inician en <b>$40.000</b>.
            </td>
            <td style="text-align:right; border:none; color:#666; font-size: 13px;">
                <b>LINA Core V20.0</b><br>
                Desarrollado por:<br>
                <b>ING. Gerardo Martinez Lemus</b><br>
                Bogotá, {ahora.year}
            </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)
