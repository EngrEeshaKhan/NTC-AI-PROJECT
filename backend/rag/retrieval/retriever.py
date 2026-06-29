from backend.rag.embeddings.embedder import embed
from backend.rag.vectorstore.faiss_store import FAISSStore

class Retriever:
    def __init__(self, store: FAISSStore):
        self.store = store

    def retrieve(self, doc_id: str, query: str, k: int = 3):
        # 1. embed query
        query_vector = embed([query])[0]

        # 2. search FAISS
        chunks = self.store.search(doc_id, query_vector, k=k)

        return chunks