from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(question):
    MODEL = "models/gemini-2.5-flash"

    URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent"

    payload = {
        "contents": [{"parts": [{"text": question}]}]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    if "candidates" in data:
        return data["candidates"][0]["content"]["parts"][0]["text"]

    return f"ERROR FROM GEMINI: {data}"
