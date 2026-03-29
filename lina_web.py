import streamlit as st
import os
import base64
import datetime
import urllib.parse
from streamlit_autorefresh import st_autorefresh
from fpdf import FPDF  # Necesitarás instalarlo: pip install fpdf2

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | M Y M Soluciones", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. FUNCIONES DE APOYO ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def generar_enlace_whatsapp(tel, mensaje):
    msg_encoded = urllib.parse.quote(mensaje)
    return f"https://wa.me/{tel}?text={msg_encoded}"

# Función para crear el PDF del Derecho de Petición
def crear_pdf_peticion(nombre, cedula, entidad, asunto, cuerpo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "DERECHO DE PETICIÓN (Art. 23 C.P.)", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, f"Bogotá D.C., {ahora_bog.strftime('%d de %B de %Y')}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, f"A la entidad: {entidad.upper()}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, f"ASUNTO: {asunto.upper()}", ln=True)
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 7, cuerpo)
    pdf.ln(15)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, f"Atentamente,", ln=True)
    pdf.cell(200, 10, f"{nombre.upper()}", ln=True)
    pdf.cell(200, 10, f"C.C. {cedula}", ln=True)
    
    return pdf.output(dest='S')

# Carga de recursos
fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

if 'seccion' not in st.session_state:
    st.session_state.seccion = "PREVENTIVO"

# --- 3. DISEÑO VISUAL (CSS) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{ width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF; box-shadow: 0 0 25px #00FFFF; object-fit: cover; }}
    .neon-titulo {{ font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF; text-align: center; margin: 0; }}
    .barra-metalica {{ background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%); border: 2px solid #666; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
    .cuadro-inversion {{ background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 450px; margin: 20px auto; }}
</style>
""", unsafe_allow_html=True)

# --- 4. ENCABEZADO ---
col_logo, col_text = st.columns([1, 2.5])
with col_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with col_text:
    st.markdown(f'<div style="text-align:center;"><h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1><p style="color:#008fb3; font-weight:bold;">M Y M Soluciones Tecnológicas - Desde 2007</p></div>', unsafe_allow_html=True)

# --- 5. NAVEGACIÓN ---
btns = st.columns(6)
ops = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, o in enumerate(ops):
    if btns[i].button(o, use_container_width=True):
        st.session_state.seccion = o.split()[1]
        st.rerun()

st.divider()

# --- 8. SECCIÓN GESTIÓN Y DERECHOS DE PETICIÓN ---
if st.session_state.seccion == "GESTIÓN":
    st.header("⚖️ Centro de Gestión Legal y Cartera")
    tabs = st.tabs(["📊 Liquidación Honorarios", "📄 Generador de Derechos de Petición", "📚 Normativa"])
    
    with tabs[0]:
        st.subheader("Liquidación de Honorarios M Y M")
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            nom_g = st.text_input("Nombre del Cliente:", value="GERARDO MARTINEZ LEMUS")
            monto_deuda = st.number_input("Valor que le cobran al cliente ($):", value=1851000)
            capital_real = st.number_input("Capital Real de la deuda ($):", value=150000)
        
        with col_g2:
            tipo_g = st.radio("Criterio de Cobro:", ["Solo Consulta ($40.000)", "Gestión Integral (10% del Ahorro)"])
            mod_g = st.radio("Modalidad:", ["Virtual", "Oficina", "Domicilio"], horizontal=True)

        ahorro = monto_deuda - capital_real
        total_pago_mym = 40000 if "Solo Consulta" in tipo_g else (ahorro * 0.10)
        total_pago_mym += (20000 if mod_g == "Domicilio" else 0)

        st.markdown(f"""
        <div class="cuadro-inversion">
            <h4 style="color:#444;">TOTAL A PAGAR A M Y M SOLUCIONES</h4>
            <h1 style="color:#008fb3;">$ {total_pago_mym:,.0f}</h1>
            <p>Ahorro logrado para el cliente: ${ahorro:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("📝 Creador de Derechos de Petición Profesionales")
        st.info("Esta sección genera un documento legal válido para cualquier entidad (pública o privada).")
        
        p_nom = st.text_input("Nombre Completo del Peticionario:", value=nom_g)
        p_id = st.text_input("Cédula de Ciudadanía:", value="79951815")
        p_entidad = st.text_input("Entidad a la que se dirige:", placeholder="Ej: Rapicredit, Movistar, Alcaldía...")
        p_asunto = st.text_input("Asunto del Derecho de Petición:", placeholder="Ej: Solicitud de prescripción de deuda / Reclamo de servicios")
        
        p_cuerpo = st.text_area("Cuerpo de la Petición (Hechos y Peticiones):", height=250, 
                                value="Por medio de la presente, en ejercicio del Derecho Fundamental de Petición (Art. 23 C.P.), solicito cordialmente...")

        if st.button("🛠️ Generar PDF para Descargar"):
            if p_entidad and p_asunto:
                pdf_data = crear_pdf_peticion(p_nom, p_id, p_entidad, p_asunto, p_cuerpo)
                st.download_button(
                    label="📥 Descargar Derecho de Petición (PDF)",
                    data=pdf_data,
                    file_name=f"Derecho_Peticion_{p_entidad}.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("Por favor completa la Entidad y el Asunto para generar el PDF.")

# (Resto del código para PREVENTIVO, CORRECTIVO y PRIVADO se mantiene igual)
