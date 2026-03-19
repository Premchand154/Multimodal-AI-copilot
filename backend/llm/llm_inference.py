import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def generate_response(context, question, memory_context=""):

    prompt = f"""
You are an advanced AI assistant.

Use the provided context carefully.
If not sufficient, use reasoning.

Conversation history:
{memory_context}

Context:
{context}

Question: {question}

Give a clear, structured answer.
"""

    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
    )

    return response.json().get("response", "Error")

