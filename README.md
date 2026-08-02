# 💬 Simple AI Chatbot

A minimal Streamlit chat UI powered by Mistral (via LangChain).

## Features
- Clean, default white-background chat interface
- Chat history persists across the session
- "Clear Chat" button to reset conversation

## Setup

1. Install dependencies:
   ```bash
   pip install streamlit langchain-mistralai python-dotenv
   ```

2. Create a `.env` file in the project folder:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

3. Run the app:
   ```bash
   streamlit run simple_chat_app.py
   ```

## LLM / Model Used
- LangChain Mistral (`mistral-small-2506`)

## Notes
- The AI's personality is set via a `SystemMessage` ("You are a funny AI agent.") — edit it in the code to change tone/behavior.
