import streamlit as st
import google.generativeai as genai

# Ta clé API
API_KEY = "AIzaSyBG6MNYkTi1qDwiJQizX-N9z5rnLqntIaI"

# FORCE LA VERSION STABLE ICI
genai.configure(api_key=API_KEY, transport='grpc')

# On utilise le nom complet du modèle stable
model = genai.GenerativeModel('models/gemini-1.5-flash')

st.set_page_config(page_title="IA de Mahamat")
st.title("🤖 Assistant de Mahamat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pose ta question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Appel direct
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erreur : {e}")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e2:
                st.error(f"Erreur finale : {e2}")
