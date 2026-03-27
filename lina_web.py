import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN Y RELOJ ---
st.set_page_config(page_title="LINA V15.5 | MyM Soluciones", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE VARIABLES (PARA EVITAR EL ERROR ROJO) ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = "DASHBOARD"
if 'doc_final' not in st.session_state:
    st.session_state.doc_final = ""

# --- 3. RECURSOS VISUALES ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 4. ESTILOS CSS (L.I.N.A. & MyM) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 8px;
    }}
    .titulo-neon {{
        font-family: 'Comic Sans MS', cursive; font-size: clamp(30px, 5vw, 60px); 
        color: #000; text-shadow: 0 0 10px #7FFFD4; margin-bottom: 0;
    }}
    .footer-mym {{
        background-color: #f1f1f1; padding: 20px; border-radius: 10px;
        border-left: 5px solid #008fb3; margin-top: 30px; font-size: 14px;
    }}
    .social-links a {{
        margin-left: 15px; text-decoration: none; font-weight: bold; color: #004d61;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO CON REDES SOCIALES ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}
    </div>
    <div class="social-links">
        <a href="https://wa.me/573114759768" target="_blank">🟢 WhatsApp</a>
        <a href="https://facebook.com" target="_blank">🔵 Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-neon">L.I.N.A. V15.5</h1>', unsafe_allow_html=True)
st.markdown("**Laboratorio de Inteligencia y Nuevos Algoritmos** | *SOLUCIONES TECNOLÓGICAS MyM*")

# --- 6. NAVEGACIÓN ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("📊 DASHBOARD", use_container_width=True): st.session_state.seccion = "DASHBOARD"
with c2: 
    if st.button("⚖️ LEGAL", use_container_width=True): st.session_state.seccion = "LEGAL"
with c3: 
    if st.button("🔧 TÉCNICO", use_container_width=True): st.session_state.seccion = "TECNICO"
with c4: 
    if st.button("💰 EXTRAS", use_container_width=True): st.session_state.seccion = "EXTRAS"

st.divider()

# --- 7. CONTENIDO ---
if st.session_state.seccion == "DASHBOARD":
    st.subheader("📊 Control de Metas y Vivienda")
    # Monitor de Respuesta
    st.info("📅 **Monitor de Respuesta (Silencio Administrativo)**")
    fecha_radicacion = st.date_input("¿Qué día radicó esta petición?", value=ahora - timedelta(days=5))
    fecha_estimada = fecha_radicacion + timedelta(days=21)
    faltan_dias = (fecha_estimada - ahora.date()).days
    
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Faltan para término legal", f"{faltan_dias} días")
    col_m2.metric("Fecha estimada respuesta", fecha_estimada.strftime('%d/%m/%Y'))

elif st.session_state.seccion == "LEGAL":
    st.subheader("📝 Radicación y Generación de Peticiones")
    
    with st.expander("🔍 Ver costos de gestión detallada", expanded=False):
        st.write("Si NO inicias proceso: $40.000 (Consulta).")
        st.write("Si INICIAS proceso: **GRATIS**. Solo cobramos el 10% del ahorro conseguido.")

    col_l1, col_l2 = st.columns(2)
    with col_l1:
        u_nom = st.text_input("Nombre Completo:")
        u_ced = st.text_input("Cédula:")
        u_tel = st.text_input("Teléfono:")
    with col_l2:
        u_ent = st.text_input("Casa de Cobranza / Entidad:")
        u_cor = st.text_input("Correo Electrónico:")
        u_dir = st.text_input("Dirección de Residencia (Bogotá):")

    st.file_uploader("📂 Adjuntar Foto de Cédula (Opcional)", type=['jpg', 'png', 'pdf', 'jpeg'])

    if st.button("🔨 GENERAR DOCUMENTO DE DEFENSA"):
        st.session_state.doc_final = f"DOCUMENTO DE RECLAMACIÓN\nTitular: {u_nom}\nCC: {u_ced}\nEntidad: {u_ent}\n..."
        st.success("Documento generado. Revisa la vista previa abajo.")

    st.text_area("📄 Vista Previa:", value=st.session_state.doc_final, height=200)

# --- 8. PIE DE PÁGINA (TUS CONDICIONES) ---
st.markdown(f"""
<div class="footer-mym">
    <h3>⚠️ Nota: Sus honorarios se basan en el éxito del ahorro conseguido.</h3>
    <p><b>📈 VALOR DEL SERVICIO:</b> 10% del valor total ahorrado.</p>
    <p><b>📑 CONDICIÓN:</b> Solo se cobra si el proceso es exitoso.</p>
    <hr>
    <p>Si prefieres no iniciar proceso de defensa, el diagnóstico técnico/legal tiene un costo de <b>$40.000</b>.</p>
    <p style="font-size: 11px; color: #666;">💡 Al descargar o usar este documento, aceptas que MyM Soluciones gestione tu caso bajo estas condiciones.</p>
</div>
""", unsafe_allow_html=True)

st.caption(f"L.I.N.A. V15.5 | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
