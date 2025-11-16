# Text Chatbot with NLP + Sentiment Analysis (Starter Kit)

## Overview
A minimal starter project containing:
- Response generator (placeholders for T5 / DialoGPT)
- Sentiment analyzer (placeholder, swap to BERT/TinyBERT fine-tuned on SST-2)
- FastAPI endpoints and a Streamlit demo (code included)
- Small sample datasets and a simulated results screenshot

## Structure
```
text-chatbot/
├─ data/
│  ├─ dialogues.csv
│  └─ sentiment_dataset.csv
├─ src/
│  ├─ app.py
│  ├─ model/
│  │  ├─ nlp_model.py
│  │  └─ sentiment.py
│  ├─ preprocess.py
│  └─ utils/
├─ notebooks/
├─ requirements.txt
└─ README.md
```

## How to run (local)
1. Create a Python virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate    # on Linux/macOS
   venv\Scripts\activate     # on Windows
   pip install -r requirements.txt
   ```
2. Run the FastAPI app:
   ```bash
   uvicorn src.app:app --reload --port 8000
   ```
   Then POST JSON to `http://localhost:8000/chat`:
   ```json
   { "text": "I'm feeling sad today." }
   ```

3. (Optional) Replace the placeholder sentiment and generator with Hugging Face models:
   - For sentiment: use `transformers.pipeline("sentiment-analysis", model="textattack/bert-base-uncased-SST-2")`
   - For generation: use `transformers` models like `microsoft/DialoGPT-small` or `t5-small` with fine-tuning.

## Notes
- This repo contains starter code and simulated results. It does not bundle pretrained models.
- For full training/fine-tuning you'll need GPU and datasets (links suggested in the project description).