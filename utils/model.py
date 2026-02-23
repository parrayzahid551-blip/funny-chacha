from huggingface_hub import InferenceClient
import os
import streamlit as st

HF_TOKEN = os.getenv("HF_TOKEN") or st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="google/flan-t5-large",
    token=HF_TOKEN
)

def generate_response(prompt, temperature=0.9):
    response = client.text_generation(
        prompt,
        max_new_tokens=200,
        temperature=temperature
    )
    return response