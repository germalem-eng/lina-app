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
    st.session_state.seccion = "INICIO"

# --- 3. PROCESAMIENTO DE IMÁGENES (BASE64) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ARQUITECTURA VISUAL (CSS AISLADO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{
        width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF;
        box-shadow: 0 0 25px #00FFFF; object-fit: cover;
    }}
    .neon-titulo {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 1; margin: 0; text-align: center;
    }}
    .alerta-amarilla {{
        background-color: #fff9c4; border: 2px solid #fbc02d; color: #444;
        padding: 15px; border-radius: 10px; margin-top: 20px; margin-bottom: 10px;
        font-size: 15px; text-align: center; font-weight: bold; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .barra-metalica {{
        background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border: 2px solid #666; border-radius: 15px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .reloj-bogota {{
        font-family: 'Courier New', monospace; font-weight: bold; color: #111;
        font-size: 16px; border-bottom: 2px solid #888; margin-bottom: 12px;
        padding-bottom: 10px; display: flex; justify-content: space-between;
    }}
    .boton-social {{
        text-decoration: none !important; color: #333 !important; background: white;
        padding: 8px 15px; border-radius: 10px; font-weight: bold; font-size: 13px;
        transition: 0.3s ease; border: 1px solid #999; display: inline-block;
    }}
    .boton-social:hover {{
        transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,255,255,0.5);
        border-color: #00FFFF;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
col_logo, col_text = st.columns([1, 2.5])
with col_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with col_text:
    st.markdown(f"""
    <div style="text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:10px;">
            <span style="color:#008fb3; font-weight:bold; font-size:18px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span>
        </div>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:8px;">
            <span style="color:#444; font-weight:bold; font-size:14px;">Soluciones Tecnológicas M Y M - Desde 2007</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL DE CONTROL OPERATIVO (6 BOTONES) ---
st.write("### 🚀 Panel Operativo:")
btns = st.columns(6)
opciones = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, opcion in enumerate(opciones):
    if btns[i].button(opcion, use_container_width=True):
        st.session_state.seccion = opcion.split()[1]
        st.rerun()

st.divider()

# --- 7. MANTENIMIENTO PREVENTIVO (DETALLE TÉCNICO) ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    
    col_info, col_check = st.columns(2)
    
    with col_info:
        st.subheader("📋 Datos del Equipo")
        tipo_equipo = st.selectbox("Tipo de Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca del Producto:")
        specs = st.text_area("Características y Especificaciones (Procesador, RAM, etc.):")
        modalidad = st.radio("Modalidad del Servicio:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)

    with col_check:
        st.subheader("✅ Checklist (Antes/Después)")
        st.checkbox("¿Enciende correctamente?")
        st.checkbox("Limpieza de polvo (Componentes internos)")
        st.checkbox("Borrado de archivos basura / Temporales")
        st.checkbox("Escaneo de Antivirus / Seguridad")
        st.checkbox("Verificación de puertos (USB, Carga, Video)")
        
        st.subheader("🔍 Diagnóstico Final")
        resultado = st.radio("Estado del Equipo:", ["Todo está OK", "Requiere Mantenimiento Correctivo"], index=0)
        
        if resultado == "Requiere Mantenimiento Correctivo":
            st.text_area("Descripción de la necesidad detectada:")
        else:
            st.success("Diagnóstico: Equipo en óptimas condiciones.")

    # Cálculo de Inversión
    base = 40000
    recargo = 20000 if modalidad == "A Domicilio" else 0
    total = base + recargo

    st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 450px; margin: 20px auto;">
        <h4 style="margin:0; color:#444;">Inversión Total del Servicio</h4>
        <h1 style="color: #008fb3; margin: 10px 0;">$ {total:,.0f}</h1>
        <p style="font-size: 13px;"><b>ING. Gerardo Martinez Lemus</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- 8. BLOQUE FINAL: ADVERTENCIA + CONTACTO + FIRMA ---

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
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
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

st.markdown(f"""
<div style="background: rgba(255,255,255,0.8); padding:15px; border-radius:10px; border-left:6px solid #008fb3; margin-top:25px; text-align:right;">
    <p style="color:#444; margin:0; font-size:13px;">
        <b>LINA Core V20.0</b> | © {ahora_bog.year} <b>ING. Gerardo Martinez Lemus</b>
    </p>
</div>
""", unsafe_allow_html=True)
