import streamlit as st
import os
import base64
import datetime
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="daterefresh")

# Ajuste de hora Colombia (UTC-5)
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "INICIO"

# --- 3. RECURSOS VISUALES ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ESTILOS CSS ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
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
        width: 220px; height: 220px;
        border-radius: 50%; border: 6px solid #00FFFF;
        box-shadow: 0 0 35px #00FFFF; object-fit: cover;
    }}
    .neon-imponente {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 0.85; margin: 0; text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO CENTRADO CON PLACAS INDIVIDUALES (CORREGIDO) ---
col_izq, col_der = st.columns([1, 2.2])

with col_izq:
    st.markdown(f'''
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final">
        </div>
    ''', unsafe_allow_html=True)

with col_der:
    st.markdown(f"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 250px; text-align: center;">
        
        <h1 class="neon-imponente" style="font-size: 85px; margin: 0; padding: 0;">L.I.N.A.</h1>
        
        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 15px; width: 100%; align-items: center;">
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 10px 20px; border-radius: 12px; border: 2px solid #00FFFF; box-shadow: 0 0 15px rgba(0,255,255,0.2); width: fit-content;">
                <span style="color: #008fb3; font-size: 20px; font-weight: bold; display: block; white-space: nowrap;">
                    Laboratorio de Inteligencia y Nuevos Algoritmos
                </span>
            </div>
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 10px 20px; border-radius: 12px; border: 2px solid #00FFFF; box-shadow: 0 0 15px rgba(0,255,255,0.2); width: fit-content;">
                <span style="color: #444; font-size: 16px; font-weight: bold; display: block; white-space: nowrap;">
                    Soluciones Tecnológicas M Y M - Desde 2007
                </span>
            </div>
            
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO (BOTONES) ---
st.write("### 🚀 Seleccione el Servicio Requerido:")
f1c1, f1c2, f1c3 = st.columns(3)
f2c1, f2c2, f2c3 = st.columns(3)

with f1c1:
    if st.button("🛠️ Mant. Preventivo", use_container_width=True): st.session_state.seccion = "PREVENTIVO"; st.rerun()
with f1c2:
    if st.button("🔧 Mant. Correctivo", use_container_width=True): st.session_state.seccion = "CORRECTIVO"; st.rerun()
with f1c3:
    if st.button("⚖️ Gestión Legal", use_container_width=True): st.session_state.seccion = "GESTION_LEGAL"; st.rerun()
with f2c1:
    if st.button("📝 Radicación", use_container_width=True): st.session_state.seccion = "RADICACION"; st.rerun()
with f2c2:
    if st.button("🛡️ Casos Legales", use_container_width=True): st.session_state.seccion = "CASOS_LEGALES"; st.rerun()
with f2c3:
    if st.button("📁 Archivo", use_container_width=True): st.session_state.seccion = "ARCHIVO"; st.rerun()

st.divider()

# --- 7. LÓGICA DE SECCIONES (CONTENIDO) ---

# --- SECCIÓN: MANTENIMIENTO PREVENTIVO ---
if st.session_state.seccion == "PREVENTIVO":
    st.subheader("🛠️ Mantenimiento Preventivo Especializado")
    col_izq, col_der = st.columns([2, 1])
    
    with col_izq:
        st.markdown("#### 🔍 Datos del Equipo")
        tipo_e = st.selectbox("Tipo de Producto:", ["PC de Mesa", "Todo en Uno", "Portátil", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca y Modelo:")
        
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        tipo_at = st.radio("Atención:", ["Solo Consulta", "Servicio Completo (Limpieza + Optimización)"], horizontal=True)
        
        if mod == "A Domicilio":
            dir_v = st.text_input("Dirección de visita:")
            col_f, col_h = st.columns(2)
            fecha_v = col_f.date_input("Fecha sugerida:")
            hora_v = col_h.time_input("Hora sugerida:")

        st.markdown("#### 📋 Checklist de Entrada")
        c1 = st.checkbox("¿Enciende correctamente?")
        c2 = st.checkbox("¿Ruidos extraños?")
        diag = st.text_area("Descripción inicial / Estado actual del equipo:")

    with col_der:
        base = 40000
        extra = 20000 if mod == "A Domicilio" else 0
        total = (base + extra) if tipo_at == "Solo Consulta" else (base + extra if mod == "A Domicilio" else base)
        
        st.markdown(f"""
        <div style="background:white; padding:20px; border-radius:15px; border:3px solid #00FFFF; text-align:center;">
            <h3>Inversión</h3>
            <h1 style="color:#008fb3;">$ {total:,.0f}</h1>
            <p><b>ING. Gerardo Martinez Lemus</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💾 Guardar Informe"):
            st.success("Informe Técnico generado con éxito.")

# --- SECCIÓN: LEGAL / RAPICREDIT (TU CASO ESPECÍFICO) ---
elif st.session_state.seccion == "CASOS_LEGALES":
    st.subheader("🛡️ Defensa Legal: Lina vs RapiCredit")
    cap, deb = 200000, 502837
    st.error(f"⚠️ Alerta: Excedente detectado de $ {(deb-cap):,.0f}".replace(",", "."))
    
    if st.button("📝 Generar Argumentos para SIC"):
        doc = f"HECHOS:\n1. Oferta SMS: $200.000\n2. Débito: $502.837\n3. Factura No. RCC6205119 emitida el 28/03/2026 posterior al cobro."
        st.text_area("Copia este texto:", value=doc, height=150)

# --- 8. PIE DE PÁGINA (SIEMPRE VISIBLE) ---
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 50px;">
    <p style="margin:0;"><b>⚠️ MyM Nota:</b> Honorarios por éxito (10% ahorro) o tarifas base de <b>$40.000</b>.</p>
    <p style="text-align:right; color:#666; margin:0;">LINA Core V20.0 | © {ahora.year} <b>ING. Gerardo Martinez Lemus</b></p>
</div>
""", unsafe_allow_html=True)
