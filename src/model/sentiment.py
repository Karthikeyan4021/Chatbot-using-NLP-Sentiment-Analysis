# src/model/sentiment.py
# Minimal sentiment analyzer wrapper. Replace with a Hugging Face model for production.
# Example using HF pipeline (commented) for when internet is available and models are downloaded.
# from transformers import pipeline
# sentiment_pipe = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text: str) -> str:
    # Very small heuristic sentiment as a placeholder.
    t = text.lower()
    if any(w in t for w in ["love", "great", "fantastic", "good", "awesome"]):
        return "POSITIVE"
    if any(w in t for w in ["hate", "worst", "sad", "angry", "terrible", "bad"]):
        return "NEGATIVE"
    return "NEUTRAL"