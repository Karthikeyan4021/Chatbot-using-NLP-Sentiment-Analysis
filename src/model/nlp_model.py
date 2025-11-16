# src/model/nlp_model.py
# Minimal response generation. This file demonstrates where you'd call a transformer model such as T5 or DialoGPT.
# For this starter kit we provide a simple rule-based fallback and an optional Hugging Face pipeline usage (commented).
from typing import Optional

def generate_response(text: str, sentiment: Optional[str] = None) -> str:
    # If sentiment is NEGATIVE, be extra empathetic.
    if sentiment and sentiment.upper().startswith("NEG"):
        return "I'm sorry you're feeling that way. Tell me more — I'm here to listen."
    # Simple rule-based examples
    if "joke" in text.lower():
        return "Why don't scientists trust atoms? Because they make up everything!"
    if "how are you" in text.lower():
        return "I'm a bot — running smoothly! How can I help you?"
    # Fallback
    return "Thanks for sharing. Could you elaborate a bit?"