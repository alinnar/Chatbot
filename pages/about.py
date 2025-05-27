import streamlit as st
import os
from PIL import Image

def show_about():
    def load_css(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../resources/style/style.css")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)

    st.markdown("""
        <div class='header'><h1>🧾Tentang</h1></div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
            <div class='header'><h2>Fitur Utama</h2></div>
            <div class='font'>
                <p>Website ini menyediakan dua fitur utama:</p>
                \n<strong><p>🧾Tes Tingkat Kecemasan (GAD-7):</strong><br>
                Pada menu Home, pengguna dapat mengikuti tes GAD-7 (Generalized Anxiety Disorder-7), yaitu kuesioner yang terdiri dari 7 pertanyaan untuk menilai tingkat kecemasan yang dialami. 
                Setelah menjawab seluruh pertanyaan, pengguna akan mendapatkan skor dan interpretasi tingkat kecemasan mereka, mulai dari minimal hingga berat. 
                Tes ini bersifat informatif dan dapat membantu pengguna memahami kondisi emosional mereka secara lebih baik.
                </p>
                \n<p><strong>💬Chatbot Pendamping Emosional</strong><br>
                Di menu Chatbot, pengguna dapat berbicara secara bebas dengan bot yang dirancang sebagai teman yang empatik dan mendukung. 
                Chatbot ini akan mendengarkan curhatan, keluh kesah, atau perasaan pengguna dengan bahasa yang santai dan menenangkan. 
                Jika pengguna mengungkapkan hal-hal yang mengarah pada risiko diri, chatbot juga akan memberikan informasi kontak layanan profesional secara ramah dan tidak menghakimi.
                </p>
            </div>
        </div> 
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
            <div class='header'><h2>Keterbatasan Aplikasi</h2></div>
            <div class='font'>
                <p>
                <strong>1. Bukan Pengganti Profesional Kesehatan Mental:</strong> Chatbot dalam aplikasi ini tidak dapat memberikan diagnosis medis atau terapi psikologis secara profesional. Hasil dari tes GAD-7 hanya sebagai alat skrining awal dan bukan sebagai keputusan akhir.<br>
                <strong>2. Respons Chatbot Terbatas:</strong> Chatbot dirancang untuk merespons dengan empati, namun masih memiliki keterbatasan dalam memahami konteks percakapan yang kompleks, ambigu, atau mendalam secara emosional.<br>
                <strong>3. Keterbatasan Bahasa dan Ekspresi:</strong> Saat ini, chatbot hanya mendukung bahasa Indonesia dalam bentuk formal atau semi-formal. Ekspresi slang, campuran bahasa, atau dialek tertentu mungkin belum dipahami secara optimal.<br>
                </p> 
            </div>
        </div> 
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='section'>
        <div class='header'><h2>Pengembang</h2></div>
        <div class='subheader2'><h3> Revalin Arianti Rajagukguk - 22537144009 </h3></div>
        <div class="icon-container">
            <a href="https://github.com/alinnar" target="_blank" class="social-icon github" aria-label="Github"></a>
            <a href="https://www.instagram.com/alinnrar?igsh=ZHF6bXQ4M3BzbGwx" target="_blank" class="social-icon instagram" aria-label="Instagram"></a>
            <a href="mailto:revalinarianti.2022@student.uny.ac.id" class="social-icon email" aria-label="Email"></a>
        </div>
    </div>
    """, unsafe_allow_html=True)