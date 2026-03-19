import faiss
import numpy as np
from rag.embeddings import create_embeddings


class VectorStore:
    def __init__(self):
        self.documents = []
        self.index = None

    def build(self, chunks):
        self.documents = chunks

        embeddings = np.array(
            [create_embeddings(c) for c in chunks]
        ).astype("float32")

        faiss.normalize_L2(embeddings)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings)

    def search(self, query, k=3):

        if self.index is None or len(self.documents) == 0:
            return ["No knowledge base loaded. Please upload data first."]

        query_emb = np.array(
            [create_embeddings(query)]
        ).astype("float32")

        faiss.normalize_L2(query_emb)

        k = min(k, len(self.documents))

        scores, indices = self.index.search(query_emb, k)

        results = [self.documents[i] for i in indices[0]]

        return results


vector_store = VectorStore()