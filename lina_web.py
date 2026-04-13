import streamlit as st
import os
import base64
import datetime
import tempfile
from streamlit_autorefresh import st_autorefresh
from fpdf import FPDF # Recuerda instalar: pip install fpdf2

# --- 1. CONFIGURACIÓN MECÁNICA DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")

# Sincronización exacta con Bogotá (UTC-5)
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. GESTIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "INICIO"

# --- 3. PROCESAMIENTO DE IMÁGENES (BASE64) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ARQUITECTURA VISUAL (CSS AISLADO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{
        width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF;
        box-shadow: 0 0 25px #00FFFF; object-fit: cover;
    }}
    .neon-titulo {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 1; margin: 0; text-align: center;
    }}
    .alerta-amarilla {{
        background-color: #fff9c4; border: 2px solid #fbc02d; color: #444;
        padding: 15px; border-radius: 10px; margin-top: 20px; margin-bottom: 10px;
        font-size: 15px; text-align: center; font-weight: bold; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .barra-metalica {{
        background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border: 2px solid #666; border-radius: 15px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .cuadro-total {{
        background: white; padding: 25px; border-radius: 15px; border: 4px solid #00FFFF;
        text-align: center; max-width: 500px; margin: 20px auto;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
col_logo, col_text = st.columns([1, 2.5])
with col_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with col_text:
    st.markdown(f"""
    <div style="text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:10px;">
            <span style="color:#008fb3; font-weight:bold; font-size:18px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span>
        </div>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:8px;">
            <span style="color:#444; font-weight:bold; font-size:14px;">Soluciones Tecnológicas M Y M - Desde 2007</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL DE CONTROL OPERATIVO ---
btns = st.columns(6)
opciones = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, opcion in enumerate(opciones):
    if btns[i].button(opcion, use_container_width=True):
        st.session_state.seccion = opcion.split()[1]
        st.rerun()

st.divider()

# --- 7. LÓGICA DE SECCIONES ---

# --- SECCIÓN PREVENTIVO ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    col_info, col_check = st.columns(2)
    with col_info:
        st.subheader("📋 Datos del Equipo")
        tipo_equipo = st.selectbox("Tipo de Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno"], key="p_tipo")
        marca = st.text_input("Marca del Producto:", key="p_marca")
        modalidad = st.radio("Modalidad del Servicio:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True, key="p_mod")
    
    with col_check:
        st.subheader("✅ Checklist")
        st.checkbox("¿Enciende correctamente?", key="c1")
        st.checkbox("Limpieza de polvo", key="c2")
        resultado = st.radio("Estado Final:", ["Todo OK", "Requiere Correctivo"], key="p_res")

    total_prev = 40000 + (20000 if modalidad == "A Domicilio" else 0)
    st.markdown(f'<div class="cuadro-total"><h4>Inversión Total</h4><h1 style="color:#008fb3;">$ {total_prev:,.0f}</h1></div>', unsafe_allow_html=True)

# --- SECCIÓN GESTIÓN (MEJORADA) ---
elif st.session_state.seccion == "GESTIÓN":
    t_liq, t_hab = st.tabs(["📊 Liquidación Honorarios", "🛡️ Habeas Data & PDF"])
    
    with t_liq:
        st.subheader("📊 Liquidación de Honorarios M Y M")
        cg1, cg2 = st.columns(2)
        with cg1:
            nom_c = st.text_input("Nombre del Cliente:", key="g_nom", value="CLIENTE GENERAL")
            m_deuda = st.number_input("Valor de la deuda ($):", value=1851000, key="g_deuda")
            c_real = st.number_input("Capital Real ($):", value=150000, key="g_cap")
        with cg2:
            tipo_c = st.radio("Criterio:", ["Consulta ($40.000)", "Éxito (10% Ahorro)"], key="g_tipo")
            mod_c = st.radio("Sede:", ["Oficina", "Domicilio"], horizontal=True, key="g_mod")
        
        ahorro = m_deuda - c_real
        base_h = 40000 if "Consulta" in tipo_c else (ahorro * 0.10)
        total_g = base_h + (20000 if mod_c == "Domicilio" else 0)

        st.markdown(f"""
        <div class="cuadro-total">
            <h3 style="margin:0; color:#444;">TOTAL A PAGAR A M Y M</h3>
            <h1 style="color:#008fb3; font-size:60px;">$ {total_g:,.0f}</h1>
            <p style="color:green; font-weight:bold;">Ahorro para el cliente: ${ahorro:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)

    with t_hab:
        st.subheader("📝 Generador de Derechos de Petición")
        pdf_ent = st.text_input("Entidad:", key="h_ent", placeholder="Ej: Rapicredit")
        pdf_asu = st.text_input("Asunto:", key="h_asu", placeholder="Ej: Solicitud Prescripción")
        pdf_firma = st.file_uploader("Subir foto de la firma:", type=['png','jpg','jpeg'], key="h_firma")
        pdf_body = st.text_area("Cuerpo:", key="h_body", value=f"Yo, {nom_c}, solicito cordialmente...")

        if st.button("🚀 Generar PDF Firmado", key="h_btn"):
            if pdf_ent and pdf_asu:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 16)
                pdf.cell(0, 10, "DERECHO DE PETICIÓN", ln=True, align='C')
                pdf.ln(10)
                pdf.set_font("Arial", '', 12)
                pdf.cell(0, 10, f"Bogotá, {ahora_bog.strftime('%d/%m/%Y')}", ln=True)
                pdf.cell(0, 10, f"A: {pdf_ent.upper()}", ln=True)
                pdf.cell(0, 10, f"Asunto: {pdf_asu.upper()}", ln=True)
                pdf.ln(10)
                pdf.multi_cell(0, 7, pdf_body)
                if pdf_firma:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                        tmp.write(pdf_firma.getvalue())
                        pdf.image(tmp.name, x=10, y=pdf.get_y()+5, w=40)
                st.download_button("📥 Descargar PDF", data=pdf.output(dest='S'), file_name=f"Peticion_{pdf_ent}.pdf", mime="application/pdf")

# --- 8. BLOQUE FINAL (BARRA Y FIRMA) ---
st.divider()
st.markdown(f"""
<div class="barra-metalica">
    <div style="display: flex; justify-content: space-between; font-family: monospace; font-weight: bold; margin-bottom: 10px;">
        <span>📍 BOGOTÁ, COLOMBIA</span>
        <span>📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}</span>
    </div>
    <div style="display: flex; justify-content: space-around;">
        <a href="https://wa.me/573114759768" target="_blank" class="boton-social">🟢 WhatsApp</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia/" target="_blank" class="boton-social">🔵 Facebook</a>
    </div>
</div>
<div style="text-align:right; margin-top:20px;">
    <p style="color:#444; font-size:13px;"><b>LINA Core V20.0</b> | © {ahora_bog.year} <b>ING. Gerardo Martinez Lemus</b></p>
</div>
""", unsafe_allow_html=True)
