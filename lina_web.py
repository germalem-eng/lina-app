import streamlit as st
from datetime import datetime
import base64

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="L.I.N.A. - Soluciones Tecnológicas MYM", layout="wide")

# --- 2. LÓGICA DE ESTADO (SESIÓN) ---
if "seccion" not in st.session_state:
    st.session_state.seccion = "INICIO"

ahora = datetime.now()

# --- 3. CARGA DE IMÁGENES (Simulación de Base64 para fondo y logo) ---
# Nota: Aquí asumo que ya tienes tus funciones para cargar 'Logos/fondo.jpg' y 'Logos/robot.jpg'
# Si usas archivos locales, asegúrate de que existan en tu repo de GitHub.
def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

fondo_b64 = get_base64("Logos/fondo.jpg")
logo_robot_b64 = get_base64("Logos/robot.jpg")

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

    .resaltado-renglon {{
        background-color: rgba(173, 216, 230, 0.7);
        border-radius: 8px; padding: 5px 15px; margin: 5px 0;
        display: inline-block; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }}

    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #fff;
        text-shadow: 0 0 15px #7FFFD4, 0 0 30px #7FFFD4, 0 0 45px #7FFFD4;
        line-height: 1.1; margin-bottom: 10px; text-align: center;
    }}

    .social-tag {{
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (BARRA PLATEADA) ---
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

# --- SECCIÓN DE LOGO Y TÍTULOS ---
col_izq, col_der = st.columns([1.2, 2.3])

with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center; align-items:center; height:100%;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)

with col_der:
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

# --- 6. PANEL OPERATIVO (NAVEGACIÓN) ---
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

# --- 7. LÓGICA DE SECCIONES (SISTEMA INTEGRADO) ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador Técnico")
    base = 40000
    ser = st.selectbox("Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Consultoría"])
    mod = st.radio("Modalidad:", ["Virtual", "Domicilio"], horizontal=True)
    extra = 20000 if mod == "Domicilio" else 0
    total = base + extra
    st.metric("Inversión Estimada", f"$ {total:,.0f}".replace(",", "."))
    st.info("📍 Tarifa de Revisión: $40.000 | 🏠 Domicilio: $20.000")

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Radicación Legal (Ley 2485 de 2025)")
    with st.form("form_legal"):
        cliente = st.text_input("Nombre del Cliente:")
        operador = st.selectbox("Operador:", ["WOM", "Claro", "Movistar", "Tigo"])
        motivo = "Cobro ilegal de reconexión"
        if st.form_submit_button("Generar Documento"):
            st.success(f"Documento generado para {cliente} contra {operador}.")
            st.download_button("Descargar PDF (Simulado)", "Contenido del PDF", file_name="reclamacion.pdf")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Gestión de Casos Activos")
    st.write("No hay casos pendientes por procesar.")

elif st.session_state.seccion == "FINANZAS":
    st.subheader("🔒 Acceso Privado MyM")
    st.text_input("Contraseña de Administrador:", type="password")

# --- 8. PIE DE PÁGINA ---
st.markdown(f"""
<div style="background-color: rgba(241, 241, 241, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota Profesional:</b> Honorarios legales basados en el 10% del ahorro conseguido. 
    Revisiones técnicas base: <b>$40.000</b>.
</div>
""", unsafe_allow_html=True)
