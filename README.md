# CourseMateAI

CourseMateAI is a Retrieval-Augmented Generation (RAG) based system that enables users to interact with their documents through natural language queries. The system supports dynamic document ingestion, processes content into embeddings, stores them in a vector database, and retrieves relevant information to generate accurate, context-aware responses using a language model.

---

## Overview

CourseMateAI is designed to solve the problem of extracting meaningful insights from large and diverse study materials such as PDFs, text files, and web pages. Instead of manually searching through documents, users can upload content or provide URLs and ask questions directly.

The system is built as a modular and extensible architecture with clear separation between ingestion, retrieval, and API layers.

The architecture follows a two-phase pipeline:

* **Ingestion Phase (Dynamic / On-demand):** Document loading, chunking, embedding generation, and storage in a vector database
* **Retrieval + Generation Phase (Online):** Query processing, semantic retrieval, and response generation using an LLM

---

## Architecture

### System Flow

```
Ingestion Phase:
User Input (PDF / TXT / URL) → Loader → Chunking → Embeddings → Vector Database (Chroma)

Query Phase:
User Query → FastAPI → Retriever → Vector Database
           → Top-K Relevant Chunks → Context + Query → LLM → Final Answer
```

---

## Features

* Dynamic document ingestion (PDF, TXT, URL)
* Modular loader system with factory pattern
* Semantic chunking using RecursiveCharacterTextSplitter
* Embedding generation using Google Gemini
* Vector storage using Chroma DB with persistence
* Efficient similarity search using MMR
* Context-aware answer generation using Mistral LLM
* REST API using FastAPI for interaction
* Lightweight UI using Streamlit for testing
* Scalable and clean architecture separating concerns

---

## Tech Stack

* **Language Model:** Mistral (`mistral-small-2506`)
* **Embedding Model:** Google Gemini (`embedding-001`)
* **Vector Database:** Chroma DB
* **Framework:** LangChain
* **Backend API:** FastAPI
* **UI (Testing):** Streamlit
* **Language:** Python

---

## Project Structure

```
CourseMateAI/
│
├── loaders/                # PDF, Text, Web loaders
├── processing/             # Chunking logic
├── vectorstore/            # Embedding + Chroma DB logic
├── services/               # Ingestion and query pipelines
├── utils/                  # Helper functions (file type detection)
├── api/                    # API routes (optional separation)
├── chroma_db/              # Persistent vector database
├── main.py                 # FastAPI entry point
├── streamlit_app.py        # Minimal UI for testing
├── requirements.txt
├── .env
└── README.md
```

---

## How It Works

### 1. Ingestion Pipeline

* Accepts user input (file upload or URL)
* Detects file type dynamically
* Loads content using appropriate loader
* Splits content into chunks
* Generates embeddings
* Stores embeddings and metadata in Chroma DB

This pipeline is triggered via API and runs on-demand.

---

### 2. Retrieval Pipeline

* Receives user query via API
* Converts query into embedding
* Performs similarity search in vector database
* Uses MMR to retrieve relevant and diverse chunks
* Combines retrieved chunks into context
* Passes context and query to LLM
* Generates a grounded response

---

### 3. API Layer (FastAPI)

* `/upload` → Upload and process documents
* `/upload/url` → Process web URLs
* `/query` → Ask questions on ingested data

This layer exposes the backend as a service.

---

### 4. UI Layer (Streamlit)

* Upload files and URLs
* Ask questions interactively
* View generated responses

Used for testing and rapid prototyping.

---

## Installation

```bash
git clone https://github.com/Mitali-A13/CourseMateAI.git
cd CourseMateAI
```

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```
GOOGLE_API_KEY=your_gemini_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

---

## Usage

### 1. Start backend server

```bash
uvicorn main:app --reload
```

---

### 2. Start Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

### 3. Use the application

* Upload a document or provide a URL
* Ask questions based on the content
* Receive context-aware answers

---

## Retrieval Strategy

The system uses Maximum Marginal Relevance (MMR) to balance:

* Relevance to the query
* Diversity among retrieved chunks

This improves the quality of context passed to the LLM and reduces redundancy.

---

## Design Decisions

* Separation of ingestion and query pipelines
* Modular architecture (loaders, services, vectorstore)
* API-first backend design
* Persistent vector storage to avoid recomputation
* Use of MMR for improved retrieval quality
* Lightweight UI for rapid testing

---

## Limitations

* No conversational memory
* Context size limited by LLM token constraints
* No reranking layer
* Basic UI (not production-grade)

---

## Future Improvements

* Add conversational memory
* Implement hybrid search (keyword + vector)
* Add reranking for improved retrieval accuracy
* Support more file types (DOCX, Markdown)
* Multi-user support with document isolation
* Production-grade frontend (React)

---

## Conclusion

CourseMateAI implements a complete, modular RAG pipeline with dynamic ingestion, semantic retrieval, and LLM-based response generation. The system reflects real-world backend architecture patterns, including API-based interaction, separation of concerns, and scalable design, making it a strong foundation for production-grade AI applications.

