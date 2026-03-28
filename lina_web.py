import streamlit as st
import os
import base64
import datetime
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
# Ajuste de hora (Colombia UTC-5)
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
archivo_casos = "database_casos_mym.csv"

# --- 3. RECURSOS VISUALES ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS GENERALES ---
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
        width: 280px; height: 280px;
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}

    /* RECUADROS BLANCOS SOLICITADOS */
    .resaltado-blanco {{
        background-color: rgba(255, 255, 255, 0.8); /* Blanco puro con ligera transparencia */
        border-radius: 8px; padding: 5px 15px; margin: 5px 0;
        display: inline-block; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }}

    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #fff;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF, 0 0 45px #00FFFF;
        line-height: 1.1; margin-bottom: 15px; text-align: center;
    }}

    .social-tag {{
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (BARRA PLATEADA Y LOGOS) ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; color: #333;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | S T M Y M
    </div>
    <div>
        <a href="https://www.youtube.com/@gerardomartinezlemus7969" target="_blank" class="social-tag" style="background-color: #FF0000;">YouTube</a>
        <a href="https://www.instagram.com/solucionesmym_2007/" target="_blank" class="social-tag" style="background-color: #E1306C;">Instagram</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="https://t.me/+573114759768" target="_blank" class="social-tag" style="background-color: #0088CC;">Telegram</a>
        <a href="https://x.com/" target="_blank" class="social-tag" style="background-color: #000000;">X</a>
    </div>
</div>
""", unsafe_allow_html=True)

col_izq, col_der = st.columns([1.2, 2.3])

with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center; align-items:center; height:100%;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: -30px; width: 100%;">
        <h1 class="neon-imponente" style="font-size: 110px; margin: 0; padding: 0; line-height: 0.85;">L.I.N.A.</h1>
        
        <div style="display: flex; flex-direction: column; align-items: center; gap: 5px; width: 100%;">
            <div class="resaltado-blanco">
                <span style="color: #008fb3; font-size: 26px; font-weight: bold;">Laboratorio de Inteligencia</span>
            </div>
            <div class="resaltado-blanco">
                <span style="color: #008fb3; font-size: 26px; font-weight: bold;">y Nuevos Algoritmos</span>
            </div>
            
            <div class="resaltado-blanco" style="margin-top: 10px;">
                <span style="color: #444; font-size: 18px; font-weight: bold;">Soluciones Tecnológicas M Y M</span>
            </div>
            <div class="resaltado-blanco">
                <span style="color: #444; font-size: 16px; font-weight: bold;">Desde 2007</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)    
# --- 7. LÓGICA DE SECCIONES (ACTUALIZADO) ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        dom = 20000 if mod == "A Domicilio" else 0
        total = (base * 1.20) + dom if "Mantenimiento" in ser else base + dom
        st.metric("Inversión Total", f"$ {total:,.0f}".replace(",", "."))
    with col_info:
        st.markdown("""
        <div style="background-color:rgba(255,255,255,0.8);padding:15px;border-radius:10px;border:2px solid #00d4ff;">
            <h4 style="text-align:center;">📋 Tarifas Oficiales</h4>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>📍 <b>Revisión:</b> $40.000</li>
                <li>⚖️ <b>Legal:</b> 10% del ahorro</li>
                <li>🏠 <b>Domicilio:</b> $20.000</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Generador de Peticiones Legales")
    col_input, col_view = st.columns([1, 1])
    with col_input:
        u_nom = st.text_input("Nombre del Titular:", value="LINA PAOLA MOJICA").upper()
        u_ced = st.text_input("Cédula:")
        u_ent = st.text_input("Entidad:", value="RAPICREDIT").upper()
        doc_legal = f"""Bogotá D.C., {ahora.strftime('%d/%m/%Y')}\nSeñores: {u_ent}\nREF: LEY 2157 DE 2021\n\nYo, {u_nom}, con C.C. {u_ced}..."""
    with col_view:
        st.text_area("📄 Vista Previa:", value=doc_legal, height=250)
        if st.button("💾 Guardar"): st.success("Documento listo.")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Historial de Casos")
    if os.path.exists(archivo_casos):
        st.dataframe(pd.read_csv(archivo_casos), use_container_width=True)
    else: st.info("No hay casos registrados aún.")

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Privado")
    st.metric("Meta Sistecrédito", "$898.771")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota Profesional:</b> Honorarios por éxito (10% ahorro) o tarifa base revisión: <b>$40.000</b>.
</div>
""", unsafe_allow_html=True)

st.caption(f"LINA Core V20.0 | © {ahora.year} Gerardo Martinez Lemus | Soluciones Tecnológicas M Y M")
