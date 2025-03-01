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
            position: absolute;
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

# Texto de la pagina web.
# Aquí va el contenido de tu aplicación
st.title("Mi aplicación con fondo personalizado")
st.write("Este texto aparecerá completamente opaco sobre el fondo semi-transparente")
      

st.markdown("""
    # Lista de profesores
    """
)


#    .sidebar .sidebar-content {{background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})}}
