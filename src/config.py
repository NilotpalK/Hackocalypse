import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "all-MiniLM-L6-v2"
    VECTOR_DIMENSION = 384
    TOP_K_RESULTS = 3