from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# load the pdf
data = PyPDFLoader("document loaders/deeplearning.pdf")
docs = data.load()

# split the pdf into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# limiting the chunks
chunks = chunks[:20]
# create the embeddings
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# store in the vector store
vector_store = Chroma.from_documents(
    documents=chunks, embedding=embedding_model, persist_directory="chroma_db"
)
