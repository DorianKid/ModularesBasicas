import streamlit as st
import base64

st.set_page_config(
    page_title="Modulares",
    page_icon=":pencil    :",
    layout="wide",    
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

st.title("¿Qué son los modulares?")
