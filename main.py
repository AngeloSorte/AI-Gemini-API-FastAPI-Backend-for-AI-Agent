import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS per Wix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "models/gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent"


class RequestBody(BaseModel):
    prompt: str
    history: list = []


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/ask")
def ask(body: RequestBody):

    system_prompt = """
You are a helpful AI assistant.
You answer clearly and concisely.
Keep context from previous messages.
"""

    history_text = ""

    for msg in body.history:
        role = msg.get("role", "")
        text = msg.get("text", "")
        history_text += f"{role}: {text}\n"

    full_prompt = system_prompt + "\n\nCHAT HISTORY:\n" + history_text + "\nUSER:\n" + body.prompt

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": full_prompt}
                ]
            }
        ]
    }

    r = requests.post(
        URL,
        params={"key": API_KEY},
        json=payload,
        timeout=60
    )

    data = r.json()

    if "candidates" in data:
        return {
            "response": data["candidates"][0]["content"]["parts"][0]["text"]
        }

    return {"error": data}
