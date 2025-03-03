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

st.title("Proyectos Modulares")
st.markdown("""
#### Los Proyectos Modulares constituyen una estrategia educativa fundamental dentro del modelo académico del Centro Universitario de Ciencias Exactas e Ingenierías (CUCEI) de la Universidad de Guadalajara. Estos proyectos representan un sistema de evaluación integral que permite a los estudiantes demostrar la adquisición y aplicación de competencias específicas en diferentes etapas de su formación profesional.
""")
st.header("¿Qué son los modulares?") 
st.markdown("""
Los Proyectos Modulares son actividades académicas estructuradas que permiten evaluar la integración de conocimientos, habilidades y actitudes adquiridas por los estudiantes durante un período específico de su formación. Más que simples trabajos finales, estos proyectos representan evidencias concretas del desarrollo de competencias profesionales y metodológicas que serán necesarias en el ejercicio de su profesión.
Características Comunes
Independientemente de la carrera específica dentro de CUCEI, los Proyectos Modulares comparten características esenciales:

Enfoque progresivo: Se organizan en niveles de complejidad creciente, acompañando el avance del estudiante a lo largo de su formación.
Integración de conocimientos: Requieren que el estudiante aplique de manera interrelacionada los conocimientos adquiridos en diversas asignaturas.
Orientación práctica: Buscan la resolución de problemas reales o simulados del ámbito profesional.
Desarrollo metodológico: Exigen la aplicación de métodos científicos y técnicas específicas según la disciplina.
Evaluación integral: No solo se evalúan los resultados finales, sino también el proceso, la metodología y las competencias demostradas.
Acompañamiento docente: Cuentan con asesoría especializada de profesores durante todo el proceso de desarrollo.

Importancia Educativa
Los Proyectos Modulares desempeñan un papel crucial en la formación académica por varias razones:

Vinculación teórico-práctica: Permiten aplicar los conocimientos teóricos a situaciones concretas.
Desarrollo de competencias profesionales: Fomentan habilidades de investigación, análisis, resolución de problemas y comunicación.
Evaluación auténtica: Evalúan el desempeño en contextos similares a los que enfrentarán en su vida profesional.
Preparación para el campo laboral: Desarrollan capacidades necesarias para el ejercicio profesional.
Fomento a la creatividad e innovación: Estimulan la generación de soluciones originales a problemas específicos.

Modalidades de Presentación
Los Proyectos Modulares pueden presentarse en diferentes formatos según los requisitos específicos de cada carrera y nivel:

Presentaciones orales: Exposiciones formales ante comités evaluadores.
Pósters científicos: Presentaciones visuales que sintetizan el trabajo realizado.
Prototipos: Desarrollo de modelos físicos o funcionales.
Reportes técnicos: Documentos detallados que describen el proceso y resultados.
Artículos científicos: Trabajos estructurados según los estándares de publicaciones académicas.

Adaptación por Disciplina
Aunque mantienen una estructura común, los Proyectos Modulares se adaptan a las particularidades de cada carrera:

En Física, se enfocan en el desarrollo de habilidades metodológicas, capacidad analítica y creatividad en la resolución de problemas científicos.
En Químico Farmacobiólogo, se orientan a competencias intermedias y avanzadas relacionadas con parámetros físicos, químicos, biológicos y farmacéuticos.
En Ingenierías, suelen enfocarse en el diseño y desarrollo de soluciones tecnológicas a problemas específicos.

Los Proyectos Modulares representan un componente distintivo de la formación académica en CUCEI, proporcionando un mecanismo efectivo para evaluar el progreso de los estudiantes y prepararlos para los desafíos profesionales que enfrentarán al egresar.
""")
