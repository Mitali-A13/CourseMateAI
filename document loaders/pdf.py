from langchain_community.document_loaders import PyPDFLoader
import os

docs = []

folder_path = "document loaders"

for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(folder_path, file))
        docs.extend(loader.load())

print(docs)
