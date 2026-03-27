from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

url = "https://www.geeksforgeeks.org/artificial-intelligence/what-is-generative-ai/"

data = WebBaseLoader(url)

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)

chunks = splitter.split_documents(docs)

print(chunks[20].page_content)
