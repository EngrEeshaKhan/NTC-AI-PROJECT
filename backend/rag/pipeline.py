import uuid
import json
import os

from backend.rag.chunking.chunker import chunk_text
from backend.rag.embeddings.embedder import embed
from backend.rag.ingestion.loader import load_pdf
from backend.rag.vectorstore.faiss_store import FAISSStore
from backend.rag.llm.ollama_llm import generate
from backend.rag.retrieval.retriever import Retriever


DOC_FILE = "data/doc_registry.json"


def load_docs():
    if not os.path.exists(DOC_FILE):
        return {}
    with open(DOC_FILE, "r") as f:
        return json.load(f)


def save_docs(docs):
    with open(DOC_FILE, "w") as f:
        json.dump(docs, f, indent=2)


class Pipeline:
    def __init__(self):
        self.store = FAISSStore()
        self.retriever = Retriever(self.store)

        # ✅ NOW PERSISTENT
        self.docs = load_docs()

    # ------------------------
    # UPLOAD
    # ------------------------
    async def upload(self, file):
        doc_id = str(uuid.uuid4())

        path = f"data/uploads/{file.filename}"
        content = await file.read()

        with open(path, "wb") as f:
            f.write(content)

        text = load_pdf(path)
        chunks = chunk_text(text)
        vectors = embed(chunks)

        self.store.create_doc(doc_id, dim=len(vectors[0]))
        self.store.add(doc_id, vectors, chunks)

        # ✅ SAVE DOCS TO FILE (IMPORTANT FIX)
        self.docs[doc_id] = file.filename
        save_docs(self.docs)

        return {"doc_id": doc_id, "filename": file.filename}

    # ------------------------
    # LIST DOCS
    # ------------------------
    def list_docs(self):
        return self.docs

    # ------------------------
    # DELETE DOC
    # ------------------------
    def delete_doc(self, doc_id):
        self.store.delete(doc_id)

        self.docs.pop(doc_id, None)
        save_docs(self.docs)

        return {"status": "deleted"}

    # ------------------------
    # ASK
    # ------------------------
    def ask(self, doc_id, question):
        chunks = self.retriever.retrieve(doc_id, question)

        if not chunks:
            return "No response (no context found)"

        context = "\n\n".join(chunks)

        return generate(context, question)