import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
from utils import add_background

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Heart to Hear", 
    page_icon="👂", 
    initial_sidebar_state="collapsed"
)

image_path = r"./resources/gambar/latarnew.png"

#
add_background(image_path)

# Daftar halaman
pages = ["Home", "Bot", "About"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
urls = {}

# Style untuk navbar
styles = {
    "nav": {
        "display": "flex",
        "background-color": "#ffc1d3",  # Pink background
        "justify-content": "center",
        "align-items": "center",
        "height": "60px",
        "gap": "60px",  # Spasi antar item navbar
    },
    "span": {
        "color": "#000000",  # Hitam untuk teks biasa
        "padding": "10px 0px",
        "cursor": "pointer",
        "text-align": "center",
        "font-size": "16px",
        "font-weight": "400",
        "text-decoration": "none",
        "position": "relative",
    },
    "active": {
        "color": "#ffffff",  # Warna putih untuk teks aktif
        "font-weight": "bold",
        "text-decoration": "underline",  # Garis bawah
        "text-underline-offset": "5px", # Jarak garis bawah dari teks
    },
}

# Opsi tampilan navbar
options = {
    "show_menu": True,
    "show_sidebar": False,
}

# Tampilkan navbar dan ambil halaman yang dipilih
page = st_navbar(
    pages,
    styles=styles,
    options=options
)

# Default ke halaman Home jika tidak ada yang dipilih
if not page:
    page = "Home"

# Pemanggilan fungsi berdasarkan halaman yang dipilih
functions = {
    "Home": pg.show_home,
    "Bot": pg.show_bot,
    "About": pg.show_about,
}

go_to = functions.get(page)

if go_to:
    go_to()
else:
    st.write("Halaman tidak ditemukan")