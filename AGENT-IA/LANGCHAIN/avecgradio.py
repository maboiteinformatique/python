import urllib.error
import urllib.request
import ssl
import certifi
import gradio as gr

ssl_context = ssl.create_default_context(cafile=certifi.where())

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

SYSTEM_PROMPT = "You are a literary assistant. Use fetch_text_from_url to answer questions."

@tool
def fetch_text_from_url(url: str) -> str:
    """Fetch the document from a URL."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_context) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        return f"Fetch failed: {e}"
    text = raw.decode("utf-8", errors="replace")
    return text[:15000]

model = init_chat_model(
    "meta-llama/llama-4-scout-17b-16e-instruct",
    model_provider="groq",
    temperature=0.5,
    timeout=600,
    max_tokens=8192,
    streaming=False,
)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    tools=[fetch_text_from_url],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

def ask(question):
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config={"configurable": {"thread_id": "session"}},
    )
    return result["messages"][-1].content_blocks[0]["text"]

gr.Interface(
    fn=ask,
    inputs=gr.Textbox(label="Question", placeholder="Posez une question sur un livre..."),
    outputs=gr.Textbox(label="Réponse"),
    title="Literary Assistant",
).launch()