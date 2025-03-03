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
    font-size: 14px; /* Ajustar tamaño de fuente */
    color: #3498db;
    margin-bottom: 10px;
    transition: color 0.2s; /* Agregar transición */
}

.profesor-correo:hover {
    color: #2980b9; /* Color al pasar el mouse */
}

.profesor-linea {
    font-size: 15px;
    color: #2c3e50;
    padding: 8px 12px;
    background-color: #e9ecef;
    border-radius: 5px;
    display: inline-block;
    transition: transform 0.2s; /* Agregar transición */
}

.profesor-linea:hover {
    transform: scale(1.05); /* Efecto de hover */
}

.alumno-aptitudes {
    font-size: 16px; /* Aumento del tamaño de fuente para mejor legibilidad */
    color: #34495e; /* Color de texto más oscuro para un contraste mejorado */
    padding: 10px 15px; /* Espaciado interno ajustado */
    background-color: #dff9fb; /* Color de fondo suave para resaltar */
    border: 1px solid #aed6f1; /* Borde sutil para definir el área */
    border-radius: 8px; /* Bordes más redondeados */
    display: inline-block; /* Mantiene la alineación en línea */
    margin-bottom: 10px; /* Espacio entre las aptitudes */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra sutil para profundidad */
    transition: transform 0.2s; /* Transición suave al pasar el mouse */
}

.requisitos-container {
    margin-top: 15px; /* Espacio superior */
}

.requisitos-titulo {
    font-size: 18px; /* Tamaño del título */
    color: #1e3d59; /* Color del título */
    cursor: pointer; /* Cambia el cursor al pasar sobre el título */
    transition: color 0.2s; /* Transición de color */
}

.requisitos-titulo:hover {
    color: #3498db; /* Color al pasar el mouse */
}

.requisitos-content {
    display: none; /* Oculta el contenido inicialmente */
    margin-top: 10px; /* Espacio superior para el contenido */
    padding: 10px;
    background-color: #f0f4f8; /* Color de fondo del contenido */
    border: 1px solid #d1e6f7; /* Borde del contenido */
    border-radius: 5px; /* Bordes redondeados */
}
</style>
""", unsafe_allow_html=True)

# Función para crear la tarjeta de un profesor
def mostrar_profesor(imagen, nombre, puesto, correo, aptitudes=None, SNI=None, *lineas):
    # Generar un ID único para cada profesor (para que el JavaScript funcione con múltiples profesores)
    import random
    profesor_id = f"profesor_{random.randint(10000, 99999)}"
    
    # Crear spans para cada línea
    lineas_html = ''.join([f'<span class="profesor-linea">📑 {linea}</span><br>' for linea in lineas])
    
    # HTML para el SNI si está disponible
    sni_html = f"""
    <div class="profesor-sni" style="font-size: 14px; color: #5e6572;">
        {SNI}
    </div>
    """ if SNI else ""
    
    # HTML para los requisitos desplegables si existen
    aptitudes_html = f"""
    <div class="requisitos-container">
        <button id="btn_{profesor_id}" class="requisitos-btn" onclick="toggleRequisitos('{profesor_id}')">Mostrar requisitos</button>
        <div id="req_{profesor_id}" class="requisitos-content" style="display: none;">
            <div class="profesor-aptitudes">
                <div class="alumno-aptitudes">{aptitudes}</div>
            </div>
        </div>
    </div>
    """ if aptitudes else ""
    
    # JavaScript para alternar la visibilidad de los requisitos
    js_code = f"""
    <script>
    function toggleRequisitos(id) {{
        var content = document.getElementById("req_" + id);
        var btn = document.getElementById("btn_" + id);
        
        if (content.style.display === "none") {{
            content.style.display = "block";
            btn.textContent = "Ocultar requisitos";
        }} else {{
            content.style.display = "none";
            btn.textContent = "Mostrar requisitos";
        }}
    }}
    </script>
    """
    
    # CSS para estilizar el botón y contenido de requisitos
    css = """
    <style>
    .requisitos-btn {
        background-color: #4CAF50;
        color: white;
        padding: 8px 15px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-top: 10px;
        font-size: 14px;
    }
    
    .requisitos-btn:hover {
        background-color: #45a049;
    }
    
    .requisitos-content {
        margin-top: 10px;
        padding: 10px;
        background-color: #f8f9fa;
        border-radius: 4px;
        border-left: 3px solid #4CAF50;
    }
    </style>
    """
    
    # Mostrar información del profesor con Markdown, incluyendo el botón desplegable
    st.markdown(f"""
    {css}
    {js_code}
    <div class="profesor-card">
        <img src="data:image/jpeg;base64,{imagen}" class="profesor-imagen">
        <div class="profesor-info">
            <div class="profesor-nombre">{nombre}</div>
            <div class="profesor-grado">{puesto}</div>
            {sni_html}  <!-- Mostrar SNI si existe -->
            <div class="profesor-correo"><a href="mailto:{correo}">{correo}</a></div>
            <div>
                {lineas_html}
            </div>
            {aptitudes_html}  <!-- Mostrar requisitos desplegables si existen -->
        </div>
    </div>
    """, unsafe_allow_html=True)#########################################################
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
        "nestor.gchan@academicos.udg.mx",  # Correo
        "EDP, Programación, Métodos Numéricos",  # Aptitudes
        "Miembro del Sistema Nacional de Investigadores Nivel II",  # SNI
        "Modelación matemática y simulación en problemas medioambientales"  # Líneas adicionales
    )

######################### Columna 2 #################################


#    .sidebar .sidebar-content {{background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})}} para el sidebar
