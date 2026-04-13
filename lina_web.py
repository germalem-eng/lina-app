import streamlit as st
import os
import base64
import datetime
import urllib.parse
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V21.0 | M Y M Soluciones", layout="wide", page_icon="🤖")
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

# Recursos Visuales (Asegúrate de tener las carpetas creadas)
fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

if 'seccion' not in st.session_state:
    st.session_state.seccion = "PREVENTIVO"

# --- 3. DISEÑO VISUAL (TU ESTÉTICA ORIGINAL) ---
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
    st.markdown(f"""<div style="text-align:center;"><h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>
    <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; display:inline-block; margin-top:10px;">
    <span style="color:#008fb3; font-weight:bold; font-size:18px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span></div></div>""", unsafe_allow_html=True)

st.divider()

# --- 5. PANEL DE NAVEGACIÓN ---
btns = st.columns(6)
ops = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, o in enumerate(ops):
    if btns[i].button(o, use_container_width=True):
        st.session_state.seccion = o.split()[1]
        st.rerun()

# --- 6. LÓGICA DE SECCIONES (UNIFICADA) ---

# --- SECCIÓN: GESTIÓN (INCLUYE COMPARADOR REPARADORAS) ---
if st.session_state.seccion == "GESTIÓN":
    st.header("⚖️ Consultoría y Comparador de Deuda")
    
    with st.expander("🧐 ¿REPARADORA O GESTIÓN MyM? (Herramienta de Venta)"):
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            deuda_t = st.number_input("Deuda Total Actual ($):", value=12000000)
            meta_desc = st.slider("% Descuento pretendido:", 10, 90, 50)
        
        ahorro_estimado = deuda_t * (meta_desc / 100)
        pago_banco = deuda_t - ahorro_estimado
        comision_rep = ahorro_estimado * 0.15 # Promedio reparadoras
        
        with col_r2:
            st.metric("Pago con Gestión MyM", f"$ {pago_banco:,.0f}", delta="Ahorro Máximo")
            st.metric("Pago con Reparadora", f"$ {pago_banco + comision_rep:,.0f}", delta=f"Costo extra: ${comision_rep:,.0f}", delta_color="inverse")

    st.subheader("📊 Liquidación de Honorarios MyM")
    # Tu lógica original de liquidación aquí...
    monto_reclaman = st.number_input("Monto que reclaman ($):", value=1851000)
    capital_real = st.number_input("Capital Real Adeudado ($):", value=150000)
    ahorro = monto_reclaman - capital_real
    st.info(f"Ahorro para el cliente: ${ahorro:,.0f} | Honorarios MyM (10%): ${ahorro * 0.10:,.0f}")

# --- SECCIÓN: CASO LEGAL (PROTEGIDA POR PIN) ---
elif st.session_state.seccion == "LEGAL":
    st.header("🛡️ Expedientes Legales Críticos")
    pin = st.text_input("PIN de Seguridad:", type="password")
    
    if pin == "2007":
        tab_g, tab_l = st.tabs(["👤 EXP. GERARDO", "👤 EXP. LINA"])
        with tab_g:
            st.subheader("Caso: Gerardo Martinez (Lineru/Aslegal)")
            st.warning("Estrategia: Caducidad del dato (+2655 días de mora).")
            st.code("Ley 2157 de 2021: El dato negativo debe ser eliminado por superar 8 años desde la mora.")
        
        with tab_l:
            st.subheader("Caso: Lina Mojica (RapiCredit)")
            st.error("Estado: Reintegro pendiente $302.837")
            st.write("**Factura Crítica:** RCC6205119 (Fecha 28/03 - Inconsistente)")
            if st.button("📄 Generar Texto de Denuncia SIC/DIAN"):
                denuncia = f"Denuncia por apropiación indebida. Factura No. RCC6205119 emitida posterior al cobro..."
                st.text_area("Copia y pega en el portal de la SIC:", denuncia)
    elif pin != "":
        st.error("Acceso Denegado")

# --- SECCIÓN: RADICACIÓN (DOCUMENTOS) ---
elif st.session_state.seccion == "RADICACIÓN":
    st.header("📝 Generador de Documentos Formales")
    nom_rad = st.text_input("Nombre del Solicitante:").upper()
    ent_rad = st.text_input("Entidad Destinataria:").upper()
    tipo_rad = st.selectbox("Tipo de Reclamo:", ["Derecho de Petición", "Revocatoria Débito Automático", "Solicitud de Paz y Salvo"])
    
    texto_doc = f"YO, {nom_rad}, identificado con CC _________, solicito ante {ent_rad} lo siguiente: {tipo_rad}..."
    st.text_area("Vista previa del documento:", texto_doc, height=200)

# --- MANTENEMOS TUS SECCIONES TÉCNICAS ORIGINALES ---
elif st.session_state.seccion == "PREVENTIVO":
    st.subheader("🛠️ Mantenimiento Preventivo Especializado")
    # (Aquí va exactamente tu código de la sección 6 que ya tienes)
    st.info("Carga de interfaz técnica original...")

elif st.session_state.seccion == "CORRECTIVO":
    st.subheader("🔧 Mantenimiento Correctivo y Reparación")
    # (Aquí va exactamente tu código de la sección 7 que ya tienes)
    st.info("Carga de interfaz de presupuestos original...")

elif st.session_state.seccion == "PRIVADO":
    st.subheader("🏠 Gestión Privada de Cuentas")
    # (Aquí va tu código de la sección 9 con la calculadora de utilidad)
    st.info("Carga de gestión financiera...")

# --- BARRA FINAL (TU ESTÉTICA ORIGINAL) ---
st.divider()
st.markdown(f"""
<div class="barra-metalica">
    <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 10px;">
        <span>📍 BOGOTÁ, COLOMBIA</span>
        <span>📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}</span>
    </div>
    <div style="text-align: center;">
        <a href="https://wa.me/573114759768" target="_blank" style="text-decoration:none; color:#222; margin:0 10px;">🟢 WhatsApp</a>
        <a href="#" style="text-decoration:none; color:#222; margin:0 10px;">🔵 Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)
