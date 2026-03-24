from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# DOCUMENT LOADED
data = TextLoader("document loaders/DSA.txt")
docs = data.load()

# PROMPT TEMPLATE
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}"),
    ]
)

# DEFINED THE MODEL
model = ChatMistralAI(model="mistral-small-2506")

# SENT DATA TO PROMPT
prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke(prompt)
print(result.content)
