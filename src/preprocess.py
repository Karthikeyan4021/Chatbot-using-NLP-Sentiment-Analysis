# src/preprocess.py
# Tokenization / cleaning helpers. Replace with spaCy or NLTK pipelines for production.
import re

def clean_text(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^\w\s'?.!,]", '', s)
    return s.lower()