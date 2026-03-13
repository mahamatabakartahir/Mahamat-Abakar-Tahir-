import streamlit as st
import google.generativeai as genai

# Ta clé API
API_KEY = "AIzaSyBG6MNYkTi1qDwiJQizX-N9z5rnLqntIaI"
genai.configure(api_key=API_KEY)

# Le nom de modèle le plus stable
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="IA de Mahamat")
st.title("🤖 Assistant de Mahamat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pose ta question ici..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Tentative avec le modèle flash-latest
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # Deuxième chance avec le nom court si ça échoue
            try:
                model_retry = genai.GenerativeModel('gemini-1.5-flash')
                response = model_retry.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e2:
                st.error(f"Erreur finale : {e2}")
