import streamlit as st
import requests

st.set_page_config(page_title="AI Terraform Assistant", layout="wide")

st.title("🛠️ AI Terraform Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("Type your Terraform or DevOps request here:")

if st.button("Send") and user_input.strip():
    # Add user message to chat history
    st.session_state["messages"].append(("You", user_input))

    # Send prompt to your running FastAPI server
    try:
        resp = requests.post(
            "http://127.0.0.1:8000/prompt",
            json={"request": user_input},
            timeout=30,
        )
        if resp.ok:
            answer = resp.json().get("response", "No response.")
            st.session_state["messages"].append(("Bot", answer))
        else:
            st.session_state["messages"].append(("Bot", f"Error: {resp.text}"))
    except Exception as e:
        st.session_state["messages"].append(("Bot", f"Request failed: {e}"))

# Show chat history
for who, msg in st.session_state["messages"]:
    st.markdown(f"**{who}:** {msg}")
