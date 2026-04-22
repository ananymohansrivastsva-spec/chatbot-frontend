import streamlit as st
from datetime import datetime

# Page Config
st.set_page_config(page_title="Chatbot UI", layout="centered")

# Title
st.title("🤖 Chatbot Web App")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Delete chat function
def clear_chat():
    st.session_state.messages = []

# Delete Chat Button
st.button("🗑 Delete Chat", on_click=clear_chat)

st.markdown("---")

# Display messages
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role']} ({msg['time']})**")
    st.write(msg["content"])

st.markdown("---")

# Input box
user_input = st.text_input("Type your message...")

# Send button
if st.button("Send") and user_input:
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Store user message
    st.session_state.messages.append({
        "role": "You",
        "content": user_input,
        "time": current_time
    })

    # Bot response (dummy)
    bot_reply = f"Echo: {user_input}"

    st.session_state.messages.append({
        "role": "Bot",
        "content": bot_reply,
        "time": current_time
    })

    st.rerun()
                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                