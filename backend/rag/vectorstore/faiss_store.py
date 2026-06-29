import faiss
import numpy as np

class FAISSStore:
    def __init__(self):
        self.indexes = {}   # doc_id -> index
        self.texts = {}     # doc_id -> chunks

    def create_doc(self, doc_id, dim=384):
        self.indexes[doc_id] = faiss.IndexFlatL2(dim)
        self.texts[doc_id] = []

    def add(self, doc_id, vectors, chunks):
        self.indexes[doc_id].add(np.array(vectors))
        self.texts[doc_id].extend(chunks)

    def search(self, doc_id, vector, k=3):
        if doc_id not in self.indexes:
            return []

        D, I = self.indexes[doc_id].search(np.array([vector]), k)
        return [self.texts[doc_id][i] for i in I[0]]

    def delete(self, doc_id):
        self.indexes.pop(doc_id, None)
        self.texts.pop(doc_id, None)