import streamlit as st
import google.generativeai as genai

# Ta clé API (ne pas changer)
API_KEY = "AIzaSyBG6MNYkTi1qDwiJQizX-N9z5rnLqntIaI"
genai.configure(api_key=API_KEY)

# On utilise le modèle Pro qui est le plus compatible
model = genai.GenerativeModel('gemini-pro')

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
            # Envoi de la requête
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # Si gemini-pro échoue aussi, on essaie une version plus récente
            try:
                model_alt = genai.GenerativeModel('gemini-1.0-pro')
                response = model_alt.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e2:
                st.error(f"Erreur Google : {e2}")
