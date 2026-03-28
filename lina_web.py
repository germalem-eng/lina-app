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

# ==========================================
# ⚖️ SECCIÓN: RADICACIÓN (Defensa Ciudadana)
# ==========================================
elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Centro de Defensa Ciudadana")

    # 1. Creamos una "Caja de Memoria" para que el texto NO desaparezca
    if 'texto_fijo' not in st.session_state:
        st.session_state.texto_fijo = ""

    # (Mantenemos tu bloque de Configurar Datos)
    with st.expander("👤 CONFIGURAR DATOS DEL AFECTADO (Opcional)"):
        u_nombre = st.text_input("Nombre Completo:", value="LINA PAOLA MOJICA").upper()
        u_cedula = st.text_input("Cédula de Ciudadanía:", value="1016026492")
        u_casa_cob = st.text_input("Casa de Cobranza:", placeholder="RECOVERY OF CREDITS")

    st.markdown("---")
    
    # Entradas universales para banco y monto
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        u_banco_any = st.text_input("Nombre del Banco:", placeholder="Ej: BANCOLOMBIA")
    with col_b2:
        u_monto_any = st.text_input("Monto en disputa:", value="$502.837")

    # Botones de generación de documentos
    c_btn1, c_btn2 = st.columns(2)
    
    with c_btn1:
        # AGREGAMOS 'key' ÚNICA PARA EVITAR EL ERROR DE DUPLICADO
        if st.button("🔍 GENERAR RECLAMO COBRANZA", key="btn_reclamo_cob"):
            st.session_state.texto_fijo = f"RECLAMACIÓN FORMAL - INCUMPLIMIENTO DE OFERTA COMERCIAL\nFecha: {ahora.strftime('%d/%m/%Y')}\n\nSeñores {u_casa_cob if u_casa_cob else '[CASA DE COBRANZA]'}:\n\n1. OFERTA VINCULANTE: Violación al monto de la oferta comercial.\n2. ABUSO DEL DERECHO: Débito ilegal sobre mínimo vital (Sentencia T-012/17).\n\nAtentamente,\n{u_nombre} | C.C. {u_cedula}"

    with c_btn2:
        # AGREGAMOS 'key' ÚNICA PARA EVITAR EL ERROR DE DUPLICADO
        if st.button("🏦 GENERAR RECLAMO BANCARIO", key="btn_reclamo_ban"):
            if u_banco_any:
                st.session_state.texto_fijo = f"SOLICITUD DE REVERSIÓN - CUENTA DE NÓMINA\nFecha: {ahora.strftime('%d/%m/%Y')}\n\nCliente: {u_nombre}\nEntidad: {u_banco_any.upper()}\nMonto: {u_monto_any}\nDerecho: Circular 007 de la Superfinanciera y Sentencia T-012/17."
            else:
                st.error("⚠️ Por favor, ingresa el nombre del banco primero.")

    # 2. Espacio de Visualización Permanente
    if st.session_state.texto_fijo:
        st.markdown("#### 📄 Documento Generado (Cópialo):")
        # st.code mantiene el texto fijo y con un botón de copiar rápido
        st.code(st.session_state.texto_fijo, language="text")
        
        # Botón de WhatsApp
        import urllib.parse
        msg_wa = urllib.parse.quote(st.session_state.texto_fijo)
        st.markdown(f'<a href="https://api.whatsapp.com/send?text={msg_wa}" target="_blank" style="background-color:#25D366; color:white; padding:12px; text-decoration:none; border-radius:8px; font-weight:bold; display:block; text-align:center;">📲 ENVIAR ESTE DOCUMENTO POR WHATSAPP</a>', unsafe_allow_html=True)

    # Botón de limpiar que SÍ funciona (usando key única)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("♻️ LIMPIAR FORMULARIO", use_container_width=True, key="btn_limpiar_rad"):
        st.session_state.texto_fijo = ""
        st.rerun()
# --- SECCIÓN GESTIÓN (CORREGIDA LA SANGRÍA) ---
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
