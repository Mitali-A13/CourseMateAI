from loaders.pdf_loader import load_pdf
from loaders.text_loader import load_text
from loaders.web_loader import load_web


# a function to detect which type of loader to activate
def get_loader(file_type):
    if file_type == "pdf":
        return load_pdf
    elif file_type == "text":
        return load_text
    elif file_type == "url":
        return load_web
    else:
        raise ValueError("Unsupported file type")
