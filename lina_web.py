import streamlit as st
import datetime
import urllib.parse

# --- CONFIGURACIÓN Y ESTADO ---
st.set_page_config(page_title="LINA V20.0 | Proyecto L.I.N.A.", layout="wide", page_icon="🤖")
ahora = datetime.datetime.now() - datetime.timedelta(hours=5)

if 'seccion' not in st.session_state: st.session_state.seccion = "COTIZADOR"
if 'texto_fijo' not in st.session_state: st.session_state.texto_fijo = ""

# ==========================================
# 📦 CAJA 1: EL COTIZADOR (Público)
# ==========================================
def mostrar_cotizador():
    st.subheader("💰 Cotizador de Servicios M&M")
    col1, col2 = st.columns([2, 1])
    with col1:
        servicio = st.selectbox("Seleccione Servicio:", ["Mantenimiento PC", "Asesoría Legal", "SST"])
        modalidad = st.radio("Modalidad:", ["Virtual", "Presencial"], horizontal=True)
        base = 40000
        st.metric("Inversión Sugerida", f"$ {base:,.0f}".replace(",", "."))
    with col2:
        st.info("Tarifa base por revisión técnica o asesoría inicial.")

# ==========================================
# 📦 CAJA 2: CENTRO JURÍDICO (Defensa)
# ==========================================
def mostrar_radicacion():
    st.subheader("📝 Centro de Defensa Ciudadana")
    
    with st.expander("👤 CONFIGURAR DATOS DEL AFECTADO"):
        u_nombre = st.text_input("Nombre Completo:", placeholder="LINA PAOLA MOJICA").upper() or "LINA PAOLA MOJICA"
        u_cedula = st.text_input("Cédula:", placeholder="1016026492") or "1016026492"
        u_casa = st.text_input("Casa de Cobranza:", placeholder="RECOVERY OF CREDITS").upper() or "RECOVERY OF CREDITS"

    st.markdown("---")
    col_b1, col_b2 = st.columns(2)
    with col_b1: u_banco = st.text_input("Nombre del Banco:", placeholder="Ej: BANCOLOMBIA")
    with col_b2: u_monto = st.text_input("Monto en disputa:", value="$502.837")

    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("🔍 RECLAMO COBRANZA", key="btn_cob_final"):
            st.session_state.texto_fijo = f"RECLAMACIÓN - INCUMPLIMIENTO DE OFERTA\n\nSeñores {u_casa}:\n\n1. Oferta violada.\n2. Mínimo Vital (Sentencia T-012/17).\n\nAtentamente, {u_nombre}"
    with c_btn2:
        if st.button("🏦 RECLAMO BANCARIO", key="btn_ban_final"):
            if u_banco:
                st.session_state.texto_fijo = f"SOLICITUD REVERSIÓN - {u_banco.upper()}\n\nCliente: {u_nombre}\nMonto: {u_monto}\nDerecho: Circular 007 Superfinanciera."

    if st.session_state.texto_fijo:
        st.code(st.session_state.texto_fijo)
        msg_wa = urllib.parse.quote(st.session_state.texto_fijo)
        st.markdown(f'<a href="https://api.whatsapp.com/send?text={msg_wa}" target="_blank" style="background-color:#25D366; color:white; padding:10px; text-decoration:none; border-radius:8px; display:block; text-align:center;">📲 ENVIAR POR WHATSAPP</a>', unsafe_allow_html=True)
    
    if st.button("♻️ LIMPIAR TODO", use_container_width=True):
        st.session_state.texto_fijo = ""
        st.rerun()

# ==========================================
# 📦 CAJA 3: GESTIÓN INTERNA (SST / PRIVADO)
# ==========================================
def mostrar_privado():
    st.subheader("🏠 Área Privada MyM")
    st.write("Control de SST para JP y finanzas internas.")

# --- DISEÑO DE LA PÁGINA (LOGO Y TÍTULO) ---
# (Aquí va tu código de la barra plateada y el título L.I.N.A. que ya tenemos)

# --- PANEL DE CONTROL (EL "CEREBRO") ---
st.write("### 🚀 Panel Operativo:")
c1, c2, c3 = st.columns(3)
with c1: 
    if st.button("💰 COTIZADOR", use_container_width=True): st.session_state.seccion = "COTIZADOR"
with c2: 
    if st.button("⚖️ RADICACIÓN", use_container_width=True): st.session_state.seccion = "RADICACION"
with c3: 
    if st.button("🏠 PRIVADO", use_container_width=True): st.session_state.seccion = "PRIVADO"

st.divider()

# --- AQUÍ OCURRE LA MAGIA: EL SELECTOR DE CAJAS ---
if st.session_state.seccion == "COTIZADOR":
    mostrar_cotizador()
elif st.session_state.seccion == "RADICACION":
    mostrar_radicacion()
elif st.session_state.seccion == "PRIVADO":
    mostrar_privado()
