from huggingface_hub import InferenceClient
import os
import streamlit as st

HF_TOKEN = os.getenv("HF_TOKEN") or st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="distilgpt2",
    token=HF_TOKEN
)

def generate_response(prompt, temperature=0.7):
    response = client.text_generation(
        prompt,
        max_new_tokens=150,
        temperature=temperature
    )
    return response