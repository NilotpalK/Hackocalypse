from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from typing import List, Tuple

class EmbeddingManager:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.data = []

    def create_embeddings(self, texts: List[str]) -> np.ndarray:
        """Create embeddings for a list of texts."""
        return self.model.encode(texts)

    def build_index(self, embeddings: np.ndarray):
        """Build FAISS index from embeddings."""
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def search(self, query: str, k: int = 3) -> Tuple[np.ndarray, np.ndarray]:
        """Search for similar vectors."""
        query_vector = self.model.encode([query])
        return self.index.search(query_vector, k)