import streamlit as st
import google.generativeai as genai

# --- ÉTAPE 1 : TA CLÉ API ---
CLE_API = "AIzaSyAIQ4IxXac2WlydNW8hy8CjyH9VBwHGmVo"

# --- ÉTAPE 2 : CONFIGURATION DU CERVEAU (GÉNÉRALISTE) ---
genai.configure(api_key=CLE_API)

# Instructions pour que l'IA parle de TOUT
instructions = """
Tu es l'intelligence artificielle créée par Mahamat. 
Tu es un assistant universel et très cultivé. 
Tu peux répondre à des questions sur la science, l'histoire, la technologie, 
la cuisine, le sport, la programmation, la vie quotidienne, et bien plus.
Tu réponds toujours de manière polie, claire et utile, en français ou en arabe selon le choix de l'utilisateur.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)

# --- ÉTAPE 3 : L'INTERFACE VISUELLE ---
st.set_page_config(page_title="IA de Mahamat", page_icon="🌍")
st.title("🤖 Assistant Universel de Mahamat")
st.write("Posez-moi n'importe quelle question sur n'importe quel sujet !")

# Gestion de la discussion
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Dites-moi n'importe quoi...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # L'IA génère sa réponse sur n'importe quel sujet
    response = model.generate_content(user_input)
    
    with st.chat_message("assistant"):
        st.write(response.text)
        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
