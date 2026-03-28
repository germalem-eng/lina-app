import streamlit as st
import os
import base64
import datetime
import urllib.parse
import pandas as pd  # Para el inventario

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="LINA V20.0 | Proyecto L.I.N.A.", layout="wide", page_icon="🤖")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. MEMORIA DE SESIÓN ---
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'texto_fijo' not in st.session_state: st.session_state.texto_fijo = ""
# Memoria para el inventario (se guarda mientras la app esté abierta)
if 'inventario' not in st.session_state:
    st.session_state.inventario = [
        {"Fecha": "2026-03-15", "Equipo": "HP Compaq dc5800 SFF", "Trabajo": "Cambio de pasta térmica y reemplazo de disco duro HDD por SSD.", "Estado": "Entregado"}
    ]

# --- 3. ESTILOS CSS (TU DISEÑO NEÓN) ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .nav-bar-silver {{
        padding: 10px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 12px; margin-bottom: 20px; text-align: center;
    }}
    .logo-redondo-final {{
        width: 220px; height: 220px; border-radius: 50%; border: 5px solid #00FFFF; box-shadow: 0 0 25px #00FFFF;
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
    }}
    .resaltado-blanco {{
        background-color: rgba(255, 255, 255, 0.85); border-radius: 8px; padding: 5px 15px; display: inline-block;
    }}
</style>
""", unsafe_allow_html=True)

# --- 4. MENÚ LATERAL (AJUSTADO PARA NO CONFUNDIR) ---
with st.sidebar:
    st.markdown("### 🛠️ MENÚ L.I.N.A.")
    st.image(f"data:image/jpeg;base64,{logo_robot_b64}", width=150)
    
    st.markdown("---")
    st.write("**📱 ÁREA CLIENTE**")
    if st.button("💰 Cotizador de Servicios", use_container_width=True): st.session_state.seccion = "COTIZADOR"
    
    st.markdown("---")
    st.write("**🔒 ÁREA ADMINISTRADOR**")
    if st.button("📝 Radicación Legal", use_container_width=True): st.session_state.seccion = "RADICACION"
    if st.button("🖥️ Inventario de Mantenimiento", use_container_width=True): st.session_state.seccion = "INVENTARIO"
    
    st.markdown("---")
    st.info(f"Sesión: {ahora.strftime('%H:%M:%S')}")

# --- 5. ENCABEZADO PRINCIPAL ---
st.markdown(f'<div class="nav-bar-silver"><b>PROYECTO L.I.N.A. | Soluciones MyM 2007</b></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final"></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<h1 class="neon-imponente" style="font-size: 80px; margin-bottom:0;">L.I.N.A.</h1>', unsafe_allow_html=True)
    st.markdown('<div class="resaltado-blanco"><b style="color:#008fb3;">Inventario & Gestión Digital</b></div>', unsafe_allow_html=True)

st.divider()

# --- 6. LÓGICA DE SECCIONES ---

# --- SECCIÓN: COTIZADOR ---
if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador para Clientes")
    st.info("Esta es la sección que verían tus clientes para pedir presupuestos.")
    # Aquí puedes poner el código del cotizador de antes...

# --- SECCIÓN: RADICACIÓN ---
elif st.session_state.seccion == "RADICACION":
    st.subheader("⚖️ Radicación de Reclamos Legales")
    # (Aquí va el código de Radicación que ya arreglamos antes)
    st.warning("Usa esta sección para generar documentos de cobranza o bancos.")

# --- SECCIÓN: INVENTARIO (NUEVO) ---
elif st.session_state.seccion == "INVENTARIO":
    st.subheader("🖥️ Inventario de Mantenimientos Realizados")
    
    with st.expander("➕ REGISTRAR NUEVO TRABAJO"):
        with st.form("nuevo_mantenimiento"):
            f_equipo = st.text_input("Marca y Modelo del Equipo:", placeholder="Ej: Dell Optiplex 790")
            f_fecha = st.date_input("Fecha del servicio:", datetime.date.today())
            f_detalle = st.text_area("Descripción del trabajo:", placeholder="Limpieza, software, hardware...")
            f_estado = st.selectbox("Estado:", ["En proceso", "Listo para entrega", "Entregado"])
            
            if st.form_submit_button("Guardar en Bitácora"):
                nuevo_item = {"Fecha": str(f_fecha), "Equipo": f_equipo, "Trabajo": f_detalle, "Estado": f_estado}
                st.session_state.inventario.append(nuevo_item)
                st.success("¡Registro guardado!")
                st.rerun()

    st.markdown("### 📋 Historial de Equipos")
    df = pd.DataFrame(st.session_state.inventario)
    st.table(df) # Muestra una tabla limpia con los trabajos realizados
