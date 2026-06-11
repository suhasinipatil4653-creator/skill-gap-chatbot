import streamlit as st
import requests

st.title("🤖 Skill Gap AI Chatbot (Ollama)")

# Chat history storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to talk to Ollama
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    return response.json()["response"]

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask your skill gap question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # AI response
    with st.spinner("Thinking..."):
        reply = ask_ollama(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
    import streamlit as st
import requests


uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

# Rest of your chatbot code below...