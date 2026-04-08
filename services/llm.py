from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()


def get_llm():
    return ChatMistralAI(model="mistral-small-2506")
