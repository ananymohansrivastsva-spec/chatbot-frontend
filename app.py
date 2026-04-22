import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="Conceptly AI Tutor", layout="wide")

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
    color: white;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

/* Chat */
.chat-box {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.user {
    background-color: #dbeafe;
}

.bot {
    background-color: #f1f5f9;
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    background-color: #2563eb;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("## 🤖")
    st.markdown("### Conceptly AI")

    st.write("")

    if st.button("💬 Chat"):
        st.session_state.page = "chat"

    if st.button("📘 Learn"):
        st.session_state.page = "learn"

    if st.button("⚙ Settings"):
        st.session_state.page = "settings"

    st.write("---")

    if st.button("🗑 Delete Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------- SESSION --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "page" not in st.session_state:
    st.session_state.page = "chat"

# -------------------- MAIN LAYOUT --------------------
col1, col2 = st.columns([3, 2])

# -------------------- LEFT SIDE (CONTENT) --------------------
with col1:

    # HERO SECTION
    st.markdown("""
    <div class="card">
        <h5 style="color:#2563eb;">CONCEPTLY AI TUTOR</h5>
        <h2>Learn deeply, ask freely, and grow with every concept.</h2>
        <p>Explain tough topics step-by-step, check your understanding, and keep momentum with guided follow-ups.</p>
    </div>
    """, unsafe_allow_html=True)

    # CONCEPT CARD
    st.markdown("""
    <div class="card">
        <h5 style="color:#2563eb;">CONCEPT</h5>
        <h3>Quadratic Equations by Factoring</h3>
        <p>Let's solve <b>x² + 5x + 6 = 0</b></p>
        <p>1. Identify numbers → 2 and 3</p>
        <p>2. Factor form → (x + 2)(x + 3) = 0</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- RIGHT SIDE (CHAT) --------------------
with col2:
    st.markdown("### 💬 Chat")

    # Chat history
    for msg in st.session_state.messages:
        role_class = "user" if msg["role"] == "You" else "bot"
        st.markdown(
            f'<div class="chat-box {role_class}"><b>{msg["role"]}</b> ({msg["time"]})<br>{msg["content"]}</div>',
            unsafe_allow_html=True
        )

    # Input
    user_input = st.text_input("Type your question")

    colA, colB = st.columns([1, 1])

    with colA:
        send = st.button("Send")

    with colB:
        upload = st.button("📎")

    # Send logic
    if send and user_input.strip() != "":
        time_now = datetime.now().strftime("%H:%M")

        st.session_state.messages.append({
            "role": "You",
            "content": user_input,
            "time": time_now
        })

        st.session_state.messages.append({
            "role": "Bot",
            "content": "I'm your AI tutor 👋",
            "time": time_now
        })

        st.rerun()