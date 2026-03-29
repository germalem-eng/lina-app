import streamlit as st
import os
import base64
import datetime
from streamlit_autorefresh import st_autorefresh

# ==========================================
# LINA CORE V20.0 - VERSIÓN ESTABLE DE RESCATE
# ==========================================

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. GESTIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "PREVENTIVO"

# --- 3. PROCESAMIENTO DE IMÁGENES ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

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
    .boton-social {{ text-decoration: none !important; color: #333 !important; background: white; padding: 8px 15px; border-radius: 10px; font-weight: bold; border: 1px solid #999; display: inline-block; }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
c_l, c_t = st.columns([1, 2.5])
with c_l: st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with c_t:
    st.markdown('<h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-weight:bold; color:#008fb3;">Soluciones Tecnológicas M Y M - Desde 2007</p>', unsafe_allow_html=True)

st.divider()

# --- 6. PANEL OPERATIVO ---
btns = st.columns(6)
ops = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, o in enumerate(ops):
    if btns[i].button(o, use_container_width=True):
        st.session_state.seccion = o.split()[1]
        st.rerun()

st.divider()

# --- 7. SECCIÓN: MANTENIMIENTO PREVENTIVO ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo")
    col_a, col_b = st.columns(2)
    with col_a:
        tipo = st.selectbox("Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca:")
        specs = st.text_area("Especificaciones Técnicas:")
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
    with col_b:
        st.subheader("✅ Checklist")
        st.checkbox("Limpieza física profunda")
        st.checkbox("Borrado archivos basura")
        st.checkbox("Antivirus y Seguridad")
        res = st.radio("Resultado:", ["Todo OK", "Requiere Correctivo"])
        if res == "Requiere Correctivo": st.text_area("Descripción:")
    
    # Cálculo
    total = 40000 + (20000 if mod == "A Domicilio" else 0)
    st.markdown(f'<div style="background:white; padding:15px; border:3px solid #00FFFF; border-radius:15px; text-align:center; max-width:350px; margin:auto;"><h3>Total: $ {total:,.0f}</h3><p>ING. Gerardo Martinez</p></div>', unsafe_allow_html=True)

# --- 8. BLOQUE FINAL: ADVERTENCIA + CONTACTO + FIRMA ---

st.markdown("""
<div class="alerta-amarilla">
    ⚠️ NOTA: Honorarios por éxito (10% ahorro) o tarifas base de $40.000.
</div>
""", unsafe_allow_html=True)

html_barra = f"""
<div class="barra-metalica">
    <div class="reloj-bogota">
        <span>📍 BOGOTÁ, COLOMBIA</span>
        <span>📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div style="font-weight: bold; color: #222;">🌐 REDES OFICIALES:</div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="https://wa.me/573114759768" target="_blank" class="boton-social">🟢 WhatsApp</a>
            <a href="https://web.facebook.com/MyMsolucionesdetecnologia/" target="_blank" class="boton-social">🔵 Facebook</a>
            <a href="https://instagram.com" target="_blank" class="boton-social">🟣 Instagram</a>
            <a href="https://linkedin.com" target="_blank" class="boton-social">💠 LinkedIn</a>
            <a href="https://youtube.com" target="_blank" class="boton-social">🔴 YouTube</a>
        </div>
    </div>
</div>
"""
st.markdown(html_inf, unsafe_allow_html=True)
st.markdown(f'<p style="text-align:right; font-size:12px;">LINA Core V20.0 | © {ahora_bog.year} Gerardo Martinez</p>', unsafe_allow_html=True)
