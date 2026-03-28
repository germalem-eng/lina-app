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

# --- 4. ESTILOS CSS (REVERTIDO: SIN RECUADRO) ---
st.markdown(f"""
<style>
    /* FONDO CON TRANSPARENCIA DEL 50% */
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

# --- 5. ENCABEZADO VISUAL COMPLETO (BARRA, LOGO Y TÍTULOS) ---

# 1. Barra Plateada Superior con Redes Sociales
st.markdown(f"""
<style>
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 25px;
    }}
    .social-tag {{
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
</style>

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

# 2. Distribución en Dos Columnas (Logo e Información)
col_izq, col_der = st.columns([1.2, 2.3])

with col_izq:
    # Logo gigante a la izquierda con neón azul
    st.markdown(f'<div style="display:flex; justify-content:center; align-items:center; height:100%;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_der:
    st.markdown(f"""
<style>
    .resaltado-renglon {{
        background-color: rgba(173, 216, 230, 0.7);
        border-radius: 8px;
        padding: 5px 15px;
        margin: 5px 0;
        display: inline-block;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive;
        color: #fff;
        text-shadow: 0 0 10px #7FFFD4, 0 0 20px #7FFFD4, 0 0 40px #7FFFD4, 0 0 80px #7FFFD4;
        line-height: 1.2;
        margin-bottom: 10px;
        text-align: center;
    }}
</style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center;">
        <h1 class="neon-imponente" style="font-size: 110px;">L.I.N.A.</h1>
        <div class="resaltado-renglon">
            <span style="color: #000; font-size: 28px; font-weight: bold;">Laboratorio de Inteligencia</span>
        </div><br>
        <div class="resaltado-renglon">
            <span style="color: #000; font-size: 28px; font-weight: bold;">y Nuevos Algoritmos</span>
        </div><br>
        <div class="resaltado-renglon" style="margin-top: 15px;">
            <span style="color: #444; font-size: 18px; font-weight: bold;">Soluciones Tecnológicas MYM</span>
        </div><br>
        <div class="resaltado-renglon">
            <span style="color: #444; font-size: 16px; font-weight: bold;">Desde 2007</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
            /* Efecto NEÓN POTENTE E IMPONENTE para L.I.N.A. */
            .neon-imponente {{
                font-family: 'Comic Sans MS', cursive; 
                font-weight: bold;
                color: #fff; 
                text-transform: uppercase;
                text-shadow: 0 0 10px #7FFFD4, 0 0 20px #7FFFD4, 0 0 30px #7FFFD4, 0 0 40px #7FFFD4, 0 0 70px #7FFFD4, 0 0 80px #7FFFD4, 0 0 100px #7FFFD4, 0 0 150px #7FFFD4;
                letter-spacing: 5px; 
                margin-bottom: 20px;
                line-height: 1;
                display: inline-block;
            }}
            
            /* Ajuste de contenedor para centrado */
            .contenedor-titulos-derecha-v2 {{
                text-align: center;
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
        </style>
        """, unsafe_allow_html=True)

        # 2. Generamos el contenido escalonado con recuadros claros
        st.markdown(f"""
        <div class="contenedor-titulos-derecha-v2">
            <h1 class="neon-imponente" style="font-size: 130px;">L.I.N.A.</h1>
            
            <div class="resaltado-renglon" style="color: #000; font-size: 30px; font-weight: bold;">Laboratorio de Inteligencia</div>
            <div class="resaltado-renglon" style="color: #000; font-size: 30px; font-weight: bold;">y Nuevos Algoritmos</div>
            
            <div class="resaltado-renglon" style="color: #444; font-size: 18px; margin-top: 15px;">Soluciones Tecnológicas M Y M</div>
            <div class="resaltado-renglon" style="color: #444; font-size: 16px;">Desde 2007</div>
        </div>
        """, unsafe_allow_html=True)
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

# --- 7. LÓGICA DE SECCIONES (ACTUALIZADO CON FORMATO COLOMBIANO) ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Inteligente")
    col_calc, col_info = st.columns([2, 1])
    with col_calc:
        ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal"])
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        base = 40000
        dom = 20000 if mod == "A Domicilio" else 0
        total = (base * 1.20) + dom if "Mantenimiento" in ser else base + dom
        # Formato de moneda colombiana con separador de miles
        st.metric("Inversión Total", f"$ {total:,.0f}".replace(",", "."))
        
    with col_info:
        # Aquí eliminamos la 'k' y pusimos el formato correcto
        st.markdown("""
        <div style="background-color:rgba(248,249,250,0.7);padding:15px;border-radius:10px;border:2px solid #00d4ff;">
            <h4 style="text-align:center;">📋 Tarifas Oficiales</h4>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>📍 <b>Revisión:</b> $40.000</li>
                <li>⚖️ <b>Legal:</b> 10% del ahorro</li>
                <li>🏠 <b>Domicilio:</b> $20.000</li>
            </ul>
            <small>* La revisión es gratis si se realiza el servicio.</small>
        </div>
        """, unsafe_allow_html=True)

# --- (Las secciones de RADICACION, GESTION y FINANZAS se mantienen igual) ---

# --- 8. PIE DE PÁGINA (EJECUTIVO) ---
st.markdown(f"""
<div style="background-color: rgba(241, 241, 241, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota de Honorarios:</b> Nuestros honorarios se basan en el éxito conseguido (10% del ahorro legal) 
    o tarifas base de <b>$40.000</b> por revisión técnica.
</div>
""", unsafe_allow_html=True)

st.caption(f"LINA Core | © {ahora.year} Gerardo Martinez Lemus | Soluciones Tecnológicas M Y M")
