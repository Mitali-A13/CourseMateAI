from loaders.loaders_factory import get_loader
from processing.chunking import get_text_splitter
from vectorstore.chroma_store import add_documents_to_store


def ingest_data(source, file_type):
    loader = get_loader(file_type)
    docs = loader(source)

    splitter = get_text_splitter()
    chunks = splitter.split_documents(docs)

    add_documents_to_store(chunks)

    return "Ingestion complete"
