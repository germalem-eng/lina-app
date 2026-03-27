import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V15.6 | MyM Soluciones", layout="wide", page_icon="🤖")

# Sincronización de Reloj (Colombia UTC-5)
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE VARIABLES (ESTO MATA EL ERROR ROJO PARA SIEMPRE) ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = "DASHBOARD"
if 'doc_final' not in st.session_state:
    # Inicializamos la variable que causaba el error como texto vacío
    st.session_state.doc_final = ""

# --- 3. RECURSOS VISUALES (RESTAURADOS) ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# Restauramos las rutas originales de tus logos
logo_robot_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 4. ESTILOS CSS MyM (RESTAURADOS Y MEJORADOS) ---
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
        border-bottom: 3px solid #666; border-radius: 8px; margin-bottom: 20px;
    }}
    .titulo-neon {{
        font-family: 'Comic Sans MS', cursive; font-size: clamp(30px, 5vw, 60px); 
        color: #000; text-shadow: 0 0 10px #7FFFD4; margin: 0;
    }}
    .subtitulo-mym {{
        color: #008fb3; font-size: 18px; font-weight: bold; font-family: 'Comic Sans MS', cursive;
    }}
    .social-bar {{
        display: flex; gap: 15px; align-items: center;
    }}
    .social-bar a {{
        text-decoration: none; font-size: 20px; transition: transform 0.2s;
    }}
    .social-bar a:hover {{
        transform: scale(1.1);
    }}
    .footer-mym {{
        background-color: #f1f1f1; padding: 20px; border-radius: 10px;
        border-left: 5px solid #008fb3; margin-top: 30px; font-size: 14px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO RESTAURADO (LOGO, RELOJ, TODAS LAS REDES) ---
# Barra superior (Reloj y Redes)
# Usamos emojis como placeholders de iconos para máxima compatibilidad móvil
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}
    </div>
    <div class="social-bar">
        <a href="https://youtube.com/@mymsoluciones" target="_blank" title="YouTube">🔴</a>
        <a href="https://instagram.com/mymsoluciones" target="_blank" title="Instagram">🟣</a>
        <a href="https://facebook.com/mymsolucionestech" target="_blank" title="Facebook">🔵</a>
        <a href="https://wa.me/573114759768" target="_blank" title="WhatsApp">🟢</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Bloque del Logo y Título
logo_img = f'<img src="data:image/jpeg;base64,{logo_robot_b64}" style="width: clamp(80px, 10vw, 120px); border-radius: 50%; border: 3px solid #00d4ff;">' if logo_robot_b64 else "🤖"

st.markdown(f"""
<div style="display: flex; align-items: center; gap: 20px; padding: 0 20px; margin-bottom: 20px;">
    {logo_img}
    <div>
        <h1 class="titulo-neon">L.I.N.A. V15.6</h1>
        <div class="subtitulo-mym">GESTIÓN PROFESIONAL MyM | DESDE 2007</div>
        <div style="font-size: 14px;">Laboratorio de Inteligencia y Nuevos Algoritmos</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. NAVEGACIÓN ( Multiplataforma) ---
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

# --- 7. CONTENIDO DINÁMICO ---
if st.session_state.seccion == "DASHBOARD":
    st.subheader("📊 Control de Metas y Vivienda")
    
    # Monitor de Respuesta (Silencio Administrativo)
    st.info("📅 **Monitor de Respuesta (Silencio Administrativo)**")
    fecha_radicacion = st.date_input("¿Qué día radicó esta petición?", value=ahora - timedelta(days=5))
    # Cálculo exacto de 21 días
    fecha_estimada = fecha_radicacion + timedelta(days=21)
    faltan_dias = (fecha_estimada - ahora.date()).days
    
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Faltan para término legal", f"{max(0, faltan_dias)} días")
    col_m2.metric("Fecha estimada respuesta", fecha_estimada.strftime('%d/%m/%Y'))
    
    st.markdown("---")
    st.write("### 🏠 Metas Vivienda")
    st.metric("Sistecrédito (Saldo)", "$898.771")

elif st.session_state.seccion == "LEGAL":
    st.subheader("📝 Radicación y Generación de Peticiones")
    
    with st.expander("🔍 Ver costos de gestión detallada", expanded=False):
        st.write("Si NO inicias proceso: **$40.000** (Consulta técnica/legal).")
        st.write("Si INICIAS proceso de defensa: **GRATIS**. Solo cobramos el 10% del ahorro conseguido.")

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
        if u_nom and u_ced and u_ent:
            # Construimos la carta
            st.session_state.doc_final = f"""Bogotá D.C., {ahora.strftime('%d/%m/%Y')}
Señores: {u_ent} | E. S. D.
REF: RECLAMACIÓN HABEAS DATA - LEY 1266 Y LEY 2157

Yo, {u_nom}, con C.C. {u_ced}, solicito la eliminación del reporte negativo.
...
Atentamente,
{u_nom} | C.C. {u_ced}"""
            st.success("Documento generado. Revisa la vista previa abajo.")
        else:
            st.warning("⚠️ Completa los datos básicos (Nombre, Cédula, Entidad).")

    # --- ESTA ES LA LÍNEA 284 QUE FALLABA ---
    # Usamos st.session_state.doc_final que ya está inicializada arriba
    st.text_area("📄 Vista Previa del Documento:", value=st.session_state.doc_final, height=250)
    
    if st.session_state.doc_final:
        st.download_button("📥 Descargar Petición TXT", data=st.session_state.doc_final, file_name=f"HabeasData_{u_nom}.txt")

# --- 8. PIE DE PÁGINA FIJO (TUS CONDICIONES) ---
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

st.caption(f"L.I.N.A. V15.6 | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
