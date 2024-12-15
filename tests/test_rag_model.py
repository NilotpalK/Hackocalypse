import pytest
from src.rag_model import RAGModel
from src.config import Config

@pytest.fixture
def rag_model():
    return RAGModel()

def test_initialization(rag_model):
    assert rag_model is not None
    assert rag_model.knowledge_base is not None

def test_context_retrieval(rag_model):
    query = "Where is the nearest safe zone?"
    context = rag_model.retrieve_context(query)
    assert len(context) > 0

def test_response_generation(rag_model):
    query = "Where is the nearest safe zone?"
    response = rag_model.process_query(query)
    assert response is not None and len(response) > 0