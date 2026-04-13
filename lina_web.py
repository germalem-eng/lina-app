import streamlit as st
import os
import base64
import datetime
import urllib.parse
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN MECÁNICA (SIN CAMBIOS) ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

if 'seccion' not in st.session_state: 
    st.session_state.seccion = "PREVENTIVO"

def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def generar_enlace_whatsapp(telefono, mensaje):
    mensaje_codificado = urllib.parse.quote(mensaje)
    return f"https://wa.me/{telefono}?text={mensaje_codificado}"

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

# --- 4. ARQUITECTURA VISUAL (TU ESTÉTICA ORIGINAL) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{ width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF; box-shadow: 0 0 25px #00FFFF; object-fit: cover; }}
    .neon-titulo {{ font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF; text-align: center; }}
    .barra-metalica {{ background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%); border: 2px solid #666; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
    .cuadro-total, .cuadro-inversion {{ background: white; padding: 25px; border-radius: 15px; border: 4px solid #00FFFF; text-align: center; margin: 20px auto; }}
    .boton-social {{ text-decoration: none; color: white !important; padding: 8px 15px; border-radius: 8px; margin: 5px; display: inline-block; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO (SIN TOCAR) ---
col_logo, col_text = st.columns([1, 2.5])
with col_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with col_text:
    st.markdown(f"""<div style="text-align:center;"><h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>
    <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:10px;">
    <span style="color:#008fb3; font-weight:bold; font-size:18px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span></div></div>""", unsafe_allow_html=True)

st.divider()

# --- 6. PANEL DE CONTROL ---
btns = st.columns(6)
opciones = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, opcion in enumerate(opciones):
    if btns[i].button(opcion, use_container_width=True):
        st.session_state.seccion = opcion.split()[1]
        st.rerun()

st.divider()

# --- 7. SECCIONES (SOLO INTEGRACIÓN DE PUNTOS FALTANTES) ---

if st.session_state.seccion == "PREVENTIVO":
    # --- TU CÓDIGO ORIGINAL SIN CAMBIOS ---
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    col_info, col_check = st.columns(2)
    with col_info:
        tipo_equipo = st.selectbox("Tipo de Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
        modalidad = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
    total = 40000 + (20000 if modalidad == "A Domicilio" else 0)
    st.markdown(f'<div class="cuadro-total"><h4>Inversión Preventivo</h4><h1>$ {total:,.0f}</h1></div>', unsafe_allow_html=True)

elif st.session_state.seccion == "CORRECTIVO":
    # --- TU CÓDIGO ORIGINAL SIN CAMBIOS ---
    st.header("🔧 Mantenimiento Correctivo y Reparación")
    col_diag, col_cotiza = st.columns(2)
    with col_cotiza:
        costo_mano_obra = st.number_input("Valor Mano de Obra ($):", value=60000)
        costo_repuestos = st.number_input("Valor Total Repuestos ($):", value=0)
        total_correctivo = costo_mano_obra + costo_repuestos
    st.markdown(f'<div class="cuadro-total" style="border-color:#FF4B4B;"><h1>$ {total_correctivo:,.0f}</h1></div>', unsafe_allow_html=True)

elif st.session_state.seccion == "GESTIÓN":
    st.header("⚖️ Gestión de Cartera y Comparador")
    # PUNTO 1: Comparador de Reparadoras (NUEVO)
    with st.expander("🧐 ¿POR QUÉ MyM Y NO UNA REPARADORA?"):
        deuda_cli = st.number_input("Deuda Total:", value=10000000)
        ahorro_est = deuda_cli * 0.5
        comision_reparadora = ahorro_est * 0.15
        comision_mym = ahorro_est * 0.10
        st.write(f"❌ Una reparadora te cobraría: **${comision_reparadora:,.0f}**")
        st.write(f"✅ Con Gestión MyM pagas solo: **${comision_mym:,.0f}**")
        st.success(f"Ahorras con nosotros: ${comision_reparadora - comision_mym:,.0f}")
    
    # Tu liquidación original
    monto_d = st.number_input("Monto que reclaman ($):", value=1851000)
    capital_r = st.number_input("Capital Real ($):", value=150000)
    st.info(f"Ahorro Cliente: ${monto_d - capital_r:,.0f}")

elif st.session_state.seccion == "LEGAL":
    # PUNTO 2 y 3: Casos Críticos (NUEVO)
    st.header("🛡️ Expedientes Críticos")
    pin_l = st.text_input("PIN de Acceso:", type="password")
    if pin_l == "2007":
        t1, t2 = st.tabs(["LINA (RapiCredit)", "GERARDO (Lineru/Aslegal)"])
        with t1:
            st.error("EXP: LINA MOJICA - Reembolso Pendiente")
            st.write("- **Monto:** $302.837")
            st.write("- **Referencia:** Factura RCC6205119")
            if st.button("Copiar Denuncia SIC"):
                st.code(f"Solicito devolución de $302.837 por cobro indebido según factura RCC6205119...")
        with t2:
            st.warning("EXP: GERARDO MARTINEZ - Caducidad")
            st.write("- **Estado:** +2655 días de mora (Desde 2018)")
            st.write("- **Acción:** Exigir eliminación por Ley 2157 (Supera 8 años)")

elif st.session_state.seccion == "RADICACIÓN":
    # PUNTO 4: Automatización de Paz y Salvos (NUEVO)
    st.header("📝 Generador de Documentos")
    tipo_doc = st.selectbox("Documento a generar:", ["Exigencia de Paz y Salvo", "Revocatoria Débito Automático"])
    nombre_c = st.text_input("Nombre Cliente:").upper()
    if st.button("Generar Texto"):
        if "Paz y Salvo" in tipo_doc:
            st.text_area("Copia este texto:", f"Cordial saludo. Yo {nombre_c}, habiendo cancelado la totalidad de la obligación, exijo mi paz y salvo...")

elif st.session_state.seccion == "PRIVADO":
    # PUNTO 6: Seguridad en Utilidad (NUEVO)
    st.header("🏠 Gestión Privada")
    pin_p = st.text_input("PIN Privado:", type="password", key="p_pin")
    if pin_p == "2007":
        cobro = st.number_input("Total Cobrado:", value=0)
        costo = st.number_input("Costo Repuesto:", value=0)
        st.metric("Utilidad Neta", f"$ {cobro - costo:,.0f}")

# --- 10. BARRA FINAL (SIN CAMBIOS EN REDES) ---
st.divider()
html_barra = f"""
<div class="barra-metalica">
    <div style="text-align:center; font-family:monospace; font-weight:bold; color:#333; margin-bottom:10px;">
        📍 BOGOTÁ, COLOMBIA | 📅 {ahora_bog.strftime('%d/%m/%Y')} | 🕒 {ahora_bog.strftime('%H:%M:%S')}
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div style="font-weight: bold; color: #222; font-size: 13px;">🌐 REDES OFICIALES:</div>
        <div style="display: flex; flex-wrap: wrap;">
            <a href="https://wa.me/573114759768" target="_blank" class="boton-social" style="background:#25D366;">WhatsApp</a>
            <a href="https://web.facebook.com/MyMsolucionesdetecnologia/" target="_blank" class="boton-social" style="background:#1877F2;">Facebook</a>
        </div>
    </div>
</div>
"""
st.markdown(html_barra, unsafe_allow_html=True)
