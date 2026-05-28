# 🚀 Vexoo Labs – AI Engineer Assignment

## 📌 Overview

This project implements a **modular AI-powered document retrieval system** inspired by Retrieval-Augmented Generation (RAG). It focuses on scalable system design, semantic search, and efficient knowledge representation.

The system processes documents, builds hierarchical knowledge representations, and retrieves relevant information using vector similarity search.

---

## 🧠 Key Features

* 📄 Document ingestion with sliding window chunking
* 🧩 Knowledge Pyramid (Raw → Summary → Keywords → Embeddings)
* 🔍 Semantic search using vector embeddings
* ⚡ Fast retrieval using FAISS
* 🧠 Query routing (math / general / legal)
* 🚀 FastAPI backend for API-based interaction
* ⚙️ Lazy loading for optimized performance

---

## 🏗️ System Architecture

```
User Query
    ↓
Query Router (optional)
    ↓
Embedding Model
    ↓
FAISS Vector Search
    ↓
Retrieve Relevant Chunks
    ↓
Generate Response
```

---

## 📂 Project Structure

```
backend/
│
├── app.py
├── ingestion/
│   ├── loader.py
│   ├── chunker.py
│   ├── summarizer.py
│   ├── keywords.py
│   └── pipeline.py
│
├── models/
│   └── embedding.py
│
├── retrieval/
│   ├── vector_store.py
│   └── query.py
│
├── utils/
│   └── router.py
│
├── data/
│   └── sample.txt
│
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd vexoo-ai-system/backend
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Server

```bash
uvicorn app:app --reload
```

---

### 4️⃣ Open API Docs

👉 http://127.0.0.1:8000/docs

---

## 📥 API Usage

### 🔹 1. Ingest Document

**POST** `/ingest`

Processes the document and stores embeddings in FAISS.

---

### 🔹 2. Query System

**GET** `/query?q=your_question`

Example:

```
/query?q=What is AI?
```

---

### 🔹 3. Smart Query (Bonus)

**GET** `/smart_query?q=your_question`

Routes query based on type (math / legal / general)

---

## 🧠 Knowledge Pyramid Design

The system transforms raw text into hierarchical representations:

* **Raw Text** → Original document content
* **Chunk Summary** → First few sentences (lightweight summarization)
* **Keywords** → Extracted important terms
* **Embeddings** → Dense vector representations using Sentence Transformers

---

## 🔍 Retrieval Strategy

* Dense vector embeddings using `all-MiniLM-L6-v2`
* FAISS-based nearest neighbor search
* Top-K relevant chunks retrieved
* Multi-level knowledge improves robustness

---

## 🤖 Technologies Used

* FastAPI (Backend API)
* Sentence Transformers (Embeddings)
* FAISS (Vector Search)
* NumPy & Scikit-learn
* Python

---

## 🧪 Example Output

```json
{
  "question": "What is AI?",
  "answer": "Artificial Intelligence is transforming industries...",
  "sources": [
    {
      "chunk": "...",
      "summary": "...",
      "keywords": ["AI", "automation"]
    }
  ]
}
```

---

## ⚡ Design Decisions

* Used character-based sliding window for simplicity
* Implemented modular pipeline for scalability
* Used lightweight summarization for speed
* Adopted FAISS for efficient similarity search
* Applied lazy loading for faster startup

---

## 🧠 Bonus: Reasoning-Aware Routing

A routing layer classifies queries:

* **Math** → symbolic reasoning
* **Legal** → structured retrieval
* **General** → semantic search

---

## 📊 Future Improvements

* Integrate LLM for answer generation
* Replace placeholder summarization with transformer models
* Add hybrid search (keyword + semantic)
* Build frontend dashboard (React)
* Deploy on cloud (Render / AWS)

---

## 🏁 Conclusion

This project demonstrates a scalable and modular approach to building AI-powered retrieval systems. By combining semantic embeddings, hierarchical knowledge representation, and efficient indexing, it enables robust and context-aware query handling.

---

## 👨‍💻 Author

**Janesh Allada**
📧 [janeshallada@gmail.com](mailto:janeshallada@gmail.com)
🔗 LinkedIn: https://linkedin.com/in/janeshallada
💻 GitHub: https://github.com/janeshallada
