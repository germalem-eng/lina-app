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

# Recursos Visuales
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
    .reloj-bogota {{ font-family: 'Courier New', monospace; font-weight: bold; color: #111; display: flex; justify-content: space-between; border-bottom: 2px solid #888; padding-bottom: 8px; margin-bottom: 12px; }}
    .cuadro-inversion {{ background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 450px; margin: 20px auto; }}
    .btn-auto {{ text-decoration: none; color: white !important; padding: 12px; border-radius: 10px; text-align: center; font-weight: bold; display: block; margin-top: 10px; }}
</style>
""", unsafe_allow_html=True)

# --- 4. ENCABEZADO ---
col_logo, col_text = st.columns([1, 2.5])
with col_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with col_text:
    st.markdown(f"""
    <div style="text-align:center;">
        <h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; display:inline-block; margin-top:10px;">
            <span style="color:#008fb3; font-weight:bold; font-size:18px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 5. PANEL DE NAVEGACIÓN ---
btns = st.columns(6)
ops = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, o in enumerate(ops):
    if btns[i].button(o, use_container_width=True):
        st.session_state.seccion = o.split()[1]
        st.rerun()

st.divider()

# --- 6. SECCIÓN PREVENTIVO (RESTAURADA) ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📋 Datos del Equipo")
        tipo = st.selectbox("Producto:", ["PC Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca del Producto:")
        specs = st.text_area("Características / Especificaciones:")
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
    with col_b:
        st.subheader("✅ Checklist Obligatorio")
        st.checkbox("Encendido inicial OK")
        st.checkbox("Limpieza física profunda")
        st.checkbox("Borrado de archivos basura")
        tiene_av = st.radio("¿Tiene Antivirus?", ["SÍ", "NO"], horizontal=True)
        extra_av = 10000 if tiene_av == "NO" and st.checkbox("Instalar Antivirus Pro (+ $10.000)") else 0

    base = 40000
    recargo_dom = 20000 if mod == "A Domicilio" else 0
    total_prev = base + extra_av + recargo_dom
    
    st.markdown(f'<div class="cuadro-inversion"><h4>Inversión Total</h4><h1>$ {total_prev:,.0f}</h1><p>ING. Gerardo Martinez</p></div>', unsafe_allow_html=True)
    if st.button("📅 Agendar y Enviar"):
        msg_p = f"Confirmo preventivo para {tipo} {marca}. Total: ${total_prev:,.0f}"
        st.markdown(f'<a href="{generar_enlace_whatsapp("573114759768", msg_p)}" target="_blank" class="btn-auto" style="background:#25D366;">📲 Confirmar WhatsApp</a>', unsafe_allow_html=True)

# --- 7. SECCIÓN CORRECTIVO (RESTAURADA) ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    
    col_info, col_check = st.columns(2)
    
    with col_info:
        st.subheader("📋 Datos del Equipo")
        tipo_equipo = st.selectbox("Tipo de Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca del Producto:")
        specs = st.text_area("Características y Especificaciones (Procesador, RAM, etc.):")
        modalidad = st.radio("Modalidad del Servicio:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)

    with col_check:
        st.subheader("✅ Checklist (Antes/Después)")
        st.checkbox("¿Enciende correctamente?")
        st.checkbox("Limpieza de polvo (Componentes internos)")
        st.checkbox("Borrado de archivos basura / Temporales")
        st.checkbox("Escaneo de Antivirus / Seguridad")
        st.checkbox("Verificación de puertos (USB, Carga, Video)")
        
        st.subheader("🔍 Diagnóstico Final")
        resultado = st.radio("Estado del Equipo:", ["Todo está OK", "Requiere Mantenimiento Correctivo"], index=0)
        
        if resultado == "Requiere Mantenimiento Correctivo":
            st.text_area("Descripción de la necesidad detectada:")
        else:
            st.success("Diagnóstico: Equipo en óptimas condiciones.")

    # Cálculo de Inversión
    base = 40000
    recargo = 20000 if modalidad == "A Domicilio" else 0
    total = base + recargo

    st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 450px; margin: 20px auto;">
        <h4 style="margin:0; color:#444;">Inversión Total del Servicio</h4>
        <h1 style="color: #008fb3; margin: 10px 0;">$ {total:,.0f}</h1>
        <p style="font-size: 13px;"><b>ING. Gerardo Martinez Lemus</b></p>
    </div>
    """, unsafe_allow_html=True)
# --- 8. SECCIÓN GESTIÓN (INTEGRADA CON COMPARADOR) ---
elif st.session_state.seccion == "GESTIÓN":
    st.header("⚖️ Consultoría de Deuda")
    with st.expander("🧐 COMPARADOR: ¿REPARADORA O GESTIÓN MyM?"):
        deuda_t = st.number_input("Deuda Total Actual ($):", value=12000000)
        ahorro_est = deuda_t * 0.50
        comision_rep = ahorro_est * 0.15
        st.write(f"Con una reparadora pagas **${comision_rep:,.0f}** más que con MyM.")
    
    # Tu liquidación original de honorarios
    monto_g = st.number_input("Monto que reclaman ($):", value=1851000)
    capital_g = st.number_input("Capital Real ($):", value=150000)
    st.metric("Ahorro Cliente", f"$ {monto_g - capital_g:,.0f}")

# --- 9. SECCIÓN CASO LEGAL (PRIVADA PARA LINA Y GERARDO) ---
elif st.session_state.seccion == "LEGAL":
    st.header("🛡️ Expedientes Privados")
    pin = st.text_input("PIN Admin:", type="password")
    if pin == "2007":
        c_l, c_g = st.columns(2)
        with c_l:
            st.error("CASO LINA: Devolución $302.837")
            st.write("Factura RCC6205119 inconsistente.")
        with c_g:
            st.info("CASO GERARDO: Caducidad (+2655 días)")
    elif pin != "": st.error("PIN Incorrecto")

# --- 10. SECCIÓN PRIVADO (RESTAURADA) ---
elif st.session_state.seccion == "PRIVADO":
    st.header("🏠 Gestión de Cuentas")
    pin = st.text_input("Introduzca PIN:", type="password", key="priv_pin")
    if pin == "2007":
        cobrado = st.number_input("Total Cobrado ($):", min_value=0)
        costo_r = st.number_input("Costo Repuesto ($):", min_value=0)
        st.metric("Utilidad Real", f"$ {cobrado - costo_r:,.0f}")

# --- BARRA FINAL ---
st.divider()
st.markdown(f"""
<div class="barra-metalica">
    <div class="reloj-bogota">
        <span>📍 BOGOTÁ, COLOMBIA</span>
        <span>📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}</span>
    </div>
</div>
""", unsafe_allow_html=True)
