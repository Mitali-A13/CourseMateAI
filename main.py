from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# CREATE EMBEDDING OF THE QUERY
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = Chroma(persist_directory="chroma_db", embedding_function=embedding_model)

# CREATE A RETRIEVER
retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
)

# DEFINED THE CHAT-MODEL
llm = ChatMistralAI(model="mistral-small-2506")

# PROMPT TEMPLATE
template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

            Use ONLY the provided context to answer the question.

            If the answer is not present in the context,
            say: "I could not find the answer in the document."
            """,
        ),
        (
            "human",
            """Context:
            {context}

            Question:
            {question}
            """,
        ),
    ]
)
