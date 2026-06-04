import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "models/gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent"


class RequestBody(BaseModel):
    prompt: str


def call_gemini(prompt: str):
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    r = requests.post(URL, params={"key": API_KEY}, json=payload)
    data = r.json()

    if "candidates" in data:
        return data["candidates"][0]["content"]["parts"][0]["text"]

    return data


@app.post("/ask")
def ask(body: RequestBody):
    return {
        "response": call_gemini(body.prompt)
    }
