# src/streamlit_app.py
import streamlit as st
from src.model.nlp_model import generate_response
from src.model.sentiment import analyze_sentiment

st.title("Chatbot + Sentiment Demo (Starter)")
user_input = st.text_input("You:")
if user_input:
    sent = analyze_sentiment(user_input)
    resp = generate_response(user_input, sentiment=sent)
    st.write("Sentiment:", sent)
    st.write("Bot:", resp)