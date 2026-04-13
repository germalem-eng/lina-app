import streamlit as st
import os
import base64
import datetime
import tempfile
from streamlit_autorefresh import st_autorefresh
from fpdf import FPDF # Recuerda instalar: pip install fpdf2

# --- 1. CONFIGURACIÓN MECÁNICA DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | Soluciones Tecnológicas M Y M", layout="wide", page_icon="🤖")
st_autorefresh(interval=1000, key="global_refresh")

# Sincronización exacta con Bogotá (UTC-5)
ahora_bog = datetime.datetime.now() - datetime.timedelta(hours=5)

# --- 2. GESTIÓN DE ESTADO ---
if 'seccion' not in st.session_state: 
    st.session_state.seccion = "INICIO"

# --- 3. PROCESAMIENTO DE IMÁGENES (BASE64) ---
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
    .logo-redondo {{
        width: 180px; height: 180px; border-radius: 50%; border: 4px solid #00FFFF;
        box-shadow: 0 0 25px #00FFFF; object-fit: cover;
    }}
    .neon-titulo {{
        font-family: 'Comic Sans MS', cursive; color: #FFFFFF;
        text-shadow: 0 0 15px #00FFFF, 0 0 30px #00FFFF;
        line-height: 1; margin: 0; text-align: center;
    }}
    .alerta-amarilla {{
        background-color: #fff9c4; border: 2px solid #fbc02d; color: #444;
        padding: 15px; border-radius: 10px; margin-top: 20px; margin-bottom: 10px;
        font-size: 15px; text-align: center; font-weight: bold; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .barra-metalica {{
        background: linear-gradient(180deg, #e0e0e0 0%, #b3b3b3 100%);
        border: 2px solid #666; border-radius: 15px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .cuadro-total {{
        background: white; padding: 25px; border-radius: 15px; border: 4px solid #00FFFF;
        text-align: center; max-width: 500px; margin: 20px auto;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. ENCABEZADO ---
col_logo, col_text = st.columns([1, 2.5])
with col_logo:
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{logo_robot_b64}" class="logo-redondo"></div>', unsafe_allow_html=True)
with col_text:
    st.markdown(f"""
    <div style="text-align:center; min-height:200px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 class="neon-titulo" style="font-size:75px;">L.I.N.A.</h1>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:10px;">
            <span style="color:#008fb3; font-weight:bold; font-size:18px;">Laboratorio de Inteligencia y Nuevos Algoritmos</span>
        </div>
        <div style="background:rgba(255,255,255,0.9); padding:8px 15px; border-radius:10px; border:2px solid #00FFFF; margin-top:8px;">
            <span style="color:#444; font-weight:bold; font-size:14px;">Soluciones Tecnológicas M Y M - Desde 2007</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. PANEL DE CONTROL OPERATIVO ---
btns = st.columns(6)
opciones = ["🛠️ PREVENTIVO", "🔧 CORRECTIVO", "⚖️ GESTIÓN", "📝 RADICACIÓN", "🛡️ CASO LEGAL", "🏠 PRIVADO"]
for i, opcion in enumerate(opciones):
    if btns[i].button(opcion, use_container_width=True):
        st.session_state.seccion = opcion.split()[1]
        st.rerun()

st.divider()

# --- 7. MANTENIMIENTO PREVENTIVO (DETALLE TÉCNICO) ---
if st.session_state.seccion == "PREVENTIVO":
    st.header("🛠️ Mantenimiento Preventivo Especializado")
    
    col_info, col_check = st.columns(2)
    
    with col_info:
        st.subheader("📋 Datos del Equipo")
        tipo_equipo = st.selectbox("Tipo de Producto:", ["Computador de Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"], key="prev_tipo")
        marca = st.text_input("Marca del Producto:", key="prev_marca")
        specs = st.text_area("Especificaciones:", key="prev_specs")
        modalidad = st.radio("Modalidad:", ["Virtual", "En Oficina", "A Domicilio"], horizontal=True, key="prev_mod")

    with col_check:
        st.subheader("✅ Checklist")
        st.checkbox("¿Enciende correctamente?", key="chk_1")
        st.checkbox("Limpieza interna", key="chk_2")
        st.checkbox("Software / Temporales", key="chk_3")
        
        st.subheader("🔍 Diagnóstico")
        resultado = st.radio("Estado:", ["Todo está OK", "Requiere Mantenimiento Correctivo"], key="prev_res")
        
        if resultado == "Requiere Mantenimiento Correctivo":
            st.warning("⚠️ Se recomienda pasar a la sección CORRECTIVO para cotizar reparación.")

    # Cálculo Preventivo
    total = 40000 + (20000 if modalidad == "A Domicilio" else 0)
    st.markdown(f'<div class="cuadro-total"><h4>Inversión Preventivo</h4><h1 style="color:#008fb3;">$ {total:,.0f}</h1></div>', unsafe_allow_html=True)

# --- NUEVA SECCIÓN: MANTENIMIENTO CORRECTIVO ---
elif st.session_state.seccion == "CORRECTIVO":
    st.header("🔧 Mantenimiento Correctivo y Reparación")
    
    col_diag, col_cotiza = st.columns(2)
    
    with col_diag:
        st.subheader("🛠️ Informe Técnico de Falla")
        falla_reportada = st.text_area("Descripción de la Falla:", placeholder="Ej: No da video, pantalla azul, bisagras rotas...")
        repuestos = st.text_area("Repuestos Requeridos:", placeholder="Ej: Disco SSD 480GB, Pantalla LED 14'', Teclado...")
        mod_corr = st.radio("Modalidad del Servicio:", ["En Oficina", "A Domicilio"], horizontal=True, key="corr_mod")

    with col_cotiza:
        st.subheader("💰 Cotización de Reparación")
        costo_mano_obra = st.number_input("Valor Mano de Obra ($):", min_value=0, value=60000, step=5000)
        costo_repuestos = st.number_input("Valor Total Repuestos ($):", min_value=0, value=0, step=10000)
        recargo_corr = 20000 if mod_corr == "A Domicilio" else 0
        
        total_correctivo = costo_mano_obra + costo_repuestos + recargo_corr
        
        st.info(f"El valor de los repuestos es un estimado basado en el mercado actual.")

    # Cuadro visual del Correctivo
    st.markdown(f"""
    <div style="background: white; padding: 25px; border-radius: 15px; border: 3px solid #FF4B4B; text-align: center; max-width: 500px; margin: 20px auto; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
        <h4 style="margin:0; color:#444;">Presupuesto de Reparación (Correctivo)</h4>
        <h1 style="color: #FF4B4B; margin: 10px 0;">$ {total_correctivo:,.0f}</h1>
        <div style="border-top: 1px solid #eee; padding-top: 10px; font-size: 14px; color: #666;">
            Mano de Obra: ${costo_mano_obra:,.0f} | Repuestos: ${costo_repuestos:,.0f}
        </div>
        <p style="margin-top:10px; font-size: 13px;"><b>ING. Gerardo Martinez Lemus</b></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📁 Registrar Orden de Reparación"):
        st.success("Orden de mantenimiento correctivo registrada en el sistema L.I.N.A.")
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
