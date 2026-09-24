import pandas as pd
from langchain_community.document_loaders import DataFrameLoader
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma

# Charger le dataset
df = pd.read_csv("07_Marvel_DC_Comic_Characters.csv").head(5)
df['text'] = df.apply(lambda row: row.to_string(), axis=1)

# Charger les documents
loader = DataFrameLoader(df, page_content_column="text")
documents = loader.load()

# Créer les embeddings et la base vectorielle
embeddings = OllamaEmbeddings(model="mistral")
db = Chroma.from_documents(documents, embeddings)

# Poser une question
question = "Quel est le personnage Marvel avec le plus d'apparitions ?"
docs = db.similarity_search(question)
context = "\n".join([d.page_content for d in docs])

llm = OllamaLLM(model="mistral")
response = llm.invoke(f"Contexte:\n{context}\n\nQuestion: {question}")
print(response)
