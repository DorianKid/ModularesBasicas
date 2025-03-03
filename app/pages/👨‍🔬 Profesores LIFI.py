import streamlit as st
import base64

st.set_page_config(
    page_title="Profesores LIFI",
    page_icon=":telescope:",
    layout="wide",    
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

############################ BACKGROUND ##############################################
# Definir una función para cargar la imagen como base64
def get_base64_from_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        st.error(f"Error al leer la imagen: {e}")
        return None

# Intentar encontrar la imagen relativa al directorio del script
file_path = '/mount/src/modularesbasicas/app/maestros_bg.jpg'
# Obtener la imagen en base64
img_base64 = get_base64_from_file(file_path)

# Estilo del fondo
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        opacity: 0.4;
        z-index: -1;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

################################# Estilos CSS ################################
st.markdown("""
<style>
/* Estilo de las tarjetas de profesor */
.profesor-card {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.profesor-imagen {
    width: 120px;
    height: 120px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.profesor-nombre {
    font-size: 20px;
    font-weight: bold;
    color: #1e3d59;
    margin-bottom: 5px;
}
.profesor-grado {
    font-size: 16px;
    color: #5e6572;
    margin-bottom: 10px;
}
.profesor-correo a {
    font-size: 14px;
    color: #3498db;
    text-decoration: none;
}
.profesor-correo a:hover {
    text-decoration: underline;
}
.profesor-linea {
    font-size: 14px;
    color: #2c3e50;
    background-color: #f0f4f8;
    padding: 5px 10px;
    border-radius: 5px;
    display: inline-block;
    margin-top: 10px;
}
.requisitos-container {
    margin-top: 15px;
    font-size: 14px;
    color: #34495e;
    background-color: #dff9fb;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# Función para crear la tarjeta de un profesor
def mostrar_profesor(imagen, nombre, puesto, correo, aptitudes, SNI=None, *lineas):
    # Crear HTML para líneas de investigación
    lineas_html = ''.join([f'<div class="profesor-linea">📑 {linea}</div>' for linea in lineas])

    # HTML para requisitos
    requisitos_html = f"""
    <div class="requisitos-container">
        {aptitudes}
    </div>
    """

    # HTML para el SNI si está disponible
    sni_html = f"""
    <div class="profesor-grado">{SNI}</div>
    """ if SNI else ""

    # Construir la tarjeta del profesor
    html = f"""
    <div class="profesor-card">
        <img src="data:image/jpeg;base64,{imagen}" class="profesor-imagen">
        <div class="profesor-nombre">{nombre}</div>
        <div class="profesor-grado">{puesto}</div>
        {sni_html}
        <div class="profesor-correo"><a href="mailto:{correo}">{correo}</a></div>
        {lineas_html}
        {requisitos_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

#########################################################
st.title("Profesores")
st.header("Licenciatura en Física")

col1, col2 = st.columns(2)

###################### Columna 1 ###################################
with col1:
    foto_path = '/mount/src/modularesbasicas/app/LQFB/uscanga.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    mostrar_profesor(
        foto_base64,
        "Dr. Néstor García Chan",
        "Profesor Investigador Titular B",
        "nestor.gchan@academicos.udg.mx",
        "EDP, Programación, Métodos Numéricos",
        "Miembro del Sistema Nacional de Investigadores Nivel II",
        "Modelación matemática y simulación en problemas medioambientales"
    )
