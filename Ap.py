import streamlit as st
import google.generativeai as genai

# --- ÉTAPE 1 : TA CLÉ API ---
API_KEY = "AIzaSyAIQ4IxXac2WlydNW8hy8CjyH..." # Ta clé est déjà là

# --- ÉTAPE 2 : CONFIGURATION ---
genai.configure(api_key=API_KEY)

instructions = "Tu es l'intelligence artificielle créée par Mahamat Abakar Tahir. Tu es un assistant universel et poli."

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)

# --- ÉTAPE 3 : L'INTERFACE ---
st.set_page_config(page_title="IA de Mahamat")
st.title("🤖 Assistant Universel de Mahamat")
st.write("Posez-moi n'importe quelle question !")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Dites-moi n'importe quoi...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = model.generate_content(user_input)
    
    with st.chat_message("assistant"):
        st.write(response.text)
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
