import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V19.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
archivo_casos = "database_casos_mym.csv"

# --- 3. RECURSOS VISUALES (RUTAS DIRECTAS) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS (FONDO 50% Y DISEÑO AZUL) ---
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
    .social-tag {{
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
    .logo-redondo-final {{
        width: 280px; height: 280px;
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .contenedor-titulos-derecha {{
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; text-align: center; height: 100%;
    }}
    .titulo-lina-final {{
        font-family: 'Comic Sans MS', cursive; 
        font-size: 140px; color: #004d61; 
        text-shadow: 0 0 30px #00FFFF; margin: 0; line-height: 0.8;
    }}
    .sub-laboratorio {{
        color: #008fb3; font-size: 30px; font-weight: bold; line-height: 1.1; margin-top: 10px;
    }}
    .sub-mym {{
        color: #444; font-size: 20px; font-weight: 500; margin-top: 8px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (BARRA Y LOGOS) ---
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

with col_der:
    st.markdown(f"""
    <div class="contenedor-titulos-derecha">
        <h1 class="titulo-lina-final">L.I.N.A.</h1>
        <div class="sub-laboratorio">Laboratorio de Inteligencia<br>y Nuevos Algoritmos</div>
        <div class="sub-mym">Soluciones Tecnológicas MYM<br>Desde 2007</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("💰 COTIZADOR", use_container_width=True): st.session_state.seccion = "COTIZADOR"
with c2:
    if st.button("⚖️ GESTIÓN DE CASOS", use_container_width=True): st.session_state.seccion = "GESTION"
with c3:
    if st.button("📝 RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"
with c4:
    if st.button("🏠 PRIVADO MyM", use_container_width=True): st.session_state.seccion = "FINANZAS"

st.divider()

# --- 7. LÓGICA DE SECCIONES ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        dom = 20000 if mod == "A Domicilio" else 0
        total = (base * 1.20) + dom if "Mantenimiento" in ser else base + dom
        st.metric("Inversión Total", f"${total:,.0f} ")
    with col_info:
        st.markdown('<div style="background-color:rgba(248,249,250,0.7);padding:15px;border-radius:10px;border:2px solid #00d4ff;"><h4>📋 Tarifas</h4><li>Revisión: $40k</li><li>Legal: 10% ahorro</li><li>Domicilio: $20k</li></div>', unsafe_allow_html=True)

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Generador de Peticiones Legales")
    col_input, col_view = st.columns([1, 1])
    
    with col_input:
        u_nom = st.text_input("Nombre del Titular:", value="LINA PAOLA MOJICA").upper()
        u_ced = st.text_input("Cédula:")
        u_ent = st.text_input("Entidad:", value="RAPICREDIT").upper()
        
        # Lógica de generación de texto
        doc_legal = "" 
        if u_nom and u_ced and u_ent:
            doc_legal = f"""Bogotá D.C., {ahora.strftime('%d/%m/%Y')}
Señores: {u_ent}
E. S. D.

REF: SOLICITUD DE ACTUALIZACIÓN Y RECTIFICACIÓN (LEY 2157 DE 2021)

Yo, {u_nom}, identificado con C.C. No. {u_ced}, en ejercicio del derecho fundamental al Habeas Data, solicito la aplicación de los beneficios de la Ley de Borrón y Cuenta Nueva sobre mi historial crediticio..."""

    with col_view:
        st.text_area("📄 Vista Previa del Documento:", value=doc_legal, height=300)
        if st.button("💾 Guardar en Memoria"):
            st.session_state.doc_final = doc_legal
            st.success("Copiado al portapapeles de la sesión.")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Historial de Casos")
    if os.path.exists(archivo_casos):
        st.dataframe(pd.read_csv(archivo_casos), use_container_width=True)
    else:
        st.info("No hay casos registrados aún.")

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Privado")
    st.metric("Meta Sistecrédito", "$898.771")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: rgba(241, 241, 241, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota:</b> Honorarios por éxito (10% ahorro) o tarifas base según servicio.
</div>
""", unsafe_allow_html=True)

st.caption(f"LINA Core | © {ahora.year} Gerardo Martinez Lemus | Soluciones Tecnológicas M Y M")
