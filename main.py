from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(question):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": question}]}]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]

@app.get("/ask")
def ask(q: str):
    return {"answer": ask_gemini(q)}