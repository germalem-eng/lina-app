import streamlit as st
import time

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="L.I.N.A. | Grupo JPL", layout="centered", initial_sidebar_state="collapsed")

# --- 2. ESTILOS CSS (L.I.N.A. STYLE: Vinotinto, Gris, Marca de Agua) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        background-size: 55%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.95); z-index: -1;
    }

    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin: -65px -20px 25px -20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); }
    .card-proceso { background-color: rgba(255, 255, 255, 0.92); padding: 15px; border-radius: 20px; border-left: 10px solid #800000; margin-bottom: 15px; box-shadow: 0px 2px 8px rgba(0,0,0,0.1); }
    .box-amenazas-jpl { background-color: #BEBEBE; padding: 15px; border-radius: 20px; border: 2px solid #800000; margin-bottom: 15px; color: black; }

    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 12px; border: 1px solid #800000; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE NAVEGACIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'

# --- PANTALLA: SPLASH ---
if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=250)
    st.markdown("<h1 style='color:#800000; font-size:60px;'>L.I.N.A.</h1>", unsafe_allow_html=True)
    st.markdown("<p>Legalidad e Innovación en Normativa Aplicada</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    time.sleep(3)
    st.session_state.pantalla = 'inicio'
    st.rerun()

# --- PANTALLA: INICIO ---
elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h2>PROYECTO L.I.N.A.</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-proceso"><h3>SST - Grupo JPL</h3><p>Gestión avanzada de Estándares Mínimos (Res. 0312/2019)</p></div>', unsafe_allow_html=True)
    
    if st.button("🛡️ EVALUACIÓN DE 60 ÍTEMS"):
        st.session_state.pantalla = 'sst'
        st.rerun()
    if st.button("💰 CONSULTAR PLANES"):
        st.session_state.pantalla = 'licencias'
        st.rerun()

# --- PANTALLA: AUDITORÍA ---
elif st.session_state.pantalla == 'sst':
    st.markdown('<div class="top-bar-jpl"><h3>L.I.N.A. | AUDITORÍA</h3></div>', unsafe_allow_html=True)
    
    # Selector de Ciclos para no saturar la pantalla
    ciclo = st.radio("Seleccione el Ciclo a evaluar:", ["PLANEAR", "HACER", "VERIFICAR / ACTUAR"], horizontal=True)

    if ciclo == "PLANEAR":
        st.markdown('<div class="card-proceso"><h4>I. RECURSOS</h4>', unsafe_allow_html=True)
        # Aquí puedes listar los primeros ítems (1-8)
        st.selectbox("1.1.1 Responsable del Sistema", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("1.1.3 Asignación de Recursos", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

    elif ciclo == "HACER":
        st.markdown('<div class="card-proceso"><h4>II y III. SALUD Y RIESGOS</h4>', unsafe_allow_html=True)
        st.selectbox("2.1.1 Descripción Sociodemográfica", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("3.1.1 Identificación de Peligros", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box-amenazas-jpl"><h4>IV. AMENAZAS (Gris Ratón)</h4>', unsafe_allow_html=True)
        st.radio("43. Plan de Emergencias", ["Cumple", "No Cumple"], key="r43")
        st.radio("46. Simulacros", ["Cumple", "No Cumple"], key="r46")
        st.markdown('</div>', unsafe_allow_html=True)

    elif ciclo == "VERIFICAR / ACTUAR":
        st.markdown('<div class="card-proceso"><h4>V-VII. MEJORA CONTINUA</h4>', unsafe_allow_html=True)
        st.selectbox("5.1.1 Auditoría Anual", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("6.1.1 Plan de Mejoramiento", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ VOLVER AL INICIO"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

# --- PANTALLA: LICENCIAS ---
elif st.session_state.pantalla == 'licencias':
    st.markdown('<div class="top-bar-jpl"><h3>PLANES L.I.N.A.</h3></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    p = [("PEQUEÑA", "$40k"), ("MEDIANA", "$60k"), ("GRANDE", "$100k")]
    for i, col in enumerate([c1, c2, c3]):
        with col:
            st.markdown(f'<div class="card-proceso" style="font-size:12px;"><b>{p[i][0]}</b><br>{p[i][1]}</div>', unsafe_allow_html=True)
            st.button("Elegir", key=f"btn_{i}")
    
    if st.button("⬅️ VOLVER"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

# --- BARRA INFERIOR DE NAVEGACIÓN ---
if st.session_state.pantalla != 'splash':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div style="position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; border-top: 2px solid #800000;">', unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        if st.button("🏠"): st.session_state.pantalla = 'inicio'; st.rerun()
    with cols[1]:
        if st.button("🛡️"): st.session_state.pantalla = 'sst'; st.rerun()
    with cols[2]:
        if st.button("📊"): st.info("Próximamente")
    st.markdown('</div>', unsafe_allow_html=True)
