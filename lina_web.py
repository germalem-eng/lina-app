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

# --- 2. GESTIÓN DE ESTADO (PERSISTENCIA) ---
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
# Separamos el CSS para que las llaves {} no choquen con las variables de Python
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{
        width: 220px; height: 220px; border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .neon-titulo {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 1; margin: 0; text-align: center;
    }}
    .alerta-amarilla {{
        background-color: #fff9c4; border: 2px solid #fbc02d; color: #444;
        padding: 15px; border-radius: 10px; margin-top: 30px; margin-bottom: 10px;
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

# --- 5. ENCABEZADO E IDENTIDAD ---
col1, col2 = st.columns([1, 2.2])
with col1:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="text-align:center; min-height:250px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 class="neon-titulo" style="font-size:85px;">L.I.N.A.</h1>
        <div style="background:rgba(255,255,255,0.9); padding:10px 20px; border-radius:10px; border:2px solid #00FFFF; margin-top:15px;">
            <span style="color:#008fb3; font-weight:bold; font-size:20px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span>
        </div>
        <div style="background:rgba(255,255,255,0.9); padding:10px 20px; border-radius:10px; border:2px solid #00FFFF; margin-top:10px;">
            <span style="color:#444; font-weight:bold; font-size:16px;">Soluciones Tecnológicas M Y M - Desde 2007</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL DE CONTROL OPERATIVO ---
st.write("### 🚀 Panel Operativo:")
btns = st.columns(6)
opciones = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, opcion in enumerate(opciones):
    if btns[i].button(opcion, use_container_width=True):
        st.session_state.seccion = opcion.split()[1]
        st.rerun()

st.divider()

# --- 7. DESARROLLO DE SECCIONES (EJEMPLO PREVENTIVO) ---
if st.session_state.seccion == "PREVENTIVO":
    st.subheader("🛠️ Mantenimiento Preventivo")
    c_izq, c_der = st.columns([2, 1])
    with c_izq:
        st.selectbox("Equipo:", ["PC Mesa", "Portátil", "Todo en Uno"])
        st.text_area("Detalles del estado inicial:")
    with c_der:
        st.info("Tarifa base: $40.000")

# --- 8. BLOQUE FINAL: ADVERTENCIA + CONTACTO + FIRMA ---

# A. Nota de Honorarios (Amarillo Advertencia)
st.markdown("""
<div class="alerta-amarilla">
    ⚠️ NOTA: Honorarios por éxito (10% ahorro) o tarifas base de $40.000.
</div>
""", unsafe_allow_html=True)

# B. Barra Plateada (Reloj y Redes) - Sin CSS interno para evitar errores
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
            <a href="https://x.com" target="_blank" class="boton-social">⚫ X</a>
        </div>
    </div>
</div>
"""
st.markdown(html_barra, unsafe_allow_html=True)

# C. Footer con Firma Profesional
st.markdown(f"""
<div style="background: rgba(255,255,255,0.8); padding:15px; border-radius:10px; border-left:6px solid #008fb3; margin-top:25px; text-align:right;">
    <p style="color:#444; margin:0; font-size:13px;">
        <b>LINA Core V20.0</b> | © {ahora_bog.year} <b>ING. Gerardo Martinez Lemus</b>
    </p>
</div>
""", unsafe_allow_html=True)
