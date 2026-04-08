def get_file_type(filename: str):
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return "pdf"
    elif filename.endswith(".txt"):
        return "text"
    else:
        raise ValueError("Unsupported file type")
