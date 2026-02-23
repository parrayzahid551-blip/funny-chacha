import streamlit as st
from utils.model import generate_response
from utils.prompt import build_prompt
from utils.memory import initialize_memory, add_message, get_messages

# Page config
st.set_page_config(
    page_title="Funny Chacha 🤡",
    page_icon="🤡",
    layout="centered"
)

# Header
st.markdown(
    "<h1 style='text-align:center;'>🤡 Funny Chacha</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Your AI-Powered Humorous Assistant</p>",
    unsafe_allow_html=True
)

st.info("⚠️ This chatbot generates AI-based humorous responses.")

initialize_memory()

# Sidebar
st.sidebar.title("⚙️ Chacha Settings")
temperature = st.sidebar.slider("Humor Level", 0.5, 1.2, 0.9)

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display conversation
for msg in get_messages():
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Talk to Chacha..."):
    add_message("user", user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = build_prompt(get_messages(), user_input)

    response = generate_response(prompt, temperature=temperature)

    add_message("assistant", response)

    with st.chat_message("assistant"):
        st.markdown(response)
        banned_words = ["hate", "kill", "idiot"]

if any(word in user_input.lower() for word in banned_words):
    st.warning("Chacha refuses to go there 😌 Let's keep it friendly!")
    st.stop()