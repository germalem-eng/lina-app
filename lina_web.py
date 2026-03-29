import streamlit as st
import os
import base64
import datetime
import urllib.parse
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN MECÁNICA DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | M Y M Soluciones", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")

# Sincronización Bogotá (UTC-5)
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

# Carga de recursos
fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 3. GESTIÓN DE ESTADO ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = "PREVENTIVO"

# --- 4. ARQUITECTURA VISUAL (CSS AISLADO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{ width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF; box-shadow: 0 0 25px #00FFFF; object-fit: cover; }}
    .neon-titulo {{ font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF; text-align: center; }}
    .alerta-amarilla {{ background-color: #fff9c4; border: 2px solid #fbc02d; color: #444; padding: 15px; border-radius: 10px; margin-top: 20px; font-weight: bold; text-align: center; }}
    .barra-metalica {{ background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%); border: 2px solid #666; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
    .reloj-bogota {{ font-family: 'Courier New', monospace; font-weight: bold; color: #111; display: flex; justify-content: space-between; border-bottom: 2px solid #888; padding-bottom: 8px; margin-bottom: 12px; }}
    .boton-social {{ text-decoration: none !important; color: #333 !important; background: white; padding: 6px 10px; border-radius: 8px; font-weight: bold; font-size: 11px; border: 1px solid #999; display: inline-block; margin: 2px; }}
    .btn-auto {{ text-decoration: none; color: white !important; padding: 12px; border-radius: 10px; text-align: center; font-weight: bold; display: block; margin-top: 10px; }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
c_logo, c_tit = st.columns([1, 2.5])
with c_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with c_tit:
    st.markdown('<h1 class="neon-titulo" style="font-size:70px;">L.I.N.A.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-weight:bold; color:#008fb3; font-size:18px;">Soluciones Tecnológicas M Y M - Desde 2007</p>', unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO ---
btns = st.columns(6)
ops = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, o in enumerate(ops):
    if btns[i].button(o, use_container_width=True):
        st.session_state.seccion = o.split()[1]
        st.rerun()

st.divider()

# --- 7. MANTENIMIENTO PREVENTIVO ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📋 Datos del Equipo")
        tipo = st.selectbox("Producto:", ["PC Mesa", "Portátil", "Todo en Uno", "Tablet", "Componente electrónico", "Electrodoméstico", "Componente del electrodoméstico",])
        marca = st.text_input("Marca del Producto:")
        specs = st.text_area("Características / Especificaciones:")
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)

    with col_b:
        st.subheader("✅ Checklist Obligatorio")
        st.checkbox("Encendido inicial OK")
        st.checkbox("Limpieza física profunda (Polvo/Componentes)")
        st.checkbox("Borrado de archivos basura / Temporales")
        
        # --- Lógica de Antivirus (S/N) con Incremento Automático ---
        tiene_av = st.radio("¿Tiene Antivirus? (S/N)", ["SÍ", "NO"], horizontal=True)
        
        extra_antivirus = 0 # Inicializa el incremento en cero
        
        if tiene_av == "SÍ":
            st.checkbox("Escaneo Antivirus y Seguridad (Incluido)")
        else:
            instalar_av = st.checkbox("Instalar Antivirus (+ $10.000)")
            if instalar_av:
                extra_antivirus = 10000 # Se activa la fórmula de incremento
        
        st.checkbox("Verificación de puertos y carga")

    st.divider()

    # --- LÓGICA POR MODALIDAD ---
    inversion = 40000 

    if mod == "Virtual":
        st.info("💻 **Asesoría Virtual**")
        toma_servicio = st.radio("¿Toma servicio técnico?", ["No (Solo asesoría)", "Sí (Agendar Cita)"])
        
        if toma_servicio == "Sí (Agendar Cita)":
            inversion = 0 
            st.success("📅 **Datos para agendar:**")
            ca, cb = st.columns(2)
            with ca:
                nom = st.text_input("Nombre del Cliente:")
                tel = st.text_input("Teléfono (WhatsApp):")
                dir_c = st.text_input("Dirección de la Cita:")
            with cb:
                f_c = st.date_input("Fecha:", ahora_bog.date())
                h_c = st.time_input("Hora:", datetime.time(8, 0))
            
            if nom and tel:
                st.write("---")
                c_wa, c_cal = st.columns(2)
                msg = f"Hola, soy {nom}. Confirmo cita M.P. el {f_c} a las {h_c}. Dirección: {dir_c}. Equipo: {tipo} {marca}."
                link_wa = generar_enlace_whatsapp("573114759768", msg)
                with c_wa:
                    st.markdown(f'<a href="{link_wa}" target="_blank" class="btn-auto" style="background:#25D366;">📲 WhatsApp Confirmar</a>', unsafe_allow_html=True)
                start = f"{f_c.strftime('%Y%m%d')}T{h_c.strftime('%H%M%S')}"
                link_cal = f"https://www.google.com/calendar/render?action=TEMPLATE&text=M.P.+{nom}&details=Equipo:+{tipo}+{marca}&location={dir_c}&dates={start}/{start}"
                with c_cal:
                    st.markdown(f'<a href="{link_cal}" target="_blank" class="btn-auto" style="background:#4285F4;">🗓️ Google Calendar</a>', unsafe_allow_html=True)

    elif mod == "En Oficina":
        oficina_estado = st.radio("Estado:", ["Evaluación y Ejecución", "Sin equipo (Pasar a Domicilio)"])
        if oficina_estado == "Sin equipo (Pasar a Domicilio)":
            mod = "A Domicilio"
            inversion = 60000
        else:
            inversion = 40000

    if mod == "A Domicilio":
        st.subheader("🏠 Proceso en Domicilio")
        st.text_input("Dirección de visita:")
        st.text_input("Telefono:")
        st.text_input("e-Mail:")
        st.text_input("S/N se traslada a oficina equipo:")
        inversion = 60000 

    # --- CUADRO DE INVERSIÓN FINAL ---
    st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 400px; margin: 30px auto;">
        <h4 style="margin:0; color:#444;">Inversión del Servicio</h4>
        <h1 style="color: #008fb3; margin: 10px 0;">$ {inversion:,.0f}</h1>
        <p><b>ING. Gerardo Martinez Lemus</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- 8. BLOQUE FINAL: ADVERTENCIA + BARRA PLATEADA CON TODAS LAS REDES ---
st.markdown('<div class="alerta-amarilla">⚠️ NOTA: Honorarios por éxito (10% ahorro) o tarifas base de $40.000.</div>', unsafe_allow_html=True)

html_barra = f"""
<div class="barra-metalica">
    <div class="reloj-bogota">
        <span>📍 BOGOTÁ, COLOMBIA</span>
        <span>📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div style="font-weight: bold; color: #222; font-size: 13px;">🌐 REDES OFICIALES:</div>
        <div style="display: flex; flex-wrap: wrap; justify-content: flex-end;">
            <a href="https://wa.me/573114759768" target="_blank" class="boton-social">🟢 WhatsApp</a>
            <a href="https://web.facebook.com/MyMsolucionesdetecnologia/" target="_blank" class="boton-social">🔵 Facebook</a>
            <a href="https://instagram.com" target="_blank" class="boton-social">🟣 Instagram</a>
            <a href="https://youtube.com" target="_blank" class="boton-social">🔴 YouTube</a>
            <a href="https://t.me" target="_blank" class="boton-social">✈️ Telegram</a>
            <a href="https://tiktok.com" target="_blank" class="boton-social">🎵 TikTok</a>
            <a href="https://x.com" target="_blank" class="boton-social">⚫ X</a>
        </div>
    </div>
</div>
"""
st.markdown(html_barra, unsafe_allow_html=True)

st.markdown(f'<p style="text-align:right; font-size:12px; margin-top:10px;">LINA Core V20.0 | © {ahora_bog.year} Gerardo Martinez Lemus</p>', unsafe_allow_html=True)
