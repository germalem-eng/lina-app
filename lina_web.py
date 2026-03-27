import streamlit as st
import os
import base64
import datetime
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V16.5 | Core MyM", layout="wide", page_icon="🤖")

# Sincronización de Reloj (Colombia UTC-5)
st_autorefresh(interval=1000, key="daterefresh")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. INICIALIZACIÓN DE VARIABLES (Blindaje Total) ---
# Inicializamos TODAS las variables en el Session State al principio para evitar NameErrors.
if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'doc_final' not in st.session_state: st.session_state.doc_final = ""
if 'log_file' not in st.session_state: st.session_state.log_file = "registro_lina_mym.csv"

# --- 3. FUNCIONES DE APOYO ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

def guardar_log(entidad, usuario, ahorro_estimado):
    nueva_fila = {
        "Fecha": [ahora.strftime('%Y-%m-%d %H:%M')],
        "Entidad": [entidad],
        "Usuario": [usuario],
        "Ahorro_Meta": [ahorro_estimado]
    }
    df = pd.DataFrame(nueva_fila)
    if not os.path.isfile(st.session_state.log_file):
        df.to_csv(st.session_state.log_file, index=False)
    else:
        df.to_csv(st.session_state.log_file, mode='a', header=False, index=False)

# --- 4. RECURSOS VISUALES ---
# Restauramos las rutas originales de tus logos.
logo_robot_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 5. ESTILOS CSS MyM (Nivel Ejecutivo V16.5) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover !important;
        background-attachment: fixed !important;
    }}
    /* Barra Superior Silver */
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border-bottom: 3px solid #666; border-radius: 8px; margin-bottom: 10px;
    }}
    .social-tag {{
        padding: 4px 12px; border-radius: 15px; text-decoration: none;
        color: white !important; font-weight: bold; font-size: 13px; margin-left: 8px;
    }}
    
    /* EFECTOS DE DISEÑO EXECUTIVO V16.5 */
    
    /* 1. LINA Monumental (Más Grande y Centrado) */
    .titulo-lina-final {{
        font-family: 'Comic Sans MS', cursive; 
        font-size: clamp(60px, 12vw, 120px); /* 40% más grande */
        color: #000; text-shadow: 0 0 15px #7FFFD4, 0 0 30px #7FFFD4; 
        margin: 0; line-height: 1; text-align: center;
    }}
    
    /* 2. Logo Maximizada y Perfectamente Centrado */
    .logo-redondo-final {{
        width: clamp(140px, 18vw, 200px); /* Más grande */
        height: clamp(140px, 18vw, 200px);
        border-radius: 50%; border: 4px solid #7FFFD4; 
        box-shadow: 0 0 20px #7FFFD4;
        object-fit: cover;
    }}
    .col-logo-final {{
        display: flex; justify-content: center; align-items: center; height: 100%;
    }}
    
    /* 3. Títulos Intercambiados Centrados */
    .col-titulos-final {{
        display: flex; flex-direction: column; justify-content: center;
        text-align: center; height: 100%;
    }}
    .tit-laboratorio {{
        color: #008fb3; font-size: 26px; font-weight: bold; margin-bottom: 5px;
    }}
    .tit-soluciones-mym {{
        color: #444; font-size: 18px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 6. ENCABEZADO CORREGIDO (DISEÑO FINAL V16.5) ---

# Barra Plateada Superior
st.markdown(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')} | SOLUCIONES MyM</div>
    <div>
        <a href="#" class="social-tag" style="background-color: #FF0000;">YouTube</a>
        <a href="#" class="social-tag" style="background-color: #E1306C;">Instagram</a>
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia" target="_blank" class="social-tag" style="background-color: #4267B2;">Facebook</a>
        <a href="https://wa.me/573114759768" target="_blank" class="social-tag" style="background-color: #25D366;">WhatsApp</a>
        <a href="#" class="social-tag" style="background-color: #0088CC;">Telegram</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Cuerpo Central (Dos Columnas: Logo y Texto)
col_logo, col_titulos = st.columns([1, 2.5])

with col_logo:
    # Mostramos el logo maximizado y centrado.
    if logo_robot_b64:
        st.markdown(f"""
        <div class="col-logo-final">
            <img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo-final">
        </div>
        """, unsafe_allow_html=True)

with col_titulos:
    # Mostramos LINA monumental y los títulos intercambiados.
    st.markdown(f"""
    <div class="col-titulos-final">
        <h1 class="titulo-lina-final">L.I.N.A.</h1>
        <div class="tit-laboratorio">Laboratorio de Inteligencia y Nuevos Algoritmos</div>
        <div class="tit-soluciones-mym">Soluciones Tecnológicas M Y M | Desde 2007</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 7. NAVEGACIÓN (Multiplataforma) ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3, c4 = st.columns(4)
with c1: if st.button("💰 COTIZADOR", use_container_width=True): st.session_state.seccion = "COTIZADOR"
with c2: if st.button("⚖️ GESTIÓN DE CASOS", use_container_width=True): st.session_state.seccion = "GESTION"
with c3: if st.button("📝 RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"
with c4: if st.button("🏠 PRIVADO MyM", use_container_width=True): st.session_state.seccion = "FINANZAS"

st.divider()

# --- 8. LÓGICA DE SECCIONES (Mantenemos la funcionalidad blindada) ---

if st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Cotizador de Servicios MyM")
    col_precios, col_calc = st.columns([1, 2])
    
    with col_precios:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 2px solid #00d4ff; text-align: center;">
            <h4>📋 Lista de Precios Base</h4>
            <p><b>Revisión Técnica:</b> $40.000<br>(GRATIS si acepta servicio)</p>
            <p><b>Asesoría Legal / Habeas Data:</b> $40.000<br>(GRATIS si inicia proceso)</p>
            <p><b>Recargo Domicilio (Bogotá):</b> $20.000</p>
        </div>
        """, unsafe_allow_html=True)

    with col_calc:
        tipo_servicio = st.selectbox("Tipo de Servicio:", ["Mantenimiento Preventivo", "Mantenimiento Correctivo", "Asesoría Legal / Habeas Data"])
        modalidad = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        
        # Lógica de Cobro
        base = 40000
        domicilio = 20000 if modalidad == "A Domicilio" else 0
        
        if tipo_servicio == "Asesoría Legal / Habeas Data":
            total = base + domicilio
            detalle = "Si inicias proceso legal, solo pagas el 10% del ahorro al finalizar. ¡Esta consulta es gratis si firmas!"
        else:
            # Estrategia 20% sobre el mínimo
            total = (base * 1.20) + domicilio
            detalle = "¡La revisión es GRATIS! El valor incluye repuestos básicos y mano de obra calificada."

        st.metric("Total a Pagar", f"${total:,.0f} COP", f"+{domicilio} domicilio" if domicilio > 0 else "")
        st.caption(f"💡 {detalle}")
        st.link_button("📍 AGENDAR CITA AHORA", "https://wa.me/573114759768")

elif st.session_state.seccion == "GESTION":
    st.subheader("⚖️ Seguimiento a Casos Generados")
    
    # Monitor de Silencio Administrativo
    with st.expander("📅 Monitor de Tiempos Legales", expanded=True):
        f_rad = st.date_input("Fecha de radicación:", value=ahora.date() - timedelta(days=5))
        f_est = f_rad + timedelta(days=21)
        dias_rest = (f_est - ahora.date()).days
        
        cm1, cm2 = st.columns(2)
        cm1.metric("Días para vencimiento", f"{max(0, dias_rest)} días")
        cm2.metric("Fecha estimada de respuesta", f_est.strftime('%d/%m/%Y'))

    # Base de datos de Cobros
    st.markdown("### 💸 Control de Honorarios Pendientes")
    if os.path.exists(st.session_state.log_file):
        df = pd.read_csv(st.session_state.log_file)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay casos registrados aún. Genera una radicación para empezar.")

elif st.session_state.seccion == "RADICACION":
    st.subheader("📝 Generador de Peticiones Legales")
    u_nom = st.text_input("Nombre Completo:")
    u_ced = st.text_input("Cédula:")
    u_aho = st.number_input("Ahorro Proyectado:", min_value=0)
    
    # Esta es la línea 284 que blindamos arriba. st.session_state.doc_final siempre existe.
    st.text_area("📄 Vista Previa del Documento:", value=st.session_state.doc_final, height=200)

elif st.session_state.seccion == "FINANZAS":
    st.subheader("💰 Control Personal MyM")
    st.metric("Meta Sistecrédito", "$898.771")

# --- 9. PIE DE PÁGINA (Ejecutivo) ---
st.markdown(f"""
<div style="background-color: #f1f1f1; padding: 15px; border-radius: 10px; border-left: 5px solid #008fb3; margin-top: 20px;">
    <b>⚠️ Nota de Honorarios:</b> Nuestros honorarios se basan estrictamente en el éxito conseguido. 
    Defensa Legal: 10% del ahorro. Mantenimiento: Revisión gratis si se realiza el proceso.
</div>
""", unsafe_allow_html=True)

st.caption(f"LINA Core | © {ahora.year} Gerardo Martinez Lemus | Soluciones M Y M")
