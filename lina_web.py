import streamlit as st
import os
import base64
import datetime
import urllib.parse
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from fpdf import FPDF

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.2 | Soluciones MyM", layout="wide", page_icon="🤖")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. MEMORIA DE SESIÓN ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'texto_fijo' not in st.session_state: st.session_state.texto_fijo = ""
if 'inventario' not in st.session_state:
    st.session_state.inventario = [
        {"Fecha": "2026-03-15", "Equipo": "HP Compaq dc5800 SFF", "Trabajo": "Cambio de pasta térmica y reemplazo de disco duro HDD por SSD.", "Estado": "Entregado"}
    ]
# --- 3. RECURSOS VISUALES ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    return ""


logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS (FONDO TRANSPARENTE EN SIDEBAR) ---
st.markdown(f"""
<style>
    /* Fondo Global */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    /* Sidebar Transparente */
    [data-testid="stSidebar"] {{
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 255, 255, 0.2);
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 25px;
    }}
    .logo-redondo-final {{
        width: 250px; height: 250px; border-radius: 50%; border: 6px solid #00FFFF; box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .sidebar-logo {{
        display: block; margin: auto; width: 180px; height: 180px; border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 15px #00FFFF; object-fit: cover;
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 0.85; margin: 0; text-align: center;
    }}
    .resaltado-blanco {{
        background-color: rgba(255, 255, 255, 0.85); border-radius: 8px; padding: 5px 15px; margin: 3px 0; display: inline-block;
    }}
    .social-tag {{
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important; color: white !important; font-weight: bold; font-size: 12px; margin-left: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO SUPERIOR ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; color: #333;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | S T M Y M
    </div>
    <div style="display: flex; flex-wrap: wrap; justify-content: flex-end;">
        <a href="https://www.youtube.com/@gerardomartinezlemus7969" target="_blank" class="social-tag" style="background-color: #FF0000;">YouTube</a>
        <a href="https://www.tiktok.com/@solucionesmym" target="_blank" class="social-tag" style="background-color: #000000;">TikTok</a>
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. TÍTULO PRINCIPAL ---
st.markdown(f'<div style="display:flex; justify-content:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)
st.markdown(f'<h1 class="neon-imponente" style="font-size: 90px; margin-top: 10px;">L.I.N.A.</h1>', unsafe_allow_html=True)
st.divider()

# --- 7. MENÚ LATERAL (LOGO ARRIBA + PANEL ABAJO) ---
with st.sidebar:
    if logo_robot_b64:
        st.markdown(f'<img src="data:image/jpeg;base64,{logo_robot_b64}" class="sidebar-logo">', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🛠️ PANEL OPERATIVO")
    
    if st.button("💰 COTIZADOR", use_container_width=True, key="side_cot"): 
        st.session_state.seccion = "COTIZADOR"
    
    st.markdown("---")
    st.write("**🔒 ADMINISTRATIVO**")
    if st.button("📝 RADICACIÓN LEGAL", use_container_width=True, key="side_rad"): 
        st.session_state.seccion = "RADICACION"
    if st.button("🖥️ INVENTARIO PC", use_container_width=True, key="side_inv"): 
        st.session_state.seccion = "INVENTARIO"
    
    st.markdown("---")
    st.caption(f"Soluciones MyM | © {ahora.year}")

# --- 8. LÓGICA DE SECCIONES ---

# SECCIÓN COTIZADOR (ACTUALIZADA)
if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        extra = 20000 if mod == "A Domicilio" else 0
        total = base + extra
        st.metric("Inversión Total", f"$ {total:,.0f}".replace(",", "."))
    with col_info:
        st.markdown('<div style="background-color:rgba(255,255,255,0.8);padding:15px;border-radius:10px;border:2px solid #00d4ff;color:black;"><h4>📋 Tarifas</h4><li>Revisión: $40.000</li><li>Legal: 10% ahorro</li><li>Domicilio: $20.000</li></div>', unsafe_allow_html=True)

# SECCIÓN INVENTARIO
elif st.session_state.seccion == "INVENTARIO":
    st.subheader("🖥️ Inventario de Mantenimientos")
    # (Aquí va tu código de inventario previo...)

# SECCIÓN RADICACIÓN
elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Radicación Legal")
    # (Aquí va tu código de radicación previo...)
