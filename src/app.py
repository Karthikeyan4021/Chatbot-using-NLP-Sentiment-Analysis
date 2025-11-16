# src/app.py
# Simple FastAPI app exposing two endpoints:
#  - /chat : returns a generated response (uses a simple rule or HF model if available)
#  - /sentiment : returns sentiment label for a given text
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from .model.nlp_model import generate_response
from .model.sentiment import analyze_sentiment

app = FastAPI(title="Text Chatbot with Sentiment")

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(msg: Message):
    sent = analyze_sentiment(msg.text)
    response = generate_response(msg.text, sentiment=sent)
    return {"input": msg.text, "sentiment": sent, "response": response}

@app.post("/sentiment")
async def sentiment_endpoint(msg: Message):
    sent = analyze_sentiment(msg.text)
    return {"input": msg.text, "sentiment": sent}

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)