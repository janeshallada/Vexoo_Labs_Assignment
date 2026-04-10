import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.data = []

    def add(self, embeddings, metadata):
        embeddings = np.array(embeddings).astype("float32")   # 🔥 FIX
        self.index.add(embeddings)
        self.data.extend(metadata)

    def search(self, query_embedding, k=3):
        query_embedding = np.array([query_embedding]).astype("float32")  # 🔥 FIX
        D, I = self.index.search(query_embedding, k)
        return [self.data[i] for i in I[0]]