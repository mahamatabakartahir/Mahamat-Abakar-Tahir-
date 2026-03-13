import streamlit as st
import google.generativeai as genai

# Configuration de la clé
API_KEY = "AIzaSyBG6MNYkTi1qDwiJQizX-N9z5rnLqntIaI"
genai.configure(api_key=API_KEY)

# Configuration du modèle
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="IA de Mahamat")
st.title("🤖 Assistant de Mahamat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Pose-moi une question...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = model.generate_content(user_input)
        assistant_text = response.text
    except Exception as e:
        assistant_text = "Désolé, j'ai un petit problème technique. Réessaie !"

    with st.chat_message("assistant"):
        st.write(assistant_text)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_text})
