import streamlit as st
import os
import base64
import datetime
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh
import pandas as pd

# --- 1. CONFIGURACIÓN Y RELOJ (Sincronización Colombia UTC-5) ---
st.set_page_config(page_title="LINA V20.0 | Gestión MyM", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# Memoria de Sesión
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'inventario' not in st.session_state:
    st.session_state.inventario = [
        {"Fecha": "2026-03-15", "Equipo": "HP Compaq dc5800 SFF", "Trabajo": "Mantenimiento preventivo, pasta térmica y SSD", "Estado": "Entregado"}
    ]

# --- 2. RECURSOS VISUALES ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f: return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 3. ESTILOS CSS (Fusión V15.5 + V20.0) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)),
                          url("data:image/jpeg;base64,{fondo_b64 if fondo_b64 else ''}") !important;
        background-size: cover !important;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 40px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%) !important;
        border-bottom: 3px solid #666; margin-bottom: 20px; border-radius: 8px;
    }}
    .titulo-neon-v15 {{
        font-family: 'Comic Sans MS', cursive !important;
        font-size: 70px !important; color: #000 !important;
        text-shadow: 0 0 10px #7FFFD4, 0 0 20px #7FFFD4 !important;
        margin: 0; line-height: 1;
    }}
    .logo-v15 {{
        width: 130px; border-radius: 50%; border: 4px solid #00d4ff;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
    }}
</style>
""", unsafe_allow_html=True)

# --- 4. BARRA SUPERIOR (Reloj y Fecha) ---
st.html(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; font-size: 16px; color: #333;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}
    </div>
    <div style="font-size: 12px; font-weight: bold; color: #555;">SOLUCIONES TECNOLÓGICAS M&M</div>
</div>
""")

# --- 5. MENÚ LATERAL PROFESIONAL ---
with st.sidebar:
    st.markdown("### 🛠️ PANEL DE CONTROL")
    if logo_b64: st.image(f"data:image/jpeg;base64,{logo_b64}", width=180)
    
    st.markdown("---")
    st.write("**📱 PÚBLICO**")
    if st.button("💰 Cotizador", use_container_width=True): st.session_state.seccion = "COTIZADOR"
    
    st.markdown("---")
    st.write("**🔒 ADMINISTRATIVO**")
    if st.button("📝 Radicación Legal", use_container_width=True): st.session_state.seccion = "RADICACION"
    if st.button("🖥️ Inventario PC", use_container_width=True): st.session_state.seccion = "INVENTARIO"
    
    st.markdown("---")
    st.caption(f"L.I.N.A. Core V20.0 | © {ahora.year}")

# --- 6. ENCABEZADO PRINCIPAL (Estilo V15.5) ---
logo_html = f'<img src="data:image/jpeg;base64,{logo_b64}" class="logo-v15">' if logo_b64 else "🤖"
st.html(f"""
<div style="display: flex; align-items: center; gap: 30px; padding: 10px 20px;">
    {logo_html}
    <div>
        <h1 class="titulo-neon-v15">L.I.N.A.</h1>
        <div style="color: #008fb3; font-weight: bold; border-top: 2px solid #00d4ff;">
            GESTIÓN PROFESIONAL MyM | DESDE 2007
        </div>
    </div>
</div>
""")

st.divider()

# --- 7. LÓGICA DE SECCIONES ---

if st.session_state.seccion == "INVENTARIO":
    st.subheader("🖥️ Inventario de Mantenimientos")
    
    # Formulario para registrar equipos
    with st.expander("➕ REGISTRAR NUEVO MANTENIMIENTO"):
        with st.form("form_inv"):
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                f_equipo = st.text_input("Equipo:", placeholder="Ej: HP Compaq dc5800")
            with col_f2:
                f_estado = st.selectbox("Estado:", ["Recibido", "En Reparación", "Entregado"])
            
            f_detalle = st.text_area("Detalles técnicos (Pasta térmica, componentes, etc.):")
            
            if st.form_submit_button("Guardar Registro"):
                st.session_state.inventario.append({
                    "Fecha": ahora.strftime('%Y-%m-%d'),
                    "Equipo": f_equipo,
                    "Trabajo": f_detalle,
                    "Estado": f_estado
                })
                st.success("¡Equipo registrado!")
                st.rerun()

    # Mostrar la tabla de historial
    st.table(pd.DataFrame(st.session_state.inventario))

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Centro de Radicación")
    st.info("Sección configurada para generación de documentos legales.")

else: # COTIZADOR
    st.subheader("💰 Cotizador de Servicios")
    st.write("Bienvenido al área de cotización para clientes.")
