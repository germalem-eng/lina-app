import streamlit as st
import os
import base64
import datetime
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN MECÁNICA DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")

# Sincronización exacta con Bogotá (UTC-5)
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. GESTIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "PREVENTIVO" # Por defecto entra a preventivo como pidió

# --- 3. RECURSOS (IMÁGENES) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ARQUITECTURA VISUAL (CSS) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{ width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF; box-shadow: 0 0 20px #00FFFF; object-fit: cover; }}
    .neon-titulo {{ font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 10px #00FFFF, 0 0 20px #00FFFF; text-align: center; }}
    .alerta-amarilla {{ background-color: #fff9c4; border: 2px solid #fbc02d; color: #444; padding: 15px; border-radius: 10px; margin: 20px 0; font-weight: bold; text-align: center; }}
    .barra-metalica {{ background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%); border: 2px solid #666; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
    .reloj-bogota {{ font-family: 'Courier New', monospace; font-weight: bold; color: #111; display: flex; justify-content: space-between; border-bottom: 2px solid #888; padding-bottom: 5px; margin-bottom: 10px; }}
    .boton-social {{ text-decoration: none !important; color: #333 !important; background: white; padding: 6px 12px; border-radius: 8px; font-weight: bold; font-size: 12px; border: 1px solid #999; display: inline-block; }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
c1, c2 = st.columns([1, 3])
with c1:
    st.markdown(f'<center><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></center>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<h1 class="neon-titulo" style="font-size:60px; margin:0;">L.I.N.A.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-weight:bold; color:#008fb3;">Soluciones Tecnológicas M Y M - Desde 2007</p>', unsafe_allow_html=True)

st.divider()

# --- 6. SECCIÓN ÚNICA: MANTENIMIENTO PREVENTIVO ---
st.header("🛠️ Mantenimiento Preventivo Especializado")

col_info, col_check = st.columns(2)

with col_info:
    st.subheader("📋 Datos del Equipo")
    tipo_equipo = st.selectbox("Tipo de Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
    marca = st.text_input("Marca del Producto:")
    specs = st.text_area("Características y Especificaciones (Procesador, RAM, Modelo, etc.):")
    modalidad = st.radio("Modalidad del Servicio:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)

with col_check:
    st.subheader("✅ Lista de Chequeo (Antes/Después)")
    c1 = st.checkbox("¿Enciende correctamente?")
    c2 = st.checkbox("Limpieza de polvo (Componentes internos)")
    c3 = st.checkbox("Borrado de archivos basura / Temporales")
    c4 = st.checkbox("Escaneo de Antivirus / Seguridad")
    c5 = st.checkbox("Verificación de puertos (USB, Carga, Video)")
    
    st.subheader("🔍 Diagnóstico Final")
    estado_final = st.radio("Resultado del Mantenimiento:", ["Todo está OK (Equipo en óptimas condiciones)", "Requiere Mantenimiento Adicional / Correctivo"], index=0)
    
    if estado_final == "Requiere Mantenimiento Adicional / Correctivo":
        desc_mant = st.text_area("Descripción detallada de la necesidad detectada:")
    else:
        st.success("Estado del equipo: OK")

# --- 7. CÁLCULO DE INVERSIÓN ---
st.divider()
base = 40000
recargo_domicilio = 20000 if modalidad == "A Domicilio" else 0
total = base + recargo_domicilio

st.markdown(f"""
<div style="background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 400px; margin: auto;">
    <h4 style="margin:0; color:#444;">Inversión del Servicio</h4>
    <h1 style="color: #008fb3; margin: 10px 0;">$ {total:,.0f}</h1>
    <p style="font-size: 12px; color: #666;">Incluye: Limpieza física profunda, optimización de software y diagnóstico preventivo.</p>
    <p><b>ING. Gerardo Martinez Lemus</b></p>
</div>
""", unsafe_allow_html=True)

# --- 8. CIERRE: ADVERTENCIA Y BARRA CONTACTO ---
st.markdown("""
<div class="alerta-amarilla">
    ⚠️ NOTA: Honorarios por éxito (10% ahorro) o tarifas base de $40.000.
</div>
""", unsafe_allow_html=True)

html_barra = f"""
<div class="barra-metalica">
    <div class="reloj-bogota">
        <span>📍 BOGOTÁ, COLOMBIA</span>
        <span>📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div style="font-weight: bold; color: #222;">🌐 REDES OFICIALES:</div>
        <div style="display: flex; gap: 8px;">
            <a href="https://wa.me/573114759768" target="_blank" class="boton-social">🟢 WhatsApp</a>
            <a href="https://web.facebook.com/MyMsolucionesdetecnologia/" target="_blank" class="boton-social">🔵 Facebook</a>
            <a href="https://instagram.com" target="_blank" class="boton-social">🟣 Instagram</a>
            <a href="https://linkedin.com" target="_blank" class="boton-social">💠 LinkedIn</a>
            <a href="https://youtube.com" target="_blank" class="boton-social">🔴 YouTube</a>
        </div>
    </div>
</div>
"""
st.markdown(html_barra, unsafe_allow_html=True)

# Pie de página final
st.markdown(f'<p style="text-align:right; font-size:12px; color:#555; margin-top:10px;">LINA Core V20.0 | © {ahora_bog.year} Gerardo Martinez Lemus</p>', unsafe_allow_html=True)
