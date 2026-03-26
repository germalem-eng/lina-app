import streamlit as st
import os
import base64
import datetime

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V15.4 | Gestión MyM", layout="wide")

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Recursos Visuales (Ruta: Logos/)
logo_original_b64 = get_base64("Logos/logo_robot_2007.jpg")
fondo_b64 = get_base64("Logos/fondo.jpg")

# --- 2. ESTILOS CSS (NEÓN Y DISEÑO MyM) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.96), rgba(255, 255, 255, 0.96)),
                          url("data:image/jpeg;base64,{fondo_b64 if fondo_b64 else ''}") !important;
        background-size: cover !important;
    }}
    .nav-bar-silver {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 40px; background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%) !important;
        border-bottom: 3px solid #666; margin-bottom: 20px;
    }}
    .social-links a {{
        color: #1a1a1a !important; text-decoration: none; font-weight: bold;
        font-family: sans-serif; font-size: 11px; padding: 5px 10px;
        border: 1px solid #999; border-radius: 4px; background: white; margin-left: 5px;
    }}
    .titulo-neon {{
        font-family: 'Comic Sans MS', cursive !important;
        font-size: 85px !important; color: #000 !important;
        text-shadow: 0 0 10px #7FFFD4, 0 0 20px #7FFFD4, 0 0 30px #00d4ff !important;
        margin: 0; line-height: 1;
    }}
    .subtitulo-mym {{
        color: #008fb3 !important; font-size: 22px !important;
        font-weight: bold; font-family: 'Comic Sans MS', cursive !important;
        border-top: 2px solid #00d4ff; display: inline-block; padding-top: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 3. BARRA SUPERIOR E IDENTIDAD ---
ahora = datetime.datetime.now()
st.html(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold;">📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}</div>
    <div class="social-links">
        <a href="https://www.facebook.com/share/18U3tNcSUK/" target="_blank">FACEBOOK</a>
        <a href="https://wa.me/573114759768" target="_blank">WHATSAPP</a>
        <a href="#">X</a> <a href="#">INSTAGRAM</a> <a href="#">TIKTOK</a> <a href="#">YOUTUBE</a> <a href="#">TELEGRAM</a>
    </div>
</div>
""")

logo_img = f'<img src="data:image/jpeg;base64,{logo_original_b64}" style="width: 150px; border-radius: 50%; border: 4px solid #00d4ff;">' if logo_original_b64 else "🤖"
st.html(f"""
<div style="display: flex; align-items: center; gap: 40px; padding: 20px 60px;">
    {logo_img}
    <div>
        <h1 class="titulo-neon">L.I.N.A. V15.4</h1>
        <p style="font-family: 'Comic Sans MS'; font-weight: bold; font-size: 18px; color: #333; margin: 0;">LABORATORIO DE INTELIGENCIA Y NUEVOS ALGORITMOS</p>
        <div class="subtitulo-mym">🛠️ SOLUCIONES TECNOLÓGICAS M & M | DESDE 2007</div>
    </div>
</div>
""")

# --- 4. LÓGICA DE NAVEGACIÓN ---
if 'seccion' not in st.session_state:
    st.session_state.seccion = "INICIO"

st.write("### 🚀 Panel Operativo Principal:")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("⚖️ HABEAS DATA", use_container_width=True):
        st.session_state.seccion = "LEGAL"
with c2:
    if st.button("🔧 TÉCNICO M&M", use_container_width=True):
        st.session_state.seccion = "TECNICO"
with c3:
    if st.button("💰 COTIZADOR", use_container_width=True):
        st.session_state.seccion = "COTIZADOR"
with c4:
    if st.button("📅 CITAS", use_container_width=True):
        st.session_state.seccion = "CITAS"

st.divider()

# --- 5. DESPLIEGUE DE CONTENIDO ---

if st.session_state.seccion == "LEGAL":
    st.subheader("🛡️ Escudo Anti-Abuso y Habeas Data")
    tab1, tab2, tab3 = st.tabs(["🔍 Evaluador", "📞 ¿Qué responder?", "📝 Petición"])

    with tab1:
        st.info("📊 **Análisis de Viabilidad de la Deuda**")
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            fecha_vence = st.number_input("Años desde la mora:", min_value=0, max_value=20, step=1)
            tipo_d = st.selectbox("Tipo de Deuda:", ["Tarjeta/Banco", "Celular/Internet", "Revistas/Varios", "Sistecrédito/Ropa"])
        with col_l2:
            ya_pago = st.checkbox("¿Ya pagó la deuda?")
            acoso = st.checkbox("¿Acoso telefónico? (Ley 2300)")

        if fecha_vence >= 8:
            st.success("✅ **CADUCIDAD:** El reporte debe ser borrado (Ley 2157).")
        elif fecha_vence >= 3 and tipo_d != "Tarjeta/Banco":
            st.warning("⚠️ **POSIBLE PRESCRIPCIÓN:** No reconozca la deuda sin asesoría.")
        if acoso:
            st.error("🚫 **ABUSO:** Están violando la Ley 'Dejen de Fregar'.")

    with tab2:
        st.markdown("### 🗣️ Respuestas Legales Inmediatas")
        with st.expander("1. Si exigen pago de deuda vieja (+4 años)"):
            st.info("Diga: 'Solicite el soporte del títulovalor (pagaré) antes de negociar. Me acojo al derecho de inspección.'")
        with st.expander("2. Si llaman en horarios prohibidos"):
            st.info("Diga: 'Está incumpliendo la Ley 2300 de 2023. Procederé a denunciar ante la SIC si persiste.'")

    with tab3:
        st.markdown("### 📝 Datos para la Radicación")
        col_d1, col_d2 = st.columns(2)
        
        with col_d1:
            u_nom = st.text_input("Nombre Completo:").upper()
            u_ced = st.text_input("Número de Cédula de Ciudadanía:")
            u_tel = st.text_input("Teléfono de Contacto:")
        
        with col_d2:
            u_ent = st.text_input("Casa de Cobranza / Entidad:").upper()
            u_cor = st.text_input("Correo Electrónico para notificación:")
            u_dir = st.text_input("Dirección de Residencia (Bogotá):")

        if u_nom and u_ced and u_ent:
            # Cuerpo del documento con todos los datos integrados
            doc = (
                f"Bogotá D.C., {ahora.strftime('%d/%m/%Y')}\n\n"
                f"Señores:\n{u_ent}\nE. S. D.\n\n"
                f"ASUNTO: RECLAMACIÓN DIRECTA - EJERCICIO DERECHO DE HABEAS DATA\n\n"
                f"Yo, {u_nom}, identificado(a) con Cédula de Ciudadanía No. {u_ced}, "
                f"residente en la dirección {u_dir}, con correo electrónico {u_cor} y teléfono {u_tel}; "
                f"amparado en la Ley 1266 de 2008 y la Ley 2157 de 2021 (Borrón y Cuenta Nueva), "
                f"solicito de manera respetuosa la ELIMINACIÓN, CORRECCIÓN O ACTUALIZACIÓN del reporte negativo "
                f"presente en las centrales de riesgo (DataCrédito/Cifín) asociado a su entidad.\n\n"
                f"Lo anterior debido a que la obligación ha cumplido el término de permanencia legal "
                f"o presenta inconsistencias en su reporte.\n\n"
                f"Quedo atento a su respuesta en los términos de ley (15 días hábiles).\n\n"
                f"Cordialmente,\n\n"
                f"{u_nom}\n"
                f"C.C. {u_ced}"
            )
            
            st.text_area("📄 Vista Previa del Documento:", value=doc, height=250)
            
            # Botón de descarga con el nombre del cliente para tu archivo
            st.download_button(
                label="📥 Descargar Petición Lista",
                data=doc,
                file_name=f"Reclamacion_{u_nom.replace(' ', '_')}.txt",
                mime="text/plain"
            )
elif st.session_state.seccion == "TECNICO":
    st.subheader("🔧 Soporte Técnico: Computadores y Electrodomésticos")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        tipo_eq = st.selectbox("Equipo:", ["PC/Portátil", "Nevera", "Lavadora", "Otro"])
        serial = st.text_input("Serial / Modelo:")
    with col_t2:
        falla = st.text_area("Diagnóstico inicial:")
    st.button("Registrar en Base de Datos")

elif st.session_state.seccion == "COTIZADOR":
    st.subheader("💰 Generador de Precios MyM")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        modalidad = st.radio("Lugar del Servicio:", ["En Oficina", "A Domicilio"])
        recargo = 20000 if modalidad == "A Domicilio" else 0
        total = 40000 + recargo
    with col_c2:
        st.metric("Total a Cobrar", f"${total:,} COP")
        st.caption(f"Base Mínima: $40.000 + Domicilio: ${recargo}")

elif st.session_state.seccion == "CITAS":
    st.subheader("📅 Agendamiento MyM")
    ca1, ca2 = st.columns(2)
    with ca1:
        if st.button("📍 CITA EN OFICINA"):
            st.success("✅ Agendado en Oficina. Valor base: $40.000")
    with ca2:
        if st.button("🏠 VISITA DOMICILIARIA"):
            st.warning("✅ Agendada Visita. Valor total: $60.000")

else:
    st.info("Seleccione un servicio arriba para desplegar las herramientas.")

st.divider()
st.caption(f"L.I.N.A. V15.4 | © {ahora.year} Soluciones M&M - Gerardo Martinez Lemus")