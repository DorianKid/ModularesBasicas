import streamlit as st

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

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://img.freepik.com/vector-gratis/concepto-coleccion-maestros_52683-37592.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://img.freepik.com/vector-gratis/concepto-coleccion-maestros_52683-37592.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("# Profesores")

st.markdown(
"""
"""
)
