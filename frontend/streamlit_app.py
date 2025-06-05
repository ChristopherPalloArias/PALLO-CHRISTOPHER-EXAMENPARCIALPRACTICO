import streamlit as st
import requests

st.set_page_config(page_title="Clasificador de Mensajes IA", layout="wide")

# =================== CARGAR ESTILOS CSS ===================
def load_css():
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Cargar estilos
load_css()

# =================== CABECERA ===================
st.markdown("<h2 class='main-title'><i class='fas fa-brain'></i> Clasificador Inteligente de Mensajes</h2>",
            unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Clasifica mensajes automáticamente como Urgente, Moderado o Normal usando IA (Gemini)</p>",
    unsafe_allow_html=True)

# =================== VERIFICACIÓN API ===================
try:
    ping = requests.get("http://localhost:8000/")
    if ping.status_code == 200:
        st.success("API conectada")
    else:
        st.error(f"API error: {ping.status_code}")
        st.stop()
except Exception as e:
    st.error(f"Sin conexión API: {e}")
    st.stop()

# =================== INTERFAZ PRINCIPAL ===================
col_izq, col_der = st.columns([1, 2], gap="large")

# ==== Panel izquierdo: información y ejemplos ====
with col_izq:
    st.markdown("<h3 class='section-title'><i class='fas fa-list'></i> Categorías</h3>", unsafe_allow_html=True)
    st.markdown(
        "<div class='category-item'><i class='fas fa-fire icon-urgent'></i> <strong>Urgente</strong>: acción inmediata</div>",
        unsafe_allow_html=True)
    st.markdown(
        "<div class='category-item'><i class='fas fa-clock icon-moderate'></i> <strong>Moderado</strong>: importante</div>",
        unsafe_allow_html=True)
    st.markdown(
        "<div class='category-item'><i class='fas fa-check-circle icon-normal'></i> <strong>Normal</strong>: informativo</div>",
        unsafe_allow_html=True)

    st.markdown("<h3 class='section-title'><i class='fas fa-rocket'></i> Ejemplos rápidos</h3>", unsafe_allow_html=True)

    # Inicializar el estado de la sesión
    if "texto" not in st.session_state:
        st.session_state.texto = ""

    if st.button("Urgente", key="urgente"):
        st.session_state.texto = "¡Hay un incendio en el laboratorio!"
        st.rerun()

    if st.button("Moderado", key="moderado"):
        st.session_state.texto = "He notado que algunos correos no llegan a tiempo. Sería bueno revisarlo en los próximos días."
        st.rerun()

    if st.button("Normal", key="normal"):
        st.session_state.texto = "La reunión será el viernes a las 10h."
        st.rerun()

# ==== Panel derecho: clasificación ====
with col_der:
    st.markdown("<h3 class='section-title'><i class='fas fa-edit'></i> Clasificación</h3>", unsafe_allow_html=True)

    mensaje = st.text_area("Escribe tu mensaje:", value=st.session_state.texto, height=100)

    col1, col2 = st.columns([1, 1])

    with col1:
        clasificar = st.button("Clasificar", key="clasificar")

    with col2:
        limpiar = st.button("Limpiar", key="limpiar")

    # Manejar el botón limpiar
    if limpiar:
        st.session_state.texto = ""
        st.rerun()

    # ==== Resultado ====
    if clasificar and mensaje.strip():
        with st.spinner("Clasificando..."):
            try:
                response = requests.post("http://localhost:8000/clasificar", json={"texto": mensaje})
                if response.status_code == 200:
                    categoria = response.json().get("clasificacion", "").strip()
                    st.markdown("<h4 class='section-title'><i class='fas fa-clipboard-check'></i> Resultado:</h4>",
                                unsafe_allow_html=True)

                    if categoria == "Urgente":
                        st.markdown(
                            '<div class="result-box urgent-box"><h4><i class="fas fa-fire"></i> Urgente</h4></div>',
                            unsafe_allow_html=True)
                    elif categoria == "Moderado":
                        st.markdown(
                            '<div class="result-box moderate-box"><h4><i class="fas fa-clock"></i> Moderado</h4></div>',
                            unsafe_allow_html=True)
                    elif categoria == "Normal":
                        st.markdown(
                            '<div class="result-box normal-box"><h4><i class="fas fa-check-circle"></i> Normal</h4></div>',
                            unsafe_allow_html=True)
                    else:
                        st.info(f"Respuesta inesperada: {categoria}")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"No se pudo conectar con la API: {e}")
    elif clasificar:
        st.warning("Ingresa un mensaje antes de clasificar.")