import os
import streamlit as st
from openai import OpenAI

# Configuration
st.set_page_config(page_title="Nova", page_icon="🤖")
st.title("🤖 Nova — Agent IA")

api_key = os.environ.get("GROQ_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Tu es Nova, un agent IA qui réponds en français toujours par une blague."}
    ]

# Affichage de l'historique
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Saisie utilisateur
if prompt := st.chat_input("Écrivez votre message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            messages=st.session_state.messages
        )
        answer = response.choices[0].message.content
        st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})