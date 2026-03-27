import streamlit as st
import os
import base64
import datetime
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA Y FECHAS ---
st.set_page_config(page_title="LINA V15.5 | Gestión MyM & Vivienda", layout="wide")

# Sincronización de Reloj (Colombia UTC-5)
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# Fechas de Seguimiento para Vivienda
fecha_pago_siste = datetime.datetime(2026, 4, 1)
faltan_siste = (fecha_pago_siste.date() - ahora.date()).days
fecha_limite_aslegal = ahora + timedelta(days=21)
faltan_aslegal = (fecha_limite_aslegal.date() - ahora.date()).days

# --- 2. RECURSOS VISUALES ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

logo_original_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 3. ESTILOS CSS MyM ---
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
    .titulo-neon {{
        font-family: 'Comic Sans MS', cursive !important;
        font-size: 75px !important; color: #000 !important;
        text-shadow: 0 0 10px #7FFFD4, 0 0 20px #7FFFD4 !important;
        margin: 0; line-height: 1;
    }}
    .subtitulo-mym {{
        color: #008fb3 !important; font-size: 20px !important;
        font-weight: bold; font-family: 'Comic Sans MS', cursive !important;
        border-top: 2px solid #00d4ff; display: inline-block; padding-top: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 4. BARRA SUPERIOR Y LOGO ---
st.html(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; font-size: 16px;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}
    </div>
    <div style="font-size: 12px; font-weight: bold;">SOLUCIONES TECNOLÓGICAS M&M</div>
</div>
""")

logo_img = f'<img src="data:image/jpeg;base64,{logo_original_b64}" style="width: 120px; border-radius: 50%; border: 3px solid #00d4ff;">' if logo_original_b64 else "🤖"
st.html(f"""
<div style="display: flex; align-items: center; gap: 30px; padding: 10px 60px;">
    {logo_img}
    <div>
        <h1 class="titulo-neon">L.I.N.A. V15.5</h1>
        <div class="subtitulo-mym">GESTIÓN PROFESIONAL MyM | DESDE 2007</div>
    </div>
</div>
""")

# --- 5. NAVEGACIÓN ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = "DASHBOARD"

st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("📊 DASHBOARD VIVIENDA", use_container_width=True): st.session_state.seccion = "DASHBOARD"
with c2:
    if st.button("⚖️ HABEAS DATA", use_container_width=True): st.session_state.seccion = "LEGAL"
with c3:
    if st.button("🔧 TÉCNICO M&M", use_container_width=True): st.session_state.seccion = "TECNICO"
with c4:
    if st.button("💰 COTIZADOR / CITAS", use_container_width=True): st.session_state.seccion = "EXTRAS"

st.divider()

# --- 6. CONTENIDO ---

if st.session_state.seccion == "DASHBOARD":
    st.subheader("📊 Control de Metas para Vivienda")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sistecrédito", "$898.771", f"Faltan {faltan_siste} días")
    with col2:
        st.metric("Rapicredit", "$200.000", "Meta: Capital Base")
    with col3:
        st.metric("Respuesta ASLEGAL", fecha_limite_aslegal.strftime('%d/%m/%Y'), f"{faltan_aslegal} días restantes")
    
    st.info("💡 **Estrategia Solventa:** No aceptar abonos del 60%. Solo pago total por $704.000 (Capital).")

elif st.session_state.seccion == "LEGAL":
    st.subheader("🛡️ Escudo Legal y Generador de Peticiones")
    tab1, tab2 = st.tabs(["📝 Generador de Petición", "🗣️ Respuestas Legales"])
    
    with tab1:
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            u_nom = st.text_input("Titular:", value="LINA PAOLA MOJICA RUIZ").upper()
            u_ced = st.text_input("Cédula:", value="1016026492")
            u_ent = st.text_input("Entidad:", value="ASLEGAL / ZINOBE").upper()
        with col_l2:
            u_dir = st.text_input("Dirección:", value="Bogotá D.C.")
            u_tel = st.text_input("Teléfono:", value="3114759768")
            u_cor = st.text_input("Correo:", value="linamojica977@gmail.com")

        # FUSIÓN: Definición de variable doc antes de su uso
        doc = f"""Bogotá D.C., {ahora.strftime('%d/%m/%Y')}

Señores: {u_ent} | E. S. D.
REF: RECLAMACIÓN HABEAS DATA - LEY 1266 Y LEY 2157

Yo, {u_nom}, con C.C. {u_ced}, solicito la eliminación del reporte negativo.
Argumento: La obligación inició mora en 2018 (hace más de 7 años), cumpliendo el término de caducidad legal.
Adicionalmente, el cobro actual pretende intereses que superan la tasa de usura vigente.

Atentamente,
{u_nom} | C.C. {u_ced}"""

        st.text_area("📄 Vista Previa del Documento:", value=doc, height=250)
        st.download_button("📥 Descargar Petición TXT", data=doc, file_name=f"HabeasData_{u_nom}.txt")

    with tab2:
        with st.expander("❓ ¿Cómo responder a Solventa sobre el 'abono del 60%'?"):
            st.write("Respuesta: 'No acepto abonos parciales. Mi oferta es por el capital ($704.000) para cierre total bajo Ley 2157.'")

elif st.session_state.seccion == "TECNICO":
    st.subheader("🔧 Módulo de Servicio Técnico")
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.selectbox("Tipo de Equipo:", ["HP Compaq dc5800", "Dell Optiplex", "Portátil", "Electrodoméstico"])
        st.text_area("Descripción de la Falla:")
    with t_col2:
        st.date_input("Fecha Ingreso:", value=ahora)
        st.button("Registrar Servicio en Base de Datos")

elif st.session_state.seccion == "EXTRAS":
    st.subheader("💰 Cotizador y 📅 Citas")
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        mod = st.radio("Servicio:", ["Oficina", "Domicilio"])
        precio = 40000 if mod == "Oficina" else 60000
        st.metric("Total COP", f"${precio:,}")
    with c_col2:
        st.button("📍 Agendar Cita")

st.divider()
st.caption(f"L.I.N.A. V15.5 | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
