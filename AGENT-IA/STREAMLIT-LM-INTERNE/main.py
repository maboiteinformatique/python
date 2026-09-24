""" import requests

url = "http://10.163.120.18:11434/api/generate"

data = {
    "model": "qwen3.5",
    "prompt": "Explique la récursion simplement",
    "stream": False
}

response = requests.post(url, json=data)

print(response.json()["response"]) """

import requests
import streamlit as st

OLLAMA_URL = "http://10.163.120.15:11434/api/chat"

st.set_page_config(page_title="Nova", page_icon="🤖")
st.title("🤖 Nova — Agent IA (Local)")

# historique
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "Tu t'appelles Nova, un agent IA spécialisé dans les personnages de marvel"
        }
    ]

# affichage historique
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# input utilisateur
if prompt := st.chat_input("Écrivez votre message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": "mistral",   # ou mistral, phi, etc.
                    "messages": st.session_state.messages,
                    "stream": False
                },
                timeout=120
            )

            answer = response.json()["message"]["content"]

        except Exception as e:
            answer = f"Erreur serveur: {e}"

        st.write(answer)
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )