import os
from huggingface_hub import InferenceClient
import streamlit as st
import os

HF_TOKEN = os.getenv("HF_TOKEN") or st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_TOKEN
)

def generate_response(prompt, temperature=0.9):
    response = client.text_generation(
        prompt,
        max_new_tokens=200,
        temperature=temperature,
        do_sample=True
    )
    return response