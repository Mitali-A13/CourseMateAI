from langchain_community.document_loaders import TextLoader


# data loading
def load_pdf(path):
    loader = TextLoader(path)
    return loader.load()
