from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def get_retriever():
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    vector_store = Chroma(
        persist_directory="chroma_db", embedding_function=embedding_model
    )

    return vector_store.as_retriever(
        search_type="mmr", search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
    )
