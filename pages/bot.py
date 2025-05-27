"""Main program for the Mental Health Companion Chatbot with Ollama"""

import requests
import os
import streamlit as st

def show_bot():
    def load_css(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Menentukan path file style.css
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../resources/style/style.css")
    load_css(css_path)

    # System Prompt
    system_prompt = """
    You act as a supportive, relaxed, and empathetic peer.
    You are there to listen to users who want to talk about their feelings, emotions, or mental health.
    Respond with light, warm, and casual language, like you are chatting with a close friend.
    Avoid using overly romantic or dramatic terms like "darling or dear".
    Focus on listening, validating feelings, and providing support in a simple, sincere way.
    Use casual, natural Bahasa in Indonesian not English, and avoid coming across as a novel. 

    If a user shares something that could potentially harm themselves or others, immediately provide information about professional helplines (Hotline Sejiwa: 119 (kemudian tekan angka 8) dan Halo Kemenkes Nomor: 1500 567 
    WhatsApp: +62 812 6050 0567) in a warm, non-judgmental way. 
    Remember, you are not providing a diagnosis or medical advice, you are simply being a supportive friend.

    However, if the user asks about topics unrelated to emotions, mental well-being, or personal struggles (like math, coding, trivia, news, etc.), respond with:
    "Maaf, saya tidak mengerti. Saya hanya di sini untuk mendengarkan dan mendampingi kamu dalam hal yang berkaitan dengan perasaan dan kesehatan mental."
    Always keep responses empathetic and focused only on mental health and emotional support.
    """

    # OLLAMA Configuration
    OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"
    OLLAMA_MODEL = "gemma3"

    # Tuning parameters
    OLLAMA_PARAMETERS = {
        "temperature": 0.7, #kreativitas jawaban
        "top_p": 0.9, # menjaga output agar tetap masuk akal
        "top_k": 40, #membantu mengurangi kata-kata aneh
        "repetition_penalty": 1.1, #mencegah model mengulang-ulang kata yang sama
        "stream": False # jika true respon yang diberikan secara bertahap, false: langsung memberi jawaban
    }

    # User Interface
    st.caption("Powered locally by Ollama")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        greeting_message = "Halo! Saya adalah bot yang akan mendengarkan dan mendukung Anda. Jangan ragu untuk berbagi apa pun yang ada dalam pikiran Anda 😊"
        st.session_state.messages.append({"role": "assistant", "content": greeting_message})

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("Ceritakan bagaimana perasaan Anda..."):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        built_chat_history = [{"role": "system", "content": system_prompt}]
        for chat in st.session_state.messages:
            built_chat_history.append({"role": chat["role"], "content": chat["content"]})

        payload = {
            "model": OLLAMA_MODEL,
            "messages": built_chat_history,
            **OLLAMA_PARAMETERS
        }

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = requests.post(OLLAMA_API_URL, json=payload)
                    response.raise_for_status()
                    assistant_reply = response.json()['choices'][0]['message']['content']
                    st.markdown(assistant_reply)
                except Exception as e:
                    assistant_reply = "Sorry, I couldn't connect to the AI server."
                    st.error(assistant_reply)

        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})