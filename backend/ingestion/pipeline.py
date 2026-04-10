from ingestion.loader import load_text
from ingestion.chunker import chunk_text
from ingestion.summarizer import summarize
from ingestion.keywords import extract_keywords
from models.embedding import get_embedding

def process_document(file_path):
    text = load_text(file_path)
    chunks = chunk_text(text)

    processed = []

    for chunk in chunks:
        summary = summarize(chunk)
        keywords = extract_keywords(chunk)
        embedding = get_embedding(chunk)

        processed.append({
            "chunk": chunk,
            "summary": summary,
            "keywords": keywords,
            "embedding": embedding
        })

    return processed