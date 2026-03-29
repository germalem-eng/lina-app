import streamlit as st
import os
import base64
import datetime
import urllib.parse
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="LINA V20.0 | M Y M Soluciones", layout="wide", page_icon="🤖")
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

fondo_b64 = get_image_base64("Logos/fondo.jpg")
logo_robot_b64 = get_image_base64("Logos/logo_robot_2007.jpg")

if 'seccion' not in st.session_state:
    st.session_state.seccion = "PREVENTIVO"

# --- 3. DISEÑO VISUAL (CSS) ---
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

# --- 4. ENCABEZADO ---
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

# --- 5. PANEL DE CONTROL ---
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

    base = 40000
    extra_antivirus = 0
    recargo_domicilio = 20000 if mod == "A Domicilio" else 0
    
    with col_b:
        st.subheader("✅ Checklist Obligatorio")
        st.checkbox("Encendido inicial OK")
        st.checkbox("Limpieza física profunda (Polvo/Componentes)")
        st.checkbox("Borrado de archivos basura / Temporales")
        
        tiene_av = st.radio("¿Tiene Antivirus? (S/N)", ["SÍ", "NO"], horizontal=True)
        if tiene_av == "SÍ":
            st.checkbox("Escaneo Antivirus y Seguridad (Incluido)")
        else:
            instalar_av = st.checkbox("Instalar Antivirus (+ $10.000)")
            if instalar_av:
                extra_antivirus = 10000
        
        st.checkbox("Verificación de puertos y carga")

    st.divider()

    inversion = base + recargo_domicilio + extra_antivirus

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
                msg = f"Hola, soy {nom}. Confirmo cita M.P. el {f_c} a las {h_c}. Dirección: {dir_c}."
                link_wa = generar_enlace_whatsapp("573114759768", msg)
                st.markdown(f'<a href="{link_wa}" target="_blank" class="btn-auto" style="background:#25D366;">📲 Confirmar WhatsApp</a>', unsafe_allow_html=True)

    elif mod == "En Oficina":
        oficina_estado = st.radio("Estado:", ["Evaluación y Ejecución", "Sin equipo (Pasar a Domicilio)"])
        if oficina_estado == "Sin equipo (Pasar a Domicilio)":
            inversion = base + 20000 + extra_antivirus

    st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 15px; border: 3px solid #00FFFF; text-align: center; max-width: 400px; margin: 30px auto;">
        <h4 style="margin:0; color:#444;">Inversión Total del Servicio</h4>
        <h1 style="color: #008fb3; margin: 10px 0;">$ {inversion:,.0f}</h1>
        <p><b>ING. Gerardo Martinez Lemus</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECCIÓN MANTENIMIENTO CORRECTIVO ---
