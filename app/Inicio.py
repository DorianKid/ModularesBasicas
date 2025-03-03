import streamlit as st
import base64
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(
    page_title="Modulares",
    page_icon=":pencil:",
    layout="wide",    
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

# Título principal con icono
st.title("📚 Proyectos Modulares: Evaluación Integral en CUCEI")

# Sección: ¿Qué son los modulares?
st.header("🔍 ¿Qué son los modulares?")
# Descripción inicial
st.markdown("""
Los **Proyectos Modulares** son una estrategia educativa clave en el modelo académico del 
Centro Universitario de Ciencias Exactas e Ingenierías (**CUCEI**) de la **Universidad de Guadalajara**. Estos proyectos constituyen un **sistema de evaluación integral** que permite a los estudiantes demostrar la adquisición y aplicación de competencias específicas en diversas etapas de su formación profesional.

Son actividades académicas estructuradas que evalúan la integración de **conocimientos, habilidades y actitudes** adquiridas durante un período determinado. Más que simples trabajos finales, representan **evidencias concretas** del desarrollo de competencias profesionales y metodológicas necesarias para el ejercicio de su profesión.
""")

# Importancia educativa con resaltado
st.success("📢 **Importancia Educativa:** Los Proyectos Modulares desempeñan un papel crucial en la formación académica, asegurando que los estudiantes adquieran competencias aplicables al mundo real.")

st.divider()

# Características comunes con diseño de columnas
st.header("📌 Características")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Enfoque progresivo")
    st.markdown("""
    - Se organizan en **niveles de complejidad creciente** a lo largo de la formación.
    - Integran **conocimientos de diversas asignaturas**.
    - Se enfocan en la **resolución de problemas reales o simulados** del ámbito profesional.
    """)

with col2:
    st.subheader("🔬 Desarrollo metodológico")
    st.markdown("""
    - Aplicación de **métodos científicos y técnicas específicas** según la disciplina.
    - **Evaluación integral**: se consideran proceso, metodología y competencias adquiridas.
    - **Asesoría especializada** por parte de profesores.
    """)

st.divider()

# Modalidades de presentación con diseño en columnas
st.header("📑 Modalidades de Presentación")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - 🗣️ **Presentaciones orales**: Exposiciones formales ante comités evaluadores.
    - 📊 **Pósters científicos**: Presentaciones visuales del trabajo realizado.
    - 🔧 **Prototipos**: Desarrollo de modelos físicos o funcionales.
    """)

with col2:
    st.markdown("""
    - 📋 **Reportes técnicos**: Documentos detallados del proceso y resultados.
    - 📄 **Artículos científicos**: Trabajos estructurados según estándares académicos.
    - 🖍️ **Materiales Educativos**: Creación de recursos didácticos para el aprendizaje
    """)
st.warning("⚠️ Importante: Los requerimientos y modalidades de presentación pueden variar según la carrera. Es recomendable revisar las especificaciones particulares de cada programa académico.")

st.divider()

# Física
st.header("🔭 Modulares en Física")
st.markdown("""
Los [proyectos modulares](https://www.cucei.udg.mx/carreras/fisica/proyectos-modulares) en Física evalúan progresivamente habilidades metodológicas, analíticas y creativas:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### **Modular 1: Habilidades Básicas** *(Presentación en Póster)*
    - **Metodológicas:** Aplicación del método científico en planteamiento y resolución de problemas
    - **Capacidad Analítica:** Obtención de resultados con fundamentos científicos
    - **Creatividad:** Soluciones innovadoras al problema planteado
    - **Formato:** Póster de máximo 90x120 cm, legible a 2 metros de distancia
    
    #### **Modular 3: Habilidades Especializantes** *(Presentación Oral)*
    - **Metodológicas:** Aplicación en áreas de física contemporánea con métodos matemáticos
    - **Capacidad Analítica:** Resultados con amplia discusión teórica y experimental
    - **Creatividad:** Originalidad en contenido teórico o desarrollo experimental
    - **Formato:** Presentación oral de 20 minutos + 5 minutos para preguntas
    """)

with col2:
    st.markdown("""
    #### **Modular 2: Habilidades Fundamentales** *(Presentación Oral)*
    - **Metodológicas:** Disertación y fundamentación de temas específicos de física
    - **Capacidad Analítica:** Resultados analíticamente fundamentados con interpretación teórica
    - **Creatividad:** Originalidad en la resolución y discusión
    - **Formato:** Presentación oral de 20 minutos + 5 minutos para preguntas
    
    #### **Modular 4: Habilidad Inter o Multidisciplinar** *(Presentación Oral)*
    - **Metodológicas:** Aplicación de la física en otras ciencias o disciplinas
    - **Capacidad Analítica:** Resultados con perspectiva interdisciplinar
    - **Creatividad:** Contenido original o reportes técnicos/servicio social
    - **Formato:** Presentación oral de 20 minutos + 5 minutos para preguntas
    """)

st.markdown("""
**Requisitos generales:** Documento de máximo 10 páginas, manejo adecuado de conceptos físicos y modelos matemáticos, dominio de herramientas computacionales e instrumentos de laboratorio cuando sea necesario.
""")

st.divider()

# Químico Farmacobiólogo
st.header("💊 Modulares en Químico Farmacéutico Biólogo")
st.markdown("""
Los [proyectos modulares](https://www.cucei.udg.mx/carreras/farmaceutica/es/documento/proyectos-modulares) en Químico Farmacéutico Biólogo se enfocan en competencias intermedias y avanzadas:
""")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### **Proyectos Modulares de Competencias Intermedias**
    - Determinación de parámetros físicos, químicos, biológicos y farmacéuticos
    - Análisis de componentes y factores en procesos biológicos e industriales
    - Aplicación de conocimientos para estrategias y productos innovadores
    - Análisis y procesamiento de datos con herramientas estadísticas
    - Comparación de referencias mediante uso adecuado de información
    """)

with col2:
    st.markdown("""
    #### **Proyectos Modulares de Competencias Avanzadas**
    - Desarrollo de habilidades avanzadas en investigación farmacéutica y biológica
    - Aplicación de conocimientos especializados en situaciones profesionales
    - Integración de fundamentos teóricos con aplicaciones prácticas
    """)
    
st.markdown("""
#### **Modalidades disponibles:**
1. **Trabajo de Investigación:** Desarrollo de proyectos con método científico, hipótesis y resultados analíticos
2. **Materiales Educativos:** Creación de recursos didácticos para el aprendizaje en ciencias farmacéuticas
3. **Prototipo:** Desarrollo de modelos físicos o funcionales de productos farmacéuticos o biológicos
4. **Reporte:** Documentación técnica de procesos o investigaciones específicas
5. **Vinculación Social:** Proyectos con impacto en comunidades o sectores específicos
""")

pdf_path = '/mount/src/modularesbasicas/app/files/Lineamientos_Trabajo_Investigacion.pdf'

# Contenedor expandible para el PDF
#with st.expander("Ver PDF", expanded=False):
#    pdf_viewer(pdf_path, pages_to_render= 1)

# Contenedor expandible para el PDF
with st.expander("Ver PDF", expanded=True):
    pdf_viewer(
        input=pdf_path,
        pages_to_render=[1,2],  # Renderiza solo la página actual
        width=700,
        height=600
    )
