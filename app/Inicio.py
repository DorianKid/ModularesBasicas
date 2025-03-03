import streamlit as st
import base64

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

# Descripción inicial
st.markdown("""
Los **Proyectos Modulares** constituyen una estrategia educativa fundamental dentro del modelo académico del 
Centro Universitario de Ciencias Exactas e Ingenierías (**CUCEI**) de la **Universidad de Guadalajara**. Estos proyectos representan un **sistema de evaluación integral** que permite a los estudiantes demostrar la adquisición y aplicación de competencias específicas en diferentes etapas de su formación profesional.
""")

st.divider()  # Separador visual

# Sección: ¿Qué son los modulares?
st.header("🔍 ¿Qué son los modulares?")
st.markdown("""
Los **Proyectos Modulares** son actividades académicas estructuradas que permiten evaluar la integración de **conocimientos, habilidades y actitudes** adquiridas por los estudiantes durante un período específico de su formación.
Más que simples trabajos finales, estos proyectos representan **evidencias concretas** del desarrollo de competencias profesionales y metodológicas necesarias para el ejercicio de su profesión.
""")

st.divider()

# Características comunes con diseño de columnas
st.header("📌 Características Comunes")
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

# Importancia educativa con resaltado
st.success("📢 **Importancia Educativa:** Los Proyectos Modulares desempeñan un papel crucial en la formación académica, asegurando que los estudiantes adquieran competencias aplicables al mundo real.")

st.markdown("""
- **Vinculación teórico-práctica**: Aplicación de conocimientos a situaciones concretas.
- **Desarrollo de competencias profesionales**: Investigación, análisis, resolución de problemas y comunicación.
- **Evaluación auténtica**: Simulación de contextos profesionales.
- **Preparación para el campo laboral**: Desarrollo de habilidades clave para el ejercicio profesional.
- **Fomento a la creatividad e innovación**: Creación de soluciones originales a problemas específicos.
""")

st.divider()
st.warning("⚠️ Importante: Los requerimientos y modalidades de evaluación pueden variar según la carrera. Es recomendable revisar las especificaciones particulares de cada programa académico.")

# Modalidades de presentación con diseño en columnas
st.header("📑 Modalidades de Presentación")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - 🎤 **Presentaciones orales**: Exposiciones formales ante comités evaluadores.
    - 📊 **Pósters científicos**: Presentaciones visuales del trabajo realizado.
    - 🔧 **Prototipos**: Desarrollo de modelos físicos o funcionales.
    """)

with col2:
    st.markdown("""
    - 📄 **Reportes técnicos**: Documentos detallados del proceso y resultados.
    - 📰 **Artículos científicos**: Trabajos estructurados según estándares académicos.
    """)

st.divider()

# Adaptación por disciplina
st.header("⚙️ Adaptación por Disciplina")
st.markdown("""
Los **Proyectos Modulares** mantienen una estructura común pero se adaptan a las particularidades de cada carrera:

- **🔭 Física:** Desarrollo de habilidades metodológicas, capacidad analítica y resolución de problemas científicos.
- **💊 Químico Farmacobiólogo:** Enfoque en parámetros físicos, químicos, biológicos y farmacéuticos.
- **🛠️ Ingenierías:** Diseño y desarrollo de soluciones tecnológicas a problemas específicos.

Los **Proyectos Modulares** representan un componente distintivo de la formación académica en **CUCEI**, proporcionando un mecanismo efectivo para evaluar el progreso de los estudiantes y prepararlos para los desafíos profesionales que enfrentarán al egresar.
""")

