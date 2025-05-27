import streamlit as st
import os
from PIL import Image

def show_home():

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
        <div class='header'><h1>Heart to Hear 💬❤️</h1></div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
            <div class='header'><h2>Apa itu Heart to Hear?</h2></div>
            <div class='font'>
                <p><strong>Heart to Hear</strong> adalah sebuah website interaktif yang dirancang untuk mendampingi pengguna dalam menjaga kesehatan mental.</p>
                <p>Di halaman utama ini, pengguna dapat melakukan <strong>Tes GAD-7 (Generalized Anxiety Disorder-7)</strong> untuk mengetahui tingkat kecemasan yang sedang dialami.</p
                <P>Selain itu, tersedia fitur <strong>Chatbot</Strong> yang siap menemani kapan pun dibutuhkan, memberikan ruang bagi siapa saja yang ingin mencurahkan isi hati. </p>
                <p>Website ini diciptakan sebagai tempat aman untuk berbagi, tanpa menghakimi, dan menjadi langkah awal menuju perasaan yang lebih baik.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
            <div class='font'>
                Ayo Ikuti Tes Tingkat Kecemasan anda terlebih dahulu!😊
            </div>    
        </div>
                """, unsafe_allow_html=True)

    # Inisialisasi session_state
    if "show_gad7" not in st.session_state:
        st.session_state.show_gad7 = False

    with st.expander("Mulai Tes GAD-7 (klik untuk membuka)"):
        st.markdown("""
            <div class='section'>
                <div class='header'><h2>Kuesioner GAD-7</h2></div>
        """, unsafe_allow_html=True)

        questions = [
            "1. Merasa gugup, cemas, atau sangat tegang?",
            "2. Tidak bisa menghentikan atau mengontrol rasa khawatir?",
            "3. Terlalu banyak khawatir terhadap berbagai hal berbeda?",
            "4. Kesulitan untuk rileks?",
            "5. Gelisah sehingga sulit untuk duduk diam?",
            "6. Mudah kesal atau mudah merasa terganggu?",
            "7. Merasa takut seolah sesuatu yang buruk akan terjadi?",
        ]

        options = {
            "Tidak pernah": 0,
            "Beberapa hari": 1,
            "Lebih dari setengah hari": 2,
            "Hampir setiap hari": 3
        }

        jawaban = {}
        skor_total = 0

        with st.form(key="form_gad7"):
            for idx, p in enumerate(questions):
                st.markdown(f"**{p}**")
                jawaban[idx] = st.radio("Pilih jawaban:", list(options.keys()), index=None, key=f"gad7_q_{idx}", label_visibility="collapsed")

            tombol_submit = st.form_submit_button("Lihat Hasil")

        if tombol_submit:
            if None in jawaban.values():
                st.warning("Harap jawab semua pertanyaan sebelum melihat hasil.")
            else:
                skor_total = sum(options[j] for j in jawaban.values())

                # Interpretasi skor
                if skor_total <= 4:
                    hasil = "Tingkat kecemasan minimal."
                elif 5 <= skor_total <= 9:
                    hasil = "Tingkat kecemasan ringan."
                elif 10 <= skor_total <= 14:
                    hasil = "Tingkat kecemasan sedang."
                else:
                    hasil = "Tingkat kecemasan berat."

                st.markdown(f"""
                    <div class='section'>
                        <div class='subheader2'>Hasil Tes GAD-7 Anda</div>
                        <p style='text-align: center; font-size: 20px;'>Skor Total: <b>{skor_total}</b><br>📝 {hasil}</p>
                        <div class='notes'>
                        GAD-7 dikembangkan oleh Drs. Robert L. Spitzer, Janet B.W. Williams, Kurt Kroenke dan rekan-rekannya, 
                            dengan dana hibah pendidikan dari Pfizer Inc. Tidak diperlukan izin untuk mereproduksi, menerjemahkan, menampilkan, atau mendistribusikan.
                    </div>
                """, unsafe_allow_html=True)

    st.markdown("""
        <div class='notes'>
        <i>Catatan:</i> Jika kamu merasa gejala yang kamu alami mulai mengganggu aktivitas sehari-hari atau terasa semakin berat, 
                        jangan ragu untuk mencari bantuan dari tenaga profesional seperti psikolog atau konselor. 
                        Kamu tidak sendiri, dan bantuan tersedia untukmu.
                """, unsafe_allow_html=True)
