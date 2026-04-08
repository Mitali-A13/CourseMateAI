from langchain_community.document_loaders import WebBaseLoader


# data loading
def load_web(url):
    loader = WebBaseLoader(url)
    return loader.load()
