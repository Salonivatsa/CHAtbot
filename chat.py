# import os
# from urllib import response

from dotenv import load_dotenv
from tiktoken import model
load_dotenv()

from langchain.chat_models import init_chat_model
chat_model = init_chat_model("google_genai:gemini-2.5-flash")
response = chat_model.invoke("give me a long paragraph about machine learning")
print(response.content)




# # os.environ["GOOGLE_API_KEY"] = "sk-..."
# # chat_model = init_chat_model("google_genai:gemini-2.5-flash-lite")
# chat_model = init_chat_model("google_genai:gemini-2.5-flash")

# # model = init_chat_model("gpt-5.5")
# # chat_model = init_chat_model("gpt-4.1")
# # print(chat_model)


 