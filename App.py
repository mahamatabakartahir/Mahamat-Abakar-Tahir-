import streamlit as st
import google.generativeai as genai

# Ta clé API récupérée de ton ancien code
API_KEY = "AIzaSyAIQ4IxXac2WlydNW8hy8CjyH..." 

genai.configure(api_key=API_KEY)

# Correction du nom du modèle (gemini-1.5-flash)
model = genai.GenerativeModel(
    'gemini-1.5-flash') 

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
    
    response = model.generate_content(user_input)
    
    with st.chat_message("assistant"):
        st.write(response.text)
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
