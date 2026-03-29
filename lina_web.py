import streamlit as st
import os
import base64
import datetime
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
        background-size: cover;
        background-attachment: fixed;
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
        line-height: 1; margin: 0; text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO: L.I.N.A. Y PLACAS RESALTADAS ---
col_head1, col_head2 = st.columns([1, 2.2])

with col_head1:
    st.markdown(f'''
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final">
        </div>
    ''', unsafe_allow_html=True)

with col_head2:
    contenido_html = f"""
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
    """
    st.markdown(contenido_html, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO (6 BOTONES) ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("🛠️ PREVENTIVO", use_container_width=True): st.session_state.seccion = "PREVENTIVO"; st.rerun()
with c2:
    if st.button("🔧 CORRECTIVO", use_container_width=True): st.session_state.seccion = "CORRECTIVO"; st.rerun()
with c3:
    if st.button("⚖️ GESTIÓN", use_container_width=True): st.session_state.seccion = "GESTION"; st.rerun()
with c4:
    if st.button("📝 RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"; st.rerun()
with c5:
    if st.button("🛡️ CASO LEGAL", use_container_width=True): st.session_state.seccion = "LEGAL"; st.rerun()
with c6:
    if st.button("🏠 PRIVADO", use_container_width=True): st.session_state.seccion = "PRIVADO"; st.rerun()

st.divider()

# --- 7. LÓGICA DE SECCIONES ---

if st.session_state.seccion == "PREVENTIVO":
    st.subheader("🛠️ Mantenimiento Preventivo Especializado")
    col_izq, col_der = st.columns([2, 1])
    
    with col_izq:
        st.markdown("#### 🔍 Identificación del Producto")
        tipo_e = st.selectbox("Tipo de Producto:", ["PC de Mesa", "Todo en Uno", "Portátil", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca del Producto:", placeholder="Ej: HP, Dell, Samsung...")
        specs = st.text_input("Características / Especificaciones:")
        
        st.markdown("#### 📋 Checklist de Entrada (Antes)")
        col_ch1, col_ch2 = st.columns(2)
        c_enc = col_ch1.checkbox("¿Enciende correctamente?")
        c_pnt = col_ch1.checkbox("¿Pantalla OK (sin manchas)?")
        c_ruido = col_ch2.checkbox("¿Sin ruidos extraños?")
        c_fisico = col_ch2.checkbox("¿Buen estado físico?")

        st.markdown("#### 🧹 Tareas Realizadas")
        st.write("- Limpieza de polvo, Borrado de basura, Escaneo Antivirus, Optimización.")
        resultado = st.text_area("Resultado del mantenimiento (Descripción):", "Todo bien, OK y sale.")

        st.markdown("#### ✅ Verificación de Salida (Después)")
        s_limpio = st.checkbox("Limpieza verificada")
        s_vel = st.checkbox("Mejora en velocidad")

    with col_der:
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        tipo_at = st.radio("Tipo de Atención:", ["Solo Consulta", "Servicio Completo"], index=1)
        
        base = 40000
        extra = 20000 if mod == "A Domicilio" else 0
        
        # Lógica de cobro solicitada
        if tipo_at == "Solo Consulta":
            total = base + extra
        else:
            total = extra if mod == "A Domicilio" else 0
            if mod in ["Virtual", "En Oficina"] and tipo_at == "Servicio Completo":
                total = base # Cobro base por el servicio técnico

        st.markdown(f"""
        <div style="background:white; padding:20px; border-radius:15px; border:3px solid #00FFFF; text-align:center;">
            <h3 style="margin:0;">Inversión Total</h3>
            <h1 style="color:#008fb3; font-size:45px;">$ {total:,.0f}</h1>
            <p style="font-size:12px;">⚠️ MyM Nota: Honorarios base de $40.000</p>
            <hr>
            <p style="font-size:12px;"><b>ING. Gerardo Martinez Lemus</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💾 Guardar Informe Técnico"):
            st.success(f"Informe de {tipo_e} {marca} guardado.")

# --- 8. BARRA PLATEADA DE REDES Y PIE DE PÁGINA ---

# Estilos CSS avanzados para la interactividad de las redes
st.markdown("""
<style>
    .silver-bar {
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        padding: 15px 25px; 
        background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border: 2px solid #666; 
        border-radius: 12px; 
        margin-top: 40px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .social-icon {
        text-decoration: none !important;
        color: #333 !important;
        background: white;
        padding: 8px 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 14px;
        transition: all 0.3s ease;
        border: 1px solid #ccc;
        display: inline-block;
    }
    .social-icon:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,255,255,0.4);
        border-color: #00FFFF;
        color: #000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Renderizado de la Barra Plateada
st.markdown(f"""
<div class="silver-bar">
    <div style="font-family: monospace; font-weight: bold; color: #222; font-size: 14px;">
        🌐 CONECTA CON SOLUCIONES MYM:
    </div>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="https://wa.me/573114759768" target="_blank" class="social-icon">🟢 WhatsApp</a>
        <a href="https://facebook.com/SolucionesMyM" target="_blank" class="social-icon">🔵 Facebook</a>
        <a href="https://instagram.com" target="_blank" class="social-icon">🟣 Instagram</a>
        <a href="https://linkedin.com" target="_blank" class="social-icon">💠 LinkedIn</a>
        <a href="https://youtube.com" target="_blank" class="social-icon">🔴 YouTube</a>
        <a href="https://x.com" target="_blank" class="social-icon">⚫ X</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Pie de Página Final (Cierre del Proyecto L.I.N.A.)
st.markdown(f"""
<div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px; 
            border-left: 6px solid #008fb3; margin-top: 20px; margin-bottom: 30px;">
    <table style="width:100%; border:none;">
        <tr>
            <td style="width:65%; border:none; vertical-align: top;">
                <p style="margin:0; font-size:15px; color:#333;">
                    ⚠️ <b>Nota Legal:</b> Los honorarios por éxito corresponden al 10% del ahorro logrado en procesos legales. 
                    Las tarifas base de revisión técnica o consulta inician en <b>$40.000</b>.
                </p>
            </td>
            <td style="text-align:right; border:none; color:#555; font-size: 13px;">
                <b style="font-size: 16px; color: #008fb3;">LINA Core V20.0</b><br>
                Desarrollado por:<br>
                <b style="color: #000;">ING. Gerardo Martinez Lemus</b><br>
                Bogotá, Colombia - 2026
            </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)
