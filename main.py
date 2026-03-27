from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

# PROMPT TEMPLATE
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}"),
    ]
)

# DEFINED THE MODEL
model = ChatMistralAI(model="mistral-small-2506")
