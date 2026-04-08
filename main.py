from fastapi import FastAPI, UploadFile
import uuid
import os
from services.ingest import ingest_data
from services.query import query_rag
from utils.file_utils import get_file_type

app = FastAPI()


# Upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile):
    file_type = get_file_type(file.filename)

    # create folder if not exists
    os.makedirs("temp", exist_ok=True)

    file_path = f"temp/{uuid.uuid4()}_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    ingest_data(file_path, file_type)

    return {"message": "File processed successfully"}


# URL endpoint
@app.post("/upload/url")
def upload_url(url: str):
    ingest_data(url, "url")
    return {"message": "URL processed successfully"}


# Query endpoint
@app.post("/query")
def query(question: str):
    answer = query_rag(question)
    return {"answer": answer}
