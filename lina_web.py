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
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
archivo_casos = "database_casos_mym.csv"

# --- 3. RECURSOS VISUALES (RUTAS) ---
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
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 12px; margin-left: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (BARRA PLATEADA COMPLETA) ---
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; color: #333;">
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
# --- SECCIÓN DE LOGO Y TÍTULOS ---
col_izq, col_der = st.columns([1.2, 2.3])

with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_der:
    st.markdown(f"""
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%; margin-top: -20px;">
        <h1 class="neon-imponente" style="font-size: 110px;">L.I.N.A.</h1>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 4px; width: 100%;">
            <div class="resaltado-blanco">
                <span style="color: #008fb3; font-size: 26px; font-weight: bold;">Laboratorio de Inteligencia</span>
            </div>
            <div class="resaltado-blanco">
                <span style="color: #008fb3; font-size: 26px; font-weight: bold;">y Nuevos Algoritmos</span>
            </div>
            <div class="resaltado-blanco" style="margin-top: 8px;">
                <span style="color: #444; font-size: 18px; font-weight: bold;">Soluciones Tecnológicas M Y M</span>
            </div>
            <div class="resaltado-blanco">
                <span style="color: #444; font-size: 16px; font-weight: bold;">Desde 2007</span>
            </div>
        </div>
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
        extra = 20000 if mod == "A Domicilio" else 0
        total = base + extra
        st.metric("Inversión Total", f"$ {total:,.0f}".replace(",", "."))
    with col_info:
        st.markdown('<div style="background-color:rgba(255,255,255,0.8);padding:15px;border-radius:10px;border:2px solid #00d4ff;"><h4>📋 Tarifas</h4><li>Revisión: $40.000</li><li>Legal: 10% ahorro</li><li>Domicilio: $20.000</li></div>', unsafe_allow_html=True)

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Centro de Defensa Ciudadana (Radicación Legal)")
    
    # --- ENTRADA DE DATOS UNIVERSAL ---
    with st.expander("👤 CONFIGURAR DATOS DEL AFECTADO (Dejar vacío para usar datos de Lina)"):
        u_nombre = st.text_input("Nombre Completo:", placeholder="LINA PAOLA MOJICA").upper() or "LINA PAOLA MOJICA"
        u_cedula = st.text_input("Cédula de Ciudadanía:", placeholder="1016026492") or "1016026492"
        u_entidad = st.text_input("Entidad Acreedora / Casa Cobranza:", placeholder="RECOVERY OF CREDITS / RAPICREDIT") or "RECOVERY OF CREDITS / RAPICREDIT"

    # --- 1. SECCIÓN DATA CRÉDITO ---
    st.markdown("---")
    st.write("### ⚖️ Gestión DataCrédito")
    radicado_dc = st.text_input("Ingrese el número de radicado de DataCrédito:", placeholder="Ej: 2026-XXXXX")
    
    if radicado_dc:
        st.info(f"✅ Seguimiento activo para: {u_nombre} | Radicado: {radicado_dc}")
        fecha_res = (ahora + datetime.timedelta(days=15)).strftime('%d/%m/%Y')
        st.write(f"📅 **Respuesta esperada:** {fecha_res}")

    # --- 2. GENERADOR RECOVERY CREDITS ---
    st.markdown("---")
    st.write("### 📄 Reclamo por Incumplimiento de Oferta")
    if st.button("🔍 GENERAR BORRADOR TÉCNICO", use_container_width=True):
        texto_legal = f"""RECLAMACIÓN FORMAL - INCUMPLIMIENTO DE OFERTA COMERCIAL\nFecha: {ahora.strftime('%d/%m/%Y')}\n\nSeñores {u_entidad}:\n\n1. OFERTA VINCULANTE: El SMS recibido establecía un plazo y monto específico. El débito realizado por un valor superior es una violación al término de la oferta.\n2. ABUSO DEL DERECHO: El uso del débito automático para vaciar cuentas sin respetar el mínimo vital es ilegal (Sentencia T-012/17).\n3. ACCIÓN LEGAL: Se informa que el radicado ante la Superfinanciera está en curso.\n\nAtentamente,\n{u_nombre} | C.C. {u_cedula}"""
        
        st.text_area("Texto para PDF:", texto_legal, height=220)
        
        # Botón de WhatsApp
        mensaje_wa = f"Hola, comparto el borrador legal generado en L.I.N.A para el caso de {u_nombre}:\n\n{texto_legal}"
        url_wa = f"https://wa.me/?text={base64.urlsafe_b64encode(mensaje_wa.encode()).decode()}" # Versión simple para probar
        st.markdown(f'<a href="https://api.whatsapp.com/send?text={mensaje_wa}" target="_blank" style="background-color:#25D366; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; font-weight:bold; display:block; text-align:center;">📲 ENVIAR BORRADOR POR WHATSAPP</a>', unsafe_allow_html=True)

    # --- 3. SECCIÓN BANCOLOMBIA ---
    st.markdown("---")
    st.write("### 🏦 Reversión Bancolombia")
    monto_banc = st.text_input("Monto a reclamar:", value="$502.837")
    if st.button("🏦 GENERAR TEXTO BANCOLOMBIA", use_container_width=True):
        texto_ban = f"SOLICITUD DE REVERSIÓN - CUENTA DE NÓMINA\nCliente: {u_nombre}\nEntidad: BANCOLOMBIA\nMonto: {monto_banc}\nCausal: Violación al Mínimo Vital y Oferta Incumplida.\nDerecho: Circular 007 Superfinanciera."
        st.code(texto_ban)
        st.markdown(f'<a href="https://api.whatsapp.com/send?text={texto_ban}" target="_blank" style="background-color:#25D366; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; font-weight:bold; display:block; text-align:center;">📲 ENVIAR RECLAMO BANCO A LINA</a>', unsafe_allow_html=True)
elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Historial de Casos")
    st.info("No hay casos registrados aún.")

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🏠 Control Privado")
    st.metric("Meta Sistecrédito", "$898.771")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota:</b> Honorarios por éxito (10% ahorro) o tarifas base de <b>$40.000</b>.
</div>
<p style="text-align:center; color:#666;">LINA Core V20.0 | © {ahora.year} Gerardo Martinez Lemus</p>
""", unsafe_allow_html=True)
