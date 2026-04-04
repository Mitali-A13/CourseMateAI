# CourseMateAI

CourseMateAI is a Retrieval-Augmented Generation (RAG) based system that enables users to interact with their documents through natural language queries. The system processes documents, converts them into embeddings, stores them in a vector database, and retrieves relevant information to generate accurate, context-aware responses using a language model.

---

## Overview

CourseMateAI is designed to solve the problem of extracting meaningful insights from large textual documents such as PDFs. Instead of manually searching through documents, users can ask questions, and the system retrieves the most relevant information and generates answers grounded in the document content.

The architecture follows a two-phase pipeline:

* **Ingestion Phase (Offline):** Document loading, chunking, embedding generation, and storage in a vector database
* **Retrieval + Generation Phase (Online):** Query processing, semantic retrieval, and response generation using an LLM

---

## Architecture

### System Flow

```
Offline Phase (Ingestion):
Documents → Chunking → Embeddings → Vector Database (Chroma)

Online Phase (Query):
User Query → Query Embedding → Retriever → Vector Database
           → Top-K Relevant Chunks → Context + Query → LLM → Final Answer
```

---

## Features

* Document ingestion from PDFs
* Semantic chunking of text
* Embedding generation using Google Gemini
* Vector storage using Chroma DB
* Efficient similarity search with MMR
* Context-aware answer generation using Mistral LLM
* Persistent vector database to avoid recomputation
* Modular architecture separating ingestion and querying

---

## Tech Stack

* **Language Model:** Mistral (`mistral-small-2506`)
* **Embedding Model:** Google Gemini (`embedding-001`)
* **Vector Database:** Chroma DB
* **Framework:** LangChain
* **Language:** Python

---

## Project Structure

```
CourseMateAI/
│
├── document loaders/        # Source documents
├── chroma_db/               # Vector database
├── vector_store.py          # Ingestion pipeline
├── main.py                  # Query pipeline
├── requirements.txt
├── .env
└── README.md
```

---

## How It Works

### 1. Ingestion Pipeline (vector_store.py)

* Loads documents
* Splits them into chunks
* Generates embeddings
* Stores embeddings and metadata in Chroma DB

This step is executed once and reused across sessions.

---

### 2. Retrieval Pipeline (main.py)

* Converts user query into an embedding
* Performs similarity search in the vector database
* Uses MMR to retrieve relevant and diverse chunks
* Combines retrieved chunks into context
* Passes context and query to the LLM
* Generates a grounded response

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

### Run ingestion pipeline

```bash
python vector_store.py
```

This will process documents, create embeddings, and store them in `chroma_db/`.

---

### Run query system

```bash
python main.py
```

You can now query your documents interactively.

---

## Retrieval Strategy

The system uses Maximum Marginal Relevance (MMR) to balance:

* Relevance to the query
* Diversity among retrieved chunks

This improves the quality of context passed to the LLM and reduces redundancy.

---

## Design Decisions

* Separation of ingestion and querying
* Persistent vector storage
* Optimized chunking strategy
* Consistent embedding model
* Grounded response generation

---

## Limitations

* No conversational memory
* Limited context window
* Retrieval quality depends on chunking

---

## Future Improvements

* Add conversational memory
* Hybrid search (keyword + vector)
* Reranking
* UI integration
* Multi-document support

---

## Conclusion

CourseMateAI implements a complete RAG pipeline combining document processing, semantic retrieval, and LLM-based reasoning. It reflects real-world system design patterns used in modern AI-powered applications.
