# # src/rag_model.py
# from typing import List
# import groq
# from .config import Config
# from .vector_store import VectorStore
# from .data_loader import DataLoader

# class RAGModel:
#     def __init__(self):
#         self.config = Config()
#         self.vector_store = VectorStore()
#         self.data_loader = DataLoader()
#         self.groq_client = groq.Client(api_key=self.config.GROQ_API_KEY)
#         self.initialize_system()
#         print("RAG Model initialized successfully!")

#     def initialize_system(self):
#         """Initialize the RAG system with initial map data."""
#         try:
#             # Load initial map data
#             initial_map = self.data_loader.load_initial_map()
            
#             # Add texts to vector store
#             self.vector_store.add_texts(initial_map)
            
#             print(f"Loaded {len(initial_map)} map descriptions into vector store")
            
#             # Optionally save the index
#             self.vector_store.save_index("data/vector_store/map_index.faiss")
            
#         except Exception as e:
#             print(f"Error initializing system: {str(e)}")

#     def process_query(self, query: str) -> str:
#         """Process a user query and return a response."""
#         try:
#             # Retrieve relevant context using vector store
#             context = self.vector_store.search(query, k=self.config.TOP_K_RESULTS)
#             prompt = self._create_prompt(query, context)
            
#             # Generate response using Groq
#             completion = self.groq_client.chat.completions.create(
#                 messages=[
#                     {
#                         "role": "system",
#                         "content": "You are a survival assistant in a zombie apocalypse scenario."
#                     },
#                     {
#                         "role": "user",
#                         "content": prompt
#                     }
#                 ],
#                 model="mixtral-8x7b-32768",
#                 temperature=0.7,
#                 max_tokens=150
#             )
            
#             return completion.choices[0].message.content
#         except Exception as e:
#             print(f"Error in process_query: {str(e)}")
#             return f"Error processing query: {str(e)}"

#     def _create_prompt(self, query: str, context: List[str]) -> str:
#         """Create a prompt for the LLM."""
#         context_str = "\n".join(context)
#         return f"""
# Based on the following map information:
# {context_str}

# Please answer this question about survival in the zombie apocalypse:
# {query}

# Provide a clear, concise response focusing on survival strategy.
# """

# src/rag_model.py
import warnings
import logging
from typing import List
import groq
from .config import Config
from .vector_store import VectorStore
from .data_loader import DataLoader

class RAGModel:
    def __init__(self):
        self.config = Config()
        self.vector_store = VectorStore()
        self.data_loader = DataLoader()
        self.groq_client = groq.Client(api_key=self.config.GROQ_API_KEY)
        self.initialize_system()
        print("RAG Model initialized successfully!")

    def initialize_system(self):
        """Initialize the RAG system with initial map data."""
        try:
            initial_map = self.data_loader.load_initial_map()
            self.vector_store.add_texts(initial_map)
            print(f"Loaded {len(initial_map)} map descriptions into vector store")
        except Exception as e:
            print(f"Error initializing system: {str(e)}")

    def process_query(self, query: str) -> str:
        """Process a user query and return a response."""
        try:
            context = self.vector_store.search(query, k=self.config.TOP_K_RESULTS)
            prompt = self._create_prompt(query, context)
            
            completion = self.groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": """You are V.A.S. (Vault Apocalypse System), an advanced AI survival assistant in a zombie apocalypse scenario. 
                        Your responses should be:
                        1. Detailed and consice so that you do not hit your token limit
                        2. Focus on practical survival advice
                        3. Consider multiple factors (safety, resources, risks)
                        4. Provide clear, actionable steps
                        5. Maintain a serious, professional tone
                        Always conclude your responses with a clear summary or final recommendation."""
                    },
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=500,  # Increased token limit
                top_p=0.9,
                stop=None  # Allow model to complete its thoughts
            )
            
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error in process_query: {str(e)}")
            return f"Error processing query: {str(e)}"

    def _create_prompt(self, query: str, context: List[str]) -> str:
        context_str = "\n".join(context)
        return f"""
Based on the following map information:
{context_str}

SURVIVAL QUERY: {query}

Please provide a detailed response that includes:
1. Initial situation assessment
2. Available resources and safe zones
3. Potential risks and threats
4. Step-by-step survival recommendations
5. Alternative options if available
6. Final survival recommendation

Format your response in clear sections and ensure it's complete and actionable.
"""