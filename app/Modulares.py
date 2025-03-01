import streamlit as st
import base64

main_bg = "modulares.avif"
main_bg_ext = "avif"

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
    f"""
    <style>
    .reportview-container {{
        background: url(data:app/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}

    </style>
    """,
    unsafe_allow_html=True
)

st.write("# Profesores")

st.markdown(
"""
"""
)


#    .sidebar .sidebar-content {{background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})}}
