from models.embedding import get_embedding

def search(query, vector_store):
    query_emb = get_embedding(query)

    results = vector_store.search(query_emb)
    return results