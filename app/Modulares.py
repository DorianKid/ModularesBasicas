import streamlit as st
import base64
from pathlib import Path
import os

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
file_path = Path(__file__).parent / "maestros.jpg"

# Si no se encuentra, buscar relativo al directorio de trabajo actual
if not file_path.exists():
    file_path = Path.cwd() / "maestros.jpg"

# Obtener la imagen en base64
img_base64 = get_base64_from_file(file_path)

if img_base64:
    # Aplicar el fondo
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            
            /* Controla el tamaño de la imagen */
            background-size: 50% auto;  /* Ancho: 50%, Alto: automático */
            
            /* Controla la posición de la imagen */
            background-position: center;  /* Hay top right, center, top left, bottom right, bottom, etc  */
            
            /* Controla si la imagen se repite */
            background-repeat: repeat;
            
            /* Controla si la imagen se desplaza con el contenido */
            background-attachment: fixed;

            /* Posicionamiento absoluto para cubrir todo el contenedor */
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            
            /* Control de opacidad - ajusta el valor entre 0.0 y 1.0 */
            opacity: 0.5;  /* De 0 a 1 siendo % de opacidad */
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("No se pudo cargar la imagen de fondo.")

# Texto de la pagina web.

st.markdown("""
    # Lista de profesores
    """
)


#    .sidebar .sidebar-content {{background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})}}
