from langchain_community.document_loaders import WebBaseLoader


# data loading
def load_pdf(url):
    loader = WebBaseLoader(url)
    return loader.load()
