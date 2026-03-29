import streamlit as st
import os
import base64
import datetime
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")

# Ajuste de hora Bogotá (UTC-5)
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

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

# --- 4. ESTILOS CSS MAESTROS ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover;
        background-attachment: fixed;
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
    .barra-metalica {{
        background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border: 2px solid #666; border-radius: 15px;
        padding: 20px; margin-top: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .reloj-bogota {{
        font-family: 'Courier New', monospace; font-weight: bold; color: #111;
        font-size: 16px; border-bottom: 2px solid #888;
        margin-bottom: 15px; padding-bottom: 10px;
        display: flex; justify-content: space-between;
    }}
    .boton-social {{
        text-decoration: none !important; color: #333 !important;
        background: white; padding: 8px 15px; border-radius: 10px;
        font-weight: bold; font-size: 13px; transition: 0.3s ease;
        border: 1px solid #999; display: inline-block;
    }}
    .boton-social:hover {{
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,255,255,0.5);
        border-color: #00FFFF;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO: L.I.N.A. Y PLACAS ---
col_h1, col_h2 = st.columns([1, 2.2])

with col_h1:
    st.markdown(f'''
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final">
        </div>
    ''', unsafe_allow_html=True)

with col_h2:
    html_header = f"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 250px; text-align: center;">
        <h1 class="neon-imponente" style="font-size: 85px; margin: 0; padding: 0;">L.I.N.A.</h1>
        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 15px; width: 100%; align-items: center;">
            <div style="background: rgba(255, 255, 255, 0.95); padding: 10px 20px; border-radius: 12px; border: 2px solid #00FFFF; width: fit-content;">
                <span style="color: #008fb3; font-size: 20px; font-weight: bold; display: block; white-space: nowrap;">
                    Laboratorio de Inteligencia y Nuevos Algoritmos
                </span>
            </div>
            <div style="background: rgba(255, 255, 255, 0.95); padding: 10px 20px; border-radius: 12px; border: 2px solid #00FFFF; width: fit-content;">
                <span style="color: #444; font-size: 16px; font-weight: bold; display: block; white-space: nowrap;">
                    Soluciones Tecnológicas M Y M - Desde 2007
                </span>
            </div>
        </div>
    </div>
    """
    st.markdown(html_header, unsafe_allow_html=True)

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
    if st.button("📝 RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"; st.rerun()
with c5:
    if st.button("🛡️ CASO LEGAL", use_container_width=True): st.session_state.seccion = "LEGAL"; st.rerun()
with c6:
    if st.button("🏠 PRIVADO", use_container_width=True): st.session_state.seccion = "PRIVADO"; st.rerun()

st.divider()

# --- 7. LÓGICA DE SECCIONES (MANTENIMIENTO PREVENTIVO) ---
if st.session_state.seccion == "PREVENTIVO":
    st.subheader("🛠️ Mantenimiento Preventivo Especializado")
    col_izq, col_der = st.columns([2, 1])
    
    with col_izq:
        tipo_e = st.selectbox("Tipo de Producto:", ["PC de Mesa", "Todo en Uno", "Portátil", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca del Producto:")
        st.markdown("#### 📋 Checklist de Verificación")
        c1 = st.checkbox("¿Enciende?")
        c2 = st.checkbox("¿Limpieza física realizada?")
        diag = st.text_area("Descripción del Servicio:")

    with col_der:
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        tipo_at = st.radio("Tipo de Atención:", ["Solo Consulta", "Servicio Completo"], index=1)
        base = 40000
        extra = 20000 if mod == "A Domicilio" else 0
        total = base + extra if tipo_at == "Solo Consulta" else (base + extra if mod == "A Domicilio" else base)
        
        st.markdown(f"""
        <div style="background:white; padding:20px; border-radius:15px; border:3px solid #00FFFF; text-align:center;">
            <h3>Inversión Total</h3>
            <h1 style="color:#008fb3;">$ {total:,.0f}</h1>
            <p><b>ING. Gerardo Martinez Lemus</b></p>
        </div>
        """, unsafe_allow_html=True)

# --- 8. BARRA PLATEADA FINAL CON RELOJ BOGOTÁ Y REDES ---
html_barra_final = f"""
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
st.markdown(html_barra_final, unsafe_allow_html=True)

# Pie de Página
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota:</b> Honorarios por éxito (10% ahorro) o tarifas base de <b>$40.000</b>.
</div>
<p style="text-align:center; color:#666;">LINA Core V20.0 | © {ahora.year} Gerardo Martinez Lemus</p>
""", unsafe_allow_html=True)
