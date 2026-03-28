import streamlit as st
import os
import base64
import datetime
import urllib.parse
import pandas as pd
from fpdf import FPDF  # <--- NUEVA LIBRERÍA PARA EL PDF

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.1 | Proyecto L.I.N.A.", layout="wide", page_icon="🤖")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. MEMORIA DE SESIÓN ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'texto_fijo' not in st.session_state: st.session_state.texto_fijo = ""
if 'inventario' not in st.session_state:
    st.session_state.inventario = [
        {"Fecha": "2026-03-15", "Equipo": "HP Compaq dc5800 SFF", "Trabajo": "Cambio de pasta térmica y reemplazo de disco duro HDD por SSD.", "Estado": "Entregado"}
    ]

# --- 3. FUNCIÓN PARA GENERAR EL RECIBO PDF ---
def generar_pdf(datos):
    pdf = FPDF()
    pdf.add_page()
    # Encabezado
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "SOLUCIONES TECNOLOGICAS M&M", ln=True, align='C')
    pdf.set_font("Arial", '', 10)
    pdf.cell(200, 10, f"Recibo de Servicio Tecnico - {ahora.strftime('%d/%m/%Y')}", ln=True, align='C')
    pdf.ln(10)
    # Cuerpo
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, f"Equipo: {datos['Equipo']}", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 10, f"Trabajo Realizado: {datos['Trabajo']}")
    pdf.ln(5)
    pdf.cell(200, 10, f"Estado Final: {datos['Estado']}", ln=True)
    pdf.ln(20)
    pdf.set_font("Arial", 'I', 9)
    pdf.cell(200, 10, "Gracias por confiar en Soluciones M&Y - Desde 2007", ln=True, align='C')
    return pdf.output(dest='S').encode('latin-1')

# --- 4. RECURSOS VISUALES (TU ESENCIA) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 5. ESTILOS CSS ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 25px;
    }}
    .logo-redondo-final {{
        width: 280px; height: 280px; border-radius: 50%; border: 6px solid #00FFFF; box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .resaltado-blanco {{
        background-color: rgba(255, 255, 255, 0.85); border-radius: 8px; padding: 5px 15px; margin: 3px 0; display: inline-block;
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 0.85; margin: 0; text-align: center;
    }}
    .social-tag {{
        padding: 5px 12px; border-radius: 15px; text-decoration: none !important; color: white !important; font-weight: bold; font-size: 12px; margin-left: 5px;
    }}
    .sidebar-logo {{
        display: block; margin: auto; width: 150px; height: 150px; border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 15px #00FFFF; object-fit: cover;
    }}
</style>
""", unsafe_allow_html=True)

# --- 6. ENCABEZADO (REDES) ---
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
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 7. TÍTULO Y LOGO ---
col_izq, col_der = st.columns([1.2, 2.3])
with col_izq:
    st.markdown(f'<div style="display:flex; justify-content:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)
with col_der:
    st.markdown(f'<div style="text-align: center;"><h1 class="neon-imponente" style="font-size: 110px;">L.I.N.A.</h1></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;"><div class="resaltado-blanco"><span style="color:#008fb3; font-size:26px; font-weight:bold;">Gestion Tecnológica Profesional</span></div></div>', unsafe_allow_html=True)

st.divider()

# --- 8. MENÚ LATERAL ---
with st.sidebar:
    st.markdown("### 🛠️ PANEL OPERATIVO")
    if logo_robot_b64:
        st.markdown(f'<img src="data:image/jpeg;base64,{logo_robot_b64}" class="sidebar-logo">', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💰 COTIZADOR", use_container_width=True): st.session_state.seccion = "COTIZADOR"
    st.markdown("---")
    if st.button("📝 RADICACIÓN LEGAL", use_container_width=True): st.session_state.seccion = "RADICACION"
    if st.button("🖥️ INVENTARIO PC", use_container_width=True): st.session_state.seccion = "INVENTARIO"

# --- 9. LÓGICA DE SECCIONES ---

if st.session_state.seccion == "INVENTARIO":
    st.subheader("🖥️ Inventario de Mantenimientos")
    
    with st.expander("➕ REGISTRAR NUEVO TRABAJO"):
        with st.form("nuevo_mantenimiento"):
            f_equipo = st.text_input("Equipo:", placeholder="Ej: HP Compaq dc5800")
            f_detalle = st.text_area("Trabajo realizado:")
            f_estado = st.selectbox("Estado:", ["En proceso", "Listo para entrega", "Entregado"])
            if st.form_submit_button("Guardar"):
                st.session_state.inventario.append({"Fecha": ahora.strftime('%Y-%m-%d'), "Equipo": f_equipo, "Trabajo": f_detalle, "Estado": f_estado})
                st.rerun()

    st.markdown("### 📋 Historial y Recibos")
    for i, item in enumerate(st.session_state.inventario):
        col_it1, col_it2 = st.columns([3, 1])
        with col_it1:
            st.write(f"**{item['Equipo']}** - {item['Fecha']}")
        with col_it2:
            # BOTÓN DE PDF
            pdf_bytes = generar_pdf(item)
            st.download_button(label="📥 Recibo PDF", data=pdf_bytes, file_name=f"Recibo_{item['Equipo']}.pdf", mime="application/pdf", key=f"pdf_{i}")
        st.divider()

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Radicación Legal")
    # ... (Tu código de radicación aquí)

elif st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador M&M")
    st.info("Área de servicios al cliente.")
