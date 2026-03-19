import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN E IDENTIDAD ---
st.set_page_config(page_title="Grupo JPL | Sistema 0312", layout="wide")

# --- 2. ESTILOS INSTITUCIONALES (CORREGIDOS PARA CELULARES) ---
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF !important; }
    
    /* Sidebar Vinotinto */
    [data-testid="stSidebar"] { 
        background-color: #800000 !important; 
        border-right: 2px solid #4F4F4F;
    }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; }

    /* Botón de Ingreso RESALTADO */
    div.stButton > button:first-child {
        background-color: #800000 !important; 
        color: white !important;
        font-weight: bold !important;
        border-radius: 5px !important;
        border: 2px solid #000000 !important;
        width: 100% !important;
        height: 3em !important;
    }

    /* Encabezado Negro */
    .app-header {
        padding: 15px; background-color: #000000;
        border-bottom: 4px solid #800000; color: #FFFFFF;
        text-align: center; font-weight: bold;
    }

    h1, h2, h3 { color: #000000 !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE ACCESO (LOGIN FLEXIBLE) ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("### 🛡️ ACCESO GRUPO JPL")
        # El .strip() elimina espacios accidentales que ponen los celulares
        usuario = st.text_input("Usuario:").strip().lower()
        clave = st.text_input("Clave:", type="password").strip()
        
        if st.button("INGRESAR A LA APP"):
            if usuario == "gerardo" and clave == "mym2007":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("❌ Credenciales incorrectas")
    st.stop()

# --- 4. CUERPO DE LA APP (DASHBOARD) ---
st.html('<div class="app-header">GRUPO JPL | Jplprevencionistas - Gestión de Riesgos</div>')

with st.sidebar:
    st.markdown("### 📱 CONTACTO OFICIAL")
    st.write("📞 **Tel:** 301 6015891")
    st.write("📧 **Email:** jplprevencionistas@gmail.com")
    st.write("🌐 **FB:** Jplprevencionistas")
    st.divider()
    menu = st.radio("MÓDULOS:", ["📊 Dashboard", "🛡️ Auditoría 60 Ítems", "🔔 Alertas"])
    if st.button("SALIR"):
        st.session_state['autenticado'] = False
        st.rerun()

# --- CONTENIDO DE MÓDULOS ---
if menu == "🛡️ Auditoría 60 Ítems":
    st.header("📋 Evaluación Res. 0312")
    marcados = 0
    with st.expander("FASE 1: Recursos (15 Items)"):
        for i in range(1, 16):
            if st.checkbox(f"Estándar {i}"): marcados += 1
    st.metric("Cumplimiento Total", f"{int((marcados/60)*100)}%")

elif menu == "🔔 Alertas":
    st.header("🔔 Alertas Algorítmicas")
    st.error("🚨 MENSUAL: Acta de COPASST")
    st.warning("⚠️ CUATRIMESTRAL: Entrega de EPP")

else:
    st.header("Dashboard General")
    st.info("Bienvenido a la terminal de gestión del Grupo JPL.")
