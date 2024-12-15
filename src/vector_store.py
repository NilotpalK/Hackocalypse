# src/vector_store.py
import faiss
import numpy as np
from typing import List, Tuple, Dict
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.text_to_id: Dict[int, str] = {}  # Map IDs to original text
        self.id_counter = 0

    def add_texts(self, texts: List[str]) -> None:
        """Add new texts to the vector store"""
        # Create embeddings
        embeddings = self.model.encode(texts)
        
        # Initialize index if it doesn't exist
        if self.index is None:
            dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
        
        # Add embeddings to index
        self.index.add(embeddings)
        
        # Store text to ID mappings
        for text in texts:
            self.text_to_id[self.id_counter] = text
            self.id_counter += 1

    def search(self, query: str, k: int = 3) -> List[str]:
        """Search for similar texts"""
        # Create query embedding
        query_embedding = self.model.encode([query])
        
        # Search in the index
        distances, indices = self.index.search(query_embedding, k)
        
        # Return the original texts
        return [self.text_to_id[int(idx)] for idx in indices[0]]

    def save_index(self, filepath: str) -> None:
        """Save the FAISS index to disk"""
        if self.index is not None:
            faiss.write_index(self.index, filepath)

    def load_index(self, filepath: str) -> None:
        """Load the FAISS index from disk"""
        self.index = faiss.read_index(filepath)