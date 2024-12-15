# Example usage in main.py
from src.rag_model import RAGModel
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY not found!")
        return

    rag_model = RAGModel()
    
    while True:
        query = input("\nEnter your question (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
            
        response = rag_model.process_query(query)
        print(f"\nResponse: {response}")

if __name__ == "__main__":
    main()