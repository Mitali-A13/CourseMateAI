import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("CourseMate AI")

# -------- FILE UPLOAD --------
st.header("Upload Study Material")

uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

    if st.button("Upload File"):
        response = requests.post(f"{API_URL}/upload", files=files)
        st.success(response.json()["message"])


# -------- URL INPUT --------
st.header("Add Web URL")

url = st.text_input("Enter URL")

if st.button("Process URL"):
    response = requests.post(f"{API_URL}/upload/url", params={"url": url})
    st.success(response.json()["message"])


# -------- QUERY --------
st.header("Ask Questions")

question = st.text_input("Enter your question")

if st.button("Get Answer"):
    response = requests.post(f"{API_URL}/query", params={"question": question})
    answer = response.json()["answer"]

    st.write("### Answer:")
    st.write(answer)
