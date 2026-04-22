import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="AI Tutor", layout="wide")

# Custom CSS (for modern UI)
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
    }
    .chat-box {
        padding: 10px;
            border-radius: 10px;
                margin-bottom: 10px;
                }
                .user {
                    background-color: #d1e7ff;
                    }
                    .bot {
                        background-color: #ffffff;
                        }
                        .card {
                            padding: 20px;
                                border-radius: 15px;
                                    background: white;
                                        box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
                                            margin-bottom: 20px;
                                            }
                                            </style>
                                            """, unsafe_allow_html=True)

                                            # Sidebar
                                            with st.sidebar:
                                                st.title("🤖")
                                                    st.markdown("### Menu")
                                                        st.button("💬 Chat")
                                                            st.button("📘 Learn")
                                                                st.button("⚙ Settings")

                                                                # Main Layout
                                                                col1, col2 = st.columns([2, 3])

                                                                # Left Side (Cards)
                                                                with col1:
                                                                    st.markdown('<div class="card">', unsafe_allow_html=True)
                                                                        st.subheader("CONCEPTLY AI TUTOR")
                                                                            st.write("Learn deeply, ask freely, and grow with every concept.")
                                                                                st.button("Learn")
                                                                                    st.button("Ask")
                                                                                        st.button("Grow")
                                                                                            st.markdown('</div>', unsafe_allow_html=True)

                                                                                                st.markdown('<div class="card">', unsafe_allow_html=True)
                                                                                                    st.subheader("Quadratic Equations by Factoring")
                                                                                                        st.write("Solve x² + 5x + 6 = 0 → (x+2)(x+3)=0")
                                                                                                            st.markdown('</div>', unsafe_allow_html=True)

                                                                                                            # Right Side (Chat)
                                                                                                            with col2:
                                                                                                                st.title("💬 Chat")

                                                                                                                    if "messages" not in st.session_state:
                                                                                                                            st.session_state.messages = []

                                                                                                                                # Show messages
                                                                                                                                    for msg in st.session_state.messages:
                                                                                                                                            role_class = "user" if msg["role"] == "You" else "bot"
                                                                                                                                                    st.markdown(
                                                                                                                                                                f'<div class="chat-box {role_class}"><b>{msg["role"]}</b> ({msg["time"]})<br>{msg["content"]}</div>',
                                                                                                                                                                            unsafe_allow_html=True
                                                                                                                                                                                    )

                                                                                                                                                                                        # Input
                                                                                                                                                                                            user_input = st.text_input("Type your question...")

                                                                                                                                                                                                if st.button("Send") and user_input:
                                                                                                                                                                                                        time_now = datetime.now().strftime("%H:%M")

                                                                                                                                                                                                                st.session_state.messages.append({
                                                                                                                                                                                                                            "role": "You",
                                                                                                                                                                                                                                        "content": user_input,
                                                                                                                                                                                                                                                    "time": time_now
                                                                                                                                                                                                                                                            })

                                                                                                                                                                                                                                                                    # Dummy bot reply
                                                                                                                                                                                                                                                                            bot_reply = "I can help you learn this step by step!"

                                                                                                                                                                                                                                                                                    st.session_state.messages.append({
                                                                                                                                                                                                                                                                                                "role": "Bot",
                                                                                                                                                                                                                                                                                                            "content": bot_reply,
                                                                                                                                                                                                                                                                                                                        "time": time_now
                                                                                                                                                                                                                                                                                                                                })

                                                                                                                                                                                                                                                                                                                                        st.rerun()