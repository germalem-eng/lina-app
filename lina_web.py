import streamlit as st
import os
import base64
import datetime
import urllib.parse
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | M Y M Soluciones", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")
# Ajuste de hora para Bogotá (UTC-5)
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

# Carga de recursos visuales
fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

if 'seccion' not in st.session_state:
    st.session_state.seccion = "PREVENTIVO"

# --- 3. DISEÑO VISUAL (CSS) ---
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                          url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover; background-attachment: fixed;
    }}
    .logo-redondo {{ width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF; box-shadow: 0 0 25px #00FFFF; object-fit: cover; }}
    .neon-titulo {{ font-family: 'Comic Sans MS', cursive; color: #FFFFFF; text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF; text-align: center; margin: 0; }}
    .alerta-amarilla {{ background-color: #fff9c4; border: 2px solid #fbc02d; color: #444; padding: 15px; border-radius: 10px; margin-top: 20px; font-weight: bold; text-align: center; }}
    .barra-metalica {{ background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%); border: 2px solid #666; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
    .reloj-bogota {{ font-family: 'Courier New', monospace; font-weight: bold; color: #111; display: flex; justify-content: space-between; border-bottom: 2px solid #888; padding-bottom: 8px; margin-bottom: 12px; }}
    .btn-auto {{ text-decoration: none; color: white !important; padding: 12px; border-radius: 10px; text-align: center; font-weight: bold; display: block; margin-top: 10px; }}
    .boton-social {{ text-decoration: none !important; color: #333 !important; background: white; padding: 6px 10px; border-radius: 8px; font-weight: bold; font-size: 11px; border: 1px solid #999; display: inline-block; margin: 2px; }}
    .cuadro-inversion {{ background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 450px; margin: 20px auto; }}
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
        </div><br>
        <div style="background:rgba(255,255,255,0.9); padding:5px 15px; border-radius:10px; border:1px solid #00FFFF; display:inline-block; margin-top:5px;">
            <span style="color:#444; font-weight:bold; font-size:14px;">Soluciones Tecnológicas M Y M - Desde 2007</span>
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

# --- 6. SECCIÓN MANTENIMIENTO PREVENTIVO ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📋 Datos del Equipo")
        tipo = st.selectbox("Producto:", ["PC Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"])
        marca = st.text_input("Marca del Producto:")
        specs = st.text_area("Características / Especificaciones:")
        mod = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True)
        nom = st.text_input("Nombre del Cliente:")
        tel = st.text_input("Teléfono (WhatsApp):")
    
    with col_b:
        st.subheader("✅ Checklist Obligatorio")
        st.checkbox("Encendido inicial OK")
        st.checkbox("Limpieza física profunda (Polvo/Componentes)")
        st.checkbox("Borrado de archivos basura / Temporales")
        
        tiene_av = st.radio("¿Tiene Antivirus? (S/N)", ["SÍ", "NO"], horizontal=True)
        extra_av = 0
        if tiene_av == "NO":
            instalar_av = st.checkbox("Instalar Antivirus Pro (+ $10.000)")
            if instalar_av:
                extra_av = 10000
        else:
            st.checkbox("Escaneo Antivirus y Seguridad (Incluido)")
        
        st.checkbox("Verificación de puertos y carga")

    base = 40000
    recargo_dom = 20000 if mod == "A Domicilio" else 0
    total_prev = base + extra_av + recargo_dom

    if mod == "Virtual":
        st.info("💻 **Asesoría Virtual**")
        toma_servicio = st.radio("¿Toma servicio técnico?", ["No (Solo asesoría)", "Sí (Agendar Cita)"])
        if toma_servicio == "Sí (Agendar Cita)":
            total_prev = 0 # Solo agenda
    
    st.markdown(f"""<div class="cuadro-inversion"><h4>Inversión Total del Servicio</h4><h1 style="color:#008fb3;">$ {total_prev:,.0f}</h1><p><b>ING. Gerardo Martinez Lemus</b></p></div>""", unsafe_allow_html=True)
    
    if st.button("📅 Agendar y Enviar a WhatsApp"):
        msg_p = f"Hola, confirmo preventivo para {tipo} {marca} ({mod}). Valor: ${total_prev:,.0f}."
        st.markdown(f'<a href="{generar_enlace_whatsapp("573114759768", msg_p)}" target="_blank" class="btn-auto" style="background:#25D366;">📲 Confirmar por WhatsApp</a>', unsafe_allow_html=True)

# --- 7. SECCIÓN MANTENIMIENTO CORRECTIVO ---
elif st.session_state.seccion == "CORRECTIVO":
    st.header("🔧 Mantenimiento Correctivo y Reparación")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("🔍 Diagnóstico")
        tipo_c = st.selectbox("Equipo:", ["PC Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"], key="tc")
        marca_c = st.text_input("Marca:", key="mc")
        falla = st.text_area("Falla reportada por el usuario:")
        causa = st.selectbox("Causa Probable:", ["Software", "Disco Duro/SSD", "RAM", "Fuente", "Pantalla", "Líquidos", "Otro"])
        
        costo_base_rep = st.number_input("Costo Base Repuesto (Su costo) $:", min_value=0, step=1000)
        # FÓRMULA SOLICITADA: (Costo * 1.30) * 1.19
        precio_final_rep = (costo_base_rep * 1.30) * 1.19
        st.info(f"💰 Precio Final Repuesto (Utilidad + IVA): $ {precio_final_rep:,.0f}")

    with col_c2:
        st.subheader("🛠️ Plan de Acción")
        detalles_tecnicos = st.text_area("Hallazgos técnicos:")
        mano_obra = st.number_input("Mano de Obra ($):", min_value=0, value=60000, step=5000)
        foto = st.file_uploader("📸 Evidencia del daño:", type=["jpg", "png", "jpeg"])
        if foto:
            st.image(foto, use_container_width=True)

    total_corr = mano_obra + precio_final_rep
    st.markdown(f"""<div class="cuadro-inversion" style="border-color:#FF4B4B;"><h4>Presupuesto de Reparación</h4><h1 style="color:#FF4B4B;">$ {total_corr:,.0f}</h1><p>Mano de Obra: ${mano_obra:,.0f} | Repuestos: ${precio_final_rep:,.0f}</p></div>""", unsafe_allow_html=True)

    if st.button("📲 Enviar Presupuesto"):
        msg_c = f"Hola, diagnóstico de su {tipo_c} {marca_c}: {detalles_tecnicos}. Total: ${total_corr:,.0f}."
        st.markdown(f'<a href="{generar_enlace_whatsapp("573114759768", msg_c)}" target="_blank" class="btn-auto" style="background:#25D366;">📲 WhatsApp Presupuesto</a>', unsafe_allow_html=True)

# --- 8. SECCIÓN GESTIÓN (CARTERA Y DEFENSA) ---
elif st.session_state.seccion == "GESTIÓN":
    st.header("⚖️ Gestión de Cartera y Defensa del Consumidor")
    st.warning("🛡️ Protocolos basados en Ley 2300/23, Ley 1266/08, Ley 2157/21 y Estatuto del Consumidor.")
    
    tabs = st.tabs(["📊 Liquidación", "🛡️ Habeas Data", "📚 Normativa"])
    
    with tabs[0]:
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.subheader("📋 Datos del Caso")
            nom_g = st.text_input("Nombre del Cliente:", key="nom_g")
            tel_g = st.text_input("WhatsApp Cliente:", key="tel_g")
            entidad_g = st.text_input("Entidad (Ej: ASLEGAL):")
            monto_deuda = st.number_input("Monto que reclaman ($):", value=1851000)
            capital_real = st.number_input("Capital Real Adeudado ($):", value=150000)
        
        with col_g2:
            st.subheader("📍 Configuración")
            tipo_g = st.radio("Tipo de Cobro:", ["Solo Consulta ($40.000)", "Gestión Integral (10% del Ahorro)"])
            mod_g = st.radio("Modalidad:", ["Virtual", "Oficina", "Domicilio"], horizontal=True, key="mod_g")
            
        ahorro = monto_deuda - capital_real
        hon_base = 40000 if "Solo Consulta" in tipo_g else (ahorro * 0.10)
        total_g = hon_base + (20000 if mod_g == "Domicilio" else 0)
        
        st.markdown(f"""<div class="cuadro-inversion" style="border-color:#008fb3;"><h4>Propuesta de Gestión M Y M</h4><h1 style="color:#008fb3;">$ {total_g:,.0f}</h1><p>Ahorro estimado para cliente: ${ahorro:,.0f}</p></div>""", unsafe_allow_html=True)
        
        if st.button("📲 Enviar Cotización"):
            msg_g = f"Hola {nom_g}, presupuesto para gestión ante {entidad_g}: ${total_g:,.0f}."
            st.markdown(f'<a href="{generar_enlace_whatsapp("573114759768", msg_g)}" target="_blank" class="btn-auto" style="background:#25D366;">📲 Enviar por WhatsApp</a>', unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("🚫 Radicación de Reclamación Formal")
        texto_h = f"""YO, {nom_g.upper() if nom_g else 'EL CLIENTE'}, IDENTIFICADO CON LA CC 79951815, EXIJO A {entidad_g.upper() if entidad_g else 'LA ENTIDAD'} LA ELIMINACIÓN DEL REPORTE NEGATIVO POR PRESCRIPCIÓN (MORA SUPERIOR A 7 AÑOS - LEY 2157/21). REVOCATORIA DE DÉBITO AUTOMÁTICO LEY 1581."""
        st.text_area("📄 Texto para Radicación:", texto_h, height=200)
        if st.button("📲 Enviar Reclamación Directa"):
            st.markdown(f'<a href="{generar_enlace_whatsapp("", texto_h)}" target="_blank" class="btn-auto" style="background:#25D366;">📲 Enviar por WhatsApp</a>', unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("📚 Sustento Legal")
        st.markdown("""
        * **Ley 2300/23:** Dejen de fregar (Horarios de cobro y canales).
        * **Ley 2157/21:** Borrón y cuenta nueva (Caducidad del dato).
        * **Ley 1266/08:** Habeas Data financiero.
        * **Art. 305 CP:** Delito de Usura (Intereses por encima del tope legal).
        """)

# --- 9. SECCIÓN PRIVADO ---
elif st.session_state.seccion == "PRIVADO":
    st.header("🏠 Gestión Privada de Cuentas")
    st.info("📊 Control interno de utilidades y saldos.")
    pin = st.text_input("Introduzca PIN de Seguridad:", type="password")
    if pin == "2007":
        st.success("Acceso Autorizado")
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.subheader("💰 Ingresos")
            cliente_p = st.text_input("Nombre del Cliente:")
            cobrado = st.number_input("Total Cobrado al Cliente ($):", min_value=0)
            abono = st.number_input("Abono Recibido ($):", min_value=0)
            metodo = st.selectbox("Método:", ["Efectivo", "Nequi", "Daviplata", "Transferencia"])
        with col_v2:
            st.subheader("📉 Egresos")
            costo_r = st.number_input("Costo Real Repuesto (Su costo) $:", min_value=0)
            gastos = st.number_input("Otros Gastos (Pasajes/Envío) $:", min_value=0)
        
        utilidad = cobrado - costo_r - gastos
        saldo_p = cobrado - abono
        
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("📈 Utilidad Real", f"$ {utilidad:,.0f}")
        c2.metric("💵 Saldo Pendiente", f"$ {saldo_p:,.0f}", delta=f"-{saldo_p:,.0f}", delta_color="inverse")
        with c3:
            if saldo_p <= 0 and cobrado > 0: st.success("✅ PAGADO")
            elif abono > 0: st.warning("⏳ ABONADO")
            else: st.error("❌ PENDIENTE")
            
        if st.button("💾 Registrar en Log"):
            st.write(f"📝 **Registro:** {cliente_p} | Utilidad: ${utilidad:,.0f} | Saldo: ${saldo_p:,.0f}")
            st.balloons()
            
    elif pin != "":
        st.error("PIN Incorrecto")

# --- 10. BARRA FINAL (RELOJ Y REDES) ---
st.divider()
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
            <a href="https://youtube.com" target="_blank" class="boton-social">🔴 YouTube</a>
            <a href="https://tiktok.com" target="_blank" class="boton-social">🎵 TikTok</a>
            <a href="https://x.com" target="_blank" class="boton-social">⚫ X</a>
        </div>
    </div>
</div>
"""
st.markdown(html_barra, unsafe_allow_html=True)
st.markdown(f'<p style="text-align:right; font-size:11px; margin-top:10px;">LINA Core V20.0 | © {ahora_bog.year} Gerardo Martinez Lemus</p>', unsafe_allow_html=True)
