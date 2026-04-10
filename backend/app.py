from fastapi import FastAPI
from ingestion.pipeline import process_document
from retrieval.vector_store import VectorStore
from retrieval.query import search
from utils.router import route_query

app = FastAPI()

store = VectorStore()

@app.get("/")
def home():
    return {"message": "Vexoo AI System Running 🚀"}

@app.post("/ingest")
def ingest():
    data = process_document("data/sample.txt")

    embeddings = [d["embedding"] for d in data]
    store.add(embeddings, data)

    return {"status": "Document processed"}

@app.get("/query")
def query(q: str):
    if len(store.data) == 0:
        return {"error": "Run /ingest first"}

    results = search(q, store)

    # ✅ FIX: remove embedding before returning
    cleaned_results = []
    for r in results:
        cleaned_results.append({
            "chunk": r["chunk"],
            "summary": r["summary"],
            "keywords": r["keywords"]
        })

    return {"results": cleaned_results}

@app.get("/smart_query")
def smart_query(q: str):
    if len(store.data) == 0:
        return {"error": "Run /ingest first"}

    route = route_query(q)
    results = search(q, store)

    cleaned_results = []
    for r in results:
        cleaned_results.append({
            "chunk": r["chunk"],
            "summary": r["summary"],
            "keywords": r["keywords"]
        })

    return {
        "route": route,
        "results": cleaned_results
    }

def generate_answer(results):
    summaries = [r["summary"] for r in results]
    return " ".join(summaries)