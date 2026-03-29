import streamlit as st
import os
import base64
import datetime
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")

# Ajuste de hora Colombia (UTC-5)
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "INICIO"

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
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 25px;
    }}
    .logo-redondo-final {{
        width: 220px; height: 220px;
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 1; margin: 0; text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO: L.I.N.A. Y PLACAS RESALTADAS ---
col_head1, col_head2 = st.columns([1, 2.2])

with col_head1:
    st.markdown(f'''
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final">
        </div>
    ''', unsafe_allow_html=True)

with col_head2:
    contenido_html = f"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 250px; text-align: center;">
        <h1 class="neon-imponente" style="font-size: 85px; margin: 0; padding: 0;">L.I.N.A.</h1>
        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 15px; width: 100%; align-items: center;">
            <div style="background: rgba(255, 255, 255, 0.95); padding: 10px 20px; border-radius: 12px; border: 2px solid #00FFFF; box-shadow: 0 0 15px rgba(0,255,255,0.2); width: fit-content;">
                <span style="color: #008fb3; font-size: 20px; font-weight: bold; display: block; white-space: nowrap;">
                    Laboratorio de Inteligencia y Nuevos Algoritmos
                </span>
            </div>
            <div style="background: rgba(255, 255, 255, 0.95); padding: 10px 20px; border-radius: 12px; border: 2px solid #00FFFF; box-shadow: 0 0 15px rgba(0,255,255,0.2); width: fit-content;">
                <span style="color: #444; font-size: 16px; font-weight: bold; display: block; white-space: nowrap;">
                    Soluciones Tecnológicas M Y M - Desde 2007
                </span>
            </div>
        </div>
    </div>
    """
    st.markdown(contenido_html, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO (6 BOTONES) ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("🛠️ PREVENTIVO", use_container_width=True): st.session_state.seccion = "PREVENTIVO"; st.rerun()
with c2:
    if st.button("🔧 CORRECTIVO", use_container_width=True): st.session_state.seccion = "CORRECTIVO"; st.rerun()
with c3:
    if st.button("⚖️ GESTIÓN", use_container_width=True): st.session_state.seccion = "GESTION"; st.rerun()
with c4:
