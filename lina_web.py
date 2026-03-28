import streamlit as st
import os
import base64
import datetime
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")

# Ajuste de hora Colombia (UTC-5)
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "COTIZADOR"

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
        width: 250px; height: 250px;
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .resaltado-blanco {{
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 8px; padding: 5px 15px; margin: 3px 0;
        display: inline-block; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 0.85; margin: 0; text-align: center;
    }}
    .social-tag {{
        padding: 5px 10px; border-radius: 10px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 11px; margin-left: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; color: #333;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | S T M Y M
    </div>
    <div style="display: flex; flex-wrap: wrap; justify-content: flex-end;">
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
        <a href="https://www.youtube.com/@gerardomartinezlemus7969" target="_blank" class="social-tag" style="background-color: #FF0000;">YouTube</a>
    </div>
</div>
""", unsafe_allow_html=True)

col_izq, col_der = st.columns([1, 2])
with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_der:
    st.markdown(f"""
    <div style="text-align: center; margin-top: -10px;">
        <h1 class="neon-imponente" style="font-size: 90px;">L.I.N.A.</h1>
        <div class="resaltado-blanco"><span style="color: #008fb3; font-size: 22px; font-weight: bold;">Laboratorio de Inteligencia y Nuevos Algoritmos</span></div><br>
        <div class="resaltado-blanco"><span style="color: #444; font-size: 16px; font-weight: bold;">Soluciones Tecnológicas M Y M - Desde 2007</span></div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO (BOTONES FUNCIONALES) ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("💰 COTIZADOR", use_container_width=True):
        st.session_state.seccion = "COTIZADOR"
        st.rerun()
with c2:
    if st.button("⚖️ GESTIÓN", use_container_width=True):
        st.session_state.seccion = "GESTION"
        st.rerun()
with c3:
    if st.button("📝 RADICACIÓN", use_container_width=True):
        st.session_state.seccion = "RADICACION"
        st.rerun()
with c4:
    if st.button("🏠 PRIVADO MyM", use_container_width=True):
        st.session_state.seccion = "FINANZAS"
        st.rerun()
with c5:
    if st.button("🛡️ CASO LEGAL", use_container_width=True):
        st.session_state.seccion = "LEGAL"
        st.rerun()

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
        st.info("Tarifa base: $40.000\nDomicilio: +$20.000")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Historial de Casos")
    st.info("Buscando base de datos 'database_casos_mym.csv'...")
    st.warning("No hay casos registrados actualmente.")

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Generador de Peticiones Legales")
    u_nom = st.text_input("Nombre del Titular:", value="LINA PAOLA MOJICA").upper()
    u_ced = st.text_input("Cédula:")
    if st.button("Generar Borrador"):
        doc = f"Bogotá D.C., {ahora.strftime('%d/%m/%Y')}\n\nYo, {u_nom}, con C.C. {u_ced}..."
        st.text_area("📄 Documento:", value=doc, height=150)

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Privado MyM")
    st.metric("Meta Sistecrédito", "$898.771")
    st.progress(0.4, text="Progreso de Pago")

elif st.session_state.seccion == "LEGAL":
    st.subheader("🛡️ Caso Nómina: Lina vs RapiCredit")
    cap, deb = 200000, 502837
    dif = deb - cap
    
    col1, col2 = st.columns(2)
    col1.metric("Capital Solicitado", "$ 200.000")
    col2.error(f"Excedente Cobrado: $ {dif:,.0f}".replace(",", "."))
    
    if st.button("📝 Generar Argumentos para Radicado"):
        doc = f"""HECHOS PARA LA SUPERINTENDENCIA:
1. Oferta vinculante por SMS el 27/03 por $200.000.
2. Débito automático por $502.837 realizado el mismo día.
3. Factura No. RCC6205119 emitida el 28/03/2026.
4. Afectación de cuenta de nómina de LINA MOJICA CC 1016026492."""
        st.text_area("Copia este resumen:", value=doc, height=180)

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 30px;">
    <b>⚠️ MyM Nota:</b> Honorarios por éxito (10% ahorro) o tarifas base de <b>$40.000</b>.
</div>
<p style="text-align:center; color:#666; font-size: 12px; margin-top: 10px;">LINA Core V20.0 | © {ahora.year} Gerardo Martinez Lemus</p>
""", unsafe_allow_html=True)
