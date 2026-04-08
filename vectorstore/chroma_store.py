from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# create embedding model
def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


# create vectore store
def get_vectorstore(persist_directory="chroma_db"):
    embedding_model = get_embedding_model()

    return Chroma(
        persist_directory=persist_directory, embedding_function=embedding_model
    )


# add documents to vector store
def add_documents_to_store(chunks):
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)
    vectorstore.persist()  # important

    return vectorstore