elif st.session_state.seccion == "CORRECTIVO":
    st.header("🔧 Mantenimiento Correctivo y Reparación")
    
    col_diag, col_rep = st.columns(2)
    
    with col_diag:
        st.subheader("🔍 Diagnóstico Técnico")
        tipo_c = st.selectbox("Equipo:", ["PC Mesa", "Portátil", "Todo en Uno", "Tablet", "Electrodoméstico"], key="tc")
        marca_c = st.text_input("Marca:", key="mc")
        falla_cliente = st.text_area("Falla reportada por el usuario:")
        causa = st.selectbox("Causa Probable:", [
            "Falla de Software / S.O.", "Hardware - Disco Duro / SSD", 
            "Hardware - Memoria RAM", "Hardware - Fuente de Poder",
            "Hardware - Pantalla / Video", "Daño por Líquidos / Corto", "Otro"
        ])
        
        foto_dano = st.file_uploader("📸 Subir evidencia del daño:", type=["jpg", "png", "jpeg"])
        if foto_dano:
            st.image(foto_dano, caption="Evidencia cargada", use_container_width=True)

    with col_rep:
        st.subheader("🛠️ Plan de Reparación")
        detalles_tecnicos = st.text_area("¿Qué se encontró y qué se hará?")
        
        repuesto_necesario = st.radio("¿Requiere Repuestos?", ["SÍ", "NO"], horizontal=True, index=1)
        
        # Inicializamos las variables para que no den error NameError
        costo_repuesto = 0
        nombre_repuesto = ""
        
        if repuesto_necesario == "SÍ":
            nombre_repuesto = st.text_input("Nombre del repuesto:")
            costo_base = st.number_input("Costo base del repuesto (Lo que le costó) $:", min_value=0, step=1000)
            
            # --- FÓRMULA SOLICITADA: COSTO + 30% UTILIDAD + 19% IVA ---
            costo_repuesto = (costo_base * 1.30) * 1.19
            
            st.success(f"💰 Precio Final Repuesto: $ {costo_repuesto:,.0f}")
            st.caption("(Incluye 30% de utilidad y 19% de IVA)")
        
        mano_obra = st.number_input("Valor Mano de Obra ($):", min_value=0, step=5000, value=60000)

    st.divider()

    # Ahora la suma siempre funcionará porque costo_repuesto siempre vale algo (0 o el calculado)
    total_reparacion = mano_obra + costo_repuesto
    
    st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 15px; border: 3px solid #FF4B4B; text-align: center; max-width: 450px; margin: auto;">
        <h4 style="margin:0; color:#444;">Presupuesto de Reparación</h4>
        <h1 style="color: #FF4B4B; margin: 10px 0;">$ {total_reparacion:,.0f}</h1>
        <p style="font-size:12px;">Mano de Obra: ${mano_obra:,.0f} | Repuestos: ${costo_repuesto:,.0f}</p>
        <hr>
        <p><b>ING. Gerardo Martinez Lemus</b></p>
    </div>
    """, unsafe_allow_html=True)

    if total_reparacion > 0:
        msg_c = f"Hola, el diagnóstico de su {tipo_c} {marca_c} es: {detalles_tecnicos}. Presupuesto total: ${total_reparacion:,.0f}. ¿Autoriza el proceso?"
        link_rep = generar_enlace_whatsapp("573114759768", msg_c)
        st.markdown(f'<a href="{link_rep}" target="_blank" class="btn-auto" style="background:#25D366; margin-top:20px;">📲 Enviar Presupuesto vía WhatsApp</a>', unsafe_allow_html=True)

# --- 9. SECCIÓN PRIVADO (GESTIÓN DE ABONOS Y UTILIDAD) ---
elif st.session_state.seccion == "PRIVADO":
    st.header("🏠 Gestión Privada de Cuentas")
    st.info("📊 Esta sección es solo para su control interno de gastos y utilidades.")

    col_cta1, col_cta2 = st.columns(2)

    with col_cta1:
        st.subheader("💰 Registro de Abonos")
        cliente_pago = st.text_input("Nombre del Cliente:")
        total_servicio = st.number_input("Total Cobrado al Cliente ($):", min_value=0, step=5000)
        abono_recibido = st.number_input("Monto Recibido (Abono) ($):", min_value=0, step=5000)
        metodo_pago = st.selectbox("Método de Pago:", ["Efectivo", "Nequi", "Daviplata", "Transferencia Bancaria"])

    with col_cta2:
        st.subheader("📉 Control de Costos")
        costo_real_repuesto = st.number_input("Costo Real del Repuesto (Lo que usted pagó) $:", min_value=0, step=1000)
        gastos_extra = st.number_input("Otros Gastos (Pasajes, Envío, etc.) $:", min_value=0, step=500)
        
        # --- CÁLCULO DE SALDOS Y GANANCIA ---
        saldo_pendiente = total_servicio - abono_recibido
        utilidad_neta = total_servicio - costo_real_repuesto - gastos_extra

    st.divider()

    # --- TABLERO DE RESULTADOS PRIVADO ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.metric(label="💵 Saldo por Cobrar", value=f"$ {saldo_pendiente:,.0f}", delta=f"-{saldo_pendiente:,.0f}", delta_color="inverse")
    
    with c2:
        st.metric(label="📈 Utilidad Real (Ganancia)", value=f"$ {utilidad_neta:,.0f}")
        
    with c3:
        # Estado del servicio basado en el pago
        if saldo_pendiente <= 0 and total_servicio > 0:
            st.success("✅ SERVICIO PAGADO TOTALMENTE")
        elif abono_recibido > 0:
            st.warning("⏳ PAGO PARCIAL (ABONADO)")
        else:
            st.error("❌ SIN PAGO REGISTRADO")

    # Botón para guardar en un historial (Simulado por ahora con un log visual)
    if st.button("💾 Registrar Movimiento en Log"):
        st.write(f"📝 **Registro guardado:** Cliente {cliente_pago} | Total: ${total_servicio:,.0f} | Abono: ${abono_recibido:,.0f} | Saldo: ${saldo_pendiente:,.0f}")
        st.balloons()

# --- 10. BARRA FINAL (SIEMPRE VISIBLE) ---
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
st.markdown(f'<p style="text-align:right; font-size:11px; margin-top:10px;">LINA Core V20.0 | © {ahora_bog.year} Gerardo Martinez Lemus</p>', unsafe_allow_html=True)
