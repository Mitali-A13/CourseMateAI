from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

# data loaded
data = PyPDFLoader("document loaders/javascript.pdf")
docs = data.load()

# data splitted into chunks
splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=10)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)
