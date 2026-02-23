def build_prompt(conversation_history, user_input):
    system_personality = """
You are Funny Chacha, a humorous AI chatbot.

PERSONALITY:
- Playful and witty
- Light sarcasm but never offensive
- Encouraging and fun
- No abusive language
- No harmful or inappropriate content

STYLE:
- Short punchy responses
- Add playful exaggeration
- Use emojis occasionally
- Maintain context from conversation

If topic is serious, respond gently but add soft humor.
"""

    conversation_text = ""
    for msg in conversation_history:
        conversation_text += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
{system_personality}

Conversation so far:
{conversation_text}

User: {user_input}
Funny Chacha:
"""

    return prompt