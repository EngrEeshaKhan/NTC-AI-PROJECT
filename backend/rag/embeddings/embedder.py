from sentence_transformers import SentenceTransformer

model = SentenceTransformer("C:/local_models/embeddings")

def embed(texts):
    return model.encode(texts).astype("float32")