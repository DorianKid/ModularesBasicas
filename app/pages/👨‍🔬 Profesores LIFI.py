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
/* Tarjeta principal */
.profesor-card {
    display: flex;
    flex-direction: row;
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s;
    align-items: center; /* Centra verticalmente todos los elementos */
}

.profesor-card:hover {
    transform: translateY(-5px);
}

/* Contenedor de imagen centrado verticalmente */
.profesor-imagen {
    width: 100px;
    height: 120px; /* Un poco más alto para fotos de tipo credencial */
    border-radius: 10px;
    margin-right: 20px;
    object-fit: cover; /* Mantiene la proporción de la imagen */
    align-self: center; /* Asegura el centrado vertical */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Sombra sutil */
}

.profesor-info {
    flex: 1;
    align-self: stretch; /* Estira para llenar el espacio vertical */
    display: flex;
    flex-direction: column;
}

.profesor-nombre {
    font-size: 24px;
    font-weight: bold;
    color: #1e3d59;
    margin-bottom: 5px;
}

.profesor-nombre a {
    text-decoration: none;
    color: #1e3d59;
    transition: color 0.3s, text-decoration 0.3s;
}

.profesor-nombre a:hover {
    color: #3498db;
    text-decoration: underline;
    cursor: pointer;
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

/* OPCIÓN 1: Estilo moderno con botón tipo badge */
.requisitos-container {
    margin-top: 15px;
}

.requisitos-titulo {
    display: inline-block;
    font-size: 14px;
    font-weight: 500;
    color: white;
    cursor: pointer;
    background-color: #3498db;
    padding: 7px 15px;
    border-radius: 20px;
    transition: background-color 0.3s;
}

.requisitos-titulo:hover {
    background-color: #2980b9;
}

.requisitos-content {
    display: none;
    margin-top: 12px;
    padding: 15px;
    background-color: #f8f9fa;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border-left: 4px solid #3498db;
    animation: fadeIn 0.3s ease-in-out;
}

/* OPCIÓN 2: Estilo Material Design */
/*
.requisitos-container {
    margin-top: 15px;
}

.requisitos-titulo {
    display: inline-flex;
    align-items: center;
    font-size: 14px;
    font-weight: 500;
    color: #1976d2;
    cursor: pointer;
    background-color: transparent;
    padding: 8px 16px;
    border-radius: 4px;
    transition: background-color 0.3s;
    border: 1px solid #1976d2;
}

.requisitos-titulo:hover {
    background-color: rgba(25, 118, 210, 0.08);
}

.requisitos-titulo::after {
    content: "▼";
    font-size: 10px;
    margin-left: 6px;
}

.requisitos-container input[type="checkbox"]:checked ~ .requisitos-titulo::after {
    content: "▲";
}

.requisitos-content {
    display: none;
    margin-top: 12px;
    padding: 16px;
    background-color: white;
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    animation: slideDown 0.2s ease-out;
}
*/

/* OPCIÓN 3: Estilo Minimalista */
/*
.requisitos-container {
    margin-top: 15px;
}

.requisitos-titulo {
    display: inline-block;
    font-size: 14px;
    color: #555;
    cursor: pointer;
    background-color: transparent;
    padding: 5px 0;
    position: relative;
    border-bottom: 1px dotted #888;
}

.requisitos-titulo:hover {
    color: #000;
}

.requisitos-content {
    display: none;
    margin-top: 10px;
    padding: 15px;
    background-color: #fafafa;
    border-radius: 0;
    border: none;
    border-left: 2px solid #ddd;
}
*/

/* Animación para el contenido */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

.requisitos-container input[type="checkbox"] {
    display: none;
}

.requisitos-container input[type="checkbox"]:checked ~ .requisitos-content {
    display: block;
}

/* Mejora para la visualización de aptitudes */
.alumno-aptitudes {
    line-height: 1.6;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# Función para mostrar un profesor
def mostrar_profesor(imagen, nombre, puesto, correo, aptitudes, SNI=None, enlace=None, *lineas ):
    # Crear un ID único basado en el nombre (sin espacios ni caracteres especiales para HTML)
    profesor_id = "".join(c for c in nombre if c.isalnum()).lower()
    
    lineas_html = ''.join([f'<span class="profesor-linea">📑 {linea}</span><br>' for linea in lineas])
    
    requisitos_html = f"""
    <div class="requisitos-container">
        <label class="requisitos-titulo" for="requisitos-{profesor_id}">Mostrar Requisitos</label>
        <input type="checkbox" id="requisitos-{profesor_id}">
        <div class="requisitos-content">
            <div class="alumno-aptitudes">{aptitudes}
    """
    sni_html = f"<div class='profesor-sni' style='font-size: 14px; color: #5e6572;'>{SNI}</div>" if SNI else ""

    html_nombre = f'<div class="profesor-nombre"><a href="{enlace}" class="profesor-nombre">{nombre}</a></div>' if enlace else f'<div class="profesor-nombre">{nombre}</div>'
    
    html = f"""
    <div class="profesor-card">
        <img src="data:image/jpeg;base64,{imagen}" class="profesor-imagen">
        <div class="profesor-info">
            {html_nombre}
            <div class="profesor-grado">{puesto}</div>
            {sni_html}
            <div class="profesor-correo"><a href="mailto:{correo}">{correo}</a></div>
            <div>{lineas_html}</div>
            {requisitos_html}

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
            "https://academicos.cucei.udg.mx/academicos/2306093",
            "Modelación matemática y simulación en problemas medioambientales"
            )

    foto_path = '/mount/src/modularesbasicas/app/LQFB/uscanga.jpg'
    foto_base64 = get_base64_from_file(foto_path)
    if foto_base64:
        mostrar_profesor(
            foto_base64,
            "Dr. José Guadalupe Quiñones Galván",
            "Profesor Investigador Titular A",
            "jose.quinones@academicos.udg.mx",
            "Electromagnetismo",
            "Miembro del Sistema Nacional de Investigadores Nivel II",
            "https://academicos.cucei.udg.mx/academicos/2955507",
            "Síntesis de materiales por técnicas físicas y químicas"
            )
