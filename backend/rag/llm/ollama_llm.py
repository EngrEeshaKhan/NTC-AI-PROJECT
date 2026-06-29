import requests

def generate(context, question):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2:3b",
        "prompt": f"""
You are an AI assistant.

Context:
{context}

Question:
{question}

Answer clearly:
""",
        "stream": False
    })

    return res.json()["response"]