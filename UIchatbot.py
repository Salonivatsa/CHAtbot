import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# ── Page setup (plain, default white background) ──
st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💬 Simple AI Chatbot")
# Force white background (override dark theme if present)
st.markdown(
    """
    <style>
    body, .stApp, .block-container { background-color: #ffffff !important; color: #000000 !important; }
    header, footer, .css-1v3fvcr { background-color: #ffffff !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Model ──
model = ChatMistralAI(model="mistral-small-2506", temperature=0.7, max_tokens=512)

# ── Session state: keep chat history across reruns ──
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI agent.")
    ]

# ── Render previous chat history ──
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)
    # SystemMessage is not shown in the UI

# ── Chat input box (sticky at bottom by default) ──
prompt = st.chat_input("Type your message...")

if prompt:
    # show user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    # get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))

# ── Optional: clear chat button ──
if st.button("Clear Chat"):
    st.session_state.messages = [SystemMessage(content="You are a funny AI agent.")]
    st.rerun()