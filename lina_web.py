import streamlit as st
import datetime
import os
import base64
import tempfile
from fpdf import FPDF # Asegúrate de tener: pip install fpdf2

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="LINA V20.0 | M Y M Soluciones", layout="wide", page_icon="🤖")
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. FUNCIONES BASE ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 3. ESTILOS ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .neon-titulo {{ font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF; text-align: center; }}
    .cuadro-pago {{ background: white; padding: 30px; border-radius: 15px; border: 4px solid #00FFFF; text-align: center; max-width: 500px; margin: auto; }}
</style>
""", unsafe_allow_html=True)

# --- 4. ENCABEZADO ---
col1, col2 = st.columns([1, 2.5])
with col1:
    if logo_robot_b64:
        st.markdown(f'<img src="data:image/jpeg;base64,{logo_robot_b64}" style="width:160px; border-radius:50%; border:3px solid #00FFFF;">', unsafe_allow_html=True)
with col2:
    st.markdown('<h1 class="neon-titulo" style="font-size:60px;">L.I.N.A.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#008fb3; font-weight:bold;">M Y M Soluciones Tecnológicas</p>', unsafe_allow_html=True)

# --- 5. MENÚ DE NAVEGACIÓN ---
if 'seccion_actual' not in st.session_state:
    st.session_state.seccion_actual = "GESTIÓN"

c_nav = st.columns(4)
if c_nav[0].button("🛠️ EQUIPOS", use_container_width=True): st.session_state.seccion_actual = "EQUIPOS"
if c_nav[1].button("⚖️ GESTIÓN", use_container_width=True): st.session_state.seccion_actual = "GESTIÓN"
if c_nav[2].button("🛡️ LEGAL", use_container_width=True): st.session_state.seccion_actual = "LEGAL"
if c_nav[3].button("🏠 PRIVADO", use_container_width=True): st.session_state.seccion_actual = "PRIVADO"

st.divider()

# --- 6. CUERPO DE LA APP ---
if st.session_state.seccion_actual == "EQUIPOS":
    st.header("🛠️ Registro de Equipos")
    # Usamos keys únicas para que no choque con otras secciones
    t_eq = st.selectbox("Tipo:", ["PC Mesa", "Portátil", "Cámara", "Otro"], key="eq_tipo")
    m_eq = st.text_input("Marca:", key="eq_marca")
    mod_eq = st.text_input("Modelo:", key="eq_modelo")

elif st.session_state.seccion_actual == "GESTIÓN":
    t_liq, t_hab, t_norm = st.tabs(["📊 Liquidación", "🛡️ Habeas Data (PDF)", "📚 Normativa"])
    
    with t_liq:
        st.subheader("Liquidación de Honorarios")
        col_a, col_b = st.columns(2)
        with col_a:
            nom_c = st.text_input("Cliente:", key="liq_nom", value="CLIENTE GENERAL")
            m_deuda = st.number_input("Deuda Total ($):", value=1851000, key="liq_monto")
            c_real = st.number_input("Capital Real ($):", value=150000, key="liq_cap")
        with col_b:
            tipo_c = st.radio("Cobro:", ["Consulta ($40.000)", "Éxito (10% Ahorro)"], key="liq_tipo")
            mod_c = st.radio("Sede:", ["Oficina", "Domicilio"], horizontal=True, key="liq_sede")
        
        # Cálculo
        ahorro = m_deuda - c_real
        base = 40000 if "Consulta" in tipo_c else (ahorro * 0.10)
        domicilio = 20000 if mod_c == "Domicilio" else 0
        total = base + domicilio

        st.markdown(f"""
        <div class="cuadro-pago">
            <h3>TOTAL A PAGAR A M Y M</h3>
            <h1 style="color:#008fb3;">$ {total:,.0f}</h1>
            <p style="color:green;"><b>Ahorro Logrado: ${ahorro:,.0f}</b></p>
        </div>
        """, unsafe_allow_html=True)

    with t_hab:
        st.subheader("Generador de Derecho de Petición")
        entidad = st.text_input("Entidad:", key="hab_ent", placeholder="Ej: Rapicredit")
        asunto = st.text_input("Asunto:", key="hab_asu", placeholder="Ej: Solicitud Prescripción")
        firma = st.file_uploader("Firma (Imagen):", type=['png','jpg','jpeg'], key="hab_firma")
        cuerpo = st.text_area("Mensaje:", key="hab_msg", value=f"Yo, {nom_c}, solicito...")

        if st.button("🚀 Generar PDF Firmado", key="hab_btn"):
            if entidad and asunto:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 16)
                pdf.cell(0, 10, "DERECHO DE PETICIÓN", ln=True, align='C')
                pdf.ln(10)
                pdf.set_font("Arial", '', 12)
                pdf.cell(0, 10, f"Bogotá D.C., {ahora_bog.strftime('%d/%m/%Y')}", ln=True)
                pdf.cell(0, 10, f"A: {entidad.upper()}", ln=True)
                pdf.cell(0, 10, f"Asunto: {asunto.upper()}", ln=True)
                pdf.ln(10)
                pdf.multi_cell(0, 7, cuerpo)
                
                if firma:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                        tmp.write(firma.getvalue())
                        pdf.image(tmp.name, x=10, y=pdf.get_y()+5, w=40)
                
                res_pdf = pdf.output(dest='S')
                st.download_button("📥 Descargar Documento", data=res_pdf, file_name=f"Peticion_{entidad}.pdf", mime="application/pdf")

# --- 7. BARRA FINAL ---
st.divider()
st.markdown(f'<p style="text-align:right; font-size:12px; color:gray;">© {ahora_bog.year} Gerardo Martinez Lemus | LINA Core V20.0</p>', unsafe_allow_html=True)
