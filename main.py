from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# DOCUMENT LOADED
data = PyPDFLoader("document loaders/deeplearning.pdf")
docs = data.load()
print("loaded")

# CHUNKING THE DATA
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

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
prompt = template.format_messages(data=docs)

result = model.invoke(prompt)
print(result.content)
