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

# Función para convertir imagen a base64
def get_base64_from_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        st.error(f"Error al leer la imagen: {e}")
        return None

# Cargar imagen de fondo
file_path = '/mount/src/modularesbasicas/app/maestros_bg.jpg'
img_base64 = get_base64_from_file(file_path)

if img_base64:
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            opacity: 0.4;
            z-index: 0;
        }}
        [data-testid="stAppViewContainer"] > * {{
            position: relative;
            z-index: 1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Estilos CSS
st.markdown("""
<style>
.profesor-card {
    display: flex;
    flex-direction: row;
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s;
}
.profesor-card:hover {
    transform: translateY(-5px);
}
.profesor-imagen {
    width: 100px;
    height: 100px;
    border-radius: 10px;
    margin-right: 20px;
}
.profesor-info {
    flex: 1;
}
.profesor-nombre {
    font-size: 24px;
    font-weight: bold;
    color: #1e3d59;
    margin-bottom: 5px;
}
.profesor-grado {
    font-size: 16px;
    font-style: italic;
    color: #5e6572;
    margin-bottom: 10px;
}
.profesor-correo {
    font-size: 14px;
    color: #3498db;
    margin-bottom: 10px;
}
.profesor-linea {
    font-size: 15px;
    color: #2c3e50;
    padding: 8px 12px;
    background-color: #e9ecef;
    border-radius: 5px;
    display: inline-block;
    margin-bottom: 5px;
}
.requisitos-container {
    margin-top: 15px;
}
.requisitos-titulo {
    font-size: 16px;
    font-weight: bold;
    color: #1e3d59;
    cursor: pointer;
    background-color: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
}
.requisitos-content {
    display: none;
    margin-top: 10px;
    padding: 10px;
    background-color: #f0f4f8;
    border: 1px solid #d1e6f7;
    border-radius: 5px;
}
.requisitos-container input[type="checkbox"] {
    display: none;
}
.requisitos-container input[type="checkbox"]:checked ~ .requisitos-content {
    display: block;
}
</style>
""", unsafe_allow_html=True)

# Función para mostrar un profesor
def mostrar_profesor(imagen, nombre, puesto, correo, aptitudes, SNI=None, *lineas):
    # Crear un ID único basado en el nombre (sin espacios ni caracteres especiales para HTML)
    profesor_id = "".join(c for c in nombre if c.isalnum()).lower()
    
    lineas_html = ''.join([f'<span class="profesor-linea">📑 {linea}</span><br>' for linea in lineas])
    
    requisitos_html = f"""
    <div class="requisitos-container">
        <label class="requisitos-titulo" for="requisitos-{profesor_id}">Mostrar Requisitos</label>
        <input type="checkbox" id="requisitos-{profesor_id}">
        <div class="requisitos-content">
            <div class="alumno-aptitudes">{aptitudes}
        
    </div>
    """
    sni_html = f"<div class='profesor-sni' style='font-size: 14px; color: #5e6572;'>{SNI}</div>" if SNI else ""
    
    html = f"""
    <div class="profesor-card">
        <img src="data:image/jpeg;base64,{imagen}" class="profesor-imagen">
        <div class="profesor-info">
            <div class="profesor-nombre">{nombre}</div>
            <div class="profesor-grado">{puesto}</div>
            {sni_html}
            <div class="profesor-correo"><a href="mailto:{correo}">{correo}</a></div>
            <div>{lineas_html}</div>
            {requisitos_html}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

st.title("Profesores")
st.header("Licenciatura en Física")

col1, col2 = st.columns(2)

with col1:
    foto_path = '/mount/src/modularesbasicas/app/LQFB/uscanga.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. Néstor García Chan",
            "Profesor Investigador Titular B",
            "nestor.gchan@academicos.udg.mx",
            "EDP, Programación, Métodos Numéricos",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "Modelación matemática y simulación en problemas medioambientales"
        )
