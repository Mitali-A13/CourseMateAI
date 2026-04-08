from langchain_community.document_loaders import PyPDFLoader


# data loading
def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()
