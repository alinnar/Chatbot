import base64
import streamlit as st

def add_background(image_path):
    """
    Menambahkan gambar latar belakang ke seluruh halaman Streamlit.
    """
    with open(image_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
    bg_style = f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{b64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100%;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)
