import streamlit as st
import os
import base64
import datetime
import pytz # Agrega esto al inicio de tu archivo (Línea 1 o 2)

# Reemplaza tu línea 60 por esta:
zona_bogota = pytz.timezone('America/Bogota')
ahora = datetime.datetime.now(zona_bogota)
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

# --- 3. BARRA SUPERIOR CON RELOJ SINCRONIZADO ---
# Usamos un componente de Streamlit para capturar la hora del cliente
from streamlit_autorefresh import st_autorefresh

# Actualiza el componente cada 1 segundo (1000 ms)
st_autorefresh(interval=1000, key="daterefresh")

# Ajuste manual para Colombia (UTC-5) si el servidor está en UTC
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

st.html(f"""
<div class="nav-bar-silver">
    <div style="font-family: monospace; font-weight: bold; font-size: 16px;">
        📅 {ahora.strftime('%d/%m/%Y')} | 🕒 {ahora.strftime('%H:%M:%S')}
    </div>
    <div class="social-links">
        <a href="https://web.facebook.com/MyMsolucionesdetecnologia/" target="_blank">FACEBOOK</a>
        <a href="https://wa.me/573114759768?text=Hola%20Gerardo%2C%20necesito%20asesoría" target="_blank">WHATSAPP</a>
        <a href="#">INSTAGRAM</a> <a href="#">TIKTOK</a> <a href="#">YOUTUBE</a>
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
    st.subheader("🛡️ Escudo Anti-Abuso y Liquidación MyM")
    tab1, tab2, tab3 = st.tabs(["🔍 Evaluador y Honorarios", "📞 ¿Qué responder?", "📝 Petición"])

    with tab1:
        st.markdown("### 📊 Diagnóstico y Liquidación de Comisión MyM")
        col_l1, col_l2 = st.columns(2)
        
        with col_l1:
            v_deuda = st.number_input("Valor que exige el cobrador ($):", min_value=0, value=1789977)
            v_capital = st.number_input("Capital original (Meta de pago) ($):", min_value=0, value=700000)
            dias_mora = st.number_input("Días de mora reportados:", min_value=0, value=801)
        
        with col_l2:
            ya_pago = st.checkbox("¿Ya pagó la deuda?")
            acoso = st.checkbox("¿Acoso telefónico? (Ley 2300)")
            
            # Lógica de Estado basada en la mora
            if dias_mora <= 90:
                st.warning("🟡 **ESTADO: COBRANZA ADMINISTRATIVA**")
                st.write("Estrategia: Exija desglose y detenga el reporte con la Ley 1266.")
            elif dias_mora <= 360:
                st.error("🟠 **ESTADO: PRE-JURÍDICO**")
                st.write("Estrategia: Ofrezca el 100% del capital para frenar demanda.")
            else:
                st.error("🔴 **ESTADO: CARTERA CASTIGADA**")
                st.write("Estrategia (Caso Solventa): Negocie solo capital. El riesgo es mínimo.")

        st.divider()
        # --- EL MOTOR DE TU NEGOCIO (EL 10%) ---
        ahorro_real = v_deuda - v_capital
        comision_mym = ahorro_real * 0.10 if ahorro_real > 0 else 0

        c1, c2, c3 = st.columns(3)
        c1.metric("Ahorro del Cliente", f"${ahorro_real:,.0f}")
        c2.metric("Meta de Pago", f"${v_capital:,.0f}")
        c3.metric("Honorarios MyM (10%)", f"${comision_mym:,.0f}", delta="Tu Ganancia")
        
        st.caption("⚠️ Nota: Sus honorarios se basan en el éxito del ahorro conseguido.")
    with tab2:
        st.markdown("### 🗣️ Respuestas Legales Basadas en Normatividad")
        st.info("💡 *Use estas respuestas cuando el cobrador intente presionarlo. Cite las leyes para demostrar conocimiento técnico.*")
        
        # PREGUNTA 1: INTERESES ABUSIVOS
        with st.expander("❓ ¿Por qué el cobro supera el doble del capital inicial?"):
            st.write("""
            **Respuesta Legal:** 'Bajo el **Art. 884 del Código de Comercio**, cualquier cobro que supere la Tasa de Usura es ilegal. Exijo un desglose certificado donde se demuestre que no hay anatocismo (cobro de intereses sobre intereses) y que se respete el tope legal de la Superfinanciera.'
            """)
            st.caption("⚖️ Norma: Código de Comercio Art. 884 / Ley 1266 de 2008.")

        # PREGUNTA 2: NEGOCIACIÓN DE BUENA FE
        with st.expander("❓ ¿Están obligados a aceptarme un acuerdo por el capital base?"):
            st.write("""
            **Respuesta Legal:** 'Según la **Ley 2157 de 2021 (Borrón y Cuenta Nueva)**, las entidades deben facilitar la extinción de deudas en cartera castigada. Dado que el reporte es negativo y afecta mi buen nombre, mi oferta de pago por el capital busca la democratización del crédito que promueve esta ley.'
            """)
            st.caption("⚖️ Norma: Ley 2157 de 2021.")

        # PREGUNTA 3: VERACIDAD DEL DATO (HABEAS DATA)
        with st.expander("❓ ¿Qué pasa si el valor que reportan no coincide con mis cuentas?"):
            st.write("""
            **Respuesta Legal:** 'La **Ley 1266 de 2008** exige que el dato reportado sea VERAZ y EXACTO. Si ustedes no pueden demostrar el origen de cada peso de esos $1.7M, están incurriendo en un reporte ilegal. Solicito la corrección inmediata en centrales de riesgo.'
            """)
            st.caption("⚖️ Norma: Ley 1266 de 2008.")

        # PREGUNTA 4: HORARIOS DE ACOSO (LEY 2300)
        with st.expander("❓ ¿Me pueden llamar un domingo o a las 8:00 PM?"):
            st.write("""
            **Respuesta Legal:** 'Usted está violando la **Ley 2300 de 2023 (Dejen de Fregar)**. Esta ley prohíbe el contacto fuera de horarios hábiles (L-V 7am-7pm, S 8am-3pm) y más de dos veces por semana. Esta llamada está siendo registrada para la queja ante la SIC.'
            """)
            st.caption("⚖️ Norma: Ley 2300 de 2023.")
       
        # CASO REAL: RESPUESTA A SOLVENTA / CARTERA CASTIGADA
        with st.expander("❓ El cobrador (Solventa) dice que 'no es posible' el descuento por capital"):
            st.error("🚨 **ALERTA DE PRESIÓN:** Intentan que pagues intereses inflados de 801 días.")
            st.write("""
            **Respuesta Técnica Sugerida:**
            'Entiendo su posición, pero jurídicamente la obligación tiene **más de 800 días de mora**, lo que la sitúa en **Cartera Castigada**. Bajo la **Ley 2157 de 2021**, las entidades deben facilitar la extinción de deudas para trámites de vivienda. 
            
            Mi oferta de **$700.000** cubre el capital original. Si persisten en el cobro de intereses abusivos sobre una deuda castigada, elevaré una **Queja Formal ante la Superintendencia Financiera** por falta de voluntad de negociación.'
            """)
            st.caption("⚖️ Estrategia: Presión por Trámite de Vivienda y Superfinanciera.")    
    with tab3:
        # --- POLÍTICA DE COBRO MYM ---
           st.info("💡 **Información sobre nuestra Asesoría**")
           st.write("El diagnóstico inicial es **GRATIS** con tus datos básicos.")
    
    with st.expander("🔍 Ver costos de gestión detallada"):
        st.markdown("""
        * **Si NO inicias proceso con nosotros:** El costo de la consulta técnica y legal es de **$40.000**.
        * **Si INICIAS proceso de defensa:** ¡Consulta GRATIS! Solo cobramos el **10%** de lo que logremos ahorrarte al finalizar con éxito.
        """)
        st.markdown("---")
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
            st.markdown("---")
            foto_cedula = st.file_uploader("📂 Adjuntar Foto de Cédula (Opcional)", type=['jpg', 'png', 'pdf'])

        if foto_cedula is not None:
            st.success(f"✅ Archivo '{foto_cedula.name}' cargado con éxito.")
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
                # --- NUEVO: MONITOR DE SEGUIMIENTO LEGAL ---

         # --- BLOQUE DE HONORARIOS Y CONDICIONES ---
    st.markdown("---")
    st.warning("""
⚠️ **Nota de Honorarios:** Nuestros honorarios se basan estrictamente en el éxito del ahorro conseguido. 
Se estipula un cobro del **10% sobre el valor real ahorrado** por el cliente. 
*Si no hay ahorro, ¡no pagas honorarios de éxito!* (Consulta técnica independiente: $40.000).
""")
    col_h1, col_h2 = st.columns(2)
    
    with col_h1:
        st.write("📈 **VALOR DEL SERVICIO:**")
        st.title("10%")
        st.caption("Del valor total ahorrado")

    with col_h2:
        st.write("📑 **CONDICIÓN:**")
        st.write("* Solo se cobra si el proceso es exitoso.")
        st.write("* Si prefieres no iniciar proceso de defensa, el diagnóstico tiene un costo de **$40.000**.")

        st.info("💡 *Al descargar o usar este documento, aceptas que MyM Soluciones gestione tu caso bajo estas condiciones.*")
        st.markdown("---")       
        st.markdown("---")
        st.subheader("📅 Monitor de Respuesta (Silencio Administrativo)")
            
            # Calendario para marcar el día que se envió el correo o radicó
        fecha_radicado = st.date_input("¿Qué día radicó esta petición?", value=ahora)
            
            # Calculamos 15 días hábiles (aprox. 21 días calendario)
        fecha_vencimiento = fecha_radicado + datetime.timedelta(days=21) 
            
            # Diferencia contra el día de hoy
        dias_restantes = (fecha_vencimiento - ahora.date()).days

        if dias_restantes > 0:
                st.warning(f"⏳ Faltan **{dias_restantes}** días para que se cumpla el término legal.")
                st.info(f"📅 Fecha estimada de respuesta: **{fecha_vencimiento.strftime('%d/%m/%Y')}**")
        else:
                st.error("🚨 **¡PLAZO VENCIDO!** Si no hay respuesta, puedes solicitar el Silencio Administrativo Positivo.")
                         
            
            
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