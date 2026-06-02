# AI Gemini API – FastAPI Backend

This project is a minimal AI backend built with FastAPI and Google Gemini API.

It exposes a simple endpoint that allows users to send a question and receive an AI-generated response.

---

## Features

- FastAPI REST API
- Google Gemini integration
- Cloud deployment ready
- Lightweight architecture
- Foundation for AI agents and SaaS products

---

## API Usage

### GET /ask

Example:

/ask?q=hello

Example response:

{
  "answer": "AI generated response here"
}

---

## Installation

Clone the repository:

git clone <repository-url>

Enter the project folder:

cd ai-gemini-api

Install dependencies:

pip install -r requirements.txt

---

## Running Locally

Start the server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

to access the automatic FastAPI documentation.

---

## Environment Variables

Set the following environment variable:

GEMINI_API_KEY=your_api_key_here

Do not store API keys directly in source code.

---

## Deployment

This project can be deployed on:

- Render
- Railway
- Fly.io

Render start command:

uvicorn main:app --host 0.0.0.0 --port 10000

---

## Technologies

- Python
- FastAPI
- Requests
- Google Gemini API

---

## Future Improvements

- Conversation memory
- Authentication
- User accounts
- Rate limiting
- Chat interface
- Wix integration
- AI agents with tools

---

## License

MIT License
