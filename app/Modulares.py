import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Modulares",
    page_icon=":microscope:",
    layout="wide",    
    initial_sidebar_state="expanded",
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
file_path = Path(__file__).parent / "maestros_bg.jpg"

# Obtener la imagen en base64
img_base64 = get_base64_from_file(file_path)

if img_base64:
    # Aplicar un pseudo-elemento para el fondo
    st.markdown(
        f"""
        <style>
        /* Crear un pseudo-elemento para el fondo */
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: 50% auto;
            background-position: center; /* Hay top right, center, top left, bottom right, bottom, etc  */
            background-repeat: repeat;
            background-attachment: fixed;
            
            /* Posicionamiento para cubrir todo */
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            opacity: 0.5;  /* De 0 a 1 siendo % de opacidad */ 
            z-index: 0;  /* Coloca el fondo detrás del contenido */
        }}
        
        /* Asegura que el contenedor principal tenga posición relativa */
        [data-testid="stAppViewContainer"] {{
            position: relative;
            overflow: auto !important;
            height: 100vh;
        }}
        
        /* Asegura que el texto tenga la opacidad completa */
        [data-testid="stAppViewContainer"] > * {{
            opacity: 1 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
)
else:
    st.warning("No se pudo cargar la imagen de fondo.")

################################# Estilos CSS ################################
# Estilo para las tarjeta de profesores
st.markdown("""
<style>
.profesor-card {
    display: flex;
    flex-direction: row; /* Cambiar a columna en móviles */
    background-color: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.profesor-imagen {
    width: 100px; /* Reducir tamaño para móviles */
    height: 100px;
    border-radius: 10px;
    margin-right: 20px;
}

@media (max-width: 768px) {
    .profesor-card {
        flex-direction: column; /* Cambiar a columna en móviles */
        align-items: center; /* Centrar contenido */
    }

    .profesor-imagen {
        margin-right: 0; /* Eliminar margen en móviles */
        margin-bottom: 10px; /* Espacio entre imagen y texto */
    }
    
    .profesor-nombre {
        font-size: 20px; /* Ajustar tamaño de fuente */
    }

    .profesor-grado {
        font-size: 14px; /* Ajustar tamaño de fuente */
    }

    .profesor-correo {
        font-size: 12px; /* Ajustar tamaño de fuente */
    }

    .profesor-linea {
        font-size: 15px;
        color: #2c3e50;
        padding: 8px 12px;
        background-color: #e9ecef;
        border-radius: 5px;
        display: inline-block;
    }
}
</style>
""", unsafe_allow_html=True)

# Función para crear la tarjeta de un profesor
def mostrar_profesor(imagen, nombre, puesto, correo, *lineas):
    # Crear spans para cada línea
    lineas_html = ''.join([f'<span class="profesor-linea">📑 {linea}</span><br>' for linea in lineas])
    
    html = f"""
    <div class="profesor-card">
        <img src="data:image/jpeg;base64,{imagen}" class="profesor-imagen">
        <div class="profesor-info">
            <div class="profesor-nombre">{nombre}</div>
            <div class="profesor-grado">{puesto}</div>
            <div class="profesor-correo"><a href="mailto:{correo}">{correo}</a></div>
            <div>
                {lineas_html}
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Texto de la pagina web.
st.title("Profesores para modulares")
st.header("Licenciatura en Químico Farmacéutico Biólogo")


col1, col2 = st.columns(2)

###################### Columna 1 ###################################
with col1:
    foto_path = Path(__file__).parent / "Fotos_QFB" / "uscanga.jpg"
    foto_base64 = get_base64_from_file(foto_path)
    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

######################### Columna 2 #################################

with col2:
    foto_path = Path(__file__).parent / "Fotos_QFB" / "uscanga.jpg"
    foto_base64 = get_base64_from_file(foto_path)
    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")

    mostrar_profesor(
        foto_base64,
        "Dra. Aguilar Uscanga Blanca Rosa",
        "Profesor Investigador Titular B",
        "blanca.aguilar@academicos.udg.mx",
        "Fenómenos Químicos AHDV",
        "Ayuda Comunitaria",
        "Microbiologia Industrial")


#    .sidebar .sidebar-content {{background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})}}
