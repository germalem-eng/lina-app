import streamlit as st
import os
import base64
import datetime
import urllib.parse
import pandas as pd
from fpdf import FPDF
from streamlit_autorefresh import st_autorefresh # <--- Necesitas esta para el reloj vivo

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.2 | Soluciones MyM", layout="wide", page_icon="🤖")

# REFRESCO AUTOMÁTICO (Cada 1 segundo para el reloj)
st_autorefresh(interval=1000, key="daterefresh")

ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. MEMORIA DE SESIÓN ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'texto_fijo' not in st.session_state: st.session_state.texto_fijo = ""
if 'inventario' not in st.session_state:
    st.session_state.inventario = [
        {"Fecha": "2026-03-15", "Equipo": "HP Compaq dc5800 SFF", "Trabajo": "Cambio de pasta térmica.", "Estado": "Entregado"}
    ]

# --- 3. RECURSOS VISUALES ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS (SIDEBAR TRANSPARENTE + DISEÑO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    [data-testid="stSidebar"] {{
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 25px;
    }}
    .sidebar-logo {{
        display: block; margin: auto; width: 180px; height: 180px; border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 15px #00FFFF; object-fit: cover;
    }}
    .social-tag {{
        padding: 4px 10px; border-radius: 10px; text-decoration: none !important; color: white !important; font-weight: bold; font-size: 11px; margin-left: 4px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO SUPERIOR (LINKS COMPLETOS + RELOJ VIVO) ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; color: #333; font-size: 16px;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | S T M Y M
    </div>
    <div style="display: flex; flex-wrap: wrap; justify-content: flex-end;">
        <a href="https://www.youtube.com/@gerardomartinezlemus7969" target="_blank" class="social-tag" style="background-color: #FF0000;">YouTube</a>
        <a href="https://www.tiktok.com/@solucionesmym" target="_blank" class="social-tag" style="background-color: #000000;">TikTok</a>
        <a href="https://www.instagram.com/solucionesmym_2007/" target="_blank" class="social-tag" style="background-color: #E1306C;">Instagram</a>
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="https://t.me/+573114759768" target="_blank" class="social-tag" style="background-color: #0088CC;">Telegram</a>
        <a href="https://x.com/" target="_blank" class="social-tag" style="background-color: #000000;">X</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. LOGO Y TEXTO PRINCIPAL DE L.I.N.A (RESTAURADO) ---
st.markdown(f"""
<div style="text-align: center;">
    <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final">
    <h1 class="neon-imponente" style="font-size: 80px; margin-bottom: 0px;">L.I.N.A.</h1>
    <h3 style="color: #00d4ff; font-family: 'Courier New', monospace; margin-top: -10px;">
        Lógica, Inteligencia y Nuevos Algoritmos
    </h3>
    <h4 style="color: #FFFFFF; font-weight: 300; letter-spacing: 2px;">
        Soluciones Tecnológicas M Y M
    </h4>
    <p style="color: #e0e0e0; font-style: italic;">Desde 2007</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 7. LÓGICA DE SECCIONES ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        extra = 20000 if mod == "A Domicilio" else 0
        st.metric("Inversión Total", f"$ {(base + extra):,.0f}".replace(",", "."))
    with col_info:
        st.markdown('<div style="background-color:rgba(255,255,255,0.8);padding:15px;border-radius:10px;border:2px solid #00d4ff;color:black;"><h4>📋 Tarifas</h4><li>Revisión: $40.000</li><li>Legal: 10% ahorro</li><li>Domicilio: $20.000</li></div>', unsafe_allow_html=True)

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Radicación Legal")
    st.write("Área administrativa en desarrollo.")

elif st.session_state.seccion == "INVENTARIO":
    st.subheader("🖥️ Inventario PC")
    st.write("Registro de mantenimientos.")
