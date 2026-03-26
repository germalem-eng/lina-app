import streamlit as st
import os
import base64
import datetime

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V15.4 | Gestión MyM", layout="wide")

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Recursos Visuales (Ruta: Logos/)
logo_original_b64 = get_base64("Logos/Logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 2. ESTILOS CSS (NEÓN, BOTONES Y REDES) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)),
                          url("data:image/jpeg;base64,{fondo_b64 if fondo_b64 else ''}") !important;
        background-size: cover !important;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 40px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%) !important;
        border-bottom: 3px solid #666; margin-bottom: 20px;
    }}
    .social-links a {{
        color: #1a1a1a !important; text-decoration: none; font-weight: bold;
        font-family: sans-serif; font-size: 11px; padding: 5px 10px;
        border: 1px solid #999; border-radius: 4px; background: white; margin-left: 5px;
    }}
    .titulo-neon {{
        font-family: 'Comic Sans MS', cursive !important;
        font-size: 85px !important; color: #000 !important;
        text-shadow: 0 0 10px #7FFFD4, 0 0 20px #7FFFD4, 0 0 30px #00d4ff !important;
        margin: 0; line-height: 1;
    }}
    .subtitulo-mym {{
        color: #008fb3 !important; font-size: 22px !important;
        font-weight: bold; font-family: 'Comic Sans MS', cursive !important;
        border-top: 2px solid #00d4ff; display: inline-block; padding-top: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 3. BARRA SUPERIOR E IDENTIDAD ---
ahora = datetime.datetime.now()
st.html(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}</div>
    <div class="social-links">
        <a href="https://www.facebook.com/share/18U3tNcSUK/" target="_blank">FACEBOOK</a>
        <a href="https://wa.me/573114759768" target="_blank">WHATSAPP</a>
        <a href="#">X</a> <a href="#">INSTAGRAM</a> <a href="#">TIKTOK</a> <a href="#">YOUTUBE</a> <a href="#">TELEGRAM</a>
    </div>
</div>
""")

logo_img = f'<img src="data:image/jpeg;base64,{logo_original_b64}" style="width: 150px; border-radius: 50%; border: 4px solid #00d4ff;">' if logo_original_b64 else "🤖"
st.html(f"""
<div style="display: flex; align-items: center; gap: 40px; padding: 20px 60px;">
    {logo_img}
    <div>
        <h1 class="titulo-neon">L.I.N.A. V15.4</h1>
        <p style="font-family: 'Comic Sans MS'; font-weight: bold; font-size: 18px; color: #333; margin: 0;">LABORATORIO DE INTELIGENCIA Y NUEVOS ALGORITMOS</p>
        <div class="subtitulo-mym">🛠️ SOLUCIONES TECNOLÓGICAS M & M | DESDE 2007</div>
    </div>
</div>
""")

# ... (Mantén tus secciones 1, 2 y 3 exactamente igual)

# --- 4. LÓGICA DE NAVEGACIÓN ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = "INICIO"

st.write("### 🚀 Panel Operativo Principal:")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("⚖️ HABEAS DATA", use_container_width=True):
        st.session_state.seccion = "LEGAL"
with c2:
    if st.button("🔧 SOPORTE TÉCNICO", use_container_width=True):
        st.session_state.seccion = "TECNICO"
with c3:
    if st.button("💰 COTIZADOR MyM", use_container_width=True):
        st.session_state.seccion = "COTIZADOR"
with c4:
    if st.button("📅 AGENDAR CITA", use_container_width=True):
        st.session_state.seccion = "CITAS"

st.divider()

# --- 5. DESPLIEGUE DE CONTENIDO ---

if st.session_state.seccion == "LEGAL":
    st.subheader("⚖️ Gestión de Habeas Data & Reclamaciones")
    
    # NUEVO: Evaluador de Viabilidad
    st.info("🔍 **Evaluador de Viabilidad Legal**")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        tiempo_mora = st.number_input("Años de mora o reporte:", min_value=0, max_value=20, step=1)
    with col_l2:
        ya_pago = st.checkbox("¿La deuda ya fue pagada?")
    
    if tiempo_mora >= 8:
        st.success("✅ **DIAGNÓSTICO:** Viable por CADUCIDAD (Ley 2157). El reporte debe ser borrado.")
    elif ya_pago:
        st.success("✅ **DIAGNÓSTICO:** Viable por PAGO. Se solicita actualización inmediata.")
    else:
        st.warning("⚠️ Requiere análisis detallado de la historia crediticia.")

    st.divider()
    u_nom = st.text_input("Nombre Completo:").upper()
    u_ent = st.text_input("Entidad a Reclamar:").upper()
    if u_nom and u_ent:
        doc = f"Bogotá, {ahora.strftime('%d/%m/%Y')}\n\nSeñores {u_ent}:\n\nYo, {u_nom}, en ejercicio del derecho de Habeas Data..."
        st.text_area("Borrador de Documento:", value=doc, height=150)
        st.download_button("📥 Descargar Petición", doc, file_name=f"Peticion_{u_nom}.txt")

elif st.session_state.seccion == "TECNICO":
    st.subheader("🔧 Mantenimiento Preventivo y Correctivo")
    st.write("Especialistas en Computadores y Electrodomésticos.")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        tipo_equipo = st.selectbox("Tipo de Equipo:", ["Computador PC/Portátil", "Nevera / Refrigeración", "Lavadora", "Otro Electrodoméstico"])
        serial = st.text_input("Serial o Modelo:")
    with col_t2:
        falla = st.text_area("Descripción de la Falla:")
    st.button("Registrar Ingreso a Laboratorio")

elif st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Generador de Precios MyM")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        serv_tipo = st.selectbox("Tipo de Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Diagnóstico Técnico"])
        modalidad = st.radio("Lugar del Servicio:", ["En Oficina", "A Domicilio"])
    
    # Lógica de Precios Gerardo M&M
    tarifa_base = 40000
    domicilio = 20000 if modalidad == "A Domicilio" else 0
    total = tarifa_base + domicilio
    
    with col_c2:
        st.metric("Total a Cobrar", f"${total:,} COP")
        st.caption(f"Base: ${tarifa_base:,} + Domicilio: ${domicilio:,}")
        if st.button("Generar PDF de Cotización"):
            st.write("Generando documento...")

elif st.session_state.seccion == "CITAS":
    st.subheader("📅 Agendamiento de Servicios")
    st.write("Seleccione la modalidad para su visita técnica o legal.")
    ca1, ca2 = st.columns(2)
    with ca1:
        if st.button("📍 CITA EN OFICINA (Base $40.000)", use_container_width=True):
            st.success("✅ Solicitud recibida. Lo esperamos en nuestra oficina en Bogotá.")
    with ca2:
        if st.button("🏠 VISITA DOMICILIARIA ($60.000)", use_container_width=True):
            st.warning("✅ Solicitud recibida. Un técnico se desplazará a su ubicación ($40k + $20k transporte).")

# --- PIE DE PÁGINA ---
st.divider()
st.caption(f"L.I.N.A. V15.4 | © {ahora.year} Soluciones M&M - Gerardo Martinez Lemus")