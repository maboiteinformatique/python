import requests
import streamlit as st
import pandas as pd
from langchain_community.document_loaders import DataFrameLoader
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# Nova tourne sur la même machine qu'Ollama
OLLAMA_URL = "http://localhost:11434/api/chat"

st.set_page_config(page_title="Nova", page_icon="🤖")
st.title("🤖 Nova — Agent IA (Local + RAG)")

# ========== PHASE 1 : INDEXATION (une seule fois) ==========
@st.cache_resource
def charger_base():
    df = pd.read_csv("07_Marvel_DC_Comic_Characters.csv").head(5)
    df['text'] = df.apply(lambda row: row.to_string(), axis=1)
    loader = DataFrameLoader(df, page_content_column="text")
    documents = loader.load()
    embeddings = OllamaEmbeddings(model="llama3.2:1b")
    db = Chroma.from_documents(documents, embeddings)
    return db

with st.spinner("Indexation du dataset en cours... (long au premier lancement)"):
    db = charger_base()

st.success("Base prête !")

# ========== Historique ==========
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "Tu t'appelles Nova, un agent IA spécialisé dans les personnages "
                "de comics Marvel et DC. Tu réponds d'abord à partir du contexte "
                "fourni avec chaque question. Si la réponse n'y figure pas, tu réponds ce que tu sais "
            )
        }
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# ========== PHASE 2 : À CHAQUE QUESTION ==========
if prompt := st.chat_input("Écrivez votre message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    # --- RAG : recherche + contexte ---
    docs = db.similarity_search(prompt)
    context = "\n".join(d.page_content for d in docs)
    prompt_enrichi = f"Contexte:\n{context}\n\nQuestion: {prompt}"

    # Historique envoyé à Mistral : la dernière question est remplacée
    # par sa version enrichie (l'utilisateur ne voit pas le contexte)
    messages_api = st.session_state.messages[:-1] + [
        {"role": "user", "content": prompt_enrichi}
    ]

    with st.chat_message("assistant"):
        try:
            with st.spinner("Nova réfléchit..."):
                response = requests.post(
                    OLLAMA_URL,
                    json={"model": "llama3.2:1b", "messages": messages_api, "stream": False},
                    timeout=120
                )
                answer = response.json()["message"]["content"]
        except Exception as e:
            answer = f"Erreur serveur: {e}"

        st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
